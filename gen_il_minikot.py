import sys
import lex_minikot
import os

# ==========================================
# ГЛОБАЛЬНІ ЗМІННІ
# ==========================================
num_row = 1
ilCode = []          
var_table = {}       # {name: (type, index)}
labelCounter = 0
local_var_index = 1  # Починаємо з 1, бо 0 зарезервовано під __temp

# Резервуємо змінну для swap операцій (float64)
# Вона буде завжди під індексом 0
var_table['__temp'] = ('float64', 0)

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
    ilCode.append(str(code))

def createLabel():
    global labelCounter
    labelCounter += 1
    return f"L_{labelCounter}"

def setLabel(label):
    gen(f"{label}:")

# ==========================================
# ПАРСЕР + ГЕНЕРАТОР CIL
# ==========================================

def parse_program():
    print(">>> Generating IL Code...")
    try:
        while num_row <= len(lex_minikot.table_of_symb):
            parse_statement()
        print(">>> Generation Done!")
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
        elif lex == 'fun': parse_fun_skip()
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
    global local_var_index
    parse_token(None, 'keyword')
    _, name, _ = get_symb()
    parse_token(None, 'id'); parse_token(':', 'punct')
    _, type_mk, _ = get_symb(); parse_token(None, 'keyword') 
    parse_token('=', 'assign_op')
    
    cil_type = 'int32'
    if type_mk == 'Double': cil_type = 'float64'
    elif type_mk == 'String': cil_type = 'string'
    elif type_mk == 'Boolean': cil_type = 'bool'
    
    var_table[name] = (cil_type, local_var_index)
    local_var_index += 1
    
    expr_type = parse_expression()
    
    if cil_type == 'float64' and expr_type == 'int32':
        gen("    conv.r8")
        
    idx = var_table[name][1]
    gen(f"    stloc {idx}")
    
    parse_token(';', 'punct')

def parse_assign():
    _, name, _ = get_symb(); parse_token(None, 'id')
    _, next_l, _ = get_symb()
    if next_l == '(': 
         while True:
             global num_row
             num_row += 1
             l, _, _ = get_symb()
             if l == ';': break
         return

    parse_token('=', 'assign_op')
    expr_type = parse_expression()
    
    if name in var_table:
        cil_type, idx = var_table[name]
        if cil_type == 'float64' and expr_type == 'int32':
            gen("    conv.r8")
        gen(f"    stloc {idx}")
    
    parse_token(';', 'punct')

def parse_print():
    _, lex, _ = get_symb()
    is_line = (lex == 'println')
    parse_token(lex, 'keyword'); parse_token('(', 'bracket_op')
    
    expr_type = parse_expression()
    
    method = "WriteLine" if is_line else "Write"
    
    if expr_type == 'int32': arg = 'int32'
    elif expr_type == 'float64': arg = 'float64'
    elif expr_type == 'bool': arg = 'bool'
    else: arg = 'string'
    
    gen(f"    call void [mscorlib]System.Console::{method}({arg})")
    
    parse_token(')', 'bracket_op'); parse_token(';', 'punct')

def parse_read_call():
    _, lex, _ = get_symb()
    parse_token(lex, 'keyword'); parse_token('(', 'bracket_op'); parse_token(')', 'bracket_op')
    
    gen("    call string [mscorlib]System.Console::ReadLine()")
    
    if lex == 'readInt': 
        gen("    call int32 [mscorlib]System.Int32::Parse(string)")
        return 'int32'
    if lex == 'readDouble': 
        gen("    call float64 [mscorlib]System.Double::Parse(string)")
        return 'float64'
    return 'string'

def parse_if():
    parse_token('if', 'keyword'); parse_token('(', 'bracket_op')
    parse_expression(); parse_token(')', 'bracket_op')
    
    lbl_else = createLabel()
    lbl_end = createLabel()
    
    gen(f"    brfalse {lbl_else}")
    parse_statement() 
    gen(f"    br {lbl_end}")
    gen(f"{lbl_else}:")
    _, lex, _ = get_symb()
    if lex == 'else':
        parse_token('else', 'keyword')
        parse_statement()
    gen(f"{lbl_end}:")

def parse_while():
    lbl_start = createLabel()
    lbl_end = createLabel()
    gen(f"{lbl_start}:")
    parse_token('while', 'keyword'); parse_token('(', 'bracket_op')
    parse_expression(); parse_token(')', 'bracket_op')
    gen(f"    brfalse {lbl_end}")
    parse_statement()
    gen(f"    br {lbl_start}")
    gen(f"{lbl_end}:")

def parse_fun_skip():
    global num_row
    while True:
        _, l, _ = get_symb()
        num_row += 1
        if l == '}': break

def parse_expression(): return parse_relation()

def parse_relation():
    l_type = parse_sum()
    _, lex, tok = get_symb()
    if tok == 'rel_op':
        parse_token(lex, 'rel_op')
        r_type = parse_sum()
        
        # Конвертація для порівняння (Int vs Double)
        if l_type == 'int32' and r_type == 'float64':
             # Stack: [int, float] -> save float, conv int, load float
             gen("    stloc 0") # Save top (float) to __temp
             gen("    conv.r8") # Convert int
             gen("    ldloc 0") # Load float back
        elif l_type == 'float64' and r_type == 'int32':
             gen("    conv.r8") # Simple: convert top

        if lex == '>': gen("    cgt")
        elif lex == '<': gen("    clt")
        elif lex == '==': gen("    ceq")
        return 'bool'
    return l_type

def parse_sum():
    l_type = parse_term()
    while True:
        _, lex, tok = get_symb()
        if tok == 'add_op':
            op = lex
            parse_token(lex, 'add_op')
            r_type = parse_term()
            
            if l_type == 'string' or r_type == 'string':
                gen("    call string [mscorlib]System.String::Concat(string, string)")
                l_type = 'string'
            else:
                # Математика змішаних типів (ВИПРАВЛЕНО)
                if l_type == 'int32' and r_type == 'float64':
                    # Stack: [int, float]. Need [float, float]
                    gen("    stloc 0") # __temp = float
                    gen("    conv.r8") # int -> float
                    gen("    ldloc 0") # push __temp
                    l_type = 'float64'
                elif l_type == 'float64' and r_type == 'int32':
                    # Stack: [float, int]. Need [float, float]
                    gen("    conv.r8")
                    l_type = 'float64' # Result is float
                
                if op == '+': gen("    add")
                else: gen("    sub")
        else: break
    return l_type

def parse_term():
    l_type = parse_power()
    while True:
        _, lex, tok = get_symb()
        if tok == 'mult_op':
            op = lex
            parse_token(lex, 'mult_op')
            r_type = parse_power()
            
            if l_type == 'int32' and r_type == 'float64':
                gen("    stloc 0")
                gen("    conv.r8")
                gen("    ldloc 0")
                l_type = 'float64'
            elif l_type == 'float64' and r_type == 'int32':
                gen("    conv.r8")
                l_type = 'float64'

            if op == '*': gen("    mul")
            elif op == '/': gen("    div")
        else: break
    return l_type

def parse_power():
    l_type = parse_primary()
    _, lex, tok = get_symb()
    if tok == 'power_op':
        parse_token('^', 'power_op')
        if l_type == 'int32': gen("    conv.r8")
        
        r_type = parse_power()
        if r_type == 'int32': gen("    conv.r8")
        
        gen("    call float64 [mscorlib]System.Math::Pow(float64, float64)")
        return 'float64'
    return l_type

def parse_primary():
    _, lex, tok = get_symb()
    if tok == 'int_literal':
        parse_token(lex, tok); gen(f"    ldc.i4 {lex}"); return 'int32'
    elif tok == 'double_literal':
        parse_token(lex, tok); gen(f"    ldc.r8 {lex}"); return 'float64'
    elif tok == 'string_literal':
        clean_lex = lex.strip('"')
        parse_token(lex, tok); gen(f'    ldstr "{clean_lex}"'); return 'string'
    elif tok == 'bool_literal':
        parse_token(lex, tok)
        val = 1 if lex == 'true' else 0
        gen(f"    ldc.i4 {val}")
        return 'bool'
    elif tok == 'id':
        parse_token(lex, 'id')
        if lex in var_table:
            _, idx = var_table[lex]
            gen(f"    ldloc {idx}")
            return var_table[lex][0]
        return 'int32'
    elif lex == '(':
        parse_token('(', 'bracket_op'); t = parse_expression(); parse_token(')', 'bracket_op'); return t
    elif lex in ('readInt', 'readDouble', 'readString'): return parse_read_call()
    return 'void'

# --- Збереження ---
def save_il(filename):
    fname = filename + ".il"
    with open(fname, 'w', encoding='utf-8') as f:
        f.write("// MiniKot to IL Generator\n")
        f.write(".assembly extern mscorlib { .publickeytoken = (B7 7A 5C 56 19 34 E0 89 ) .ver 4:0:0:0 }\n")
        f.write(f".assembly {filename} {{ .hash algorithm 0x00008004 .ver 0:0:0:0 }}\n")
        f.write(f".module {filename}.exe\n\n")
        
        f.write(".class private auto ansi beforefieldinit Program extends [mscorlib]System.Object\n{\n")
        f.write("  .method private hidebysig static void Main(string[] args) cil managed\n  {\n")
        f.write("    .entrypoint\n")
        f.write("    .maxstack 8\n")
        
        if var_table:
            f.write("    .locals init (\n")
            sorted_vars = sorted(var_table.items(), key=lambda item: item[1][1])
            for i, (name, (typ, idx)) in enumerate(sorted_vars):
                comma = "," if i < len(sorted_vars)-1 else ""
                f.write(f"      [{idx}] {typ} {name}{comma}\n")
            f.write("    )\n\n")
        
        for line in ilCode:
            f.write(f"{line}\n")
            
        f.write("    ret\n")
        f.write("  }\n}\n")
    print(f"Generated: {fname}")

if __name__ == "__main__":
    import os
    print("Введіть назву файлу (без розширення .minikot):")
    file_base = input("> ").strip()
    if not file_base: file_base = "test_semantic"
    
    try:
        with open(file_base + ".minikot", "r", encoding="utf-8") as f:
            lex_minikot.source_code = f.read() + " "; lex_minikot.len_code = len(lex_minikot.source_code)
            lex_minikot.num_char = -1; lex_minikot.lex()
    except FileNotFoundError: print("File not found"); sys.exit(1)
    
    if len(lex_minikot.table_of_symb) > 0:
        parse_program()
        save_il(file_base)