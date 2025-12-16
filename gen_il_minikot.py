import sys
import lex_minikot
import os

# ==========================================
# ГЛОБАЛЬНІ ЗМІННІ
# ==========================================
num_row = 1
global_fields = []       
generated_methods = []   
main_code = []           
current_code = []        
global_vars_table = {}   
current_context = {
    'scope_type': 'main',  
    'locals': {},          
    'args': {},            
    'local_idx': 0,        
    'name': 'Main'         
}
func_signatures = {}
labelCounter = 0

# ==========================================
# ДОПОМІЖНІ ФУНКЦІЇ
# ==========================================
def get_symb():
    global num_row
    if num_row > len(lex_minikot.table_of_symb): return (0, 'EOF', 'None')
    rec = lex_minikot.table_of_symb[num_row]
    return rec[0], rec[1], rec[2]

def fail_parse(msg, line):
    print(f"\nIL Generator ERROR: Line {line}\n\tMessage: {msg}"); sys.exit(1)

def parse_token(expected_lex, expected_tok):
    global num_row
    line, lex, tok = get_symb()
    match_lex = (expected_lex is None) or (lex == expected_lex)
    match_tok = (expected_tok is None) or (tok == expected_tok)
    if match_lex and match_tok: num_row += 1; return True
    else: fail_parse(f"Expected '{expected_lex}'/'{expected_tok}', got '{lex}'/'{tok}'", line)

def gen(code):
    current_code.append("    " + str(code))

def createLabel():
    global labelCounter; labelCounter += 1
    return f"L_{labelCounter}"

def setLabel(label):
    current_code.append(f"{label}:")

def get_cil_type(mk_type):
    if mk_type == 'Int': return 'int32'
    if mk_type == 'Double': return 'float64'
    if mk_type == 'String': return 'string'
    if mk_type == 'Boolean': return 'bool'
    if mk_type == 'Unit': return 'void'
    return 'void'

def resolve_variable(name):
    if name in current_context['args']:
        typ, idx = current_context['args'][name]
        return ('arg', typ, idx)
    if name in current_context['locals']:
        typ, idx = current_context['locals'][name]
        return ('local', typ, idx)
    if name in global_vars_table:
        typ = global_vars_table[name]
        return ('field', typ, name)
    fail_parse(f"Variable '{name}' not declared", num_row)

# ==========================================
# ПАРСЕР
# ==========================================

def parse_program():
    global current_code
    print(">>> Generating IL Code (Vertical Format)...")
    current_code = main_code
    current_context['locals']['__temp'] = ('float64', 0)
    current_context['local_idx'] = 1

    try:
        while num_row <= len(lex_minikot.table_of_symb):
            parse_statement()
    except SystemExit: pass

def parse_statement():
    global num_row
    _, lex, tok = get_symb()
    if tok == 'keyword':
        if lex in ('var', 'val', 'const'): parse_decl()
        elif lex == 'if': parse_if()
        elif lex == 'while': parse_while()
        elif lex in ('print', 'println'): parse_print()
        elif lex in ('readInt', 'readDouble', 'readString'): 
            parse_read_call(); parse_token(';', 'punct')
        elif lex == 'fun': parse_fun_decl()
        elif lex == 'return': parse_return()
        else: num_row += 1 
    elif tok == 'id':
        parse_assign()
    elif tok == 'bracket_op' and lex == '{':
        parse_block()
    elif tok == 'EOF': sys.exit(0)
    else: num_row += 1 

def parse_block():
    parse_token('{', 'bracket_op')
    while True:
        _, lex, tok = get_symb()
        if lex == '}' and tok == 'bracket_op': break
        parse_statement()
    parse_token('}', 'bracket_op')

def parse_decl():
    parse_token(None, 'keyword'); _, name, _ = get_symb(); parse_token(None, 'id')
    parse_token(':', 'punct'); _, type_mk, _ = get_symb(); parse_token(None, 'keyword') 
    parse_token('=', 'assign_op')
    cil_type = get_cil_type(type_mk)
    if current_context['scope_type'] == 'main':
        global_vars_table[name] = cil_type
        global_fields.append(f".field public static {cil_type} {name}")
        expr_type = parse_expression()
        if cil_type == 'float64' and expr_type == 'int32': gen("conv.r8")
        elif cil_type == 'int32' and expr_type == 'float64': gen("conv.i4")
        gen(f"stsfld {cil_type} Program::{name}")
    else:
        idx = current_context['local_idx']
        current_context['locals'][name] = (cil_type, idx)
        current_context['local_idx'] += 1
        expr_type = parse_expression()
        if cil_type == 'float64' and expr_type == 'int32': gen("conv.r8")
        elif cil_type == 'int32' and expr_type == 'float64': gen("conv.i4")
        gen(f"stloc {idx}")
    parse_token(';', 'punct')

def parse_assign():
    _, name, _ = get_symb(); parse_token(None, 'id'); _, next_l, _ = get_symb()
    if next_l == '(': 
        parse_token('(', 'bracket_op')
        if name not in func_signatures: fail_parse(f"Function '{name}' not declared", num_row)
        ret_type, expected_args = func_signatures[name]
        _parse_call_args(expected_args)
        parse_token(')', 'bracket_op'); parse_token(';', 'punct')
        args_sig = ", ".join(expected_args)
        gen(f"call {ret_type} Program::{name}({args_sig})")
        if ret_type != 'void': gen("pop")
        return
    parse_token('=', 'assign_op')
    expr_type = parse_expression()
    kind, typ, info = resolve_variable(name)
    if typ == 'float64' and expr_type == 'int32': gen("conv.r8")
    elif typ == 'int32' and expr_type == 'float64': gen("conv.i4")
    if kind == 'local': gen(f"stloc {info}")
    elif kind == 'arg': gen(f"starg {info}")
    elif kind == 'field': gen(f"stsfld {typ} Program::{info}")
    parse_token(';', 'punct')

def parse_fun_decl():
    global current_code, current_context
    parse_token('fun', 'keyword'); _, func_name, _ = get_symb(); parse_token(None, 'id')
    parse_token('(', 'bracket_op')
    new_context = {'scope_type': 'function', 'locals': {}, 'args': {}, 'local_idx': 0, 'name': func_name}
    new_context['locals']['__temp'] = ('float64', 0)
    new_context['local_idx'] = 1
    arg_types_cil = []; arg_idx = 0; _, l, _ = get_symb()
    if l != ')':
        while True:
            _, a_name, _ = get_symb(); parse_token(None, 'id')
            parse_token(':', 'punct'); _, a_type, _ = get_symb(); parse_token(None, 'keyword')
            c_type = get_cil_type(a_type)
            new_context['args'][a_name] = (c_type, arg_idx)
            arg_types_cil.append(c_type)
            arg_idx += 1
            _, comma, _ = get_symb()
            if comma == ',': parse_token(',', 'punct')
            else: break
    parse_token(')', 'bracket_op'); parse_token(':', 'punct'); _, r_lex, _ = get_symb(); parse_token(None, 'keyword')
    ret_type = get_cil_type(r_lex)
    func_signatures[func_name] = (ret_type, arg_types_cil)
    prev_context = current_context; current_context = new_context
    method_code_buffer = []; current_code = method_code_buffer 
    parse_block()
    if not method_code_buffer or "ret" not in method_code_buffer[-1]: gen("ret")
    args_str = ", ".join(arg_types_cil)
    full_method = f".method public static {ret_type} {func_name}({args_str}) cil managed\n{{\n    .maxstack 8\n"
    if new_context['locals']:
        full_method += "    .locals init (\n"
        sorted_vars = sorted(new_context['locals'].items(), key=lambda item: item[1][1])
        for i, (name, (typ, idx)) in enumerate(sorted_vars):
            comma = "," if i < len(sorted_vars)-1 else ""
            full_method += f"        [{idx}] {typ} {name}{comma}\n"
        full_method += "    )\n\n"
    full_method += "\n".join(method_code_buffer) + "\n}\n"
    generated_methods.append(full_method)
    current_context = prev_context; current_code = main_code

def parse_return():
    parse_token('return', 'keyword'); parse_expression(); gen("ret"); parse_token(';', 'punct')

def _parse_call_args(expected_types):
    arg_idx = 0; _, l, _ = get_symb()
    if l != ')':
        if arg_idx >= len(expected_types): fail_parse(f"Too many arguments", num_row)
        t = parse_expression(); check_and_convert_arg(t, expected_types[arg_idx]); arg_idx += 1
        while True:
            _, comma, _ = get_symb()
            if comma == ',': 
                parse_token(',', 'punct')
                if arg_idx >= len(expected_types): fail_parse(f"Too many arguments", num_row)
                t = parse_expression(); check_and_convert_arg(t, expected_types[arg_idx]); arg_idx += 1
            else: break
    if arg_idx != len(expected_types): fail_parse(f"Too few arguments", num_row)

def check_and_convert_arg(actual, expected):
    if actual == expected: return
    if expected == 'float64' and actual == 'int32': gen("conv.r8"); return
    fail_parse(f"Argument mismatch: expected {expected}, got {actual}", num_row)

def parse_if():
    parse_token('if', 'keyword'); parse_token('(', 'bracket_op'); parse_expression(); parse_token(')', 'bracket_op')
    lbl_else = createLabel(); lbl_end = createLabel()
    gen(f"brfalse {lbl_else}")
    parse_statement(); gen(f"br {lbl_end}"); setLabel(lbl_else)
    _, lex, _ = get_symb()
    if lex == 'else': parse_token('else', 'keyword'); parse_statement()
    setLabel(lbl_end)

def parse_while():
    lbl_start = createLabel(); lbl_end = createLabel()
    setLabel(lbl_start)
    parse_token('while', 'keyword'); parse_token('(', 'bracket_op'); parse_expression(); parse_token(')', 'bracket_op')
    gen(f"brfalse {lbl_end}")
    parse_statement(); gen(f"br {lbl_start}"); setLabel(lbl_end)

def parse_print():
    _, lex, _ = get_symb(); is_line = (lex == 'println')
    parse_token(lex, 'keyword'); parse_token('(', 'bracket_op')
    expr_type = parse_expression()
    method = "WriteLine" if is_line else "Write"
    arg = expr_type if expr_type in ('int32','float64','string','bool') else 'object'
    gen(f"call void [mscorlib]System.Console::{method}({arg})")
    parse_token(')', 'bracket_op'); parse_token(';', 'punct')

def parse_read_call():
    _, lex, _ = get_symb()
    parse_token(lex, 'keyword'); parse_token('(', 'bracket_op'); parse_token(')', 'bracket_op')
    gen("call string [mscorlib]System.Console::ReadLine()")
    if lex == 'readInt': gen("call int32 [mscorlib]System.Int32::Parse(string)"); return 'int32'
    if lex == 'readDouble': gen("call float64 [mscorlib]System.Double::Parse(string)"); return 'float64'
    return 'string'

def parse_expression(): return parse_relation()

# === ВИПРАВЛЕНА ФУНКЦІЯ parse_relation ===
def parse_relation():
    l_type = parse_sum()
    _, lex, tok = get_symb()
    if tok == 'rel_op':
        parse_token(lex, 'rel_op')
        r_type = parse_sum()
        
        # Конвертація для порівняння Int і Double
        if l_type == 'int32' and r_type == 'float64':
             gen("stloc 0"); gen("conv.r8"); gen("ldloc 0") 
        elif l_type == 'float64' and r_type == 'int32': gen("conv.r8")
        
        # Логіка порівнянь
        if lex == '>': gen("cgt")
        elif lex == '<': gen("clt")
        elif lex == '==': gen("ceq")
        elif lex == '!=': gen("ceq"); gen("ldc.i4.0"); gen("ceq")
        # --- ДОДАНО ---
        elif lex == '>=': 
            # a >= b  <=>  not (a < b)
            gen("clt"); gen("ldc.i4.0"); gen("ceq")
        elif lex == '<=': 
            # a <= b  <=>  not (a > b)
            gen("cgt"); gen("ldc.i4.0"); gen("ceq")
            
        return 'bool'
    return l_type

def parse_sum():
    l_type = parse_term()
    while True:
        _, lex, tok = get_symb()
        if tok == 'add_op':
            op = lex; parse_token(lex, 'add_op'); r_type = parse_term()
            if l_type == 'string' or r_type == 'string':
                if l_type != 'string': 
                    gen("stloc 0"); 
                    if l_type in ('int32','float64','bool'): gen(f"box [mscorlib]System.{l_type.capitalize().replace('32','32').replace('64','Double').replace('Bool','Boolean')}")
                    gen("ldloc 0")
                if r_type != 'string':
                    if r_type in ('int32','float64','bool'): gen(f"box [mscorlib]System.{r_type.capitalize().replace('32','32').replace('64','Double').replace('Bool','Boolean')}")
                gen("call string [mscorlib]System.String::Concat(object, object)")
                l_type = 'string'
            else:
                if l_type == 'int32' and r_type == 'float64': gen("stloc 0"); gen("conv.r8"); gen("ldloc 0"); l_type = 'float64'
                elif l_type == 'float64' and r_type == 'int32': gen("conv.r8"); l_type = 'float64'
                if op == '+': gen("add")
                else: gen("sub")
        else: break
    return l_type

def parse_term():
    l_type = parse_power()
    while True:
        _, lex, tok = get_symb()
        if tok == 'mult_op':
            op = lex; parse_token(lex, 'mult_op'); r_type = parse_power()
            if l_type == 'int32' and r_type == 'float64': gen("stloc 0"); gen("conv.r8"); gen("ldloc 0"); l_type = 'float64'
            elif l_type == 'float64' and r_type == 'int32': gen("conv.r8"); l_type = 'float64'
            if op == '*': gen("mul")
            elif op == '/': gen("div")
        else: break
    return l_type

def parse_power():
    l_type = parse_unary()
    while True:
        _, lex, tok = get_symb()
        if tok == 'power_op':
            parse_token('^', 'power_op')
            if l_type == 'int32': gen("conv.r8")
            r_type = parse_power()
            if r_type == 'int32': gen("conv.r8")
            gen("call float64 [mscorlib]System.Math::Pow(float64, float64)")
            return 'float64'
        else: break
    return l_type

def parse_unary():
    _, lex, tok = get_symb()
    if lex == '-' and tok == 'add_op':
        parse_token('-', 'add_op')
        t = parse_unary(); gen("neg"); return t
    return parse_primary()

# === ВИПРАВЛЕНА parse_primary: безпечна перевірка ===
def parse_primary():
    _, lex, tok = get_symb()
    if tok == 'int_literal': parse_token(lex, tok); gen(f"ldc.i4 {lex}"); return 'int32'
    elif tok == 'double_literal': parse_token(lex, tok); gen(f"ldc.r8 {lex}"); return 'float64'
    elif tok == 'string_literal': parse_token(lex, tok); clean_lex = lex.strip('"'); gen(f'ldstr "{clean_lex}"'); return 'string'
    elif tok == 'bool_literal': parse_token(lex, tok); val = 1 if lex=='true' else 0; gen(f"ldc.i4 {val}"); return 'bool'
    elif tok == 'id':
        parse_token(lex, 'id'); name = lex; _, next_l, _ = get_symb()
        if next_l == '(': 
            parse_token('(', 'bracket_op')
            if name not in func_signatures: fail_parse(f"Function '{name}' not declared", num_row)
            ret_type, args = func_signatures[name]; _parse_call_args(args)
            parse_token(')', 'bracket_op')
            gen(f"call {ret_type} Program::{name}({', '.join(args)})")
            return ret_type
        kind, typ, info = resolve_variable(name)
        if kind == 'local': gen(f"ldloc {info}")
        elif kind == 'arg': gen(f"ldarg {info}")
        elif kind == 'field': gen(f"ldsfld {typ} Program::{info}")
        return typ
    elif lex == '(':
        parse_token('(', 'bracket_op'); t = parse_expression(); parse_token(')', 'bracket_op'); return t
    elif lex in ('readInt', 'readDouble', 'readString'): return parse_read_call()
    
    # Якщо нічого не підійшло - падаємо з помилкою!
    fail_parse(f"Unexpected token in expression: '{lex}'", num_row)

def save_il(filename):
    fname = filename + ".il"
    try:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(f"// Generated IL Code for {filename}\n")
            f.write(".assembly extern mscorlib { .publickeytoken = (B7 7A 5C 56 19 34 E0 89 ) .ver 4:0:0:0 }\n")
            f.write(f".assembly {filename} {{ .hash algorithm 0x00008004 .ver 0:0:0:0 }}\n")
            f.write(f".module {filename}.exe\n\n")
            f.write(".class public auto ansi Program extends [mscorlib]System.Object\n{\n")
            if global_fields:
                f.write("\n    // --- Global Fields ---\n")
                for field in global_fields: f.write(f"    {field}\n")
                f.write("\n")
            if generated_methods:
                f.write("    // --- Functions ---\n")
                for method in generated_methods: f.write(method + "\n")
            f.write("    // --- Main Method ---\n")
            f.write("    .method public static void Main(string[] args) cil managed\n    {\n")
            f.write("        .entrypoint\n")
            f.write("        .maxstack 8\n")
            if current_context['locals']:
                f.write("        .locals init (\n")
                sorted_vars = sorted(current_context['locals'].items(), key=lambda item: item[1][1])
                for i, (name, (typ, idx)) in enumerate(sorted_vars):
                    comma = "," if i < len(sorted_vars)-1 else ""
                    f.write(f"            [{idx}] {typ} {name}{comma}\n")
                f.write("        )\n\n")
            for line in main_code: f.write(f"    {line}\n")
            f.write("        ret\n    }\n}\n")
        print(f"Generated: {fname}")
        print(f"\nТепер запустіть: ilasm {fname}")
    except Exception as e: print(f"Error saving file: {e}")

if __name__ == "__main__":
    print("Введіть назву файлу (без розширення .minikot):")
    file_base = input("> ").strip()
    if not file_base: file_base = "all_features"
    try:
        with open(file_base + ".minikot", "r", encoding="utf-8") as f:
            lex_minikot.source_code = f.read() + " "; lex_minikot.len_code = len(lex_minikot.source_code)
            lex_minikot.num_char = -1; lex_minikot.lex()
    except FileNotFoundError: print("File not found"); sys.exit(1)
    if len(lex_minikot.table_of_symb) > 0:
        parse_program()
        save_il(file_base)