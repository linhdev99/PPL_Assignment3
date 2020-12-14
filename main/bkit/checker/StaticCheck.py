
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
                lstParameter = []
                for y in x.param:
                    lstParameter.append(Unknown())                    
                func = Symbol(
                    x.name.name,
                    MType(lstParameter,VoidType())
                )
                for i in param:
                    if i.name == func.name:
                        raise Redeclared(Function(), func.name)
                param.append(func)
            
        #visit funcdeclare
        for x in ast.decl:
            if isinstance(x, FuncDecl):
                self.func_call_func = x.name.name
                self.visit(x, param)    
            
        # for x in param: #print param
        #     print(x)
        # print("===========================")
        
    def visitVarDecl(self, ast, param):
        for x in param:
            if ast.variable.name == x.name:
                raise Redeclared(Variable(), ast.variable.name)
        if ast.varInit:
            varType = self.visit(ast.varInit, ast.varDimen)
        else:
            varType = Unknown()
        return Symbol(ast.variable.name, MType([], varType))
    
    def visitFuncDecl(self, ast, param):
        local_envi = []
        para_list = []
        para_dict = {}
        is_return = False
        return_type = VoidType()
        nameFunc = ast.name.name;
        for x in ast.param:
            if x.variable.name in para_dict:
                raise Redeclared(Parameter(), x.variable.name)
            else:
                #para_list.append(x.variable.name)
                temp = self.visit(x, local_envi)
                para_dict[x.variable.name] = temp
                local_envi.append(temp)
        for vardecl in ast.body[0]:
            temp = self.visit(vardecl, local_envi)
            local_envi.append(temp)
        for stmt in ast.body[1]:
            if isinstance(stmt, Return):
                if self.visit(stmt, (local_envi + param, return_type)):
                    is_return = True
            else:
                self.visit(stmt, local_envi + param)
                
        newLstParameter = []
        for x in local_envi:
            if x.name in para_dict:
                newLstParameter.append(x.mtype.restype)
        func = Symbol(
                    ast.name,
                    MType(newLstParameter,return_type)
                )
        for idx, x in enumerate(param):
            if x.name == ast.name.name:
                param[idx] = func
        # for x in param:
        #     print(x)
        # print("=====================")
            
        # if not is_return and not isinstance(return_type, VoidType):
        #     raise FunctionNotReturn(ast.name.name)
            
    
    def visitBinaryOp(self, ast, param):
        op = ast.op
        left = ast.left
        right = ast.right
        typeLeft = self.visit(left, param)
        typeRight = self.visit(right, param)
        def check_type(accept_type, return_type=None):
            if isinstance(typeLeft, VoidType) or isinstance(typeRight, VoidType):
                raise TypeMismatchInExpression(ast)
            if isinstance(typeLeft, Unknown) and isinstance(typeRight, Unknown):
                raise TypeCannotBeInferred(ast)
            if isinstance(typeLeft, Unknown) and isinstance(typeRight, accept_type):
                return return_type
            elif isinstance(typeRight, Unknown) and isinstance(typeLeft, accept_type):
                return return_type
            if not isinstance(typeLeft, accept_type) or not isinstance(typeRight, accept_type):
                raise TypeMismatchInExpression(ast)
            if return_type:
                return return_type
        
        if op in ['+', '-', '*', '\\']:
            retype = check_type(IntType, IntType())
            if isinstance(typeLeft, Unknown):
                for idx, x in enumerate(param):
                       if left.name == x.name:
                            param[idx].mtype.restype = IntType()
            elif isinstance(typeRight, Unknown):
                for idx, x in enumerate(param):
                       if right.name == x.name:
                            param[idx].mtype.restype = IntType()
            return retype
        if op in ['+.', '-.', '*.', '\\.']:
            return check_type(FloatType, FloatType())
        if op in ['%']:
            return check_type(IntType, IntType())
        if op in ['<', '<=', '>', '>=','!=']:
            return check_type(IntType, BoolType())
        if op in ['&&', '||']:
            return check_type(BoolType, BoolType())
        if op in ['<.', '<=.', '>.', '>=.','=/=']:
            return check_type(FloatType, BoolType())
        if op in ['==']:
            return check_type((IntType, FloatType), BoolType())
        
    
    def visitUnaryOp(self, ast, param):
        op = ast.op
        expr = self.visit(ast.body, param)
        if isinstance(expr, Unknown):
            raise TypeCannotBeInferred(ast)
        if ast.op == '!':
            if isinstance(expr, BoolType):
                return expr
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op == '-':
            if isinstance(expr, IntType):
                return expr
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op == '-.':
            if isinstance(expr, FloatType):
                return expr
            else:
                raise TypeMismatchInExpression(ast)
    
    def visitCallExpr(self, ast, param):
        check_id = self.visit(ast.method, param)
        check_type = None
        if ast.param != []:
            for x in ast.param:
                check_exp = self.visit(x, param)
                if isinstance(check_exp, Unknown):
                    raise TypeCannotBeInferred(ast)
        for x in param:
            if ast.method.name == x.name:
                check_type = x.mtype.restype
        return check_type
        
    
    def visitId(self, ast, param):
        is_declare = False
        for x in param:
            if ast.name == x.name:
                is_declare = True;
                break
        if not is_declare:
            raise Undeclared(Identifier(), ast.name)
        for x in param:
            if ast.name == x.name:
                return x.mtype.restype
        
    
    def visitArrayCell(self, ast, param):
        print(ast.idx)
    
    def visitAssign(self, ast, param):
        lhs = ast.lhs
        rhs = ast.rhs
        lhsType = self.visit(lhs, param)
        rhsType = self.visit(rhs, param)
        if isinstance(rhsType, Unknown):
            raise TypeCannotBeInferred(ast)
        if isinstance(rhsType, VoidType):
            raise TypeMismatchInExpression(ast)
        elif isinstance(lhsType, Unknown):
            for idx, x in enumerate(param):
                if lhs.name == x.name:
                    param[idx].mtype.restype = rhsType
        elif not isinstance(lhsType, type(rhsType)):
            raise TypeMismatchInExpression(ast)
        else:
            for idx, x in enumerate(param):
               if lhs.name == x.name:
                    param[idx].mtype.restype = rhsType
        
    
    def visitIf(self, ast, param):
        return None
    
    def visitFor(self, ast, param):
        return None
    
    def visitContinue(self, ast, param):
        return None
    
    def visitBreak(self, ast, param):
        return None
    
    def visitReturn(self, ast, param):
        print(param)
    
    def visitDowhile(self, ast, param):
        return None

    def visitWhile(self, ast, param):
        return None

    def visitCallStmt(self, ast, param):
        check_id = self.visit(ast.method, param)
        if ast.param != []:
            for x in ast.param:
                check_exp = self.visit(x, param)
                if isinstance(check_exp, Unknown):
                    raise TypeCannotBeInferred(ast)
    
    def visitIntLiteral(self, ast, param):
        return IntType()
    
    def visitFloatLiteral(self, ast, param):
        return FloatType()
    
    def visitBooleanLiteral(self, ast, param):
        return BoolType()
    
    def visitStringLiteral(self, ast, param):
        return StringType()

    def visitArrayLiteral(self, ast, param):
        eleType = []
        for x in ast.value:
            temp = self.visit(x, param)
            eleType.append(temp)    
        return ArrayType(param, eleType)
