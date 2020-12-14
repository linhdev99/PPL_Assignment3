from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

class ASTGeneration(BKITVisitor):
    def visitProgram(self,ctx:BKITParser.ProgramContext):
        mainList = []
        for x in ctx.main():
            mainCell = self.visitMain(x)
            if isinstance(mainCell, list):
                mainList.extend(mainCell if mainCell else [])
            else:
                mainList.append(mainCell)
        return Program(mainList)

    def visitMain(self, ctx:BKITParser.MainContext):
        if ctx.var_declare():
            return self.visitVar_declare(ctx.var_declare())
        else:
            return self.visitFunc_declare(ctx.func_declare())

    def visitVar_declare(self, ctx:BKITParser.Var_declareContext):
        return self.visitVar_list(ctx.var_list())

    def visitVar_list(self, ctx:BKITParser.Var_listContext):
        return self.visitVar_normal(ctx.var_normal())

    def visitVar_normal(self, ctx:BKITParser.Var_normalContext):
        varListDecl = []
        for x in ctx.var_normal_list():
            temp = self.visitVar_normal_list(x)
            if isinstance(temp, list):
                varListDecl.extend(temp if temp else [])
            else:
                varListDecl.append(temp)
        return varListDecl

    def visitVar_normal_list(self, ctx:BKITParser.Var_normal_listContext):
        m_getScalarVar = self.visitScalar_var_int(ctx.scalar_var_int())
        m_variable = m_getScalarVar[0]
        m_varDimen = m_getScalarVar[1]
        m_varInit = None
        if ctx.array_lit():
            m_varInit = self.visitArray_lit(ctx.array_lit())
            return VarDecl(m_variable,m_varDimen,m_varInit)
        elif ctx.all_lit():
            m_varInit = self.visitAll_lit(ctx.all_lit())
            return VarDecl(m_variable,m_varDimen,m_varInit)
        else:
            return VarDecl(m_variable,m_varDimen,m_varInit)

    def visitScalar_var_int(self, ctx:BKITParser.Scalar_var_intContext):
        if ctx.getChildCount() > 1:
            listIndex = []
            for x in ctx.index_var_int():
                valueIndex = self.visitIndex_var_int(x)
                listIndex.append(valueIndex)
            return [Id(ctx.ID().getText()),listIndex]
        else:
            return [Id(ctx.ID().getText()),[]]

    def visitIndex_var_int(self,ctx:BKITParser.Index_var_intContext):
        valueBase = ctx.INTLIT().getText()
        if valueBase.count('x',0,len(valueBase)) or valueBase.count('X',0,len(valueBase)):
            return int(valueBase, 16)
        elif valueBase.count('o',0,len(valueBase)) or valueBase.count('O',0,len(valueBase)):
            return int(valueBase, 8)
        else:
            return int(valueBase)

    def visitAll_lit(self,ctx:BKITParser.All_litContext):
        if ctx.int_lit():
            return self.visitInt_lit(ctx.int_lit())
        elif ctx.float_lit():
            return self.visitFloat_lit(ctx.float_lit())
        elif ctx.string_lit():
            return self.visitString_lit(ctx.string_lit())
        elif ctx.bool_lit():
            return self.visitBool_lit(ctx.bool_lit())
        else:
            return self.visitAll_lit(ctx.all_lit(0))

    def visitFunc_declare(self, ctx:BKITParser.Func_declareContext):
        getIdFunc = Id(ctx.ID().getText())
        if ctx.parameter_func():
            listParameter = self.visitParameter_func(ctx.parameter_func())
        else:
            listParameter = []
        getBodyDecl = self.visitBody_declare(ctx.body_declare())
        listVarDecl = getBodyDecl[0]
        listStmt = getBodyDecl[1]
        return FuncDecl(getIdFunc,listParameter,(listVarDecl,listStmt))

    def visitParameter_func(self,ctx:BKITParser.Parameter_funcContext):
        temp = []
        for x in ctx.scalar_var_int():
            m_getScalarVar = self.visitScalar_var_int(x)
            m_variable = m_getScalarVar[0]
            m_varDimen = m_getScalarVar[1]
            m_varInit = None
            totalValue = VarDecl(m_variable,m_varDimen,m_varInit)
            if isinstance(totalValue, list):
                temp.extend(totalValue)
            else:
                temp.append(totalValue)
        return temp

    def visitBody_declare(self,ctx:BKITParser.Body_declareContext):
        return self.visitBody(ctx.body())

    def visitBody(self,ctx:BKITParser.BodyContext):
        lst_vardecl = []
        lst_funcdecl = []
        if ctx.var_declare():
            for x in ctx.var_declare():
                temp_var = self.visitVar_declare(x)
                if isinstance(temp_var, list):
                    lst_vardecl.extend(temp_var if temp_var else [])
                else:
                    lst_vardecl.append(temp_var)
        if ctx.stmt():
            for x in ctx.stmt():
                temp_stmt = self.visitStmt(x)
                if isinstance(temp_stmt, list):
                    lst_funcdecl.extend(temp_stmt if temp_stmt else [])
                else:
                    lst_funcdecl.append(temp_stmt)
        return [lst_vardecl, lst_funcdecl]

    def visitStmt(self,ctx:BKITParser.StmtContext):
        if ctx.stmt_notfunc():
            return self.visitStmt_notfunc(ctx.stmt_notfunc())
        else:
            return self.visitStmt_spe(ctx.stmt_spe())

    def visitStmt_notfunc(self,ctx:BKITParser.Stmt_notfuncContext):
        if ctx.if_stmt():
            return self.visitIf_stmt(ctx.if_stmt())
        elif ctx.for_stmt():
            return self.visitFor_stmt(ctx.for_stmt())
        elif ctx.while_stmt():
            return self.visitWhile_stmt(ctx.while_stmt())
        elif ctx.doWhile_stmt():
            return self.visitDoWhile_stmt(ctx.doWhile_stmt())

    def visitStmt_spe(self,ctx:BKITParser.Stmt_speContext):
        if ctx.assign_stmt():
            return self.visitAssign_stmt(ctx.assign_stmt())
        elif ctx.break_stmt():
            return self.visitBreak_stmt(ctx.break_stmt())
        elif ctx.continue_stmt():
            return self.visitContinue_stmt(ctx.continue_stmt())
        elif ctx.return_stmt():
            return self.visitReturn_stmt(ctx.return_stmt())
        elif ctx.call_stmt():
            return self.visitCall_stmt(ctx.call_stmt())

    def visitExp(self, ctx:BKITParser.ExpContext):
        if ctx.RELATIONAL():
            return BinaryOp(
                ctx.RELATIONAL().getText(),
                self.visitExp1(ctx.exp1(0)),
                self.visitExp1(ctx.exp1(1))
            )
        else:
            return self.visitExp1(ctx.exp1(0))

    def visitExp1(self,ctx:BKITParser.Exp1Context):
        if ctx.AND():
            return BinaryOp(
                ctx.AND().getText(),
                self.visitExp1(ctx.exp1()),
                self.visitExp2(ctx.exp2())
            )
        elif ctx.OR():
            return BinaryOp(
                ctx.OR().getText(),
                self.visitExp1(ctx.exp1()),
                self.visitExp2(ctx.exp2())
            )
        else:
            return self.visitExp2(ctx.exp2())

    def visitExp2(self,ctx:BKITParser.Exp2Context):
        if ctx.ADD():
            return BinaryOp(
                ctx.ADD().getText(),
                self.visitExp2(ctx.exp2()),
                self.visitExp3(ctx.exp3())
            )
        elif ctx.SUB():
            return BinaryOp(
                ctx.SUB().getText(),
                self.visitExp2(ctx.exp2()),
                self.visitExp3(ctx.exp3())
            )
        elif ctx.ADDDOT():
            return BinaryOp(
                ctx.ADDDOT().getText(),
                self.visitExp2(ctx.exp2()),
                self.visitExp3(ctx.exp3())
            )
        elif ctx.SUBDOT():
            return BinaryOp(
                ctx.SUBDOT().getText(),
                self.visitExp2(ctx.exp2()),
                self.visitExp3(ctx.exp3())
            )
        else:
            return self.visitExp3(ctx.exp3())

    def visitExp3(self,ctx:BKITParser.Exp3Context):
        if ctx.MUL():
            return BinaryOp(
                ctx.MUL().getText(),
                self.visitExp3(ctx.exp3()),
                self.visitExp4(ctx.exp4())
            )
        elif ctx.DIV():
            return BinaryOp(
                ctx.DIV().getText(),
                self.visitExp3(ctx.exp3()),
                self.visitExp4(ctx.exp4())
            )
        elif ctx.MOD():
            return BinaryOp(
                ctx.MOD().getText(),
                self.visitExp3(ctx.exp3()),
                self.visitExp4(ctx.exp4())
            )
        elif ctx.MULDOT():
            return BinaryOp(
                ctx.MULDOT().getText(),
                self.visitExp3(ctx.exp3()),
                self.visitExp4(ctx.exp4())
            )
        elif ctx.DIVDOT():
            return BinaryOp(
                ctx.DIVDOT().getText(),
                self.visitExp3(ctx.exp3()),
                self.visitExp4(ctx.exp4())
            )
        else:
            return self.visitExp4(ctx.exp4())

    def visitExp4(self,ctx:BKITParser.Exp4Context):
        if ctx.NOT():
            return UnaryOp(
                ctx.NOT().getText(),
                self.visitExp4(ctx.exp4())
            )
        else:
            return self.visitExp5(ctx.exp5())

    def visitExp5(self,ctx:BKITParser.Exp5Context):
        if ctx.SUB():
            return UnaryOp(
                ctx.SUB().getText(),
                self.visitExp5(ctx.exp5())
            )
        elif ctx.SUBDOT():
            return UnaryOp(
                ctx.SUBDOT().getText(),
                self.visitExp5(ctx.exp5())
            )
        else:
            temp = self.visitExp6(ctx.exp6())
            if isinstance(temp, list):
                return ArrayCell(temp[0], temp[1])
            else:
                return temp

    def visitExp6(self,ctx:BKITParser.Exp6Context):
        if ctx.op_index():
            getID = self.visitExp6(ctx.exp6())
            getOpIdx = self.visitOp_index(ctx.op_index())
            if isinstance(getID, list):
                value = []
                value.extend(getID[1])
                value.append(getOpIdx)
                return [getID[0], value]
            else:
                return [getID, [getOpIdx]]
        else:
            temp = self.visitOperands(ctx.operands())
            return temp

    def visitOp_index(self,ctx:BKITParser.Op_indexContext):
        temp = self.visitExp(ctx.exp())
        return temp

    def visitOperands(self,ctx:BKITParser.OperandsContext):
        if ctx.LP():
            return self.visitExp(ctx.exp())
        elif ctx.func_call():
            value = self.visitFunc_call(ctx.func_call())
            return CallExpr(value[0], value[1])
        elif ctx.LCB():
            listLiteral = []
            for x in ctx.all_lit():
                temp = self.visitAll_lit(x)
                if isinstance(temp, list):
                    listLiteral.extend(temp if temp else [])
                else:
                    listLiteral.append(temp)
            return ArrayLiteral(listLiteral)
        elif ctx.all_lit(0):
            return self.visitAll_lit(ctx.all_lit(0))
        elif ctx.ID():
            return Id(ctx.ID().getText())

    def visitAssign_stmt(self, ctx:BKITParser.Assign_stmtContext):
        temp_lhs = None
        getID = Id(ctx.ID().getText())
        if ctx.op_index():
            lstOpIdx = []
            for x in ctx.op_index():
                getOpIdx = self.visitOp_index(x)
                if isinstance(getOpIdx, list):
                    lstOpIdx.extend(getOpIdx if getOpIdx else [])
                else:
                    lstOpIdx.append(getOpIdx)
            temp_lhs = ArrayCell(getID, lstOpIdx)
        else:
            temp_lhs = getID
        temp_rhs = self.visitExp(ctx.exp())
        return Assign(temp_lhs, temp_rhs)

    def visitScalar_var(self,ctx:BKITParser.Scalar_varContext):
        temp_expr = Id(ctx.ID().getText())
        if ctx.index_var():
            temp_index = []
            for x in ctx.index_var():
                value = self.visitIndex_var(ctx.index_var())
                if isinstance(value, list):
                    temp_index.extend(value if value else [])
                else:
                    temp_index.append(value)
            return ArrayCell(temp_expr,temp_index)
        else:
            return temp_expr

    def visitIndex_var(self,ctx:BKITParser.Index_varContext):
        return self.visitExp(ctx.exp())

    def visitIf_stmt(self, ctx:BKITParser.If_stmtContext):
        tempExpr = self.visitExp(ctx.exp())

        tempBody = []
        tempElseIf = []
        tempElse = ([],[])

        temp_var = []
        temp_stmt = []

        listIfThenStmt = []
        # for x in ctx.body():
        #     temp = self.visitBody(x)
        #     if temp[0] == 0:
        #         if isinstance(temp[1], list):
        #             temp_var.extend(temp[1])
        #         else:
        #             temp_var.append(temp[1])
        #     else:
        #         if isinstance(temp[1], list):
        #             temp_stmt.extend(temp[1])
        #         else:
        #             temp_stmt.append(temp[1])
        getLstBody = self.visitBody(ctx.body())
        tempBody.append(getLstBody[0])
        tempBody.append(getLstBody[1])
        tupleIfStmt = (tempExpr, tempBody[0], tempBody[1])
        listIfThenStmt.append(tupleIfStmt)

        for x in ctx.elseif_stmt():
            temp = self.visitElseif_stmt(x)
            if isinstance(temp, list):
                tempElseIf.extend(temp if temp else [])
            else:
                tempElseIf.append(temp)
        if not (tempElseIf is None):
            listIfThenStmt.extend(tempElseIf)

        if ctx.else_stmt():
            tempElse = self.visitElse_stmt(ctx.else_stmt())
        tupleElseStmt = tempElse

        return If(listIfThenStmt,tupleElseStmt)

    def visitElseif_stmt(self,ctx:BKITParser.Elseif_stmtContext):
        tempExpr = self.visitExp(ctx.exp())
        tempBody = []
        temp_var = []
        temp_stmt = []
        # for x in ctx.body():
        #     temp = self.visitBody(x)
        #     if temp[0] == 0:
        #         if isinstance(temp[1], list):
        #             temp_var.extend(temp[1])
        #         else:
        #             temp_var.append(temp[1])
        #     else:
        #         if isinstance(temp[1], list):
        #             temp_stmt.extend(temp[1])
        #         else:
        #             temp_stmt.append(temp[1])
        getLstBody = self.visitBody(ctx.body())
        tempBody.append(getLstBody[0])
        tempBody.append(getLstBody[1])
        return (tempExpr, tempBody[0], tempBody[1])

    def visitElse_stmt(self,ctx:BKITParser.Else_stmtContext):
        tempBody = []
        temp_var = []
        temp_stmt = []
        # for x in ctx.body():
        #     temp = self.visitBody(x)
        #     if temp[0] == 0:
        #         if isinstance(temp[1], list):
        #             temp_var.extend(temp[1])
        #         else:
        #             temp_var.append(temp[1])
        #     else:
        #         if isinstance(temp[1], list):
        #             temp_stmt.extend(temp[1])
        #         else:
        #             temp_stmt.append(temp[1])
        getLstBody = self.visitBody(ctx.body())
        tempBody.append(getLstBody[0])
        tempBody.append(getLstBody[1])
        return (tempBody[0], tempBody[1])

    def visitFor_stmt(self, ctx:BKITParser.For_stmtContext):
        """
        idx1: Id
        expr1:Expr
        expr2:Expr
        expr3:Expr
        loop: Tuple[List[VarDecl],List[Stmt]]
        """
        getID = Id(ctx.ID().getText())
        getExpr1 = self.visitExp(ctx.exp())
        getExpr2 = self.visitConditionExpr(ctx.conditionExpr())
        getExpr3 = self.visitUpdateExpr(ctx.updateExpr())
        tempBody = []
        temp_var = []
        temp_stmt = []
        # for x in ctx.body():
        #     temp = self.visitBody(x)
        #     if temp[0] == 0:
        #         if isinstance(temp[1], list):
        #             temp_var.extend(temp[1])
        #         else:
        #             temp_var.append(temp[1])
        #     else:
        #         if isinstance(temp[1], list):
        #             temp_stmt.extend(temp[1])
        #         else:
        #             temp_stmt.append(temp[1])
        getLstBody = self.visitBody(ctx.body())
        tempBody.append(getLstBody[0])
        tempBody.append(getLstBody[1])
        getLoop = (tempBody[0], tempBody[1])
        return For(getID, getExpr1, getExpr2, getExpr3, getLoop)

    def visitConditionExpr(self,ctx:BKITParser.ConditionExprContext):
        return self.visitExp(ctx.exp())

    def visitUpdateExpr(self,ctx:BKITParser.UpdateExprContext):
        return self.visitExp(ctx.exp())

    def visitContinue_stmt(self, ctx:BKITParser.Continue_stmtContext):
        return Continue()

    def visitBreak_stmt(self, ctx:BKITParser.Break_stmtContext):
        return Break()

    def visitReturn_stmt(self, ctx:BKITParser.Return_stmtContext):
        temp = None
        if ctx.exp():
            temp = self.visitExp(ctx.exp())
        return Return(temp)

    def visitDoWhile_stmt(self, ctx:BKITParser.DoWhile_stmtContext):
        """
        sl:Tuple[List[VarDecl],List[Stmt]]
        exp: Expr
        """
        getExpr = self.visitExp(ctx.exp())
        tempBody = []
        temp_var = []
        temp_stmt = []
        # for x in ctx.body():
        #     temp = self.visitBody(x)
        #     if temp[0] == 0:
        #         if isinstance(temp[1], list):
        #             temp_var.extend(temp[1])
        #         else:
        #             temp_var.append(temp[1])
        #     else:
        #         if isinstance(temp[1], list):
        #             temp_stmt.extend(temp[1])
        #         else:
        #             temp_stmt.append(temp[1])
        getLstBody = self.visitBody(ctx.body())
        tempBody.append(getLstBody[0])
        tempBody.append(getLstBody[1])
        getBody = (tempBody[0], tempBody[1])
        return Dowhile(getBody, getExpr)

    def visitWhile_stmt(self, ctx:BKITParser.While_stmtContext):
        """
        exp: Expr
        sl:Tuple[List[VarDecl],List[Stmt]]
        """
        getExpr = self.visitExp(ctx.exp())
        tempBody = []
        temp_var = []
        temp_stmt = []
        # for x in ctx.body():
        #     temp = self.visitBody(x)
        #     if temp[0] == 0:
        #         if isinstance(temp[1], list):
        #             temp_var.extend(temp[1])
        #         else:
        #             temp_var.append(temp[1])
        #     else:
        #         if isinstance(temp[1], list):
        #             temp_stmt.extend(temp[1])
        #         else:
        #             temp_stmt.append(temp[1])
        getLstBody = self.visitBody(ctx.body())
        tempBody.append(getLstBody[0])
        tempBody.append(getLstBody[1])
        getBody = (tempBody[0], tempBody[1])
        return While(getExpr, getBody)

    def visitCall_stmt(self, ctx:BKITParser.Call_stmtContext):
        value = self.visitFunc_call(ctx.func_call())
        return CallStmt(value[0], value[1])

    def visitFunc_call(self,ctx:BKITParser.Func_callContext):
        if ctx.func_call_cell():
            return [Id(ctx.ID().getText()),self.visitFunc_call_cell(ctx.func_call_cell())]
        else:
            return [Id(ctx.ID().getText()),[]]

    def visitFunc_call_cell(self,ctx:BKITParser.Func_call_cellContext):
        temp = []
        for x in ctx.exp():
            valueCell = self.visitExp(x)
            if isinstance(valueCell, list):
                temp.extend(valueCell if valueCell else [])
            else:
                temp.append(valueCell)
        return temp

    def visitInt_lit(self, ctx:BKITParser.Int_litContext):
        valueBase = ctx.INTLIT().getText()
        if valueBase.count('x',0,len(valueBase)) or valueBase.count('X',0,len(valueBase)):
            return IntLiteral(int(valueBase, 16))
        elif valueBase.count('o',0,len(valueBase)) or valueBase.count('O',0,len(valueBase)):
            return IntLiteral(int(valueBase, 8))
        else:
            return IntLiteral(int(valueBase))

    def visitFloat_lit(self, ctx:BKITParser.Float_litContext):
        return FloatLiteral(float(ctx.FLOATLIT().getText()))

    def visitBool_lit(self, ctx:BKITParser.Bool_litContext):
        if ctx.TRUE():
            return BooleanLiteral(ctx.TRUE().getText())
        else:
            return BooleanLiteral(ctx.FALSE().getText())

    def visitString_lit(self, ctx:BKITParser.String_litContext):
        return StringLiteral(ctx.STRINGLIT().getText())

    def visitArray_lit(self, ctx:BKITParser.Array_litContext):
        temp = []
        for x in ctx.array_lit_cell():
            # temp.extend(self.visitArray_lit_cell(x))
            valueCell = self.visitArray_lit_cell(x)
            if isinstance(valueCell, list):
                temp.extend(valueCell if valueCell else [])
            else:
                temp.append(valueCell)
        return ArrayLiteral(temp)

    def visitArray_lit_cell(self,ctx:BKITParser.Array_lit_cellContext):
        if ctx.all_lit():
            return self.visitAll_lit(ctx.all_lit())
        else:
            return self.visitArray_lit(ctx.array_lit())
