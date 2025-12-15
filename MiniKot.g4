grammar MiniKot;

// --- СИНТАКСИЧНІ ПРАВИЛА (PARSER) ---

program: statement* EOF;

statement
    : (VAR | VAL | CONST) ID ':' type '=' expression ';'  # StmtVarDecl
    | ID '=' expression ';'                               # StmtAssign
    | (PRINT | PRINTLN) '(' expression ')' ';'            # StmtPrint
    | IF '(' expression ')' statement (ELSE statement)?   # StmtIf
    | WHILE '(' expression ')' statement                  # StmtWhile
    | '{' statement* '}'                                  # StmtBlock
    ;

type: 'Int' | 'Double' | 'String' | 'Boolean';

// Вирази
expression
    : <assoc=right> expression '^' expression             # PowExpr
    | expression op=('*'|'/') expression                  # MulDivExpr
    | expression op=('+'|'-') expression                  # AddSubExpr
    | expression op=REL_OP expression                     # RelExpr
    | ID                                                  # IdExpr
    | LITERAL                                             # LitExpr
    // --- ЗМІНА ТУТ: Ми вбудували readCall сюди ---
    | (READ_INT | READ_DOUBLE | READ_STRING) '(' ')'      # ReadExpr
    | '(' expression ')'                                  # ParenExpr
    ;

// Правило readCall видалено, бо воно тепер всередині expression

// --- ЛЕКСИЧНІ ПРАВИЛА (LEXER) ---

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

WS: [ \t\r\n]+ -> skip;
COMMENT: '//' ~[\r\n]* -> skip;