import sys
import lex_minikot

num_row = 1
parse_depth = 0

def get_symb():
    global num_row
    if num_row > len(lex_minikot.table_of_symb):
        return (0, 'EOF', 'None')
    rec = lex_minikot.table_of_symb[num_row]
    return rec[0], rec[1], rec[2]

def fail_parse(expected, actual_lex, actual_tok, line):
    print(f"\nParser ERROR: Line {line}")
    print(f"\tUnexpected token: ('{actual_lex}', '{actual_tok}')")
    print(f"\tExpected: {expected}")
    sys.exit(1)

def parse_token(expected_lex, expected_tok):
    global num_row
    line, lex, tok = get_symb()
    lex_match = (expected_lex is None) or (lex == expected_lex)
    tok_match = (expected_tok is None) or (tok == expected_tok)
    
    indent = '  ' * parse_depth
    if lex_match and tok_match:
        print(f"{indent}MATCH: {lex} ({tok})")
        num_row += 1
        return True
    else:
        fail_parse(f"('{expected_lex}', '{expected_tok}')", lex, tok, line)
        return False

def log(msg):
    print(f"{'  ' * parse_depth}{msg}")

def parse_program():
    global parse_depth
    log("parse_program(): Syntax Check Started")
    parse_depth += 1
    try:
        while num_row <= len(lex_minikot.table_of_symb):
            parse_statement()
        print("\n>>> Синтаксичний аналіз завершено успішно! <<<")
    except SystemExit: pass

def parse_statement():
    global parse_depth
    log("parse_statement")
    parse_depth += 1
    _, lex, tok = get_symb()
    
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
        else: fail_parse("Statement Keyword", lex, tok, _)
    elif tok == 'id':
        parse_id_statement()
    elif tok == 'bracket_op' and lex == '{':
        parse_block()
    elif tok == 'EOF': sys.exit(0)
    else: fail_parse("Start of Statement", lex, tok, _)
    parse_depth -= 1

def parse_block():
    parse_token('{', 'bracket_op')
    while True:
        _, lex, tok = get_symb()
        if lex == '}' and tok == 'bracket_op': break
        parse_statement()
    parse_token('}', 'bracket_op')

def parse_id_statement():
    _, _, _ = get_symb()
    next_lex = None
    if num_row + 1 <= len(lex_minikot.table_of_symb):
        next_lex = lex_minikot.table_of_symb[num_row + 1][1]
    if next_lex == '(':
        parse_primary(); parse_token(';', 'punct')
    else:
        parse_assign()

def parse_var_decl():
    parse_token('var', 'keyword')
    parse_token(None, 'id')
    parse_token(':', 'punct')
    parse_type()
    parse_token('=', 'assign_op')
    parse_expression()
    parse_token(';', 'punct')

def parse_val_decl():
    parse_token('val', 'keyword')
    parse_token(None, 'id')
    parse_token(':', 'punct')
    parse_type()
    parse_token('=', 'assign_op')
    parse_expression()
    parse_token(';', 'punct')

def parse_const_decl():
    parse_token('const', 'keyword')
    parse_token(None, 'id')
    parse_token(':', 'punct')
    parse_type()
    parse_token('=', 'assign_op')
    parse_primary() 
    parse_token(';', 'punct')

def parse_fun_decl():
    parse_token('fun', 'keyword')
    parse_token(None, 'id')
    parse_token('(', 'bracket_op')
    _, lex, _ = get_symb()
    if lex != ')':
        parse_token(None, 'id'); parse_token(':', 'punct'); parse_type()
        while True:
            _, l, _ = get_symb()
            if l == ',':
                parse_token(',', 'punct')
                parse_token(None, 'id'); parse_token(':', 'punct'); parse_type()
            else: break
    parse_token(')', 'bracket_op')
    parse_token(':', 'punct')
    parse_type()
    parse_block()

def parse_type():
    _, lex, tok = get_symb()
    if lex in ('Int', 'Double', 'Boolean', 'String'): parse_token(lex, 'keyword')
    else: fail_parse("Unknown Type", _, lex)

def parse_assign():
    parse_token(None, 'id')
    parse_token('=', 'assign_op')
    parse_expression()
    parse_token(';', 'punct')

def parse_if():
    parse_token('if', 'keyword')
    parse_token('(', 'bracket_op')
    parse_expression()
    parse_token(')', 'bracket_op')
    parse_statement()
    _, lex, tok = get_symb()
    if lex == 'else': parse_token('else', 'keyword'); parse_statement()

def parse_while():
    parse_token('while', 'keyword')
    parse_token('(', 'bracket_op')
    parse_expression()
    parse_token(')', 'bracket_op')
    parse_statement()

def parse_return():
    parse_token('return', 'keyword')
    parse_expression()
    parse_token(';', 'punct')

def parse_print():
    _, lex, _ = get_symb()
    parse_token(lex, 'keyword')
    parse_token('(', 'bracket_op')
    parse_expression()
    parse_token(')', 'bracket_op')
    parse_token(';', 'punct')

def parse_expression(): parse_relation()
def parse_relation():
    parse_sum()
    _, lex, tok = get_symb()
    if tok == 'rel_op':
        parse_token(lex, 'rel_op'); parse_sum()

def parse_sum():
    parse_term()
    while True:
        _, lex, tok = get_symb()
        if tok == 'add_op':
            parse_token(lex, 'add_op'); parse_term()
        else: break

def parse_term():
    parse_power()
    while True:
        _, lex, tok = get_symb()
        if tok == 'mult_op':
            parse_token(lex, 'mult_op'); parse_power()
        else: break

def parse_power():
    parse_primary()
    _, lex, tok = get_symb()
    if tok == 'power_op':
        parse_token('^', 'power_op'); parse_power()

def parse_primary():
    _, lex, tok = get_symb()
    if tok in ('int_literal', 'double_literal', 'string_literal', 'bool_literal'):
        parse_token(lex, tok)
    elif tok == 'id':
        parse_token(lex, 'id')
        _, next_lex, _ = get_symb()
        if next_lex == '(':
            parse_token('(', 'bracket_op')
            _, pl, _ = get_symb()
            if pl != ')':
                parse_expression()
                while True:
                    _, l, _ = get_symb()
                    if l == ',':
                        parse_token(',', 'punct'); parse_expression()
                    else: break
            parse_token(')', 'bracket_op')
    elif lex == '(':
        parse_token('(', 'bracket_op')
        parse_expression()
        parse_token(')', 'bracket_op')
    elif lex in ('readInt', 'readDouble', 'readString'):
        parse_token(lex, 'keyword')
        parse_token('(', 'bracket_op')
        parse_token(')', 'bracket_op')
    else:
        fail_parse("Expression Expected", _, lex)

if __name__ == "__main__":
    lex_minikot.run_lexer("test_semantic.minikot")
    if len(lex_minikot.table_of_symb) > 0:
        parse_program()
