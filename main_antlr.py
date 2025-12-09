import sys
from antlr4 import *
# Імпортуємо згенеровані файли (вони лежать у папці dist)
sys.path.append('dist') 
from MiniKotLexer import MiniKotLexer
from MiniKotParser import MiniKotParser
from MiniKotVisitor import MiniKotVisitor

class MiniKotInterpreter(MiniKotVisitor):
    def __init__(self):
        self.memory = {} # Змінні: {name: value}

    # --- Відвідування вузлів ---

    def visitVarDeclStmt(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        # Тут можна додати перевірку типів, якщо потрібно
        self.memory[name] = value
        return value

    def visitAssignStmt(self, ctx):
        name = ctx.ID().getText()
        if name not in self.memory:
            print(f"Error: Variable '{name}' not declared")
            sys.exit(1)
        value = self.visit(ctx.expression())
        self.memory[name] = value
        return value

    def visitPrintStmt(self, ctx):
        value = self.visit(ctx.expression())
        is_println = ctx.PRINTLN() is not None
        print(value, end='\n' if is_println else '')
        return None

    def visitBlockStmt(self, ctx):
        # Виконуємо всі стейтменти в блоці
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitIfStmt(self, ctx):
        cond = self.visit(ctx.expression())
        if cond:
            self.visit(ctx.statement(0)) # then block
        elif ctx.statement(1): # else block exists
            self.visit(ctx.statement(1))

    def visitWhileStmt(self, ctx):
        while self.visit(ctx.expression()):
            self.visit(ctx.statement())

    # --- Вирази ---

    def visitIdExpr(self, ctx):
        name = ctx.getText()
        if name in self.memory:
            return self.memory[name]
        print(f"Error: Variable '{name}' not found")
        sys.exit(1)

    def visitLiteralExpr(self, ctx):
        text = ctx.getText()
        if text.startswith('"'): return text.strip('"')
        if text == 'true': return True
        if text == 'false': return False
        if '.' in text: return float(text)
        return int(text)

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expression())

    def visitReadExpr(self, ctx):
        val = input()
        if ctx.READ_INT(): return int(val)
        if ctx.READ_DOUBLE(): return float(val)
        return val

    # Арифметика
    def visitMulDivExpr(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        if ctx.op.text == '*': return left * right
        return left / right

    def visitAddSubExpr(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        if ctx.op.text == '+': 
            # Авто-конвертація в рядок, якщо один з операндів рядок
            if isinstance(left, str) or isinstance(right, str):
                return str(left) + str(right)
            return left + right
        return left - right

    def visitPowExpr(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        return left ** right

    def visitRelationalExpr(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        op = ctx.op.text
        if op == '<': return left < right
        if op == '>': return left > right
        if op == '<=': return left <= right
        if op == '>=': return left >= right
        if op == '==': return left == right
        if op == '!=': return left != right
        return False

# --- Main Run ---
if __name__ == '__main__':
    print("Введіть назву файлу (без розширення .minikot):")
    file_base = input("> ").strip()
    if not file_base: file_base = "test_semantic"
    
    try:
        input_stream = FileStream(f"{file_base}.minikot", encoding='utf-8')
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)

    # 1. Лексичний аналіз
    lexer = MiniKotLexer(input_stream)
    stream = CommonTokenStream(lexer)
    
    # 2. Синтаксичний аналіз
    parser = MiniKotParser(stream)
    tree = parser.program() # Start rule

    # 3. Обхід дерева (Інтерпретація)
    print("\n--- ANTLR INTERPRETER START ---\n")
    visitor = MiniKotInterpreter()
    visitor.visit(tree)
    print("\n\n--- ANTLR INTERPRETER END ---")