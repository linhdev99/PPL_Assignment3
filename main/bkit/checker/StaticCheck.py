
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
        for x in ast.varDimen:
            if not isinstance(x, int):
                raise TypeMismatchInExpression(ast)
        if ast.varInit:
            if ast.varDimen != []:
                varType = self.visit(ast.varInit, (ast.varDimen, param))
            else:
                varType = self.visit(ast.varInit, param)
        else:
            if ast.varDimen != []:
                varType = ArrayType(ast.varDimen, Unknown())
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
        # kiem tra tung phan tu trong parameter cua function
        for idx,x in enumerate(ast.param):
            if x.variable.name in para_dict:
                raise Redeclared(Parameter(), x.variable.name)
            else:
                #para_list.append(x.variable.name)
                temp = self.visit(x, local_envi)
                para_dict[x.variable.name] = temp
                local_envi.append(temp)
                for y in param:
                    if nameFunc == y.name:
                        temp.mtype.restype = y.mtype.intype[idx]
                
        # Parameter function       
        # newLstParameter = []
        # for x in local_envi:
        #     if x.name in para_dict:
        #         newLstParameter.append(x.mtype.restype)
        # func = Symbol(
        #             ast.name.name,
        #             MType(newLstParameter,return_type)
        #         )
        # print(func)
        # print("####################")
        # for idx, x in enumerate(param):
        #     if x.name == ast.name.name:
        #         param[idx] = func
                
        # visit variable declare        
        for vardecl in ast.body[0]:
            temp = self.visit(vardecl, local_envi)
            local_envi.append(temp)
            
        # visit function declare   
        for stmt in ast.body[1]:
            if isinstance(stmt, Return):
                if self.visit(stmt, (local_envi + param, return_type)):
                    is_return = True
            else:
                self.visit(stmt, local_envi + param)
        
        # update type parameter function
        for x in param:
            if nameFunc == x.name:
                length = len(x.mtype.intype)
                for idx, y in enumerate(local_envi[:length]):
                    x.mtype.intype[idx] = y.mtype.restype
                
        # for x in (local_envi + param):
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
        left_name = ""
        right_name = ""
        if isinstance(left, ArrayCell):
            left_name = left.arr.name 
        elif isinstance(typeLeft, Unknown):
            left_name = left.name
        elif isinstance(typeLeft, CallExpr):
            left_name = left.method.name
            
        if isinstance(right, ArrayCell):
            right_name = right.arr.name 
        elif isinstance(typeRight, Unknown):
            right_name = right.name
        elif isinstance(typeRight, CallExpr):
            right_name = right.method.name
        
        def check_type(accept_type, return_type=None):
            # if isinstance(typeLeft, VoidType) or isinstance(typeRight, VoidType):
            #     raise TypeMismatchInExpression(ast)
            if isinstance(typeLeft, Unknown) and isinstance(typeRight, Unknown):
                raise TypeCannotBeInferred(ast)
            if isinstance(typeLeft, Unknown) and isinstance(typeRight, accept_type):
                return return_type
            if isinstance(typeRight, Unknown) and isinstance(typeLeft, accept_type):
                return return_type
            if not isinstance(typeLeft, accept_type) or not isinstance(typeRight, accept_type):
                raise TypeMismatchInExpression(ast)
            if return_type:
                return return_type
        
        if op in ['+', '-', '*', '\\']:
            retype = check_type(IntType, IntType())
            if isinstance(typeLeft, Unknown):
                for idx, x in enumerate(param):
                       if left_name == x.name:
                            param[idx].mtype.restype = IntType()
            elif isinstance(typeRight, Unknown):
                for idx, x in enumerate(param):
                       if right_name == x.name:
                            param[idx].mtype.restype = IntType()
            return retype
        if op in ['+.', '-.', '*.', '\\.']: 
            retype = check_type(FloatType, FloatType())
            if isinstance(typeLeft, Unknown):
                for idx, x in enumerate(param):
                       if left_name == x.name:
                            param[idx].mtype.restype = FloatType()
            elif isinstance(typeRight, Unknown):
                for idx, x in enumerate(param):
                       if right_name == x.name:
                            param[idx].mtype.restype = FloatType()
            return retype
        if op in ['%']:
            retypr = check_type(IntType, IntType())
            if isinstance(typeLeft, Unknown):
                for idx, x in enumerate(param):
                       if left_name == x.name:
                            param[idx].mtype.restype = IntType()
            elif isinstance(typeRight, Unknown):
                for idx, x in enumerate(param):
                       if right_name == x.name:
                            param[idx].mtype.restype = IntType()
            return retype
        if op in ['<', '<=', '>', '>=','!=']:
            retypr = check_type(IntType, BoolType())
            if isinstance(typeLeft, Unknown):
                for idx, x in enumerate(param):
                       if left_name == x.name:
                            param[idx].mtype.restype = BoolType()
            elif isinstance(typeRight, Unknown):
                for idx, x in enumerate(param):
                       if right_name == x.name:
                            param[idx].mtype.restype = BoolType()
            return retypr
        if op in ['&&', '||']:
            retypr = check_type(BoolType, BoolType())
            if isinstance(typeLeft, Unknown):
                for idx, x in enumerate(param):
                       if left_name == x.name:
                            param[idx].mtype.restype = BoolType()
            elif isinstance(typeRight, Unknown):
                for idx, x in enumerate(param):
                       if right_name == x.name:
                            param[idx].mtype.restype = BoolType()
            return retypr
        if op in ['<.', '<=.', '>.', '>=.','=/=']:
            retypr = check_type(FloatType, BoolType())
            if isinstance(typeLeft, Unknown):
                for idx, x in enumerate(param):
                       if left_name == x.name:
                            param[idx].mtype.restype = BoolType()
            elif isinstance(typeRight, Unknown):
                for idx, x in enumerate(param):
                       if right_name == x.name:
                            param[idx].mtype.restype = BoolType()
            return retypr
        if op in ['==']:
            retypr = check_type((IntType, FloatType), BoolType())
            if isinstance(typeLeft, Unknown):
                for idx, x in enumerate(param):
                       if left_name == x.name:
                            param[idx].mtype.restype = BoolType()
            elif isinstance(typeRight, Unknown):
                for idx, x in enumerate(param):
                       if right_name == x.name:
                            param[idx].mtype.restype = BoolType()
            return retypr
        
    
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
        length = 0
        if ast.param != []:
            for x in ast.param:
                check_exp = self.visit(x, param)
                if isinstance(check_exp, Unknown):
                    raise TypeCannotBeInferred(ast)
        for x in param:
            if ast.method.name == x.name:
                length = len(x.mtype.intype);
                check_type = x.mtype.restype
        if length != len(ast.param):
            raise TypeMismatchInExpression(ast)
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
        for x in ast.idx:
            getType = self.visit(x, param)
            if not isinstance(getType, IntType):
                raise TypeMismatchInExpression(ast)
        check_type = Unknown()
        for x in param:
            if x.name == ast.arr.name:
                if isinstance(x.mtype.restype, ArrayType):
                    check_type = x.mtype.restype.eletype
                else:
                    check_type = x.mtype.restype
        return check_type
        
    
    def visitAssign(self, ast, param):
        lhs = ast.lhs
        rhs = ast.rhs
        dimen = []
        lhs_name = ""
        lhsType = Unknown()
        rhsType = Unknown()
        if not isinstance(lhs, ArrayCell):
        # check lhs co phai la ArrayType
            for x in param:
                if lhs.name == x.name:
                    if isinstance(x.mtype.restype, ArrayType):
                        dimen = x.mtype.restype.dimen
                        break
            lhsType = self.visit(lhs, param)
            lhs_name = lhs.name
        else:
            lhsType = self.visit(lhs, param)
            lhs_name = lhs.arr.name
        if isinstance(rhs, ArrayLiteral):
            rhsType = self.visit(rhs, (dimen, param))
        else:
            rhsType = self.visit(rhs, param)
        # visit  
        if isinstance(rhsType, VoidType):
            raise TypeCannotBeInferred(ast)
        elif isinstance(lhsType, Unknown) and not isinstance(rhsType, Unknown):
            for idx, x in enumerate(param):
                if lhs_name == x.name and isinstance(x.mtype.restype, Unknown):
                    # param[idx].mtype.restype = rhsType
                    x.mtype.restype = rhsType
                    #break
        elif not isinstance(lhsType, Unknown) and isinstance(rhsType, Unknown):
            for idx, x in enumerate(param):
                if rhs.name == x.name:
                    param[idx].mtype.restype = lhsType
                    break
        elif not isinstance(lhsType, type(rhsType)):
            raise TypeMismatchInStatement(ast)  #xem lai cho nay
        elif isinstance(lhsType, ArrayType) and isinstance(rhsType, ArrayType):
            for idx, x in enumerate(param):
                if lhs_name == x.name:
                    param[idx].mtype.restype = rhsType
                    break
        # else:
        #     for idx, x in enumerate(param):
        #        if lhs.name == x.name:
        #             param[idx].mtype.restype = rhsType
        
    
    def visitIf(self, ast, param):
        ifthenStmt = ast.ifthenStmt
        elseStmt = ast.elseStmt
        local_var = []
        for x in ifthenStmt:
            local_var = []
            expr = x[0]
            vardecl = x[1]
            stmt = x[2]
            typeExpr = self.visit(expr, param)
            for y in vardecl:
                temp = self.visit(y, local_var)
                local_var.append(temp)
            for y in stmt:
                self.visit(y, local_var + param)          
        local_var = []
        for x in elseStmt[0]:
            temp = self.visit(x, local_var)
            local_var.append(temp)
        for x in elseStmt[1]:
            self.visit(x, local_var + param) 
            
        for y in (local_var + param):
            print(y)         
    
    def visitFor(self, ast, param):
        local_var = []
        typeIdx = self.visit(ast.idx1, param)
        print(typeIdx)
        if not isinstance(typeIdx, (IntType, Unknown)):
            raise TypeMismatchInStatement(ast)
        exp1 = self.visit(ast.expr1, param)
        exp2 = self.visit(ast.expr2, param)
        exp3 = self.visit(ast.expr3, param)
        print(exp1)
        for x in ast.loop[0]:
            temp = self.visit(x, local_var)
            local_var.append(temp)
        for x in ast.loop[1]:
            self.visit(x, local_var + param)
    
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
        getIntype = []
        newParamFunc = []
        for x in param:
            if x.name == ast.method.name:
                if not isinstance(x.mtype.restype, VoidType):
                    raise TypeMismatchInStatement(ast)
                getIntype = x.mtype.intype
        if len(ast.param) != len(getIntype):
            raise TypeMismatchInStatement(ast)
        if ast.param != []:
            for idx, x in enumerate(ast.param):
                check_exp = self.visit(x, param)
                if isinstance(check_exp, Unknown):
                    raise TypeCannotBeInferred(ast)
                if isinstance(getIntype[idx], Unknown) or isinstance(getIntype[idx], type(check_exp)):    
                    newParamFunc.append(check_exp)
                elif not isinstance(getIntype[idx], type(check_exp)):
                    raise TypeMismatchInStatement(ast)  
            for x in param:
                if x.name == ast.method.name:
                    x.mtype.intype = newParamFunc              
        # for x in param:
        #     print(x)
    
    def visitIntLiteral(self, ast, param):
        return IntType()
    
    def visitFloatLiteral(self, ast, param):
        return FloatType()
    
    def visitBooleanLiteral(self, ast, param):
        return BoolType()
    
    def visitStringLiteral(self, ast, param):
        return StringType()

    def visitArrayLiteral(self, ast, param):
        # check ArrayType
        dimen = []
        def checkBlockLit(dimen, arrList):
            # print(dimen[0])
            # print(arrList)
            # print("********")
            if dimen[0] != len(arrList):
                raise TypeCannotBeInferred(ast)
            curDimen = dimen[1:]
            if curDimen == []:
                return True
            for x in arrList:
                checkBlockLit(curDimen, x.value)
        if isinstance(param, tuple):
            dimen = param[0]
            checkBlockLit(param[0], ast.value)
            param = param[1]
        getType = Unknown()
        head = self.visit(ast.value[0],param)
        for x in ast.value:
           temp = self.visit(x,param)
           if not isinstance(head, type(temp)):
                raise TypeCannotBeInferred(ast)
        getType = head
        if isinstance(getType, ArrayType):
            getType = getType.eletype
        return ArrayType(dimen, getType)
