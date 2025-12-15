# Generated from MiniKot.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,32,92,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,5,0,10,8,0,10,0,12,
        0,13,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,43,8,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,53,8,1,10,1,12,1,56,9,1,1,
        1,3,1,59,8,1,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,
        73,8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,87,8,
        3,10,3,12,3,90,9,3,1,3,0,1,6,4,0,2,4,6,0,6,1,0,17,19,1,0,23,24,1,
        0,8,11,1,0,25,27,1,0,13,14,1,0,15,16,102,0,11,1,0,0,0,2,58,1,0,0,
        0,4,60,1,0,0,0,6,72,1,0,0,0,8,10,3,2,1,0,9,8,1,0,0,0,10,13,1,0,0,
        0,11,9,1,0,0,0,11,12,1,0,0,0,12,14,1,0,0,0,13,11,1,0,0,0,14,15,5,
        0,0,1,15,1,1,0,0,0,16,17,7,0,0,0,17,18,5,29,0,0,18,19,5,1,0,0,19,
        20,3,4,2,0,20,21,5,2,0,0,21,22,3,6,3,0,22,23,5,3,0,0,23,59,1,0,0,
        0,24,25,5,29,0,0,25,26,5,2,0,0,26,27,3,6,3,0,27,28,5,3,0,0,28,59,
        1,0,0,0,29,30,7,1,0,0,30,31,5,4,0,0,31,32,3,6,3,0,32,33,5,5,0,0,
        33,34,5,3,0,0,34,59,1,0,0,0,35,36,5,20,0,0,36,37,5,4,0,0,37,38,3,
        6,3,0,38,39,5,5,0,0,39,42,3,2,1,0,40,41,5,21,0,0,41,43,3,2,1,0,42,
        40,1,0,0,0,42,43,1,0,0,0,43,59,1,0,0,0,44,45,5,22,0,0,45,46,5,4,
        0,0,46,47,3,6,3,0,47,48,5,5,0,0,48,49,3,2,1,0,49,59,1,0,0,0,50,54,
        5,6,0,0,51,53,3,2,1,0,52,51,1,0,0,0,53,56,1,0,0,0,54,52,1,0,0,0,
        54,55,1,0,0,0,55,57,1,0,0,0,56,54,1,0,0,0,57,59,5,7,0,0,58,16,1,
        0,0,0,58,24,1,0,0,0,58,29,1,0,0,0,58,35,1,0,0,0,58,44,1,0,0,0,58,
        50,1,0,0,0,59,3,1,0,0,0,60,61,7,2,0,0,61,5,1,0,0,0,62,63,6,3,-1,
        0,63,73,5,29,0,0,64,73,5,30,0,0,65,66,7,3,0,0,66,67,5,4,0,0,67,73,
        5,5,0,0,68,69,5,4,0,0,69,70,3,6,3,0,70,71,5,5,0,0,71,73,1,0,0,0,
        72,62,1,0,0,0,72,64,1,0,0,0,72,65,1,0,0,0,72,68,1,0,0,0,73,88,1,
        0,0,0,74,75,10,8,0,0,75,76,5,12,0,0,76,87,3,6,3,8,77,78,10,7,0,0,
        78,79,7,4,0,0,79,87,3,6,3,8,80,81,10,6,0,0,81,82,7,5,0,0,82,87,3,
        6,3,7,83,84,10,5,0,0,84,85,5,28,0,0,85,87,3,6,3,6,86,74,1,0,0,0,
        86,77,1,0,0,0,86,80,1,0,0,0,86,83,1,0,0,0,87,90,1,0,0,0,88,86,1,
        0,0,0,88,89,1,0,0,0,89,7,1,0,0,0,90,88,1,0,0,0,7,11,42,54,58,72,
        86,88
    ]

class MiniKotParser ( Parser ):

    grammarFileName = "MiniKot.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'='", "';'", "'('", "')'", "'{'", 
                     "'}'", "'Int'", "'Double'", "'String'", "'Boolean'", 
                     "'^'", "'*'", "'/'", "'+'", "'-'", "'var'", "'val'", 
                     "'const'", "'if'", "'else'", "'while'", "'print'", 
                     "'println'", "'readInt'", "'readDouble'", "'readString'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "VAR", "VAL", "CONST", "IF", "ELSE", 
                      "WHILE", "PRINT", "PRINTLN", "READ_INT", "READ_DOUBLE", 
                      "READ_STRING", "REL_OP", "ID", "LITERAL", "WS", "COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_type = 2
    RULE_expression = 3

    ruleNames =  [ "program", "statement", "type", "expression" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    VAR=17
    VAL=18
    CONST=19
    IF=20
    ELSE=21
    WHILE=22
    PRINT=23
    PRINTLN=24
    READ_INT=25
    READ_DOUBLE=26
    READ_STRING=27
    REL_OP=28
    ID=29
    LITERAL=30
    WS=31
    COMMENT=32

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniKotParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniKotParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniKotParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniKotParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniKotParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 568197184) != 0):
                self.state = 8
                self.statement()
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 14
            self.match(MiniKotParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniKotParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StmtBlockContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniKotParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniKotParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniKotParser.StatementContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtBlock" ):
                return visitor.visitStmtBlock(self)
            else:
                return visitor.visitChildren(self)


    class StmtVarDeclContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniKotParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiniKotParser.ID, 0)
        def type_(self):
            return self.getTypedRuleContext(MiniKotParser.TypeContext,0)

        def expression(self):
            return self.getTypedRuleContext(MiniKotParser.ExpressionContext,0)

        def VAR(self):
            return self.getToken(MiniKotParser.VAR, 0)
        def VAL(self):
            return self.getToken(MiniKotParser.VAL, 0)
        def CONST(self):
            return self.getToken(MiniKotParser.CONST, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtVarDecl" ):
                return visitor.visitStmtVarDecl(self)
            else:
                return visitor.visitChildren(self)


    class StmtWhileContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniKotParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(MiniKotParser.WHILE, 0)
        def expression(self):
            return self.getTypedRuleContext(MiniKotParser.ExpressionContext,0)

        def statement(self):
            return self.getTypedRuleContext(MiniKotParser.StatementContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtWhile" ):
                return visitor.visitStmtWhile(self)
            else:
                return visitor.visitChildren(self)


    class StmtPrintContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniKotParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(MiniKotParser.ExpressionContext,0)

        def PRINT(self):
            return self.getToken(MiniKotParser.PRINT, 0)
        def PRINTLN(self):
            return self.getToken(MiniKotParser.PRINTLN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtPrint" ):
                return visitor.visitStmtPrint(self)
            else:
                return visitor.visitChildren(self)


    class StmtAssignContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniKotParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiniKotParser.ID, 0)
        def expression(self):
            return self.getTypedRuleContext(MiniKotParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtAssign" ):
                return visitor.visitStmtAssign(self)
            else:
                return visitor.visitChildren(self)


    class StmtIfContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniKotParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(MiniKotParser.IF, 0)
        def expression(self):
            return self.getTypedRuleContext(MiniKotParser.ExpressionContext,0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniKotParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniKotParser.StatementContext,i)

        def ELSE(self):
            return self.getToken(MiniKotParser.ELSE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtIf" ):
                return visitor.visitStmtIf(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = MiniKotParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17, 18, 19]:
                localctx = MiniKotParser.StmtVarDeclContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 16
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 917504) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 17
                self.match(MiniKotParser.ID)
                self.state = 18
                self.match(MiniKotParser.T__0)
                self.state = 19
                self.type_()
                self.state = 20
                self.match(MiniKotParser.T__1)
                self.state = 21
                self.expression(0)
                self.state = 22
                self.match(MiniKotParser.T__2)
                pass
            elif token in [29]:
                localctx = MiniKotParser.StmtAssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.match(MiniKotParser.ID)
                self.state = 25
                self.match(MiniKotParser.T__1)
                self.state = 26
                self.expression(0)
                self.state = 27
                self.match(MiniKotParser.T__2)
                pass
            elif token in [23, 24]:
                localctx = MiniKotParser.StmtPrintContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 29
                _la = self._input.LA(1)
                if not(_la==23 or _la==24):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 30
                self.match(MiniKotParser.T__3)
                self.state = 31
                self.expression(0)
                self.state = 32
                self.match(MiniKotParser.T__4)
                self.state = 33
                self.match(MiniKotParser.T__2)
                pass
            elif token in [20]:
                localctx = MiniKotParser.StmtIfContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 35
                self.match(MiniKotParser.IF)
                self.state = 36
                self.match(MiniKotParser.T__3)
                self.state = 37
                self.expression(0)
                self.state = 38
                self.match(MiniKotParser.T__4)
                self.state = 39
                self.statement()
                self.state = 42
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 40
                    self.match(MiniKotParser.ELSE)
                    self.state = 41
                    self.statement()


                pass
            elif token in [22]:
                localctx = MiniKotParser.StmtWhileContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 44
                self.match(MiniKotParser.WHILE)
                self.state = 45
                self.match(MiniKotParser.T__3)
                self.state = 46
                self.expression(0)
                self.state = 47
                self.match(MiniKotParser.T__4)
                self.state = 48
                self.statement()
                pass
            elif token in [6]:
                localctx = MiniKotParser.StmtBlockContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 50
                self.match(MiniKotParser.T__5)
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 568197184) != 0):
                    self.state = 51
                    self.statement()
                    self.state = 56
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 57
                self.match(MiniKotParser.T__6)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniKotParser.RULE_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = MiniKotParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3840) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniKotParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MulDivExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniKotParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniKotParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniKotParser.ExpressionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivExpr" ):
                return visitor.visitMulDivExpr(self)
            else:
                return visitor.visitChildren(self)


    class IdExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniKotParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiniKotParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdExpr" ):
                return visitor.visitIdExpr(self)
            else:
                return visitor.visitChildren(self)


    class ReadExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniKotParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def READ_INT(self):
            return self.getToken(MiniKotParser.READ_INT, 0)
        def READ_DOUBLE(self):
            return self.getToken(MiniKotParser.READ_DOUBLE, 0)
        def READ_STRING(self):
            return self.getToken(MiniKotParser.READ_STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadExpr" ):
                return visitor.visitReadExpr(self)
            else:
                return visitor.visitChildren(self)


    class RelExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniKotParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniKotParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniKotParser.ExpressionContext,i)

        def REL_OP(self):
            return self.getToken(MiniKotParser.REL_OP, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelExpr" ):
                return visitor.visitRelExpr(self)
            else:
                return visitor.visitChildren(self)


    class LitExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniKotParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LITERAL(self):
            return self.getToken(MiniKotParser.LITERAL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLitExpr" ):
                return visitor.visitLitExpr(self)
            else:
                return visitor.visitChildren(self)


    class PowExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniKotParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniKotParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniKotParser.ExpressionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPowExpr" ):
                return visitor.visitPowExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniKotParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(MiniKotParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddSubExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniKotParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniKotParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniKotParser.ExpressionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubExpr" ):
                return visitor.visitAddSubExpr(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniKotParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                localctx = MiniKotParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 63
                self.match(MiniKotParser.ID)
                pass
            elif token in [30]:
                localctx = MiniKotParser.LitExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 64
                self.match(MiniKotParser.LITERAL)
                pass
            elif token in [25, 26, 27]:
                localctx = MiniKotParser.ReadExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 65
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 234881024) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 66
                self.match(MiniKotParser.T__3)
                self.state = 67
                self.match(MiniKotParser.T__4)
                pass
            elif token in [4]:
                localctx = MiniKotParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 68
                self.match(MiniKotParser.T__3)
                self.state = 69
                self.expression(0)
                self.state = 70
                self.match(MiniKotParser.T__4)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 88
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 86
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = MiniKotParser.PowExprContext(self, MiniKotParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 74
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 75
                        self.match(MiniKotParser.T__11)
                        self.state = 76
                        self.expression(8)
                        pass

                    elif la_ == 2:
                        localctx = MiniKotParser.MulDivExprContext(self, MiniKotParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 77
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 78
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==13 or _la==14):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 79
                        self.expression(8)
                        pass

                    elif la_ == 3:
                        localctx = MiniKotParser.AddSubExprContext(self, MiniKotParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 80
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 81
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==15 or _la==16):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 82
                        self.expression(7)
                        pass

                    elif la_ == 4:
                        localctx = MiniKotParser.RelExprContext(self, MiniKotParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 83
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 84
                        localctx.op = self.match(MiniKotParser.REL_OP)
                        self.state = 85
                        self.expression(6)
                        pass

             
                self.state = 90
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         




