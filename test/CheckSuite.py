import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):

    def test_0(self):
        """Simple program: main"""
        input = """Function: test
                   Body:
                   EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_1(self):
        """Simple program: main"""
        input = """
        Var: x;
Function: main
Body:
    Var: x;
EndBody.
Function: foo
Parameter: x
Body:
    Var: a[3][3], b[3] = {1,2,3}, c = 1.5, d[2] = {1.3, 1.2e3};
    a[b[1] + 1] = d[1] *. c;
    a[1] = 1+ 2 + 3; 
EndBody.
        """
#         input = """
# Var: x;b
# Function: main
# Body:
#     Var: x;
# EndBody.
# Function: foo
# Parameter: x, e
# Body:
#     Var: y[2], c[2][2][3] = {{{1,2,3},{4,5,6}},{{1,2,3},{8,9,10}}};
# EndBody."""
#         input = Program(
#     [
#         FuncDecl(
#             Id("main"),
#             [],
#             (
#                 [
#                     VarDecl(
#                         Id("x"),
#                         [2,3],
#                         ArrayLiteral(
#                             [
#                                 ArrayLiteral(
#                                 [
#                                     IntLiteral(1),
#                                     IntLiteral(2),
#                                     IntLiteral(3)
#                                 ]
#                                 ),
#                                 ArrayLiteral(
#                                 [
#                                     IntLiteral(4),
#                                     IntLiteral(5),
#                                     IntLiteral(6)
#                                 ]
#                                 )
#                             ]
#                         )
#                     )
#                 ],
#                 [
#                     Assign(
#                         Id("x"),
#                         ArrayLiteral(
#                             [
#                                 ArrayLiteral(
#                                 [
#                                     IntLiteral(1),
#                                     IntLiteral(2),
#                                     IntLiteral(3)
#                                 ]
#                                 ),
#                                 ArrayLiteral(
#                                 [
#                                     IntLiteral(4),
#                                     IntLiteral(5),
#                                     IntLiteral(6)
#                                 ]
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         )
#     ])
        expect = str(Undeclared(Function(),"foo1"))
        self.assertTrue(TestChecker.test(input,expect,401))

    # def test_0(self):
    #     """Simple program: main"""
    #     input = """Function: main
    #                Body:
    #                     foo();
    #                EndBody.
    #                Function: test
    #                Body:
    #                EndBody."""
    #     expect = str(Undeclared(Function(),"foo"))
    #     self.assertTrue(TestChecker.test(input,expect,400))

    # def test_diff_numofparam_stmt(self):
    #     """Complex program"""
    #     input = """Function: main
    #                Body:
    #                     printStrLn();
    #                 EndBody."""
    #     expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
    #     self.assertTrue(TestChecker.test(input,expect,401))
    #
    # def test_diff_numofparam_expr(self):
    #     """More complex program"""
    #     input = """Function: main
    #                 Body:
    #                     printStrLn(read(4));
    #                 EndBody."""
    #     expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
    #     self.assertTrue(TestChecker.test(input,expect,402))
    #
    # def test_undeclared_function_use_ast(self):
    #     """Simple program: main """
    #     input = Program([FuncDecl(Id("main"),[],([],[
    #         CallExpr(Id("foo"),[])]))])
    #     expect = str(Undeclared(Function(),"foo"))
    #     self.assertTrue(TestChecker.test(input,expect,403))
    #
    # def test_diff_numofparam_expr_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],([],[
    #                 CallStmt(Id("printStrLn"),[
    #                     CallExpr(Id("read"),[IntLiteral(4)])
    #                     ])]))])
    #     expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
    #     self.assertTrue(TestChecker.test(input,expect,404))
    #
    # def test_diff_numofparam_stmt_use_ast(self):
    #     """Complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],([],[
    #                 CallStmt(Id("printStrLn"),[])]))])
    #     expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
    #     self.assertTrue(TestChecker.test(input,expect,405))
