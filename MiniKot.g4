grammar Minikot;

// --- PARSER RULES ---

program: statement* EOF;

statement
    : varDecl
    | constDecl
    | functionDecl          // <--- ДОДАЙТЕ ЦЕ (Оголошення функції)
    | assignment
    | printStmt
    | ifStmt
    | whileStmt
    | block
    | expressionStmt
    ;

// Оголошення функції
functionDecl
    : FUN ID '(' paramList? ')' ':' type block  // <--- ПРАВИЛО ДЛЯ ФУНКЦІЇ
    ;

paramList
    : param (COMMA param)* // <--- Використання коми
    ;

param
    : ID ':' type
    ;

// Вирази (зверніть увагу на порядок!)
expression
    : LPAREN expression RPAREN      # ParenthesizedExpr
    | MINUS expression              # UnaryMinusExpr    // <--- ПРАВИЛО ДЛЯ УНАРНОГО МІНУСА
    | expression (MULT | DIV | POW) expression  # MultiplicativeExpr
    | expression (PLUS | MINUS) expression      # AdditiveExpr
    | expression relOp expression   # RelationalExpr
    | ID LPAREN argList? RPAREN     # FunctionCallExpr  // <--- Виклик функції
    | ID                            # IdentifierExpr
    | LITERAL                       # LiteralExpr
    | functionCall                  # ReadCallExpr
    ;

argList
    : expression (COMMA expression)* ; // <--- Використання коми у виклику

// --- LEXER RULES ---

FUN: 'fun';         // <--- Ключове слово fun
RETURN: 'return';
COMMA: ',';         // <--- ОБОВ'ЯЗКОВО ДОДАЙТЕ КОМУ

// Інші токени (PLUS, MINUS, MULT, DIV, ID, INT, WS...)
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
POW: '^';
// ... ваші інші токени