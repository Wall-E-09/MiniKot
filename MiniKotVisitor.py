# Generated from MiniKot.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniKotParser import MiniKotParser
else:
    from MiniKotParser import MiniKotParser

# This class defines a complete generic visitor for a parse tree produced by MiniKotParser.

class MiniKotVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniKotParser#program.
    def visitProgram(self, ctx:MiniKotParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniKotParser#StmtVarDecl.
    def visitStmtVarDecl(self, ctx:MiniKotParser.StmtVarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniKotParser#StmtAssign.
    def visitStmtAssign(self, ctx:MiniKotParser.StmtAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniKotParser#StmtPrint.
    def visitStmtPrint(self, ctx:MiniKotParser.StmtPrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniKotParser#StmtIf.
    def visitStmtIf(self, ctx:MiniKotParser.StmtIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniKotParser#StmtWhile.
    def visitStmtWhile(self, ctx:MiniKotParser.StmtWhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniKotParser#StmtBlock.
    def visitStmtBlock(self, ctx:MiniKotParser.StmtBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniKotParser#type.
    def visitType(self, ctx:MiniKotParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniKotParser#MulDivExpr.
    def visitMulDivExpr(self, ctx:MiniKotParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniKotParser#IdExpr.
    def visitIdExpr(self, ctx:MiniKotParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniKotParser#ReadExpr.
    def visitReadExpr(self, ctx:MiniKotParser.ReadExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniKotParser#RelExpr.
    def visitRelExpr(self, ctx:MiniKotParser.RelExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniKotParser#LitExpr.
    def visitLitExpr(self, ctx:MiniKotParser.LitExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniKotParser#PowExpr.
    def visitPowExpr(self, ctx:MiniKotParser.PowExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniKotParser#ParenExpr.
    def visitParenExpr(self, ctx:MiniKotParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniKotParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:MiniKotParser.AddSubExprContext):
        return self.visitChildren(ctx)



del MiniKotParser