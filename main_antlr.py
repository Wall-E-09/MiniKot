import sys
from antlr4 import *
from MinikotLexer import MinikotLexer
from MinikotParser import MinikotParser
from MinikotVisitor import MinikotVisitor

# ==========================================
# Виняток для обробки return
# ==========================================
class ReturnException(Exception):
    def __init__(self, value):
        self.value = value

# ==========================================
# Інтерпретатор (Visitor)
# ==========================================
class MyMinikotVisitor(MinikotVisitor):
    def __init__(self):
        # self.scopes - стек областей видимості. 
        # [-1] - це поточна (локальна), [0] - глобальна.
        self.scopes = [{}] 
        self.functions = {} # Зберігає AST (дерево) функцій

    # --- Робота зі змінними ---
    def get_var(self, name):
        # 1. Шукаємо в поточній області (локальній)
        if name in self.scopes[-1]:
            return self.scopes[-1][name]
        # 2. Шукаємо в глобальній області
        if name in self.scopes[0]:
            return self.scopes[0][name]
        raise Exception(f"Runtime Error: Variable '{name}' is not defined.")

    def set_var(self, name, value):
        # При присвоєнні оновлюємо існуючу змінну
        if name in self.scopes[-1]:
            self.scopes[-1][name] = value
        elif name in self.scopes[0]:
            self.scopes[0][name] = value
        else:
            raise Exception(f"Runtime Error: Variable '{name}' is not declared.")

    def declare_var(self, name, value):
        # Оголошення завжди йде в поточну область
        self.scopes[-1][name] = value

    # --- Відвідування вузлів ---

    def visitProgram(self, ctx):
        return self.visitChildren(ctx)

    def visitBlock(self, ctx):
        return self.visitChildren(ctx)

    # --- Оголошення змінних ---
    def visitVarDecl(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        self.declare_var(name, value)
        return value

    def visitConstDecl(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        self.declare_var(name, value)
        return value

    def visitAssignment(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        self.set_var(name, value)
        return value

    # --- Функції ---
    def visitFunctionDecl(self, ctx):
        name = ctx.ID().getText()
        # Ми не виконуємо тіло функції зараз! Ми запам'ятовуємо її дерево (ctx).
        self.functions[name] = ctx
        return None

    def visitReturnStmt(self, ctx):
        value = self.visit(ctx.expression())
        # Кидаємо виняток, щоб перервати виконання блоку функції
        raise ReturnException(value)

    def visitFunctionCallExpr(self, ctx):
        func_name = ctx.ID().getText()
        
        if func_name not in self.functions:
            raise Exception(f"Runtime Error: Function '{func_name}' is not defined.")
            
        func_ctx = self.functions[func_name]
        
        # 1. Обчислюємо аргументи (actual parameters)
        args_values = []
        if ctx.argList():
            # Отримуємо список виразів через коми
            exprs = ctx.argList().expression()
            for expr in exprs:
                args_values.append(self.visit(expr))
        
        # 2. Отримуємо імена параметрів (formal parameters)
        param_names = []
        if func_ctx.paramList():
            params = func_ctx.paramList().param()
            for p in params:
                param_names.append(p.ID().getText())
        
        if len(args_values) != len(param_names):
            raise Exception(f"Error: Function '{func_name}' expects {len(param_names)} args, got {len(args_values)}")

        # 3. Створюємо нову область видимості (Scope)
        new_scope = {}
        # Заповнюємо параметри значеннями
        for name, val in zip(param_names, args_values):
            new_scope[name] = val
            
        # 4. Додаємо scope на стек
        self.scopes.append(new_scope)
        
        # 5. Виконуємо тіло
        result = None
        try:
            # Виконуємо блок коду функції
            self.visit(func_ctx.block())
        except ReturnException as e:
            # Перехоплюємо return
            result = e.value
        
        # 6. Видаляємо scope зі стеку (вихід з функції)
        self.scopes.pop()
        
        return result

    # --- Ввід / Вивід ---
    def visitPrintStmt(self, ctx):
        val = self.visit(ctx.expression())
        # Якщо print - без ентера, якщо println - з ентером
        if ctx.PRINT():
            print(val, end="")
        else:
            print(val)
        return None

    # === ВИПРАВЛЕНИЙ МЕТОД ===
    def visitReadCallExpr(self, ctx):
        # Отримуємо вкладений контекст правила readCall (це дитина поточного вузла)
        read_call_ctx = ctx.readCall()
        
        # Отримуємо текст першої дитини вузла readCall (це і є токен 'readInt'/'readString' тощо)
        op = read_call_ctx.getChild(0).getText()
        
        # Читаємо рядок (якщо це input prompt, курсор буде на новому рядку, бо так працює input() в Python без аргументів)
        text_input = input() 
        
        if op == 'readInt':
            return int(text_input)
        elif op == 'readDouble':
            return float(text_input)
        elif op == 'readString':
            return str(text_input)
        return text_input

    # --- Логіка та цикли ---
    def visitIfStmt(self, ctx):
        condition = self.visit(ctx.expression())
        if condition:
            self.visit(ctx.block(0)) # if block
        elif ctx.ELSE():
            self.visit(ctx.block(1)) # else block
        return None

    def visitWhileStmt(self, ctx):
        while self.visit(ctx.expression()):
            self.visit(ctx.block())
        return None

    # --- Вирази ---
    
    def visitIdentifierExpr(self, ctx):
        name = ctx.ID().getText()
        return self.get_var(name)

    def visitLiteralIntExpr(self, ctx):
        return int(ctx.getText())

    def visitLiteralDoubleExpr(self, ctx):
        return float(ctx.getText())

    def visitLiteralStringExpr(self, ctx):
        # Прибираємо лапки "" навколо рядка
        return ctx.getText().strip('"')

    def visitLiteralBoolExpr(self, ctx):
        return ctx.getText() == 'true'

    def visitParenthesizedExpr(self, ctx):
        return self.visit(ctx.expression())

    def visitUnaryMinusExpr(self, ctx):
        val = self.visit(ctx.expression())
        return -val

    def visitPowerExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return float(left) ** float(right)

    def visitMultiplicativeExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if ctx.MULT(): return left * right
        else: return left / right

    def visitAdditiveExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if ctx.PLUS(): return left + right
        else: return left - right

    def visitRelationalExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        
        # --- ВИПРАВЛЕННЯ ---
        # Ми отримуємо контекст правила relOp
        rel_op_ctx = ctx.relOp()
        # Отримуємо перший дочірній елемент (це і є наш токен: >, <, == тощо)
        # і беремо його тип
        op = rel_op_ctx.getChild(0).getSymbol().type
        # -------------------
        
        # Порівнюємо з токенами парсера
        if op == MinikotParser.GT: return left > right
        if op == MinikotParser.LT: return left < right
        if op == MinikotParser.GTE: return left >= right
        if op == MinikotParser.LTE: return left <= right
        if op == MinikotParser.EQ: return left == right
        if op == MinikotParser.NEQ: return left != right
        return False

# ==========================================
# ЗАПУСК
# ==========================================
if __name__ == '__main__':
    print("Введіть назву файлу (без розширення):")
    file_base = input("> ").strip()
    if not file_base:
        file_base = "all_features"

    input_file = file_base + ".minikot"
    
    try:
        input_stream = FileStream(input_file, encoding='utf-8')
        lexer = MinikotLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = MinikotParser(stream)
        
        tree = parser.program()
        
        if parser.getNumberOfSyntaxErrors() > 0:
            print("Syntax errors found. Execution aborted.")
        else:
            print(f"\n--- Running {input_file} via ANTLR Interpreter ---\n")
            visitor = MyMinikotVisitor()
            visitor.visit(tree)
            
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"Error: {e}")