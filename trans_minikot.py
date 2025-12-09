import sys
import lex_minikot
import os

# ============================================
# Глобальні структури даних
# ============================================
num_row = 1

# Структура для зберігання даних про scope (область видимості)
# 'main' - це головна програма. Інші ключі - імена функцій.
scopes = {
    'main': {
        'code': [],
        'vars': {},      
        'labels': {},
        'params_count': 0
    }
}

current_scope = 'main'  # Поточна область видимості ('main' або ім'я функції)
global_vars = {}        # Список глобальних змінних (для .globVarList)
func_signatures = {}    # name -> (ret_type, param_count)
labelCounter = 0
generate_on = True

# ============================================
# Допоміжні функції
# ============================================

def get_symb():
    global num_row
    if num_row > len(lex_minikot.table_of_symb): return (0, 'EOF', 'None')
    rec = lex_minikot.table_of_symb[num_row]
    return rec[0], rec[1], rec[2]

def parse_token(expected_lex, expected_tok):
    global num_row
    line, lex, tok = get_symb()
    match_lex = (expected_lex is None) or (lex == expected_lex)
    match_tok = (expected_tok is None) or (tok == expected_tok)
    if match_lex and match_tok: num_row += 1; return True
    else: 
        print(f"Error line {line}: Exp {expected_lex}, Got {lex}"); sys.exit(1)

def gen(lex, tok):
    if generate_on:
        # Додаємо команду в код ПОТОЧНОГО scope
        scopes[current_scope]['code'].append((lex, tok))

def createLabel():
    global labelCounter; labelCounter += 1
    return f"m{labelCounter}"

def setLabel(label):
    gen(label, 'label'); gen(':', 'colon')
    # Зберігаємо мітку в поточний scope
    scopes[current_scope]['labels'][label] = 0 

# ============================================
# Парсер (Основна логіка)
# ============================================

def parse_program():
    try:
        while num_row <= len(lex_minikot.table_of_symb): parse_statement()
    except SystemExit: pass

def parse_statement():
    global num_row
    _, lex, tok = get_symb()
    if tok == 'keyword':
        if lex in ('var', 'val', 'const'): parse_decl()
        elif lex == 'if': parse_if()
        elif lex == 'while': parse_while()
        elif lex == 'return': parse_return()
        elif lex in ('print', 'println'): parse_print()
        elif lex in ('readInt', 'readDouble', 'readString'): 
            parse_read_call(); parse_token(';', 'punct')
        elif lex == 'fun': parse_fun_decl()
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
    # var x: Int = 10;
    parse_token(None, 'keyword'); _, name, _ = get_symb(); parse_token(None, 'id')
    parse_token(':', 'punct'); _, type_mk, _ = get_symb(); parse_token(None, 'keyword') 
    parse_token('=', 'assign_op')
    
    psm_type = 'int'
    if type_mk == 'Double': psm_type = 'float'
    elif type_mk == 'String': psm_type = 'string'
    elif type_mk == 'Boolean': psm_type = 'bool'
    
    # Додаємо змінну в поточний scope
    scopes[current_scope]['vars'][name] = psm_type
    
    # Якщо ми в main, це глобальна змінна
    if current_scope == 'main':
        global_vars[name] = psm_type

    gen(name, 'l-val')
    expr_type = parse_expression()
    if psm_type == 'float' and expr_type == 'int': gen('i2f', 'conv')
    gen('=', 'assign_op'); parse_token(';', 'punct')

def parse_assign():
    _, name, _ = get_symb(); parse_token(None, 'id'); _, next_l, _ = get_symb()
    
    # Виклик процедури (ігноруємо результат)
    if next_l == '(': 
         parse_token('(', 'bracket_op')
         _parse_call_args()
         parse_token(')', 'bracket_op'); parse_token(';', 'punct')
         gen(name, 'CALL')
         return

    parse_token('=', 'assign_op'); gen(name, 'l-val'); expr_type = parse_expression()
    
    # Шукаємо тип змінної (спочатку локально, потім глобально)
    var_type = scopes[current_scope]['vars'].get(name)
    if not var_type and name in global_vars:
        var_type = global_vars[name]
    if not var_type: var_type = 'int' # Default

    if var_type == 'float' and expr_type == 'int': gen('i2f', 'conv')
    gen('=', 'assign_op'); parse_token(';', 'punct')

def _parse_call_args():
    _, l, _ = get_symb()
    if l != ')':
        parse_expression()
        while True:
            _, comma, _ = get_symb()
            if comma == ',': parse_token(',', 'punct'); parse_expression()
            else: break

def parse_fun_decl():
    global current_scope
    
    parse_token('fun', 'keyword')
    _, func_name, _ = get_symb()
    parse_token(None, 'id')
    parse_token('(', 'bracket_op')
    
    # 1. Створюємо новий scope для функції
    current_scope = func_name
    scopes[func_name] = {
        'code': [],
        'vars': {},   # Важливо: Python 3.7+ зберігає порядок вставки. PSM цього вимагає!
        'labels': {},
        'params_count': 0
    }
    
    # 2. Парсимо параметри
    param_count = 0
    _, l, _ = get_symb()
    if l != ')':
        while True:
             _, p_name, _ = get_symb(); parse_token(None, 'id')
             parse_token(':', 'punct')
             _, p_type, _ = get_symb(); parse_token(None, 'keyword')
             
             psm_type = 'int'
             if p_type == 'Double': psm_type = 'float'
             elif p_type == 'Boolean': psm_type = 'bool'
             elif p_type == 'String': psm_type = 'string'
             
             # Додаємо параметр у vars (вони мають бути ПЕРШИМИ у списку)
             scopes[func_name]['vars'][p_name] = psm_type
             param_count += 1
             
             _, comma, _ = get_symb()
             if comma == ',': parse_token(',', 'punct')
             else: break

    parse_token(')', 'bracket_op')
    parse_token(':', 'punct')
    _, ret_lex, _ = get_symb()
    parse_token(None, 'keyword') 

    ret_type = 'int'
    if ret_lex == 'Double': ret_type = 'float'
    elif ret_lex == 'Boolean': ret_type = 'bool'
    elif ret_lex == 'String': ret_type = 'string'
    elif ret_lex == 'Unit': ret_type = 'void'
    
    func_signatures[func_name] = (ret_type, param_count)
    scopes[func_name]['params_count'] = param_count

    # 3. Парсимо тіло функції (код йде в scopes[func_name]['code'])
    parse_block()
    
    # 4. Додаємо RET в кінці (якщо void або забули)
    if not scopes[func_name]['code'] or scopes[func_name]['code'][-1][0] != 'RET':
         gen('RET', 'RET')

    # 5. Повертаємось в main scope
    current_scope = 'main'

def parse_return():
    parse_token('return', 'keyword')
    parse_expression() 
    gen('RET', 'RET') 
    parse_token(';', 'punct')

def parse_if():
    parse_token('if', 'keyword'); parse_token('(', 'bracket_op'); parse_expression(); parse_token(')', 'bracket_op')
    m1 = createLabel(); gen(m1, 'label'); gen('JF', 'jf')
    parse_statement() 
    m2 = createLabel(); gen(m2, 'label'); gen('JMP', 'jump'); setLabel(m1) 
    _, lex, _ = get_symb()
    if lex == 'else': parse_token('else', 'keyword'); parse_statement()
    setLabel(m2)

def parse_while():
    m1 = createLabel(); setLabel(m1)
    parse_token('while', 'keyword'); parse_token('(', 'bracket_op'); parse_expression(); parse_token(')', 'bracket_op')
    m2 = createLabel(); gen(m2, 'label'); gen('JF', 'jf')
    parse_statement(); gen(m1, 'label'); gen('JMP', 'jump'); setLabel(m2)

def parse_print():
    _, lex, _ = get_symb(); parse_token(lex, 'keyword'); parse_token('(', 'bracket_op')
    parse_expression(); gen('OUT', 'out_op')
    parse_token(')', 'bracket_op'); parse_token(';', 'punct')

def parse_read_call():
    _, lex, _ = get_symb()
    parse_token(lex, 'keyword'); parse_token('(', 'bracket_op'); parse_token(')', 'bracket_op')
    gen('INP', 'inp_op')
    if lex == 'readInt': gen('s2i', 'conv'); return 'int'
    if lex == 'readDouble': gen('s2f', 'conv'); return 'float'
    return 'string'

def parse_expression(): return parse_relation()
def parse_relation():
    l_type = parse_sum(); _, lex, tok = get_symb()
    if tok == 'rel_op':
        parse_token(lex, 'rel_op'); r_type = parse_sum()
        if l_type == 'int' and r_type == 'float':
            gen('SWAP', 'stack_op'); gen('i2f', 'conv'); gen('SWAP', 'stack_op')
        elif l_type == 'float' and r_type == 'int': gen('i2f', 'conv')
        gen(lex, 'rel_op'); return 'bool'
    return l_type

def parse_sum():
    l_type = parse_term()
    while True:
        _, lex, tok = get_symb()
        if tok == 'add_op':
            parse_token(lex, 'add_op'); r_type = parse_term()
            if l_type == 'int' and r_type == 'float':
                gen('SWAP', 'stack_op'); gen('i2f', 'conv'); gen('SWAP', 'stack_op'); l_type = 'float'
            elif l_type == 'float' and r_type == 'int': gen('i2f', 'conv'); r_type = 'float'
            gen(lex, 'math_op')
        else: break
    return l_type

def parse_term():
    l_type = parse_power()
    while True:
        _, lex, tok = get_symb()
        if tok == 'mult_op':
            parse_token(lex, 'mult_op'); r_type = parse_power()
            if l_type == 'int' and r_type == 'float':
                gen('SWAP', 'stack_op'); gen('i2f', 'conv'); gen('SWAP', 'stack_op'); l_type = 'float'
            elif l_type == 'float' and r_type == 'int': gen('i2f', 'conv'); r_type = 'float'
            gen(lex, 'math_op')
        else: break
    return l_type

def parse_power():
    l_type = parse_primary()
    _, lex, tok = get_symb()
    if tok == 'power_op':
        parse_token('^', 'power_op')
        
        # Рекурсивний виклик для правої частини
        r_type = parse_power() 
        
        # --- АВТОМАТИЧНА КОНВЕРТАЦІЯ ТИПІВ ДЛЯ PSM ---
        # PSM вимагає float для операції степеня.
        # Стек зараз: [..., l_val, r_val] (r_val зверху)
        
        # 1. Якщо лівий операнд int -> конвертуємо
        if l_type == 'int':
            gen('SWAP', 'stack_op') # [r, l]
            gen('i2f', 'conv')      # [r, l_float]
            gen('SWAP', 'stack_op') # [l_float, r]
            
        # 2. Якщо правий операнд int -> конвертуємо
        if r_type == 'int':
            gen('i2f', 'conv')      # [l_float, r_float]

        gen('^', 'pow_op')
        return 'float' # Результат завжди float
    return l_type

def parse_primary():
    _, lex, tok = get_symb()
    if tok == 'int_literal': parse_token(lex, tok); gen(lex, 'int'); return 'int'
    elif tok == 'double_literal': parse_token(lex, tok); gen(lex, 'float'); return 'float'
    elif tok == 'string_literal': parse_token(lex, tok); gen(f'"{lex}"', 'string'); return 'string'
    elif tok == 'bool_literal': parse_token(lex, tok); gen(lex.upper(), 'bool'); return 'bool'
    elif tok == 'id':
        parse_token(lex, 'id'); name = lex
        _, next_lex, _ = get_symb()
        if next_lex == '(':
            parse_token('(', 'bracket_op')
            _parse_call_args()
            parse_token(')', 'bracket_op')
            gen(name, 'CALL')
            return func_signatures.get(name, ('int', 0))[0]
        else:
            gen(lex, 'r-val')
            return scopes[current_scope]['vars'].get(lex, global_vars.get(lex, 'int'))
    elif lex == '(':
        parse_token('(', 'bracket_op'); t = parse_expression(); parse_token(')', 'bracket_op'); return t
    elif lex in ('readInt', 'readDouble', 'readString'): return parse_read_call()

# ============================================
# ГЕНЕРАЦІЯ ФАЙЛІВ ТА ЗАПУСК
# ============================================

def write_scope_to_file(filename, scope_name):
    data = scopes[scope_name]
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(".target: Postfix Machine\n.version: 0.2\n\n")
        f.write(".vars(\n")
        for k, v in data['vars'].items(): f.write(f"   {k} {v}\n")
        f.write(")\n\n")

        if scope_name != 'main':
             f.write(".globVarList(\n")
             for g in global_vars.keys(): f.write(f"   {g}\n")
             f.write(")\n\n")
        else:
            f.write(".funcs(\n")
            for k, v in func_signatures.items(): f.write(f"   {k} {v[0]} {v[1]}\n")
            f.write(")\n\n")

        f.write(".labels(\n"); 
        for k in data['labels'].keys(): f.write(f"   {k} 0\n")
        f.write(")\n\n")
        
        f.write(".code(\n")
        for (lex, tok) in data['code']: f.write(f"   {lex} {tok}\n")
        f.write(")\n")
    print(f"Generated: {filename}")

def save_postfix(base_filename):
    write_scope_to_file(base_filename + ".postfix", 'main')
    for name in scopes:
        if name != 'main':
            fname = f"{base_filename}${name}.postfix"
            write_scope_to_file(fname, name)

if __name__ == "__main__":
    print("Введіть назву файлу (без розширення):")
    file_base = input("> ").strip()
    if not file_base: file_base = "test_semantic"
    
    try:
        with open(file_base + ".minikot", "r", encoding="utf-8") as f:
            lex_minikot.source_code = f.read() + " "
            lex_minikot.len_code = len(lex_minikot.source_code)
            lex_minikot.num_char = -1
            lex_minikot.lex()
    except FileNotFoundError:
        print("File not found"); sys.exit(1)
        
    if len(lex_minikot.table_of_symb) > 0:
        parse_program()
        save_postfix(file_base)
        
        # --- АВТОМАТИЧНИЙ ЗАПУСК PSM ---
        print("\n--- EXECUTION (PSM) ---")
        # Використовуємо той самий python інтерпретатор для запуску
        command = f"{sys.executable} PSM.py -p . -m {file_base} --symbolic-labels"
        os.system(command)