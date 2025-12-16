import sys
import lex_minikot

num_row = 1
var_table = {} 
# Структура var_table:
# Для змінних: name -> ('var'/'val'/'const', type)
# Для функцій: name -> ('fun', return_type, [arg_types_list])

def get_symb():
    global num_row
    if num_row > len(lex_minikot.table_of_symb):
        return (0, 'EOF', 'None')
    rec = lex_minikot.table_of_symb[num_row]
    return rec[0], rec[1], rec[2] 

def fail_parse(msg, line, lex=None):
    print(f"\nSemantic ERROR: Line {line}")
    if lex: print(f"\tContext: {lex}")
    print(f"\tMessage: {msg}")
    sys.exit(1)

def parse_token(expected_lex, expected_tok):
    global num_row
    line, lex, tok = get_symb()
    lex_match = (expected_lex is None) or (lex == expected_lex)
    tok_match = (expected_tok is None) or (tok == expected_tok)
    if lex_match and tok_match:
        num_row += 1
        return True
    else:
        fail_parse(f"Expected '{expected_lex}'/'{expected_tok}', got '{lex}'/'{tok}'", line)
        return False

def parse_program():
    print("parse_program(): Semantic Check Started")
    try:
        while num_row <= len(lex_minikot.table_of_symb):
            parse_statement()
        print("\n>>> Семантичний аналіз завершено успішно! <<<")
    except SystemExit: pass

def parse_statement():
    line, lex, tok = get_symb()
    if tok == 'keyword':
        if lex == 'var': parse_var_decl()
        elif lex == 'val': parse_val_decl()
        elif lex == 'const': parse_const_decl()
        elif lex == 'fun': parse_fun_decl()
        elif lex == 'if': parse_if()
        elif lex == 'while': parse_while()
        elif lex == 'return': parse_return()
        elif lex in ('print', 'println'): parse_print()
        elif lex in ('readInt', 'readDouble', 'readString'): 
             parse_primary(); parse_token(';', 'punct')
        else: fail_parse("Unknown keyword", line, lex)
    elif tok == 'id':
        parse_id_statement()
    elif tok == 'bracket_op' and lex == '{':
        parse_block()
    elif tok == 'EOF': sys.exit(0)
    else: fail_parse("Statement expected", line, lex)

def parse_block():
    parse_token('{', 'bracket_op')
    while True:
        _, lex, tok = get_symb()
        if lex == '}' and tok == 'bracket_op': break
        parse_statement()
    parse_token('}', 'bracket_op')

def parse_id_statement():
    line, name, _ = get_symb()
    next_lex = None
    if num_row + 1 <= len(lex_minikot.table_of_symb):
        next_lex = lex_minikot.table_of_symb[num_row + 1][1]
    if next_lex == '(':
        # Виклик функції як окрема інструкція (ігноруємо результат)
        parse_primary(); parse_token(';', 'punct')
    else:
        parse_assign()

def parse_var_decl():
    parse_token('var', 'keyword')
    line, name, _ = get_symb()
    parse_token(None, 'id')
    if name in var_table: fail_parse(f"Variable '{name}' is already declared", line)
    parse_token(':', 'punct')
    _, type_lex, _ = get_symb()
    parse_type()
    parse_token('=', 'assign_op')
    expr_type = parse_expression()
    if type_lex != expr_type:
        if not (type_lex == 'Double' and expr_type == 'Int'):
             fail_parse(f"Type mismatch: Cannot assign {expr_type} to {type_lex}", line, name)
    var_table[name] = ('var', type_lex)
    print(f"  Declared var: {name} : {type_lex}")
    parse_token(';', 'punct')

def parse_val_decl():
    parse_token('val', 'keyword')
    line, name, _ = get_symb()
    parse_token(None, 'id')
    if name in var_table: fail_parse(f"Variable '{name}' is already declared", line)
    parse_token(':', 'punct')
    _, type_lex, _ = get_symb()
    parse_type()
    parse_token('=', 'assign_op')
    expr_type = parse_expression()
    if type_lex != expr_type:
        if not (type_lex == 'Double' and expr_type == 'Int'):
             fail_parse(f"Type mismatch: Cannot assign {expr_type} to {type_lex}", line, name)
    var_table[name] = ('val', type_lex)
    print(f"  Declared val: {name} : {type_lex}")
    parse_token(';', 'punct')

def parse_const_decl():
    parse_token('const', 'keyword')
    line, name, _ = get_symb()
    parse_token(None, 'id')
    if name in var_table: fail_parse(f"Constant '{name}' is already declared", line)
    parse_token(':', 'punct')
    _, type_lex, _ = get_symb()
    parse_type()
    parse_token('=', 'assign_op')
    expr_type = parse_primary() 
    if type_lex != expr_type: fail_parse(f"Type mismatch: Constant {name} expects {type_lex}, got {expr_type}", line)
    var_table[name] = ('const', type_lex)
    print(f"  Declared const: {name} : {type_lex}")
    parse_token(';', 'punct')

def parse_fun_decl():
    parse_token('fun', 'keyword')
    _, func_name, _ = get_symb()
    parse_token(None, 'id')
    
    if func_name in var_table:
        fail_parse(f"Function '{func_name}' is already declared", num_row)

    parse_token('(', 'bracket_op')
    
    param_types = []
    local_params = [] # Список для запам'ятовування параметрів, щоб потім їх видалити
    
    _, lex, _ = get_symb()
    if lex != ')':
        # --- 1. Парсимо перший параметр ---
        _, p_name, _ = get_symb() # Запам'ятовуємо ім'я
        parse_token(None, 'id')
        parse_token(':', 'punct')
        _, p_type, _ = get_symb() # Запам'ятовуємо тип
        parse_type()
        
        # ДОДАЄМО В ТАБЛИЦЮ, щоб тіло функції "бачило" цю змінну
        if p_name in var_table:
             fail_parse(f"Parameter '{p_name}' shadows global variable", num_row)
        var_table[p_name] = ('var', p_type)
        
        param_types.append(p_type)
        local_params.append(p_name)
        
        while True:
            _, l, _ = get_symb()
            if l == ',':
                parse_token(',', 'punct')
                
                # --- 2. Парсимо наступні параметри ---
                _, p_name, _ = get_symb()
                parse_token(None, 'id')
                parse_token(':', 'punct')
                _, p_type, _ = get_symb()
                parse_type()
                
                if p_name in var_table:
                    fail_parse(f"Parameter '{p_name}' shadows global variable", num_row)
                var_table[p_name] = ('var', p_type)
                
                param_types.append(p_type)
                local_params.append(p_name)
            else: break
            
    parse_token(')', 'bracket_op')
    parse_token(':', 'punct')
    _, ret_type, _ = get_symb()
    parse_type()
    
    # Реєструємо саму функцію
    var_table[func_name] = ('fun', ret_type, param_types)
    print(f"  Declared fun: {func_name} ({', '.join(param_types)}) -> {ret_type}")
    
    # Парсимо тіло функції (тепер змінні x та y є у var_table)
    parse_block()
    
    # --- ОЧИЩЕННЯ ---
    # Після виходу з функції видаляємо параметри з таблиці, 
    # щоб вони не були видимі зовні (імітація локальної видимості)
    for p_name in local_params:
        if p_name in var_table:
            del var_table[p_name]

def parse_type():
    _, lex, tok = get_symb()
    if lex in ('Int', 'Double', 'Boolean', 'String'): parse_token(lex, 'keyword')
    else: fail_parse("Unknown Type", _, lex)

def parse_assign():
    line, name, _ = get_symb()
    parse_token(None, 'id')
    if name not in var_table: fail_parse(f"Variable '{name}' is not declared", line)
    
    rec = var_table[name]
    if rec[0] == 'fun': fail_parse(f"Cannot assign to function '{name}'", line)
    cat, var_type = rec

    if cat in ('val', 'const'): fail_parse(f"Cannot reassign constant/val '{name}'", line)
    parse_token('=', 'assign_op')
    expr_type = parse_expression()
    if var_type != expr_type:
        if not (var_type == 'Double' and expr_type == 'Int'):
            fail_parse(f"Type mismatch: Cannot assign {expr_type} to {var_type}", line, name)
    parse_token(';', 'punct')

def parse_if():
    parse_token('if', 'keyword')
    parse_token('(', 'bracket_op')
    cond_type = parse_expression()
    if cond_type != 'Boolean': fail_parse(f"Condition in 'if' must be Boolean, got {cond_type}", num_row)
    parse_token(')', 'bracket_op')
    parse_statement()
    _, lex, tok = get_symb()
    if lex == 'else': parse_token('else', 'keyword'); parse_statement()

def parse_while():
    parse_token('while', 'keyword')
    parse_token('(', 'bracket_op')
    cond_type = parse_expression()
    if cond_type != 'Boolean': fail_parse(f"Condition in 'while' must be Boolean, got {cond_type}", num_row)
    parse_token(')', 'bracket_op')
    parse_statement()

def parse_return():
    parse_token('return', 'keyword')
    parse_expression() # Тут можна додати перевірку відповідності типу повернення
    parse_token(';', 'punct')

def parse_print():
    _, lex, _ = get_symb()
    parse_token(lex, 'keyword')
    parse_token('(', 'bracket_op')
    parse_expression()
    parse_token(')', 'bracket_op')
    parse_token(';', 'punct')

def parse_expression(): return parse_relation()

def parse_relation():
    left_type = parse_sum()
    _, lex, tok = get_symb()
    if tok == 'rel_op':
        parse_token(lex, 'rel_op')
        right_type = parse_sum()
        
        # Сувора перевірка типів для порівняння
        is_num_l = left_type in ('Int', 'Double')
        is_num_r = right_type in ('Int', 'Double')

        if is_num_l and right_type == 'String': fail_parse("Cannot compare Number with String", num_row)
        if left_type == 'String' and is_num_r: fail_parse("Cannot compare String with Number", num_row)
        if left_type == 'Boolean' and right_type != 'Boolean': fail_parse("Boolean can only be compared with Boolean", num_row)

        return 'Boolean' 
    return left_type

def parse_sum():
    left_type = parse_term()
    while True:
        _, lex, tok = get_symb()
        if tok == 'add_op':
            op = lex
            parse_token(lex, 'add_op')
            right_type = parse_term()
            if left_type == 'String' or right_type == 'String':
                if op == '+': left_type = 'String'
                else: fail_parse("Cannot subtract Strings", num_row)
            elif left_type == 'Boolean' or right_type == 'Boolean':
                fail_parse("Arithmetic on Booleans not supported", num_row)
            elif left_type == 'Double' or right_type == 'Double': left_type = 'Double'
            else: left_type = 'Int'
        else: break
    return left_type

def parse_term():
    left_type = parse_power()
    while True:
        _, lex, tok = get_symb()
        if tok == 'mult_op':
            parse_token(lex, 'mult_op')
            right_type = parse_power()
            if 'String' in (left_type, right_type) or 'Boolean' in (left_type, right_type):
                 fail_parse("Invalid types for mult/div", num_row)
            if left_type == 'Double' or right_type == 'Double': left_type = 'Double'
            else: left_type = 'Int'
        else: break
    return left_type

def parse_power():
    left_type = parse_primary()
    _, lex, tok = get_symb()
    if tok == 'power_op':
        parse_token('^', 'power_op')
        right_type = parse_power() # Рекурсія (правоасоціативність)
        
        # Перевірка: степінь можна брати тільки від чисел
        is_num_l = left_type in ('Int', 'Double')
        is_num_r = right_type in ('Int', 'Double')
        
        if not is_num_l or not is_num_r:
             fail_parse(f"Power operation requires numeric types, got {left_type} ^ {right_type}", num_row)
             
        # ЗМІНА ТУТ:
        # Якщо обидва операнди Int -> результат Int
        if left_type == 'Int' and right_type == 'Int':
            return 'Int'
            
        # Якщо хоча б один Double -> результат Double
        return 'Double' 
    return left_type

def parse_primary():
    line, lex, tok = get_symb()
    if tok == 'int_literal': parse_token(lex, tok); return 'Int'
    elif tok == 'double_literal': parse_token(lex, tok); return 'Double'
    elif tok == 'string_literal': parse_token(lex, tok); return 'String'
    elif tok == 'bool_literal': parse_token(lex, tok); return 'Boolean'
    
    elif tok == 'id':
        parse_token(lex, 'id')
        name = lex
        if name not in var_table: fail_parse(f"Identifier '{name}' is not declared", line)
        
        record = var_table[name]
        kind = record[0]
        declared_type = record[1]

        _, next_lex, _ = get_symb()
        if next_lex == '(':
            # Це виклик функції
            if kind != 'fun': fail_parse(f"Variable '{name}' is not a function", line)
            
            expected_args = record[2]
            parse_token('(', 'bracket_op')
            
            arg_count = 0
            _, pl, _ = get_symb()
            if pl != ')':
                # Перший аргумент
                if arg_count >= len(expected_args): fail_parse(f"Too many arguments for '{name}'", line)
                arg_type = parse_expression()
                exp_type = expected_args[arg_count]
                
                if arg_type != exp_type and not (arg_type == 'Int' and exp_type == 'Double'):
                     fail_parse(f"Argument mismatch: expected {exp_type}, got {arg_type}", line)
                arg_count += 1
                
                while True:
                    _, l, _ = get_symb()
                    if l == ',':
                        parse_token(',', 'punct')
                        if arg_count >= len(expected_args): fail_parse(f"Too many arguments for '{name}'", line)
                        arg_type = parse_expression()
                        exp_type = expected_args[arg_count]
                        if arg_type != exp_type and not (arg_type == 'Int' and exp_type == 'Double'):
                            fail_parse(f"Argument mismatch: expected {exp_type}, got {arg_type}", line)
                        arg_count += 1
                    else: break
            parse_token(')', 'bracket_op')
            
            if arg_count != len(expected_args):
                 fail_parse(f"Function '{name}' expects {len(expected_args)} args, got {arg_count}", line)
            return declared_type
        else:
            # Звичайна змінна
            if kind == 'fun': fail_parse(f"Function '{name}' must be called with ()", line)
            return declared_type

    elif lex == '(':
        parse_token('(', 'bracket_op')
        t = parse_expression()
        parse_token(')', 'bracket_op')
        return t
    elif lex in ('readInt', 'readDouble', 'readString'):
        parse_token(lex, 'keyword')
        parse_token('(', 'bracket_op')
        parse_token(')', 'bracket_op')
        if lex == 'readInt': return 'Int'
        if lex == 'readDouble': return 'Double'
        if lex == 'readString': return 'String'
    fail_parse("Expression Expected", line, lex)
    return 'Error'

if __name__ == "__main__":
    lex_minikot.run_lexer("test_semantic.minikot")
    if len(lex_minikot.table_of_symb) > 0:
        parse_program()