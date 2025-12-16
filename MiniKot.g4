grammar Minikot;

// ==========================================
// ПАРСЕР (Синтаксичні правила)
// ==========================================

program
    : statement* EOF
    ;

statement
    : varDecl
    | constDecl
    | functionDecl          // Оголошення функції
    | assignment
    | printStmt
    | ifStmt
    | whileStmt
    | returnStmt            // Оператор return
    | block
    | expressionStmt
    ;

block
    : LBRACE statement* RBRACE
    ;

// --- Оголошення змінних ---
varDecl
    : VAR ID COLON type ASSIGN expression SEMI
    ;

constDecl
    : VAL ID COLON type ASSIGN expression SEMI
    | CONST ID COLON type ASSIGN expression SEMI
    ;

// --- Функції ---
functionDecl
    : FUN ID LPAREN paramList? RPAREN COLON type block
    ;

paramList
    : param (COMMA param)*
    ;

param
    : ID COLON type
    ;

returnStmt
    : RETURN expression SEMI
    ;

// --- Присвоєння ---
assignment
    : ID ASSIGN expression SEMI
    ;

// --- Друк ---
printStmt
    : PRINT LPAREN expression RPAREN SEMI
    | PRINTLN LPAREN expression RPAREN SEMI
    ;

// --- Керуючі конструкції ---
ifStmt
    : IF LPAREN expression RPAREN block (ELSE block)?
    ;

whileStmt
    : WHILE LPAREN expression RPAREN block
    ;

expressionStmt
    : expression SEMI
    ;

// --- Вирази (Пріоритет зверху вниз) ---
expression
    : LPAREN expression RPAREN                  # ParenthesizedExpr
    | MINUS expression                          # UnaryMinusExpr    // Унарний мінус (пріоритет вище за множення)
    | ID LPAREN argList? RPAREN                 # FunctionCallExpr  // Виклик функції
    | readCall                                  # ReadCallExpr
    | expression POW expression                 # PowerExpr
    | expression (MULT | DIV) expression        # MultiplicativeExpr
    | expression (PLUS | MINUS) expression      # AdditiveExpr
    | expression relOp expression               # RelationalExpr
    | ID                                        # IdentifierExpr
    | LITERAL_INT                               # LiteralIntExpr
    | LITERAL_DOUBLE                            # LiteralDoubleExpr
    | LITERAL_STRING                            # LiteralStringExpr
    | LITERAL_BOOL                              # LiteralBoolExpr
    ;

argList
    : expression (COMMA expression)*
    ;

readCall
    : (READ_INT | READ_DOUBLE | READ_STRING) LPAREN RPAREN
    ;

relOp
    : GT | LT | GTE | LTE | EQ | NEQ
    ;

type
    : TYPE_INT | TYPE_DOUBLE | TYPE_STRING | TYPE_BOOL | TYPE_UNIT
    ;

// ==========================================
// ЛЕКСЕР (Токени)
// ==========================================

// Ключові слова
VAR: 'var';
VAL: 'val';
CONST: 'const';
FUN: 'fun';
RETURN: 'return';
IF: 'if';
ELSE: 'else';
WHILE: 'while';
PRINT: 'print';
PRINTLN: 'println';
READ_INT: 'readInt';
READ_DOUBLE: 'readDouble';
READ_STRING: 'readString';

// Типи
TYPE_INT: 'Int';
TYPE_DOUBLE: 'Double';
TYPE_STRING: 'String';
TYPE_BOOL: 'Boolean';
TYPE_UNIT: 'Unit';

// Літерали
LITERAL_BOOL: 'true' | 'false';
LITERAL_INT: [0-9]+;
LITERAL_DOUBLE: [0-9]+ '.' [0-9]+;
LITERAL_STRING: '"' .*? '"';

// Оператори та пунктуація
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
POW: '^';
ASSIGN: '=';

GT: '>';
LT: '<';
GTE: '>=';
LTE: '<=';
EQ: '==';
NEQ: '!=';

LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
COLON: ':';
SEMI: ';';
COMMA: ',';  // <--- ВАЖЛИВО: Кома додана

ID: [a-zA-Z_][a-zA-Z0-9_]*;

COMMENT: '//' ~[\r\n]* -> skip;

// Пропуск пробілів
WS: [ \t\r\n]+ -> skip;