import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):

    def test_0(self):
        """Simple program: main"""
        input = """Function: main
                   Parameter: x[3], y
                   Body:
                        Var: z[2][3] = {{1,2,3},{4,5,6}};
                        Var: main, a;
                        x[1] = 1;
                        a = 1;
                   EndBody.
                   """
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,400))


    def test_1(self):
        """Simple program: main"""
        input = """
Var: x;
Function: main
Body:
    Var: x;
    Var: x;
EndBody.
Function: foo
Parameter: x, y
Body:
    Var: a[3][3], b[3] = {1,2,3}, c = 1.5, d[2] = {1.3, 1.2e3};
    a[b[1] + 1] = d[1] *. c;
    x = d[3];
    y = int_of_string("1") + 1;
    foo1(1,d[1],x);
EndBody.
Function: foo1
Parameter: x, y, z
Body:
    Var: a = 11;
    x = 1;
    y = 1.5;
    If !(a > 10) Then
        Var: x;
        x = True;
    ElseIf !(y >. 1.2) && True Then
        Var: x;
        x = "String";
    Else
        Var: f = 1;
        For (f = 1, f < 1, 1) Do
            Var: x[3];
            x = {1,2,3};
            While x[1] < 1 Do
                Var: f, b = 10, a[3] = {1.4, 1.2, 1.0};
                Var: e = True;
                f = b + int_of_float(1.5);
                a[0] = 2.0 *. float_of_int(f);
                foo(float_of_int(x[2]), f);
                Do
                    Var: a = 5;
                While (x[2] > 10) || (False && e) EndDo.
            EndWhile.
        EndFor.
    EndIf.
    a = 2;
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
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_2(self):
        """Simple program: main"""
        input = """Function: main
                   Body:
                        foo();
                   EndBody.
                   Function: test
                   Body:
                   EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_diff_numofparam_stmt(self):
        """Complex program"""
        input = """Function: main
                   Body:
                        printStrLn();
                    EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,407))
    #
    def test_diff_numofparam_expr(self):
        """More complex program"""
        input = """Function: main
                    Body:
                        printStrLn(read(4));
                    EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([FuncDecl(Id("main"),[],([],[
            CallExpr(Id("foo"),[])]))])
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_diff_numofparam_expr_use_ast(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[
                        CallExpr(Id("read"),[IntLiteral(4)])
                        ])]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_diff_numofparam_stmt_use_ast(self):
        """Complex program"""
        input = Program([
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,405))
