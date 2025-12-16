# Generated from Minikot.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MinikotParser import MinikotParser
else:
    from MinikotParser import MinikotParser

# This class defines a complete generic visitor for a parse tree produced by MinikotParser.

class MinikotVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MinikotParser#program.
    def visitProgram(self, ctx:MinikotParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinikotParser#statement.
    def visitStatement(self, ctx:MinikotParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinikotParser#block.
    def visitBlock(self, ctx:MinikotParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinikotParser#varDecl.
    def visitVarDecl(self, ctx:MinikotParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinikotParser#constDecl.
    def visitConstDecl(self, ctx:MinikotParser.ConstDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinikotParser#functionDecl.
    def visitFunctionDecl(self, ctx:MinikotParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinikotParser#paramList.
    def visitParamList(self, ctx:MinikotParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinikotParser#param.
    def visitParam(self, ctx:MinikotParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinikotParser#returnStmt.
    def visitReturnStmt(self, ctx:MinikotParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinikotParser#assignment.
    def visitAssignment(self, ctx:MinikotParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinikotParser#printStmt.
    def visitPrintStmt(self, ctx:MinikotParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinikotParser#ifStmt.
    def visitIfStmt(self, ctx:MinikotParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinikotParser#whileStmt.
    def visitWhileStmt(self, ctx:MinikotParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinikotParser#expressionStmt.
    def visitExpressionStmt(self, ctx:MinikotParser.ExpressionStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinikotParser#LiteralIntExpr.
    def visitLiteralIntExpr(self, ctx:MinikotParser.LiteralIntExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinikotParser#RelationalExpr.
    def visitRelationalExpr(self, ctx:MinikotParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinikotParser#LiteralStringExpr.
    def visitLiteralStringExpr(self, ctx:MinikotParser.LiteralStringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinikotParser#PowerExpr.
    def visitPowerExpr(self, ctx:MinikotParser.PowerExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinikotParser#MultiplicativeExpr.
    def visitMultiplicativeExpr(self, ctx:MinikotParser.MultiplicativeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinikotParser#FunctionCallExpr.
    def visitFunctionCallExpr(self, ctx:MinikotParser.FunctionCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinikotParser#ReadCallExpr.
    def visitReadCallExpr(self, ctx:MinikotParser.ReadCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinikotParser#AdditiveExpr.
    def visitAdditiveExpr(self, ctx:MinikotParser.AdditiveExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinikotParser#IdentifierExpr.
    def visitIdentifierExpr(self, ctx:MinikotParser.IdentifierExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinikotParser#LiteralBoolExpr.
    def visitLiteralBoolExpr(self, ctx:MinikotParser.LiteralBoolExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinikotParser#ParenthesizedExpr.
    def visitParenthesizedExpr(self, ctx:MinikotParser.ParenthesizedExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinikotParser#LiteralDoubleExpr.
    def visitLiteralDoubleExpr(self, ctx:MinikotParser.LiteralDoubleExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinikotParser#UnaryMinusExpr.
    def visitUnaryMinusExpr(self, ctx:MinikotParser.UnaryMinusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinikotParser#argList.
    def visitArgList(self, ctx:MinikotParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinikotParser#readCall.
    def visitReadCall(self, ctx:MinikotParser.ReadCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinikotParser#relOp.
    def visitRelOp(self, ctx:MinikotParser.RelOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinikotParser#type.
    def visitType(self, ctx:MinikotParser.TypeContext):
        return self.visitChildren(ctx)



del MinikotParser