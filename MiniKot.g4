grammar MiniKot;

// --- Парсер (Синтаксис) ---

program: statement* EOF;

statement
    : varDecl       # VarDeclStmt
    | assignment    # AssignStmt
    | printStmt     # PrintStmt
    | ifStmt        # IfStmt
    | whileStmt     # WhileStmt
    | block         # BlockStmt
    ;

block: '{' statement* '}';

varDecl: (VAR | VAL | CONST) ID ':' type '=' expression ';';

assignment: ID '=' expression ';';

printStmt: (PRINT | PRINTLN) '(' expression ')' ';';

ifStmt: IF '(' expression ')' statement (ELSE statement)?;

whileStmt: WHILE '(' expression ')' statement;

// Вирази (з урахуванням пріоритетів)
expression
    : left=expression op='^' right=expression          # PowExpr
    | left=expression op=('*'|'/') right=expression    # MulDivExpr
    | left=expression op=('+'|'-') right=expression    # AddSubExpr
    | left=expression op=REL_OP right=expression       # RelationalExpr
    | ID                                               # IdExpr
    | LITERAL                                          # LiteralExpr
    | readCall                                         # ReadExpr
    | '(' expression ')'                               # ParenExpr
    ;

readCall: (READ_INT | READ_DOUBLE | READ_STRING) '(' ')';

type: 'Int' | 'Double' | 'Boolean' | 'String';

// --- Лексер (Токени) ---

VAR: 'var';
VAL: 'val';
CONST: 'const';
IF: 'if';
ELSE: 'else';
WHILE: 'while';
PRINT: 'print';
PRINTLN: 'println';
READ_INT: 'readInt';
READ_DOUBLE: 'readDouble';
READ_STRING: 'readString';

REL_OP: '==' | '!=' | '<=' | '>=' | '<' | '>';

ID: [a-zA-Z_][a-zA-Z0-9_]*;

LITERAL
    : [0-9]+ '.' [0-9]+  // Double
    | [0-9]+             // Int
    | '"' .*? '"'        // String
    | 'true' | 'false'   // Boolean
    ;

// Пропуск пробілів та коментарів
WS: [ \t\r\n]+ -> skip;
COMMENT: '//' ~[\r\n]* -> skip;