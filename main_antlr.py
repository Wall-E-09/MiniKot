import sys
from antlr4 import *
from MiniKotLexer import MiniKotLexer
from MiniKotParser import MiniKotParser
from MiniKotVisitor import MiniKotVisitor

class MiniKotInterpreter(MiniKotVisitor):
    def __init__(self):
        self.memory = {}

    def visitStmtVarDecl(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        self.memory[name] = value
        return value

    def visitStmtAssign(self, ctx):
        name = ctx.ID().getText()
        if name not in self.memory:
            raise Exception(f"Runtime Error: Variable '{name}' is not defined.")
        value = self.visit(ctx.expression())
        self.memory[name] = value
        return value

    def visitStmtPrint(self, ctx):
        value = self.visit(ctx.expression())
        if ctx.PRINTLN():
            print(value)
        else:
            print(value, end='')
        return None

    def visitStmtBlock(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitStmtIf(self, ctx):
        cond = self.visit(ctx.expression())
        if cond:
            self.visit(ctx.statement(0))
        elif ctx.statement(1):
            self.visit(ctx.statement(1))

    def visitStmtWhile(self, ctx):
        while self.visit(ctx.expression()):
            self.visit(ctx.statement())

    def visitLitExpr(self, ctx):
        text = ctx.getText()
        if text.startswith('"'): return text.strip('"')
        if text == 'true': return True
        if text == 'false': return False
        if '.' in text: return float(text)
        return int(text)

    def visitIdExpr(self, ctx):
        name = ctx.getText()
        if name in self.memory:
            return self.memory[name]
        raise Exception(f"Runtime Error: Variable '{name}' not found.")

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expression())

    def visitPowExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return float(left) ** float(right)

    def visitMulDivExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if ctx.op.text == '*': return left * right
        return left / right

    def visitAddSubExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if isinstance(left, str) or isinstance(right, str):
            return str(left) + str(right)
        
        if ctx.op.text == '+': return left + right
        return left - right

    def visitRelExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.op.text
        if op == '<': return left < right
        if op == '>': return left > right
        if op == '<=': return left <= right
        if op == '>=': return left >= right
        if op == '==': return left == right
        if op == '!=': return left != right
        return False

    def visitReadExpr(self, ctx):
        val = input()
        if ctx.READ_INT(): return int(val)
        if ctx.READ_DOUBLE(): return float(val)
        return val

if __name__ == '__main__':
    print("Введіть назву файлу (без розширення):")
    file_base = input("> ").strip()
    if not file_base: file_base = "test_antlr"
    
    filename = file_base + ".minikot"
    try:
        input_stream = FileStream(filename, encoding='utf-8')
        lexer = MiniKotLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = MiniKotParser(stream)
        tree = parser.program()

        print(f"\n--- Running {filename} via ANTLR Interpreter ---\n")
        visitor = MiniKotInterpreter()
        visitor.visit(tree)
        print("\n--- Execution Finished ---")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")
