import sys

# ==========================================
# ТАБЛИЦІ ЛЕКСЕМ ТА АВТОМАТ
# ==========================================

token_table = {
    'var': 'keyword', 'val': 'keyword', 'const': 'keyword', 'fun': 'keyword',
    'return': 'keyword', 'if': 'keyword', 'else': 'keyword', 'while': 'keyword',
    'Int': 'keyword', 'Double': 'keyword', 'Boolean': 'keyword', 'String': 'keyword',
    'print': 'keyword', 'println': 'keyword', 
    'readInt': 'keyword', 'readDouble': 'keyword', 'readString': 'keyword',
    'true': 'bool_literal', 'false': 'bool_literal',
    '=': 'assign_op',
    '+': 'add_op', '-': 'add_op', '*': 'mult_op', '/': 'mult_op', '^': 'power_op',
    '==': 'rel_op', '!=': 'rel_op', '<': 'rel_op', '>': 'rel_op', '<=': 'rel_op', '>=': 'rel_op',
    '(': 'bracket_op', ')': 'bracket_op', '{': 'bracket_op', '}': 'bracket_op',
    ':': 'punct', ',': 'punct', ';': 'punct'
}

stf = {
    (0, 'Letter'): 1, (1, 'Letter'): 1, (1, 'Digit'): 1, (1, '_'): 1, (1, 'other'): 2,
    (0, 'Digit'): 3, (3, 'Digit'): 3, (3, 'dot'): 4, (3, 'other'): 5,
    (4, 'Digit'): 6, (4, 'other'): 102, 
    (6, 'Digit'): 6, (6, 'other'): 7,
    (0, '"'): 8, (8, 'other'): 8, (8, '"'): 9, (8, 'nl'): 101,
    (0, '='): 11, (11, '='): 12, (11, 'other'): 100,
    (0, '!'): 13, (13, '='): 14, (13, 'other'): 103,
    (0, '<'): 15, (15, '='): 16, (15, 'other'): 100,
    (0, '>'): 17, (17, '='): 16, (17, 'other'): 100,
    (0, '/'): 18, (18, '/'): 19, (18, 'other'): 20, 
    (19, 'nl'): 0, (19, 'other'): 19,
    (0, '+'): 100, (0, '-'): 100, (0, '*'): 100, (0, '^'): 100,
    (0, '('): 100, (0, ')'): 100, (0, '{'): 100, (0, '}'): 100,
    (0, ':'): 100, (0, ','): 100, (0, ';'): 100,
    (0, 'ws'): 0, (0, 'nl'): 0
}

# ==========================================
# ГЛОБАЛЬНІ ЗМІННІ
# ==========================================
source_code = ""
len_code = 0
num_char = -1
num_line = 1
state = 0
lexeme = ""
table_of_symb = {}
table_of_id = {}
table_of_const = {}

# ==========================================
# ФУНКЦІЇ ЛЕКСЕРА
# ==========================================

def next_char():
    global num_char
    num_char += 1
    if num_char >= len_code: return ""
    return source_code[num_char]

def put_char_back():
    global num_char
    num_char -= 1

def class_of_char(char):
    if char in " \t": return "ws"
    if char in "\n\r": return "nl"
    if 'a' <= char <= 'z' or 'A' <= char <= 'Z': return "Letter"
    if '0' <= char <= '9': return "Digit"
    if char == '.': return "dot"
    if char == '"': return '"'
    if char == '_': return "_"
    if char in "+-*/^=!<>()[]{}:,;<>": return char 
    return "other"

def next_state(state, class_ch):
    try:
        return stf[(state, class_ch)]
    except KeyError:
        return stf.get((state, 'other'), 103)

def is_final(state):
    return state in (2, 5, 7, 9, 12, 14, 16, 20, 100, 101, 102, 103)

def add_record(token, idx=None):
    rec_id = len(table_of_symb) + 1
    table_of_symb[rec_id] = (num_line, lexeme, token, idx)
    print(f"{num_line:<4} {lexeme:<16} {token:<16} {idx if idx else ''}")

def fail(err_code):
    print(f"Lexer Error: line {num_line}, Code {err_code}")
    sys.exit(1)

def processing():
    global state, lexeme
    
    if state in (101, 102, 103):
        fail(state)

    if state in (2, 5, 7, 20):
        put_char_back()
        lexeme = lexeme[:-1]
    
    # Обробка стану 100 (прості оператори)
    if state == 100:
        if len(lexeme) > 1:
            put_char_back()
            lexeme = lexeme[:-1]
        elif lexeme == "":
            # Якщо перехід був прямим, беремо поточний символ
            lexeme = source_code[num_char]

    token = None
    if state == 2: 
        token = token_table.get(lexeme, 'id')
        if token == 'id':
            idx = table_of_id.setdefault(lexeme, len(table_of_id) + 1)
            add_record('id', idx)
        elif token == 'bool_literal':
             idx = table_of_const.setdefault(lexeme, ('bool', len(table_of_const) + 1))[1]
             add_record(token, idx)
        else:
            add_record(token)
    elif state == 5:
        idx = table_of_const.setdefault(lexeme, ('int', len(table_of_const) + 1))[1]
        add_record('int_literal', idx)
    elif state == 7:
        idx = table_of_const.setdefault(lexeme, ('double', len(table_of_const) + 1))[1]
        add_record('double_literal', idx)
    elif state == 9:
        val = lexeme[1:-1]
        idx = table_of_const.setdefault(val, ('string', len(table_of_const) + 1))[1]
        add_record('string_literal', idx)
    elif state in (12, 14, 16): 
        token = token_table.get(lexeme)
        add_record(token)
    elif state == 20:
        add_record('mult_op')
    elif state == 100:
        token = token_table.get(lexeme)
        if token: add_record(token)

    state = 0
    lexeme = ""

def lex():
    global state, lexeme, char, num_line
    state = 0
    lexeme = ""
    num_line = 1
    table_of_symb.clear()
    table_of_id.clear()
    table_of_const.clear()
    
    print(f"{'Row':<4} {'Lexeme':<16} {'Token':<16} {'Index'}")
    print("-" * 50)
    
    while num_char < len_code:
        char = next_char()
        if not char: break
        class_ch = class_of_char(char)
        state = next_state(state, class_ch)
        if is_final(state):
            lexeme += char 
            processing()
        elif state == 0: 
            lexeme = ""
            if class_ch == 'nl': num_line += 1
        elif state == 19: 
            lexeme = ""
        else: 
            lexeme += char
            
    if state != 0 and is_final(next_state(state, "other")):
         processing()

def run_lexer(filename):
    global source_code, len_code, num_char
    try:
        with open(filename, "r", encoding="utf-8") as f:
            source_code = f.read() + " " 
            len_code = len(source_code)
            num_char = -1
            
            print(f"=== Аналіз файлу: {filename} ===\n")
            lex()
            
            print("\n--- ID Table ---")
            print(table_of_id)
            print("\n--- Const Table ---")
            print(table_of_const)
            print("\n")
            
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
        sys.exit(1)

if __name__ == "__main__":
    run_lexer("test_semantic.minikot")