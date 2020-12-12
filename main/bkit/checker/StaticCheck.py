
"""
 * Huynh Pham Phuoc Linh
 * 1710165
"""
from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from AST import * 
from Visitor import *
from StaticError import *
from functools import *

class Type(ABC):
    __metaclass__ = ABCMeta
    pass
class Prim(Type):
    __metaclass__ = ABCMeta
    pass
class IntType(Prim):
    pass
class FloatType(Prim):
    pass
class StringType(Prim):
    pass
class BoolType(Prim):
    pass
class VoidType(Type):
    pass
class Unknown(Type):
    pass

@dataclass
class ArrayType(Type):
    dimen:List[int]
    eletype: Type

@dataclass
class MType:
    intype:List[Type]
    restype:Type

@dataclass
class Symbol:
    name: str
    mtype:Type

class StaticChecker(BaseVisitor):
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = [
Symbol("int_of_float",MType([FloatType()],IntType())),
Symbol("float_of_int",MType([IntType()],FloatType())),
Symbol("int_of_string",MType([StringType()],IntType())),
Symbol("string_of_int",MType([IntType()],StringType())),
Symbol("float_of_string",MType([StringType()],FloatType())),
Symbol("string_of_float",MType([FloatType()],StringType())),
Symbol("bool_of_string",MType([StringType()],BoolType())),
Symbol("string_of_bool",MType([BoolType()],StringType())),
Symbol("read",MType([],StringType())),
Symbol("printLn",MType([],VoidType())),
Symbol("printStr",MType([StringType()],VoidType())),
Symbol("printStrLn",MType([StringType()],VoidType()))]                           
   
    def check(self):
        return self.visit(self.ast, self.global_envi)

    def visitProgram(self, ast, param):
        self.func_unused = []
        self.func_call_func = None
        #[self.visit(x,c) for x in ast.decl]
        #Check main in funcDecl exist or not
        is_main_func_defined = False
        for x in ast.decl:
            if isinstance(x, FuncDecl) and x.name.name == 'main':
                is_main_func_defined = True
                break
        if not is_main_func_defined:
            raise NoEntryPoint()
        
        #Check redeclare
        for x in ast.decl:
            if isinstance(x, VarDecl):
                param.append(self.visit(x, param))

            elif isinstance(x, FuncDecl):
                func = Symbol(
                    x.name.name,
                    MType([x.varInit for x in x.param],Unknown())
                )
                for i in param:
                    if i.name == func.name:
                        raise Redeclared(Function(), func.name)
                param.append(func)
                if func.name != 'main':
                    self.func_unused.append(func)
        
        #visit funcdeclare
        for x in ast.decl:
            if isinstance(x, FuncDecl):
                self.func_call_func = x.name.name
                self.visit(x, param)

        print(self.func_unused)
        if self.func_unused:
            raise UnreachableFunction(self.func_unused[0].name)
        #for x in param: #check param
        #    print(x)
    
    def visitVarDecl(self, ast, param):
        for x in param:
            if ast.variable.name == x.name:
                raise Redeclared(Variable(), ast.variable.name)
        varType = self.visit(ast.varInit, ast.varDimen)
        return Symbol(ast.variable.name, MType(None, varType))
    
    def visitFuncDecl(self, ast, param):
        return None
    
    def visitBinaryOp(self, ast, param):
        return None
    
    def visitUnaryOp(self, ast, param):
        return None
    
    def visitCallExpr(self, ast, param):
        return None
    
    def visitId(self, ast, param):
        return None
    
    def visitArrayCell(self, ast, param):
        return None
    
    def visitAssign(self, ast, param):
        return None
    
    def visitIf(self, ast, param):
        return None
    
    def visitFor(self, ast, param):
        return None
    
    def visitContinue(self, ast, param):
        return None
    
    def visitBreak(self, ast, param):
        return None
    
    def visitReturn(self, ast, param):
        return None
    
    def visitDowhile(self, ast, param):
        return None

    def visitWhile(self, ast, param):
        return None

    def visitCallStmt(self, ast, param):
        return None
    
    def visitIntLiteral(self, ast, param):
        return IntType()
    
    def visitFloatLiteral(self, ast, param):
        return FloatType()
    
    def visitBooleanLiteral(self, ast, param):
        return BoolType()
    
    def visitStringLiteral(self, ast, param):
        return StringType()

    def visitArrayLiteral(self, ast, param):
        eleType = ast.value[0]
        return ArrayType(param, eleType)
