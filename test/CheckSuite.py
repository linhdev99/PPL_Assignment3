import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):

#     def test_0(self):
#         """Simple program: main"""
#         input = """Function: main
#                    Parameter: x[3], y
#                    Body:
#                         Var: z[2][3] = {{1,2,3},{4,5,6}};
#                         Var: main, a;
#                         x[1] = 1;
#                         a = 1;
#                    EndBody.
#                    """
#         expect = str("")
#         self.assertTrue(TestChecker.test(input,expect,400))
#
#
#     def test_1(self):
#         """Simple program: main"""
#         input = """
# Var: x;
# Function: main
# Body:
#     Var: x;
#     Var: x;
# EndBody.
# Function: foo
# Parameter: x, y
# Body:
#     Var: a[3][3], b[3] = {1,2,3}, c = 1.5, d[2] = {1.3, 1.2e3};
#     a[b[1] + 1] = d[1] *. c;
#     x = d[3];
#     y = int_of_string("1") + 1;
#     foo1(1,d[1],x);
# EndBody.
# Function: foo1
# Parameter: x, y, z
# Body:
#     Var: a = 11;
#     x = 1;
#     y = 1.5;
#     If !(a > 10) Then
#         Var: x;
#         x = True;
#     ElseIf !(y >. 1.2) && True Then
#         Var: x;
#         x = "String";
#     Else
#         Var: f = 1;
#         For (f = 1, f < 1, 1) Do
#             Var: x[3];
#             x = {1,2,3};
#             While x[1] < 1 Do
#                 Var: f, b = 10, a[3] = {1.4, 1.2, 1.0};
#                 Var: e = True;
#                 f = b + int_of_float(1.5);
#                 a[0] = 2.0 *. float_of_int(f);
#                 foo(float_of_int(x[2]), f);
#                 Do
#                     Var: a = 5;
#                 While (x[2] > 10) || (False && e) EndDo.
#             EndWhile.
#         EndFor.
#     EndIf.
#     a = 2;
# EndBody.
#         """
# #         input = """
# # Var: x;b
# # Function: main
# # Body:
# #     Var: x;
# # EndBody.
# # Function: foo
# # Parameter: x, e
# # Body:
# #     Var: y[2], c[2][2][3] = {{{1,2,3},{4,5,6}},{{1,2,3},{8,9,10}}};
# # EndBody."""
# #         input = Program(
# #     [
# #         FuncDecl(
# #             Id("main"),
# #             [],
# #             (
# #                 [
# #                     VarDecl(
# #                         Id("x"),
# #                         [2,3],
# #                         ArrayLiteral(
# #                             [
# #                                 ArrayLiteral(
# #                                 [
# #                                     IntLiteral(1),
# #                                     IntLiteral(2),
# #                                     IntLiteral(3)
# #                                 ]
# #                                 ),
# #                                 ArrayLiteral(
# #                                 [
# #                                     IntLiteral(4),
# #                                     IntLiteral(5),
# #                                     IntLiteral(6)
# #                                 ]
# #                                 )
# #                             ]
# #                         )
# #                     )
# #                 ],
# #                 [
# #                     Assign(
# #                         Id("x"),
# #                         ArrayLiteral(
# #                             [
# #                                 ArrayLiteral(
# #                                 [
# #                                     IntLiteral(1),
# #                                     IntLiteral(2),
# #                                     IntLiteral(3)
# #                                 ]
# #                                 ),
# #                                 ArrayLiteral(
# #                                 [
# #                                     IntLiteral(4),
# #                                     IntLiteral(5),
# #                                     IntLiteral(6)
# #                                 ]
# #                                 )
# #                             ]
# #                         )
# #                     )
# #                 ]
# #             )
# #         )
# #     ])
#         expect = ""
#         self.assertTrue(TestChecker.test(input,expect,401))
#
#     def test_2(self):
#         """Simple program: main"""
#         input = """Function: main
#                    Body:
#                         foo();
#                    EndBody.
#                    Function: test
#                    Body:
#                    EndBody."""
#         expect = str(Undeclared(Function(),"foo"))
#         self.assertTrue(TestChecker.test(input,expect,406))
#
#     def test_diff_numofparam_stmt(self):
#         """Complex program"""
#         input = """Function: main
#                    Body:
#                         printStrLn();
#                     EndBody."""
#         expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
#         self.assertTrue(TestChecker.test(input,expect,407))
#     #
#     def test_diff_numofparam_expr(self):
#         """More complex program"""
#         input = """Function: main
#                     Body:
#                         printStrLn(read(4));
#                     EndBody."""
#         expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
#         self.assertTrue(TestChecker.test(input,expect,402))
#
#     def test_undeclared_function_use_ast(self):
#         """Simple program: main """
#         input = Program([FuncDecl(Id("main"),[],([],[
#             CallExpr(Id("foo"),[])]))])
#         expect = str(Undeclared(Function(),"foo"))
#         self.assertTrue(TestChecker.test(input,expect,403))
#
#     def test_diff_numofparam_expr_use_ast(self):
#         """More complex program"""
#         input = Program([
#                 FuncDecl(Id("main"),[],([],[
#                     CallStmt(Id("printStrLn"),[
#                         CallExpr(Id("read"),[IntLiteral(4)])
#                         ])]))])
#         expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
#         self.assertTrue(TestChecker.test(input,expect,404))
#
#     def test_diff_numofparam_stmt_use_ast(self):
#         """Complex program"""
#         input = Program([
#                 FuncDecl(Id("main"),[],([],[
#                     CallStmt(Id("printStrLn"),[])]))])
#         expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
#         self.assertTrue(TestChecker.test(input,expect,405))

    def test_400(self):
        input  = """
        Var: test, test;
        Function: main
            Body:
            EndBody.
        """
        expect = str(Redeclared(Variable(), 'test'))
        self.assertTrue(TestChecker.test(input,expect,400))
    def test_401(self):
        input  = """
        Function: main
            Body:
            foo();
            EndBody.
        """
        expect = str(Undeclared(Function(), 'foo'))
        self.assertTrue(TestChecker.test(input,expect,401))
    def test_402(self):
        input  = """
        Function: main
            Body:
            printStrLn(read(4));
            EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id('read'),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,402))
    def test_403(self):
        input  = """
        Function: main
            Body:
            printStrLn();
            EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('printStrLn'),[])))
        self.assertTrue(TestChecker.test(input,expect,403))
    def test_404(self):
        input  = """
        Function: main
            Body:
            EndBody.
        Function: main
            Body:
            EndBody.
        """
        expect = str(Redeclared(Function(), 'main'))
        self.assertTrue(TestChecker.test(input,expect,404))
    def test_405(self):
        input  = """
        Function: main
            Parameter: a, a
            Body:
            EndBody.
        """
        expect = str(Redeclared(Parameter(), 'a'))
        self.assertTrue(TestChecker.test(input,expect,405))
    def test_406(self):
        input  = """
        Function: main
            Body:
            x = 1;
            EndBody.
        """
        expect = str(Undeclared(Identifier(), 'x'))
        self.assertTrue(TestChecker.test(input,expect,406))
    def test_407(self):
        input  = """
        Var: x = 1;
        Function: main
            Body:
            x = 2;
            EndBody.
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,407))
    def test_408(self):
        input  = """
        Function: main
            Parameter: x, y ,z
            Body:
            y = z + foo(x);
            EndBody.
        Function: foo
            Parameter: x
            Body:
            EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id('y'),BinaryOp( '+', Id('z'),CallExpr(Id('foo'),[Id('x')])))))
        self.assertTrue(TestChecker.test(input,expect,408))
    # def test_409(self):
    #     input  = """
    #     Function: main
    #         Parameter: x, y ,z
    #         Body:
    #         x = 1;
    #         y = z + foo(x);
    #         EndBody.
    #     Function: foo
    #         Parameter: x
    #         Body:
    #         x=1.1;
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Assign(Id('x'),FloatLiteral(1.1))))
    #     self.assertTrue(TestChecker.test(input,expect,409))
    # def test_410(self):
    #     input  = """
    #     Function: main
    #         Parameter: x, y ,z
    #         Body:
    #         x = 1;
    #         y = z + foo(x);
    #         foo(x);
    #         EndBody.
    #     Function: foo
    #         Parameter: x
    #         Body:
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(CallStmt(Id('foo'),[Id('x')])))
    #     self.assertTrue(TestChecker.test(input,expect,410))
    # def test_411(self):
    #     input  = """
    #     Function: main
    #         Parameter: x, y ,z
    #         Body:
    #         x = 1;
    #         foo(x);
    #         y = z + foo(x);
    #         EndBody.
    #     Function: foo
    #         Parameter: x
    #         Body:
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInExpression(BinaryOp( '+', Id('z'),CallExpr(Id('foo'),[Id('x')]))))
    #     self.assertTrue(TestChecker.test(input,expect,411))
    # def test_412(self):
    #     input  = """
    #     Function: main
    #         Parameter: x, y ,z
    #         Body:
    #         x = 1;
    #         y = z + foo(x,y);
    #         EndBody.
    #     Function: foo
    #         Parameter: x
    #         Body:
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInExpression(CallExpr(Id('foo'),[Id('x'),Id('y')])))
    #     self.assertTrue(TestChecker.test(input,expect,412))
    # def test_413(self):
    #     input  = """
    #     Function: foo
    #         Parameter: x
    #         Body:
    #         Var: y;
    #         y = 1;
    #         foo(y);
    #         x= 1.2;
    #         EndBody.
    #     Function: main
    #         Parameter: x, y ,z
    #         Body:
    #         x = 1.1;
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Assign(Id('x'),FloatLiteral(1.2))))
    #     self.assertTrue(TestChecker.test(input,expect,413))
    def test_414(self):
        input  = """
        Function: main
            Parameter: x, y ,z
            Body:
            y = x || (x>z);
            EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp( '>', Id('x'),Id('z'))))
        self.assertTrue(TestChecker.test(input,expect,414))
    # def test_415(self):
    #     input  = """
    #     Function: main
    #         Parameter: x, y ,z
    #         Body:
    #         y = (x>z) || x;
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInExpression(BinaryOp( '||', BinaryOp( '>', Id('x'),Id('z')),Id('x'))))
    #     self.assertTrue(TestChecker.test(input,expect,415))
    # def test_416(self):
    #     input  = """
    #     Function: foo
    #         Parameter: x
    #         Body:
    #         x=1.1;
    #         Return { True };
    #         EndBody.
    #     Function: main
    #         Parameter: x, y
    #         Body:
    #         foo(x)[0] = x || (x>y);
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInExpression(BinaryOp( '||', Id('x'),BinaryOp( '>', Id('x'),Id('y')))))
    #     self.assertTrue(TestChecker.test(input,expect,416))
    def test_417(self):
        input  = """
        Function: foo
            Body:
            EndBody.
        Function: main
            Parameter: x, y
            Body:
            x = 1 + foo();
            EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp( '+', IntLiteral(1),CallExpr(Id('foo'),[]))))
        self.assertTrue(TestChecker.test(input,expect,417))
    def test_418(self):
        input  = """
        Function: foo
            Body:
            Return 1;
            EndBody.
        Function: main
            Parameter: x, y
            Body:
            x = 1. +. foo();
            EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp( '+.', FloatLiteral(1.0),CallExpr(Id('foo'),[]))))
        self.assertTrue(TestChecker.test(input,expect,418))
    def test_419(self):
        input  = """
        Var: test;
        Function: main
            Parameter: t
            Body:
            t = True;
            While t Do
                Var: t;
                EndWhile.
            EndBody.
        """
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,419))
    def test_420(self):
        input  = """
        Var: test;
        Function: main
            Parameter: t
            Body:
            Do
                Var: t;
                While 1 EndDo.
            EndBody.
        """
        expect = str(TypeMismatchInStatement(Dowhile( ([VarDecl(Id('t'), [], None)],[]),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,420))
    def test_421(self):
        input  = """
        Var: test;
        Function: main
            Body:
            Var: x;
            For (x = 1, x<10, 2) Do
                Var: y;
                EndFor.
            x = 1.1;
            EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('x'),FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input,expect,421))
    def test_422(self):
        input  = """
        Var: test;
        Function: main
            Body:
            Var: x;
            For (x = 1, 10, 2) Do
                Var: y;
                EndFor.
            EndBody.
        """
        expect = str(TypeMismatchInStatement(For(Id('x'),IntLiteral(1),IntLiteral(10),IntLiteral(2), ([VarDecl(Id('y'), [], None)],[]) )))
        self.assertTrue(TestChecker.test(input,expect,422))
    def test_423(self):
        input  = """
        Var: test;
        Function: main
            Body:
            For (x = 1, x<5, 2) Do
                Var: x;
                EndFor.
            EndBody.
        """
        expect = str(Undeclared(Identifier(), 'x'))
        self.assertTrue(TestChecker.test(input,expect,423))
    def test_424(self):
        input  = """
        Var: test = "21312";
        Function: main
            Body:
            test = 1;
            EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('test'),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,424))
    def test_425(self):
        input  = """
        Var: test[3] = { 1, 2, 3 };
        Function: main
            Body:
            test[0] =  2 * test[1];
            test[2] = 5. *. 3.;
            EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('test'),[IntLiteral(2)]),BinaryOp( '*.', FloatLiteral(5.0),FloatLiteral(3.0)))))
        self.assertTrue(TestChecker.test(input,expect,425))
    def test_426(self):
        input  = """
        Var: test;
        Function: main
            Parameter: x
            Body:
            x = test[0];
            EndBody.
        """
        # WTF is this?
        expect = str(TypeMismatchInExpression(ArrayCell(Id('test'),[IntLiteral(0)])))
        self.assertTrue(TestChecker.test(input,expect,426))
    def test_427(self):
        input  = """
        Var: test[2][2];
        Function: main
            Parameter: x
            Body:
            x= test[1];
            EndBody.
        """
        expect = str(TypeMismatchInExpression(ArrayCell(Id('test'),[IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input,expect,427))
    def test_428(self):
        input  = """
        Var: test[1];
        Function: main
            Parameter: x
            Body:
            x = test[1.1];
            EndBody.
        """
        expect = str(TypeMismatchInExpression(ArrayCell(Id('test'),[FloatLiteral(1.1)])))
        self.assertTrue(TestChecker.test(input,expect,428))
    def test_429(self):
        input  = """
        Var: test;
        Function: foo
            Body:
            EndBody.
        Function: main
            Body:
            foo(1);
            EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('foo'),[IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input,expect,429))
    def test_430(self):
        input  = """
        Var: test;
        Function: foo
            Body:
            EndBody.
        Function: main
            Body:
            test = foo(1);
            EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id('foo'),[IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input,expect,430))
    def test_431(self):
        input  = """
        Var: test;
        Function: foo
            Body:
            EndBody.
        """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_432(self):
        input  = """
        Var: test;
        Function: main
            Parameter: x
            Body:
            If True Then
                Var:x;
                x = 1;
            ElseIf False Then
                x = True;
            Else
                x = 2.1;
            EndIf.
            EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('x'),FloatLiteral(2.1))))
        self.assertTrue(TestChecker.test(input,expect,432))
    def test_433(self):
        input  = """
        Var: test;
        Function: main
            Body:
            Var: main;
            main();
            EndBody.
        """
        expect = str(Undeclared(Function(), 'main'))
        self.assertTrue(TestChecker.test(input,expect,433))
    # def test_434(self):
    #     input  = """
    #     Var: test;
    #     Function: main
    #         Body:
    #         If True Then
    #             Return 1;
    #         ElseIf False Then
    #             Return 1.1;
    #         Else
    #             Return 2.1;
    #         EndIf.
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Return(FloatLiteral(1.1))))
    #     self.assertTrue(TestChecker.test(input,expect,434))
    # def test_435(self):
    #     input  = """
    #     Function: factorial
    #         Parameter: n
    #         Body:
    #             If n == 0 Then
    #                 Return 0;
    #             Else
    #                 Return n * factorial(n - 1);
    #             EndIf.
    #         EndBody.
    #     Function: main
    #         Body:
    #             Return factorial(1);
    #         EndBody.
    #     """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input,expect,435))
    # def test_436(self):
    #     input  = """
    #     Function: main **main:: unknown -> unknown **
    #         Parameter: x
    #         Body:
    #            Var: y = 1; **infer y:: int**
    #            x = 1.0; **infer x:: float**
    #            main(y); ** main:: int|float -> void?**
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(CallStmt(Id('main'),[Id('y')])))
    #     self.assertTrue(TestChecker.test(input,expect,436))
    # def test_437(self):
    #     input  = """
    #     Function: main **main:: unknown -> unknown **
    #     Parameter: x
    #     Body:
    #        Var: y = 1; **infer y:: int**
    #        main(y); ** main:: int -> void => infer x:: int?**
    #        x = 1.0; ** Error?**
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Assign(Id('x'),FloatLiteral(1.0))))
    #     self.assertTrue(TestChecker.test(input,expect,437))
    # def test_438(self):
    #     input  = """
    #     Function: main
    #         Body:
    #             foo()[0] = 1; **1**
    #         EndBody.
    #
    #     Function: foo
    #         Body:
    #             Return 0; **2**
    #         EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(Assign(ArrayCell(CallExpr(Id('foo'),[]),[IntLiteral(0)]),IntLiteral(1))))
    #     self.assertTrue(TestChecker.test(input,expect,438))
    # def test_439(self):
    #     input  = """
    #     Var: test;
    #     Function: main
    #         Parameter: test
    #         Body:
    #         Var: test;
    #         EndBody.
    #     """
    #     expect = str(Redeclared(Variable(), 'test'))
    #     self.assertTrue(TestChecker.test(input,expect,439))
    # def test_440(self):
    #     input  = """
    #     Var: test;
    #     Function: foo
    #         Body:
    #         While True Do
    #             If test Then
    #                 Return True;
    #             EndIf.
    #         EndWhile.
    #         Return False;
    #         EndBody.
    #     Function: main
    #         Body:
    #         Var: x;
    #         x = foo();
    #         test = 1;
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Assign(Id('test'),IntLiteral(1))))
    #     self.assertTrue(TestChecker.test(input,expect,440))
    # def test_441(self):
    #     input  = """
    #     Var: test;
    #     Function: foo
    #         Parameter: x
    #         Body:
    #         Return;
    #         EndBody.
    #     Function: main
    #         Body:
    #         foo(foo(1));
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(CallStmt(Id('foo'),[CallExpr(Id('foo'),[IntLiteral(1)])])))
    #     self.assertTrue(TestChecker.test(input,expect,441))
    # def test_442(self):
    #     input  = """
    #     Var: test;
    #     Function: foo
    #         Parameter: x
    #         Body:
    #         Return ;
    #         EndBody.
    #     Function: foo1
    #         Parameter: x
    #         Body:
    #         Return 1;
    #         EndBody.
    #     Function: main
    #         Body:
    #         Var: x;
    #         x = foo(foo(1));
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInExpression(CallExpr(Id('foo'),[CallExpr(Id('foo'),[IntLiteral(1)])])))
    #     self.assertTrue(TestChecker.test(input,expect,442))
    # def test_443(self):
    #     input  = """
    #     Var: test;
    #     Function: foo
    #         Body:
    #         Return 1;
    #         EndBody.
    #     Function: main
    #         Body:
    #         foo();
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(CallStmt(Id('foo'),[])))
    #     self.assertTrue(TestChecker.test(input,expect,443))
    # def test_444(self):
    #     input  = """
    #     Var: test;
    #     Function: main
    #         Body:
    #         foo()[0] = 1;
    #         EndBody.
    #     Function: foo
    #         Body:
    #         EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(Assign(ArrayCell(CallExpr(Id('foo'),[]),[IntLiteral(0)]),IntLiteral(1))))
    #     self.assertTrue(TestChecker.test(input,expect,444))
    # def test_445(self):
    #     input  = """
    #     Var: test;
    #     Function: main
    #         Body:
    #         If (test) Then
    #             Var: test;
    #             If (test) Then
    #                 Var: test;
    #                 test = 1;
    #             EndIf.
    #         EndIf.
    #         test =2;
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Assign(Id('test'),IntLiteral(2))))
    #     self.assertTrue(TestChecker.test(input,expect,445))
    # def test_446(self):
    #     input  = """
    #     Var: arr = {{1,2},{3,4}};
    #     Function: test_array
    #         Body:
    #             arr = arr[0] * 2 - 3 + (1\\2);
    #         EndBody.
    #     Function: main
    #         Body:
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInExpression(ArrayCell(Id('arr'),[IntLiteral(0)])))
    #     self.assertTrue(TestChecker.test(input,expect,446))
    # def test_447(self):
    #     input  = """
    #     Var: test, x, y;
    #     Function: fact
    #     Parameter: n
    #     Body:
    #         If n == 0 Then
    #             Return x + 3 + -. 2 * y +1;
    #         Else
    #             Return n * fact(n-1);
    #         EndIf.
    #     EndBody.
    #     Function: main
    #         Body:
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInExpression(UnaryOp( '-.' ,IntLiteral(2))))
    #     self.assertTrue(TestChecker.test(input,expect,447))
    # def test_448(self):
    #     input  = """
    #     Var: test, some;
    #     Function: testExpression
    #     Body:
    #         some = 1 + 2 * 3 \ 2 - some % 5;
    #         Return some;
    #     EndBody.
    #     Function: main
    #         Body:
    #         testExpression();
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(CallStmt(Id('testExpression'),[])))
    #     self.assertTrue(TestChecker.test(input,expect,448))
    # def test_449(self):
    #     input  = """
    #     Var: a;
    #     Function: test_while_condition
    #         Body:
    #             While a < 0 Do
    #                 Var: b[3][2] = {{1,2}, {3,4}, {5,6}};
    #                 While a < 0 Do
    #                     Var: b[3] = {1,2,3};
    #                     a = a + 1 + b[1];
    #                 EndWhile.
    #                 a = a + 1 + b[1][1];
    #             EndWhile.
    #         EndBody.
    #     Function: main
    #         Body:
    #         test_while_condition();
    #         EndBody.
    #     """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input,expect,449))
    # def test_450(self):
    #     input  = """
    #     Var: test, x, y;
    #     Function: fact
    #     Parameter: n
    #     Body:
    #         If n == 0 Then
    #             Var: x;
    #             Return x + 3 + - 2 * y +1;
    #         Else
    #             Var: x;
    #             Return 1;
    #         EndIf.
    #     EndBody.
    #     Function: main
    #         Body:
    #         x = fact(1);
    #         EndBody.
    #     """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input,expect,450))
    # def test_451(self):
    #     input  = """
    #     Var: test;
    #     Function: main
    #         Body:
    #         foo()[1] = 1;
    #         EndBody.
    #     Function: foo
    #         Body:
    #         Return {1,2};
    #         EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(Assign(ArrayCell(CallExpr(Id('foo'),[]),[IntLiteral(1)]),IntLiteral(1))))
    #     self.assertTrue(TestChecker.test(input,expect,451))
    # def test_452(self):
    #     input  = """
    #     Var: test[5];
    #     Function: main
    #         Body:
    #         test[0] = 1;
    #         test[1] = 1.1;
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('test'),[IntLiteral(1)]),FloatLiteral(1.1))))
    #     self.assertTrue(TestChecker.test(input,expect,452))
    # def test_453(self):
    #     input  = """
    #     Var: test[5];
    #     Function: foo
    #         Body:
    #         Return 1;
    #         EndBody.
    #     Function: main
    #         Body:
    #         test[0] = 1;
    #         foo = test[0];
    #         EndBody.
    #     """
    #     expect = str(Undeclared(Identifier(), 'foo'))
    #     self.assertTrue(TestChecker.test(input,expect,453))
    # def test_454(self):
    #     input  = """
    #     Var: test[5];
    #     Function: foo
    #         Body:
    #         Return 1;
    #         EndBody.
    #     Function: main
    #         Body:
    #         test[0] = 1;
    #         test[0] = foo;
    #         EndBody.
    #     """
    #     expect = str(Undeclared(Identifier(), 'foo'))
    #     self.assertTrue(TestChecker.test(input,expect,454))
    # def test_455(self):
    #     input  = """
    #     Var: test[5];
    #     Function: foo
    #         Body:
    #         Return 1.;
    #         EndBody.
    #     Function: main
    #         Body:
    #         test[0] = 1;
    #         test[0] = foo();
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('test'),[IntLiteral(0)]),CallExpr(Id('foo'),[]))))
    #     self.assertTrue(TestChecker.test(input,expect,455))
    # def test_456(self):
    #     input  = """
    #     Var: test[5];
    #     Function: foo
    #         Body:
    #         Return 1;
    #         EndBody.
    #     Function: main
    #         Body:
    #         test[0] = 1;
    #         test[0] = foo() * foo();
    #         EndBody.
    #     """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input,expect,456))
    # def test_457(self):
    #     input  = """
    #     Var: test[5];
    #     Function: foo
    #         Body:
    #         Return 1;
    #         EndBody.
    #     Function: main
    #         Body:
    #         test[0] = 1;
    #         test[0] = foo() \\ foo();
    #         EndBody.
    #     """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input,expect,457))
    # def test_458(self):
    #     input  = """
    #     Var: test[5][5];
    #     Function: main
    #         Body:
    #         test[1] = {1};
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInExpression(ArrayCell(Id('test'),[IntLiteral(1)])))
    #     self.assertTrue(TestChecker.test(input,expect,458))
    # def test_459(self):
    #     input  = """
    #     Var: test[1][1]={{1}};
    #     Function: main
    #         Body:
    #         test[0][0] = {{1.}};
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('test'),[IntLiteral(0),IntLiteral(0)]),ArrayLiteral([ArrayLiteral([FloatLiteral(1.0)])]))))
    #     self.assertTrue(TestChecker.test(input,expect,459))
    # def test_460(self):
    #     input  = """
    #     Var: test[1][1]={{1}};
    #     Function: main
    #         Body:
    #         test[0] = {1};
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInExpression(ArrayCell(Id('test'),[IntLiteral(0)])))
    #     self.assertTrue(TestChecker.test(input,expect,460))
    # def test_461(self):
    #     input  = """
    #     Var: test[5];
    #     Function: foo
    #         Body:
    #         Return 1;
    #         EndBody.
    #     Function: main
    #         Body:
    #         test[0] = 1.;
    #         foo();
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(CallStmt(Id('foo'),[])))
    #     self.assertTrue(TestChecker.test(input,expect,461))
    # def test_462(self):
    #     input  = """
    #     Var: test[5];
    #     Function: foo
    #         Body:
    #         Return 1;
    #         EndBody.
    #     Function: main
    #         Body:
    #         test[0] = 1;
    #         test[0] = foo(1);
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInExpression(CallExpr(Id('foo'),[IntLiteral(1)])))
    #     self.assertTrue(TestChecker.test(input,expect,462))
    # def test_463(self):
    #     input  = """
    #     Var: test[5];
    #     Function: foo
    #         Body:
    #         Return 1;
    #         EndBody.
    #     Function: main
    #         Body:
    #         foo();
    #         test[0] = foo();
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(CallStmt(Id('foo'),[])))
    #     self.assertTrue(TestChecker.test(input,expect,463))
    # def test_464(self):
    #     input  = """
    #     Var: test;
    #     Function: main
    #         Parameter: x,y,z
    #         Body:
    #         x = 1;
    #         main(1.,1,1);
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(CallStmt(Id('main'),[FloatLiteral(1.0),IntLiteral(1),IntLiteral(1)])))
    #     self.assertTrue(TestChecker.test(input,expect,464))
    # def test_465(self):
    #     input  = """
    #     Var: test;
    #     Function: main
    #         Body:
    #         x = 1;
    #         y = 1;
    #         z = 1.;
    #         main(1,1,1.);
    #         EndBody.
    #     """
    #     expect = str(Undeclared(Identifier(), 'x'))
    #     self.assertTrue(TestChecker.test(input,expect,465))
    # def test_466(self):
    #     input  = """
    #     Var: test;
    #     Function: main
    #         Parameter: x,y,z
    #         Body:
    #         x = y+z;
    #         main(1,1.1,1);
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(CallStmt(Id('main'),[IntLiteral(1),FloatLiteral(1.1),IntLiteral(1)])))
    #     self.assertTrue(TestChecker.test(input,expect,466))
    # def test_467(self):
    #     input  = """
    #     Var: test;
    #     Function: main
    #         Body:
    #         main();
    #         Return 1;
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Return(IntLiteral(1))))
    #     self.assertTrue(TestChecker.test(input,expect,467))
    # def test_468(self):
    #     input  = """
    #     Var: test;
    #     Function: main
    #         Body:
    #         main()[0] = 1;
    #         Return {1};
    #         EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(Assign(ArrayCell(CallExpr(Id('main'),[]),[IntLiteral(0)]),IntLiteral(1))))
    #     self.assertTrue(TestChecker.test(input,expect,468))
    # def test_469(self):
    #     input  = """
    #     Var: test;
    #     Function: main
    #         Body:
    #         main()[0] = test+1;
    #         EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(Assign(ArrayCell(CallExpr(Id('main'),[]),[IntLiteral(0)]),BinaryOp( '+', Id('test'),IntLiteral(1)))))
    #     self.assertTrue(TestChecker.test(input,expect,469))
    # def test_470(self):
    #     input  = """
    #     Var: test;
    #     Function: main
    #         Parameter: x,y,z
    #         Body:
    #         test = (x+y) == z;
    #         x = test;
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Assign(Id('x'),Id('test'))))
    #     self.assertTrue(TestChecker.test(input,expect,470))
    # def test_471(self):
    #     input  = """
    #     Var: test;
    #     Function: main
    #         Body:
    #         test = main;
    #         EndBody.
    #     """
    #     expect = str(Undeclared(Identifier(), 'main'))
    #     self.assertTrue(TestChecker.test(input,expect,471))
    # def test_472(self):
    #     input  = """
    #     Var: test;
    #     Function: main
    #         Body:
    #         test = float_to_int(1);
    #         test = 1.+.1.;
    #         EndBody.
    #     """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input,expect,472))
    # def test_473(self):
    #     input  = """
    #     Var: test;
    #     Function: main
    #         Body:
    #         test = float_of_string("asda");
    #         test = 1.;
    #         EndBody.
    #     """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input,expect,473))
    # def test_474(self):
    #     input  = """
    #     Var: test;
    #     Function: main
    #         Body:
    #         test = "";
    #         test = 1 + 1;
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Assign(Id('test'),BinaryOp( '+', IntLiteral(1),IntLiteral(1)))))
    #     self.assertTrue(TestChecker.test(input,expect,474))
    # def test_475(self):
    #     input  = """
    #     Var: test;
    #     Function: main
    #         Parameter: test, test
    #         Body:
    #         EndBody.
    #     """
    #     expect = str(Redeclared(Parameter(), 'test'))
    #     self.assertTrue(TestChecker.test(input,expect,475))
    # def test_476(self):
    #     input  = """
    #     Var: test;
    #     Function: float_to_int
    #         Body:
    #         EndBody.
    #     Function: main
    #         Body:
    #         EndBody.
    #     """
    #     expect = str(Redeclared(Function(), 'float_to_int'))
    #     self.assertTrue(TestChecker.test(input,expect,476))
    # def test_477(self):
    #     input  = """
    #     Var: test;
    #     Function: main
    #         Body:
    #         EndBody.
    #     Function: main
    #         Body:
    #         EndBody.
    #     """
    #     expect = str(Redeclared(Function(), 'main'))
    #     self.assertTrue(TestChecker.test(input,expect,477))
    # def test_478(self):
    #     input  = """
    #     Var: test;
    #     Function: main
    #         Body:
    #         Var: x = "";
    #         print(x);
    #         x = 1;
    #         printStrLn(x);
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Assign(Id('x'),IntLiteral(1))))
    #     self.assertTrue(TestChecker.test(input,expect,478))
    # def test_479(self):
    #     input  = """
    #     Var: test;
    #     Function: main
    #         Body:
    #         Var: x = "";
    #         read(x);
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(CallStmt(Id('read'),[Id('x')])))
    #     self.assertTrue(TestChecker.test(input,expect,479))
    # def test_480(self):
    #     input  = """
    #     Var: test;
    #     Function: main
    #         Body:
    #         Var: x;
    #         x = (1+.1) == 1;
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInExpression(BinaryOp( '+.', IntLiteral(1),IntLiteral(1))))
    #     self.assertTrue(TestChecker.test(input,expect,480))
    # def test_481(self):
    #     input  = """
    #     Var: test;
    #     Function: main
    #         Body:
    #         Var: x;
    #         x = (1.+.1.) == 1;
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInExpression(BinaryOp( '==', BinaryOp( '+.', FloatLiteral(1.0),FloatLiteral(1.0)),IntLiteral(1))))
    #     self.assertTrue(TestChecker.test(input,expect,481))
    # def test_482(self):
    #     input  = """
    #     Var: test;
    #     Function: main
    #         Body:
    #         Var: x;
    #         x = 1== 1;
    #         x = True;
    #         Return main();
    #         EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(Return(CallExpr(Id('main'),[]))))
    #     self.assertTrue(TestChecker.test(input,expect,482))
    # def test_483(self):
    #     input  = """
    #     Var: test;
    #     Function: foo
    #         Body:
    #         Return test;
    #         EndBody.
    #     Function: main
    #         Body:
    #         Return foo();
    #         EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(Return(Id('test'))))
    #     self.assertTrue(TestChecker.test(input,expect,483))
    # def test_484(self):
    #     input  = """
    #     Var: test;
    #     Function: main
    #         Body:
    #         Var: test;
    #         test = test;
    #         EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(Assign(Id('test'),Id('test'))))
    #     self.assertTrue(TestChecker.test(input,expect,484))
    # def test_485(self):
    #     input  = """
    #     Var: test;
    #     Function: main
    #         Body:
    #         Return test + 1;
    #         EndBody.
    #     """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input,expect,485))
    # def test_486(self):
    #     input  = """
    #     Var: test;
    #     Function: main
    #         Body:
    #         test = 1 <2;
    #         test = 1. <. 2.;
    #         Return test +1;
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInExpression(BinaryOp( '+', Id('test'),IntLiteral(1))))
    #     self.assertTrue(TestChecker.test(input,expect,486))
    # def test_487(self):
    #     input  = """
    #     Var: test;
    #     Function: main
    #         Body:
    #         test = 1>2 ;
    #         test = 1 ==2 ;
    #         test = 1+1;
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Assign(Id('test'),BinaryOp( '+', IntLiteral(1),IntLiteral(1)))))
    #     self.assertTrue(TestChecker.test(input,expect,487))
    # def test_488(self):
    #     input  = """
    #     Var: test;
    #     Function: main
    #         Body:
    #         test =x() +1 ;
    #         EndBody.
    #     """
    #     expect = str(Undeclared(Function(), 'x'))
    #     self.assertTrue(TestChecker.test(input,expect,488))
    # def test_489(self):
    #     input  = """
    #     Var: test;
    #     Function: main
    #         Body:
    #         test = test();
    #         EndBody.
    #     """
    #     expect = str(Undeclared(Function(), 'test'))
    #     self.assertTrue(TestChecker.test(input,expect,489))
    # def test_490(self):
    #     input  = """
    #     Var: test;
    #     Function: main
    #         Body:
    #         test = test() +1 ;
    #         EndBody.
    #     """
    #     expect = str(Undeclared(Function(), 'test'))
    #     self.assertTrue(TestChecker.test(input,expect,490))
    # def test_491(self):
    #     input  = """
    #     Var: main;
    #     Function: main
    #         Body:
    #         EndBody.
    #     """
    #     expect = str(Redeclared(Function(), 'main'))
    #     self.assertTrue(TestChecker.test(input,expect,491))
    # def test_492(self):
    #     input  = """
    #     Var: test;
    #     Function: main
    #         Body:
    #         printLn(test);
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(CallStmt(Id('printLn'),[Id('test')])))
    #     self.assertTrue(TestChecker.test(input,expect,492))
    # def test_493(self):
    #     input  = """
    #     Var: test;
    #     Function: main
    #         Body:
    #         print(test);
    #         test = 1;
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Assign(Id('test'),IntLiteral(1))))
    #     self.assertTrue(TestChecker.test(input,expect,493))
    # def test_494(self):
    #     input  = """
    #     Var: test;
    #     Function: main
    #         Body:
    #         print(test +. {1,1});
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInExpression(BinaryOp( '+.', Id('test'),ArrayLiteral([IntLiteral(1),IntLiteral(1)]))))
    #     self.assertTrue(TestChecker.test(input,expect,494))
    # def test_495(self):
    #     input  = """
    #     Var: test;
    #     Function: main
    #         Body:
    #         read();
    #         print(read());
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(CallStmt(Id('read'),[])))
    #     self.assertTrue(TestChecker.test(input,expect,495))
    # def test_496(self):
    #     input  = """
    #     Var: test;
    #     Function: main
    #         Parameter: x
    #         Body:
    #         Var: hihi;
    #         print(hihi);
    #         hihi = x;
    #         print(main(x));
    #         Return 1;
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Return(IntLiteral(1))))
    #     self.assertTrue(TestChecker.test(input,expect,496))
    # def test_497(self):
    #     input  = """
    #     Var: test[5];
    #     Function: main
    #         Parameter: x[5]
    #         Body:
    #         test[0] = 1;
    #         main(test);
    #         x[0] = 1.;
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('x'),[IntLiteral(0)]),FloatLiteral(1.0))))
    #     self.assertTrue(TestChecker.test(input,expect,497))
    # def test_498(self):
    #     input  = """
    #     Var: test;
    #     Function: main
    #         Parameter: x
    #         Body:
    #         x = main(1) == 1;
    #         Return 1;
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Assign(Id('x'),BinaryOp( '==', CallExpr(Id('main'),[IntLiteral(1)]),IntLiteral(1)))))
    #     self.assertTrue(TestChecker.test(input,expect,498))
    # def test_499(self):
    #     input  = """
    #     Var: test;
    #     Function: foo
    #         Parameter: x
    #         Body:
    #         x = 1.1;
    #         Return {1.1};
    #         EndBody.
    #     Function: main
    #         Parameter: x
    #         Body:
    #         foo(main(1))[0] = x +. 1.;
    #         Return 1.1;
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInExpression(BinaryOp( '+.', Id('x'),FloatLiteral(1.0))))
    #     self.assertTrue(TestChecker.test(input,expect,499))
