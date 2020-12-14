import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test(self):
        input = """Function: main
        Body:
            Var: x[3][3];
            x[3][3] = {1,2,3};
        EndBody."""
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 201))
#     def test_0(self):
#         input = r"""Var:x;"""
#         expect = Program(
#             [
#                 VarDecl(
#                     Id("x"),
#                     [],
#                     None
#                 )
#             ]
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,300))
#
#     def test_1(self):
#         input = r"""Var:x,y;"""
#         expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)])
#         self.assertTrue(TestAST.checkASTGen(input,expect,301))
#
#     def test_2(self):
#         input = """Var:x,y[1];"""
#         expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[1],None)])
#         self.assertTrue(TestAST.checkASTGen(input,expect,302))
#
#     def test_3(self):
#         input = """Var:x,y[1]=1;"""
#         expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[1],IntLiteral(1))])
#         self.assertTrue(TestAST.checkASTGen(input,expect,303))
#
#     def test_4(self):
#         input = """Var:x = True;"""
#         expect = Program([VarDecl(Id("x"),[],BooleanLiteral(True))])
#         self.assertTrue(TestAST.checkASTGen(input,expect,304))
#
#     def test_5(self):
#         input = """Var:x = False;"""
#         expect = Program([VarDecl(Id("x"),[],BooleanLiteral(False))])
#         self.assertTrue(TestAST.checkASTGen(input,expect,305))
#
#     def test_6(self):
#         input = """Var:x = "False";"""
#         expect = Program([VarDecl(Id("x"),[],StringLiteral("False"))])
#         self.assertTrue(TestAST.checkASTGen(input,expect,306))
#
#     def test_7(self):
#         input = """Var:x = 1.2;"""
#         expect = Program([VarDecl(Id("x"),[],FloatLiteral(1.2))])
#         self.assertTrue(TestAST.checkASTGen(input,expect,307))
#
#     def test_8(self):
#         input = """Var:x[1] = 1.2;"""
#         expect = Program(
#             [
#                 VarDecl(
#                     Id("x"),
#                     [1],
#                     FloatLiteral(1.2)
#                 )
#             ]
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,308))
#
#     def test_9(self):
#         input = """Var:x[1][2][3], y[1][2] = {1,2};"""
#         expect = Program(
#             [
#                 VarDecl(
#                     Id("x"),
#                     [1,2,3],
#                     None
#                 ),
#                 VarDecl(
#                     Id("y"),
#                     [1,2],
#                     ArrayLiteral(
#                         [
#                             IntLiteral(1),
#                             IntLiteral(2)
#                         ]
#                     )
#                 )
#             ]
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,309))
#
#     def test_10(self):
#         input = """Var:x[1][2][3], y[3] = {1,2,{1,2,3}};"""
#         expect = Program([VarDecl(Id("x"),[1,2,3],None),VarDecl(Id("y"),[3],ArrayLiteral([IntLiteral(1),IntLiteral(2),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])]))])
#         self.assertTrue(TestAST.checkASTGen(input,expect,310))
#
#     def test_11(self):
#         input = """Var: m, n[10], e[1][2] = {{},{5}};"""
#         expect = Program([VarDecl(Id("m"),[],None), VarDecl(Id("n"),[10],None), VarDecl(Id("e"),[1,2],ArrayLiteral([ArrayLiteral([]), ArrayLiteral([IntLiteral(5)])]))])
#         self.assertTrue(TestAST.checkASTGen(input,expect,311))
#
#     def test_12(self):
#
#         input = """Var: m, n[20], b[2][3][5] = {2,{4},"d"};"""
#         expect = Program([VarDecl(Id("m"),[],None), VarDecl(Id("n"),[20],None), VarDecl(Id("b"),[2,3,5],ArrayLiteral([IntLiteral(2), ArrayLiteral([IntLiteral(4)]), StringLiteral("d")]))])
#         self.assertTrue(TestAST.checkASTGen(input,expect,312))
#
#     def test_13(self):
#         input = """Var:x = 0x3, y = 0X3;"""
#         expect = Program(
#             [
#                 VarDecl(
#                     Id("x"),
#                     [],
#                     IntLiteral(3)
#                 ),
#                 VarDecl(
#                     Id("y"),
#                     [],
#                     IntLiteral(3)
#                 )
#             ]
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,313))
#
#     def test_14(self):
#         input = """Var: a = 0o123, b = 0O123;"""
#         expect = Program(
#             [
#                 VarDecl(
#                     Id("a"),
#                     [],
#                     IntLiteral(83)
#                 ),
#                 VarDecl(
#                     Id("b"),
#                     [],
#                     IntLiteral(83)
#                 )
#             ]
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,314))
#
#     def test_15(self):
#         input = r"""Var: x = 1e3, y[5] = {0x2, 0o4, 1.e2, 24, 9}, z = 2.e3;"""
#         expect = Program(
#             [
#                 VarDecl(
#                     Id("x"),
#                     [],
#                     FloatLiteral(1000.0)
#                 ),
#                 VarDecl(
#                     Id("y"),
#                     [5],
#                     ArrayLiteral(
#                         [
#                             IntLiteral(2),
#                             IntLiteral(4),
#                             FloatLiteral(100.0),
#                             IntLiteral(24),
#                             IntLiteral(9)
#                         ]
#                     )
#                 ),
#                 VarDecl(
#                     Id("z"),
#                     [],
#                     FloatLiteral(2000.0)
#                 )
#             ]
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,315))
#
#     def test_16(self):
#         input = """Var: a[2][3] = {{},{4,"text"},{}};"""
#         expect = Program(
#             [
#                 VarDecl(
#                     Id("a"),
#                     [2,3],
#                     ArrayLiteral(
#                         [
#                             ArrayLiteral([]),
#                             ArrayLiteral(
#                                 [
#                                     IntLiteral(4),
#                                     StringLiteral("text")
#                                 ]
#                             ),
#                             ArrayLiteral([])
#                         ]
#                     )
#                 )
#             ]
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,316))
#
#     def test_17(self):
#         input = """Function: main
# Body:
#     foo();
# EndBody."""
#         expect = Program(
#             [
#                 FuncDecl(
#                     Id("main"),
#                     [],
#                     (
#                         [],
#                         [
#                             CallStmt(
#                                 Id("foo"),
#                                 []
#                             )
#                         ]
#                     )
#                 )
#             ]
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,317))
#
#     def test_18(self):
#         input = """Function: main
# Body:
#     a = foo();
# EndBody."""
#         expect = Program(
#             [
#                 FuncDecl(
#                     Id("main"),
#                     [],
#                     (
#                         [],
#                         [
#                             Assign(
#                                 Id("a"),
#                                 CallExpr(
#                                     Id("foo"),
#                                     []
#                                 )
#                             )
#                         ]
#                     )
#                 )
#             ]
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,318))
#
#     def test_19(self):
#         input = """Function: main
# Body:
#     Var: id[0x2][0X3];
#     Var: id[0o2][0O10];
#     foo();
#     a = foo();
# EndBody."""
#         expect = Program(
#             [
#                 FuncDecl(
#                     Id("main"),
#                     [],
#                     (
#                         [
#                             VarDecl(Id("id"),[2,3],None),
#                             VarDecl(Id("id"),[2,8],None)
#                         ],
#                         [
#                             CallStmt(
#                                 Id("foo"),
#                                 []
#                             ),
#                             Assign(
#                                 Id("a"),
#                                 CallExpr(
#                                     Id("foo"),
#                                     []
#                                 )
#                             )
#                         ]
#                     )
#                 )
#             ]
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,319))
#
#     def test_20(self):
#
#         input = """Function: foo
# Parameter: x
# Body:
# EndBody."""
#         expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None)],([],[]))])
#         self.assertTrue(TestAST.checkASTGen(input,expect,320))
#
#     def test_21(self):
#         input = """Function: foo
# Parameter: x, y[5][2]
# Body:
# EndBody."""
#         expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None),VarDecl(Id("y"),[5,2],None)],([],[]))])
#         self.assertTrue(TestAST.checkASTGen(input,expect,321))
#
#     def test_22(self):
#         input = """Var:x;
# Function: foo
# Parameter: x, y[5][2]
# Body:
# EndBody."""
#         expect = Program(
#                     [
#                         VarDecl(Id("x"),[],None),
#                         FuncDecl(Id("foo"),
#                                  [
#                                      VarDecl(Id("x"),[],None),
#                                      VarDecl(Id("y"),[5,2],None)
#                                  ],
#                                     (
#                                         [],
#                                         []
#                                     )
#                                  )
#                     ])
#         self.assertTrue(TestAST.checkASTGen(input,expect,322))
#
#     def test_23(self):
#         input = """Var:x;
# Function: foo
# Parameter: x, y[5][2]
# Body:
#     Var: r = 3.14, e = 2.7e1;
# EndBody."""
#         expect = Program(
#                     [
#                         VarDecl(Id("x"),[],None),
#                         FuncDecl(Id("foo"),
#                                  [
#                                      VarDecl(Id("x"),[],None),
#                                      VarDecl(Id("y"),[5,2],None)
#                                  ],
#                                     (
#                                         [
#                                             VarDecl(Id("r"),[],FloatLiteral(3.14)),
#                                             VarDecl(Id("e"),[],FloatLiteral(2.7e1))
#                                         ],
#                                         []
#                                     )
#                                  )
#                     ])
#         self.assertTrue(TestAST.checkASTGen(input,expect,323))
#
#     def test_24(self):
#         input = """Var:x;
# Function: foo
# Parameter: x, y[5][2]
# Body:
#     Var: r = 3.14, e = 2.7e1;
#     a = x;
# EndBody."""
#         expect = Program(
#                     [
#                         VarDecl(Id("x"),[],None),
#                         FuncDecl(Id("foo"),
#                                  [
#                                      VarDecl(Id("x"),[],None),
#                                      VarDecl(Id("y"),[5,2],None)
#                                  ],
#                                     (
#                                         [
#                                             VarDecl(Id("r"),[],FloatLiteral(3.14)),
#                                             VarDecl(Id("e"),[],FloatLiteral(2.7e1))
#                                         ],
#                                         [
#                                             Assign
#                                             (
#                                                 Id("a"),
#                                                 Id("x")
#                                             )
#                                         ]
#                                     )
#                                  )
#                     ])
#         self.assertTrue(TestAST.checkASTGen(input,expect,324))
#
#     def test_25(self):
#         input = r"""
#         Function: foo
#             Body:
#                 Break;
#                 Continue;
#             EndBody."""
#         expect = Program(
#                 [FuncDecl(Id("foo"),[],(
#                               [],
#                               [
#                                   Break(),
#                                   Continue()
#                               ]
#                             )
#                           )
#                 ]
#                 )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 325))
#
#     def test_26(self):
#         input = r"""
#         Function: foo
#             Body:
#                 a = foo();
#             EndBody."""
#         expect = Program(
#                 [FuncDecl(Id("foo"),[],
#                           (
#                               [],
#                               [
#                                   Assign(
#                                     Id("a"),
#                                     CallExpr(Id("foo"),[])
#                                   )
#                               ]
#                           )
#                           )
#                 ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 326))
#
#     def test_27(self):
#         input = r"""
#         Function: foo
#             Body:
#                 a = {1,3,5,7};
#             EndBody."""
#         expect = Program\
#                 (
#                 [FuncDecl(Id("foo"),[],
#                           (
#                               [],
#                               [
#                                   Assign(
#                                     Id("a"),
#                                     ArrayLiteral(
#                                         [
#                                         IntLiteral(1),
#                                         IntLiteral(3),
#                                         IntLiteral(5),
#                                         IntLiteral(7)
#                                         ]
#                                     )
#                                   )
#                               ]
#                           ))
#                 ]
#                 )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 327))
#
#     def test_28(self):
#         input = r"""
#         Function: foo
#             Body:
#                 a[2] = 5;
#             EndBody."""
#         expect = Program(
#                 [FuncDecl(Id("foo"),[],
#                           (
#                               [],
#                               [
#                                   Assign(
#                                     ArrayCell(
#                                         Id("a"),
#                                         [IntLiteral(2)]
#                                     ),
#                                     IntLiteral(5)
#                                   )
#                               ]
#                           ))
#                 ]
#                 )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 328))
#
#     def test_29(self):
#         input = r"""
#         Function: foo
#             Body:
#                 Return foo(x+2);
#             EndBody."""
#         expect = Program(
#                 [FuncDecl(Id("foo"),[],
#                           (
#                               [],
#                               [
#                                   Return(
#                                       CallExpr(
#                                           Id("foo"),
#                                           [BinaryOp(
#                                               "+",
#                                               Id("x"),
#                                               IntLiteral(2)
#                                           )]
#                                       )
#                                   )
#                               ]
#                           ))
#                 ]
#                 )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 329))
#
#     def test_30(self):
#         input = r"""
#         Function: foo
#             Body:
#                 If True Then
#                     foo();
#                 ElseIf False Then
#                     asd();
#                 ElseIf a < 2 Then
#                     Var: x;
#                 Else
#                     Var: x = 3;
#                     x = x + 1;
#                 EndIf.
#             EndBody."""
#         expect = Program(
#                 [FuncDecl(Id("foo"),
#                           [],
#                           (
#                               [],
#                               [
#                                   If(
#                                       [
#                                        (
#                                         BooleanLiteral(True),
#                                         [],
#                                         [
#                                             CallStmt(Id("foo"),[])
#                                         ]
#                                         ),
#                                         (
#                                         BooleanLiteral(False),
#                                         [],
#                                         [
#                                             CallStmt(Id("asd"),[])
#                                         ]
#                                         ),
#                                         (
#                                         BinaryOp("<",Id("a"),IntLiteral(2)),
#                                         [
#                                             VarDecl(Id("x"),[],None)
#                                         ],
#                                         []
#                                         )
#                                       ],
#                                       (
#                                           [
#                                               VarDecl(Id("x"),[],IntLiteral(3))
#                                           ],
#                                           [
#                                               Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))
#                                           ]
#                                       )
#                                   )
#                               ]
#                           ))
#                 ]
#                 )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 330))
#
#     def test_31(self):
#         input = r"""
#         Function: foo
#             Body:
#                 If x != y Then
#                     x = x+2*y-(3-4)\foo(x+1);
#                 EndIf.
#             EndBody."""
#         expect = Program(
#                 [FuncDecl(Id("foo"),
#                           [],
#                           (
#                               [],
#                               [
#                                   If(
#                                       [
#                                        (
#                                         BinaryOp("!=",Id("x"),Id("y")),
#                                         [],
#                                         [
#                                             Assign(
#                                                 Id("x"),
#                                                 BinaryOp("-",
#                                                          BinaryOp("+",
#                                                                   Id("x"),
#                                                                   BinaryOp("*",
#                                                                            IntLiteral(2),
#                                                                            Id("y")
#                                                                            )
#                                                                   ),
#                                                          BinaryOp("\\",
#                                                                   BinaryOp("-",
#                                                                            IntLiteral(3),
#                                                                            IntLiteral(4)),
#                                                                   CallExpr(
#                                                                       Id("foo"),
#                                                                       [BinaryOp("+",
#                                                                                 Id("x"),
#                                                                                 IntLiteral(1)
#                                                                                 )
#                                                                        ]
#                                                                   )
#                                                                   )
#                                                          )
#                                             )
#                                         ]
#                                         )
#                                       ],
#                                       (
#                                           [],
#                                           []
#                                       )
#                                   )
#                               ]
#                           ))
#                 ]
#                 )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 331))
#
#     def test_32(self):
#         input = r"""
#             Function: foo
#                 Body:
#                     For (i = 0, i < 5, 1) Do
#                         print(i);
#                     EndFor.
#                 EndBody."""
#         expect = Program(
#             [FuncDecl(
#                 Id("foo"),
#                 [],
#                 (
#                     [],
#                     [
#                         For(
#                             Id("i"),
#                             IntLiteral(0),
#                             BinaryOp("<",
#                                      Id("i"),
#                                      IntLiteral(5)),
#                             IntLiteral(1),
#                             (
#                                 [],
#                                 [
#                                     CallStmt(Id("print"),[Id("i")])
#                                 ]
#                             )
#                         )
#                     ]
#                 )
#             )
#             ]
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 332))
#
#     def test_333(self):
#         input = r"""
#             Function: testWhile
#                 Body:
#                     While (i > 10) Do
#                         i = i - 1;
#                     EndWhile.
#                 EndBody."""
#         expect = Program(
#             [
#                 FuncDecl(
#                     Id("testWhile"),
#                     [],
#                     (
#                         [],
#                         [
#                             While(
#                                 BinaryOp(
#                                     ">",
#                                     Id("i"),
#                                     IntLiteral(10)
#                                 ),
#                                 (
#                                     [],
#                                     [
#                                         Assign(
#                                             Id("i"),
#                                             BinaryOp(
#                                                 "-",
#                                                 Id("i"),
#                                                 IntLiteral(1)
#                                             )
#                                         )
#                                     ]
#                                 )
#                             )
#                         ]
#                     )
#                 )
#             ]
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 333))
#
#     def test_334(self):
#         input = r"""
#             Function: testWhile
#                 Body:
#                     While (i > 10) Do
#                     EndWhile.
#                 EndBody."""
#         expect = Program(
#             [
#                 FuncDecl(
#                     Id("testWhile"),
#                     [],
#                     (
#                         [],
#                         [
#                             While(
#                                 BinaryOp(
#                                     ">",
#                                     Id("i"),
#                                     IntLiteral(10)
#                                 ),
#                                 (
#                                     [],
#                                     []
#                                 )
#                             )
#                         ]
#                     )
#                 )
#             ]
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 334))
#
#     def test_335(self):
#         input = r"""
#             Function: testWhile
#                 Body:
#                     While (i < 10) Do
#                         Var: x = 10;
#                         i = x + 1;
#                     EndWhile.
#                 EndBody."""
#         expect = Program(
#             [
#                 FuncDecl(
#                     Id("testWhile"),
#                     [],
#                     (
#                         [],
#                         [
#                             While(
#                                 BinaryOp(
#                                     "<",
#                                     Id("i"),
#                                     IntLiteral(10)
#                                 ),
#                                 (
#                                     [
#                                         VarDecl(Id("x"),[],IntLiteral(10))
#                                     ],
#                                     [
#                                         Assign(
#                                             Id("i"),
#                                             BinaryOp(
#                                                 "+",
#                                                 Id("x"),
#                                                 IntLiteral(1)
#                                             )
#                                         )
#                                     ]
#                                 )
#                             )
#                         ]
#                     )
#                 )
#             ]
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 335))
#
#     def test_36(self):
#         input = r"""
#         Function: testDowhile
#             Body:
#                 Do
#                     i = i * 2;
#                     Break;
#                 While (i < 10)
#                 EndDo.
#             EndBody."""
#         expect = Program(
#             [
#                 FuncDecl(
#                     Id("testDowhile"),
#                     [],
#                     (
#                         [],
#                         [
#                             Dowhile(
#                                 (
#                                     [],
#                                     [
#                                         Assign(
#                                             Id("i"),
#                                             BinaryOp("*",Id("i"),IntLiteral(2))
#                                         ),
#                                         Break()
#                                     ]
#                                 ),
#                                 BinaryOp("<",Id("i"),IntLiteral(10))
#                             )
#                         ]
#                     )
#                 )
#             ]
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 336))
#
#     def test_37(self):
#         input = r"""Function: main
# Body:
#     a[1][2][3] = x[1][a][foo()];
# EndBody."""
#         expect = Program(
#             [
#                 FuncDecl(
#                     Id("main"),
#                     [],
#                     (
#                         [],
#                         [
#                             Assign(
#                                 ArrayCell(
#                                     Id("a"),
#                                     [
#                                         IntLiteral("1"),
#                                         IntLiteral("2"),
#                                         IntLiteral("3")
#                                     ]
#                                 ),
#                                 ArrayCell(
#                                     Id("x"),
#                                     [
#                                         IntLiteral("1"),
#                                         Id("a"),
#                                         CallExpr(
#                                             Id("foo"),
#                                             []
#                                         )
#                                     ]
#                                 )
#                             )
#                         ]
#                     )
#                 )
#             ]
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 337))
#
#     def test_38(self):
#         input = r"""
#         Function: foo
#             Body:
#                 a[i][1] = a[3][4] + 5 \ (2 * 3) -  a[6][b[1]];
#                 Return a[4][2];
#             EndBody."""
#         expect = Program(
#             [
#                 FuncDecl(
#                     Id("foo"),
#                     [],
#                     (
#                         [],
#                         [
#                             Assign(
#                                 ArrayCell(
#                                     Id("a"),
#                                     [
#                                         Id("i"),
#                                         IntLiteral("1")
#                                     ]
#                                 ),
#                                 BinaryOp(
#                                     "-",
#                                     BinaryOp(
#                                         "+",
#                                         ArrayCell(
#                                             Id("a"),
#                                             [
#                                                 IntLiteral(3),
#                                                 IntLiteral(4)
#                                             ]
#                                         ),
#                                         BinaryOp(
#                                             "\\",
#                                             IntLiteral(5),
#                                             BinaryOp(
#                                                 "*",
#                                                 IntLiteral(2),
#                                                 IntLiteral(3)
#                                             )
#                                         )
#                                     ),
#                                     ArrayCell(
#                                         Id("a"),
#                                         [
#                                             IntLiteral(6),
#                                             ArrayCell(
#                                                 Id("b"),
#                                                 [
#                                                     IntLiteral(1)
#                                                 ]
#                                             )
#                                         ]
#                                     )
#                                 )
#                             ),
#                             Return(
#                                 ArrayCell(
#                                     Id("a"),
#                                     [
#                                         IntLiteral(4),
#                                         IntLiteral(2)
#                                     ]
#                                 )
#                             )
#                         ]
#                     )
#                 )
#             ]
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 338))
#
#     def test_39(self):
#         input = r"""
#         Function: foo
#             Body:
#                 Return a[10][10];
#             EndBody."""
#         expect = Program(
#             [
#                 FuncDecl(
#                     Id("foo"),
#                     [],
#                     (
#                         [],
#                         [
#                             Return(
#                                 ArrayCell(
#                                     Id("a"),
#                                     [
#                                         IntLiteral(10),
#                                         IntLiteral(10)
#                                     ]
#                                 )
#                             )
#                         ]
#                     )
#                 )
#             ]
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 339))
#
#     def test_40(self):
#         input = r"""
#         Function: foo
#             Body:
#                 Var: x = "1710165";
#                 If x == "1710165" Then
#                     Return id(x);
#                 Else
#                     Continue;
#                 EndIf.
#             EndBody."""
#         expect = Program(
#             [
#                 FuncDecl(
#                     Id("foo"),
#                     [],
#                     (
#                         [
#                             VarDecl(
#                                 Id("x"),
#                                 [],
#                                 StringLiteral("1710165")
#                             )
#                         ],
#                         [
#                             If(
#                                 [
#                                     (
#                                         BinaryOp("==",Id("x"),StringLiteral("1710165")),
#                                         [],
#                                         [
#                                             Return(
#                                                 CallExpr(
#                                                     Id("id"),
#                                                     [
#                                                         Id("x")
#                                                     ]
#                                                 )
#                                             )
#                                         ]
#                                     )
#                                 ],
#                                 (
#                                     [],
#                                     [
#                                         Continue()
#                                     ]
#                                 )
#                             )
#                         ]
#                     )
#                 )
#             ]
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 340))
#
#     def test_41(self):
#         input = r"""
#         Function: foo
#             Body:
#                 Var: x = "1710165";
#                 If x == "1710165" Then
#                     Return id(x);
#                 ElseIf x == "1710166" Then
#                     x = "1710165";
#                 Else
#                     Continue;
#                 EndIf.
#             EndBody."""
#         expect = Program(
#             [
#                 FuncDecl(
#                     Id("foo"),
#                     [],
#                     (
#                         [
#                             VarDecl(
#                                 Id("x"),
#                                 [],
#                                 StringLiteral("1710165")
#                             )
#                         ],
#                         [
#                             If(
#                                 [
#                                     (
#                                         BinaryOp("==",Id("x"),StringLiteral("1710165")),
#                                         [],
#                                         [
#                                             Return(
#                                                 CallExpr(
#                                                     Id("id"),
#                                                     [
#                                                         Id("x")
#                                                     ]
#                                                 )
#                                             )
#                                         ]
#                                     ),
#                                     (
#                                         BinaryOp("==",Id("x"),StringLiteral("1710166")),
#                                         [],
#                                         [
#                                             Assign(
#                                                 Id("x"),
#                                                 StringLiteral("1710165")
#                                             )
#                                         ]
#                                     )
#                                 ],
#                                 (
#                                     [],
#                                     [
#                                         Continue()
#                                     ]
#                                 )
#                             )
#                         ]
#                     )
#                 )
#             ]
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 341))
#
#     def test_42(self):
#         input = r"""
#         Function: foo
#             Body:
#                 Var: x = "1710165";
#                 If x == "1710165" Then
#                     Return id(x);
#                 ElseIf x == "1710166" Then
#                     x = "1710165";
#                 Else
#                     For (x = 0, x < 5, 2) Do
#                         Break;
#                     EndFor.
#                 EndIf.
#             EndBody."""
#         expect = Program(
#             [
#                 FuncDecl(
#                     Id("foo"),
#                     [],
#                     (
#                         [
#                             VarDecl(
#                                 Id("x"),
#                                 [],
#                                 StringLiteral("1710165")
#                             )
#                         ],
#                         [
#                             If(
#                                 [
#                                     (
#                                         BinaryOp("==",Id("x"),StringLiteral("1710165")),
#                                         [],
#                                         [
#                                             Return(
#                                                 CallExpr(
#                                                     Id("id"),
#                                                     [
#                                                         Id("x")
#                                                     ]
#                                                 )
#                                             )
#                                         ]
#                                     ),
#                                     (
#                                         BinaryOp("==",Id("x"),StringLiteral("1710166")),
#                                         [],
#                                         [
#                                             Assign(
#                                                 Id("x"),
#                                                 StringLiteral("1710165")
#                                             )
#                                         ]
#                                     )
#                                 ],
#                                 (
#                                     [],
#                                     [
#                                         For(
#                                             Id("x"),
#                                             IntLiteral(0),
#                                             BinaryOp(
#                                                 "<",
#                                                 Id("x"),
#                                                 IntLiteral(5)
#                                             ),
#                                             IntLiteral(2),
#                                             (
#                                                 [],
#                                                 [
#                                                     Break()
#                                                 ]
#                                             )
#                                         )
#                                     ]
#                                 )
#                             )
#                         ]
#                     )
#                 )
#             ]
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 342))
#
#     def test_43(self):
#         input = r"""
#         Function: foo
#             Body:
#                 Var: x = "1710165";
#                 If x == "1710165" Then
#                     Return id(x);
#                 ElseIf x == "1710166" Then
#                     x = "1710165";
#                 Else
#                     For (x = 0, x < 5, 2) Do
#                         While (x != 1) Do
#                             Return a[1][x+1][foo(x)];
#                         EndWhile.
#                     EndFor.
#                 EndIf.
#             EndBody."""
#         expect = Program(
#             [
#                 FuncDecl(
#                     Id("foo"),
#                     [],
#                     (
#                         [
#                             VarDecl(
#                                 Id("x"),
#                                 [],
#                                 StringLiteral("1710165")
#                             )
#                         ],
#                         [
#                             If(
#                                 [
#                                     (
#                                         BinaryOp("==",Id("x"),StringLiteral("1710165")),
#                                         [],
#                                         [
#                                             Return(
#                                                 CallExpr(
#                                                     Id("id"),
#                                                     [
#                                                         Id("x")
#                                                     ]
#                                                 )
#                                             )
#                                         ]
#                                     ),
#                                     (
#                                         BinaryOp("==",Id("x"),StringLiteral("1710166")),
#                                         [],
#                                         [
#                                             Assign(
#                                                 Id("x"),
#                                                 StringLiteral("1710165")
#                                             )
#                                         ]
#                                     )
#                                 ],
#                                 (
#                                     [],
#                                     [
#                                         For(
#                                             Id("x"),
#                                             IntLiteral(0),
#                                             BinaryOp(
#                                                 "<",
#                                                 Id("x"),
#                                                 IntLiteral(5)
#                                             ),
#                                             IntLiteral(2),
#                                             (
#                                                 [],
#                                                 [
#                                                     While(
#                                                         BinaryOp(
#                                                             "!=",
#                                                             Id("x"),
#                                                             IntLiteral(1)),
#                                                             (
#                                                                 [],
#                                                                 [
#                                                                     Return(
#                                                                         ArrayCell(
#                                                                             Id("a"),
#                                                                             [
#                                                                                 IntLiteral(1),
#                                                                                 BinaryOp(
#                                                                                     "+",
#                                                                                     Id("x"),
#                                                                                     IntLiteral(1)
#                                                                                 ),
#                                                                             CallExpr(
#                                                                                 Id("foo"),
#                                                                                 [
#                                                                                     Id("x")
#                                                                                 ]
#                                                                             )
#                                                                         ]
#                                                                     )
#                                                                 )
#                                                             ]
#                                                         )
#                                                     )
#                                                 ]
#                                             )
#                                         )
#                                     ]
#                                 )
#                             )
#                         ]
#                     )
#                 )
#             ]
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 343))
#
#     def test_44(self):
#         input = r"""Var:x;
#         Var: y[1] = True;
#         Var: z[2][3] = {{1,2,"text"},{True,False,0xA}};"""
#         expect = Program(
#             [
#                 VarDecl(
#                     Id("x"),
#                     [],
#                     None
#                 ),
#                 VarDecl(
#                     Id("y"),
#                     [1],
#                     BooleanLiteral(True)
#                 ),
#                 VarDecl(
#                     Id("z"),
#                     [2,3],
#                     ArrayLiteral(
#                         [
#                             ArrayLiteral(
#                                 [
#                                     IntLiteral(1),
#                                     IntLiteral(2),
#                                     StringLiteral("text")
#                                 ]
#                             ),
#                             ArrayLiteral(
#                                 [
#                                     BooleanLiteral(True),
#                                     BooleanLiteral(False),
#                                     IntLiteral(10)
#                                 ]
#                             )
#                         ]
#                     )
#                 )
#             ]
#         )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             344))
#
#     def test_45(self):
#         input = r"""
#         Var: x;
#         Var: y[1] = True;
#         Var: z[2][3] = {{1,2,"text"},{True,False,0xA}};
#         Function: main
#         Body:
#         EndBody.
#         """
#         expect = Program(
#             [
#                 VarDecl(
#                     Id("x"),
#                     [],
#                     None
#                 ),
#                 VarDecl(
#                     Id("y"),
#                     [1],
#                     BooleanLiteral(True)
#                 ),
#                 VarDecl(
#                     Id("z"),
#                     [2,3],
#                     ArrayLiteral(
#                         [
#                             ArrayLiteral(
#                                 [
#                                     IntLiteral(1),
#                                     IntLiteral(2),
#                                     StringLiteral("text")
#                                 ]
#                             ),
#                             ArrayLiteral(
#                                 [
#                                     BooleanLiteral(True),
#                                     BooleanLiteral(False),
#                                     IntLiteral(10)
#                                 ]
#                             )
#                         ]
#                     )
#                 ),
#                 FuncDecl(
#                     Id("main"),
#                     [],
#                     (
#                         [],
#                         []
#                     )
#                 )
#             ]
#         )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             345))
#
#     def test_46(self):
#         input = r"""
#         Var: x, y[1] = True, z[2][3] = {{1,2,"text"},{True,False,0xA}};
#         Function: main
#         Parameter: b, c
#         Body:
#         EndBody.
#         """
#         expect = Program(
#             [
#                 VarDecl(
#                     Id("x"),
#                     [],
#                     None
#                 ),
#                 VarDecl(
#                     Id("y"),
#                     [1],
#                     BooleanLiteral(True)
#                 ),
#                 VarDecl(
#                     Id("z"),
#                     [2,3],
#                     ArrayLiteral(
#                         [
#                             ArrayLiteral(
#                                 [
#                                     IntLiteral(1),
#                                     IntLiteral(2),
#                                     StringLiteral("text")
#                                 ]
#                             ),
#                             ArrayLiteral(
#                                 [
#                                     BooleanLiteral(True),
#                                     BooleanLiteral(False),
#                                     IntLiteral(10)
#                                 ]
#                             )
#                         ]
#                     )
#                 ),
#                 FuncDecl(
#                     Id("main"),
#                     [
#                         VarDecl(
#                             Id("b"),
#                             [],
#                             None
#                         ),
#                         VarDecl(
#                             Id("c"),
#                             [],
#                             None
#                         )
#                     ],
#                     (
#                         [],
#                         []
#                     )
#                 )
#             ]
#         )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             346))
#
#     def test_47(self):
#         input = r"""
#         Var: x, y[1] = True, z[2][3] = {{1,2,"text"},{True,False,0xA}};
#         Function: main
#         Parameter: b, c, d[10][10]
#         Body:
#             Var: a = 1710165;
#         EndBody.
#         """
#         expect = Program(
#             [
#                 VarDecl(
#                     Id("x"),
#                     [],
#                     None
#                 ),
#                 VarDecl(
#                     Id("y"),
#                     [1],
#                     BooleanLiteral(True)
#                 ),
#                 VarDecl(
#                     Id("z"),
#                     [2,3],
#                     ArrayLiteral(
#                         [
#                             ArrayLiteral(
#                                 [
#                                     IntLiteral(1),
#                                     IntLiteral(2),
#                                     StringLiteral("text")
#                                 ]
#                             ),
#                             ArrayLiteral(
#                                 [
#                                     BooleanLiteral(True),
#                                     BooleanLiteral(False),
#                                     IntLiteral(10)
#                                 ]
#                             )
#                         ]
#                     )
#                 ),
#                 FuncDecl(
#                     Id("main"),
#                     [
#                         VarDecl(
#                             Id("b"),
#                             [],
#                             None
#                         ),
#                         VarDecl(
#                             Id("c"),
#                             [],
#                             None
#                         ),
#                         VarDecl(
#                             Id("d"),
#                             [10,10],
#                             None
#                         )
#                     ],
#                     (
#                         [
#                             VarDecl(
#                                 Id("a"),
#                                 [],
#                                 IntLiteral(1710165)
#                             )
#                         ],
#                         []
#                     )
#                 )
#             ]
#         )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             347))
#
#     def test_48(self):
#         input = r"""
#         Var: x, y[1] = True, z[2][3] = {{1,2,"text"},{True,False,0xA}};
#         Function: main
#         Parameter: b, c, d[10][10]
#         Body:
#             Var: a = 1710165;
#             Var: r = 3.1415;
#             b = -(a + r) * -c;
#         EndBody.
#         """
#         expect = Program(
#             [
#                 VarDecl(
#                     Id("x"),
#                     [],
#                     None
#                 ),
#                 VarDecl(
#                     Id("y"),
#                     [1],
#                     BooleanLiteral(True)
#                 ),
#                 VarDecl(
#                     Id("z"),
#                     [2,3],
#                     ArrayLiteral(
#                         [
#                             ArrayLiteral(
#                                 [
#                                     IntLiteral(1),
#                                     IntLiteral(2),
#                                     StringLiteral("text")
#                                 ]
#                             ),
#                             ArrayLiteral(
#                                 [
#                                     BooleanLiteral(True),
#                                     BooleanLiteral(False),
#                                     IntLiteral(10)
#                                 ]
#                             )
#                         ]
#                     )
#                 ),
#                 FuncDecl(
#                     Id("main"),
#                     [
#                         VarDecl(
#                             Id("b"),
#                             [],
#                             None
#                         ),
#                         VarDecl(
#                             Id("c"),
#                             [],
#                             None
#                         ),
#                         VarDecl(
#                             Id("d"),
#                             [10,10],
#                             None
#                         )
#                     ],
#                     (
#                         [
#                             VarDecl(
#                                 Id("a"),
#                                 [],
#                                 IntLiteral(1710165)
#                             ),
#                             VarDecl(
#                                 Id("r"),
#                                 [],
#                                 FloatLiteral(3.1415)
#                             )
#                         ],
#                         [
#                             Assign(
#                                 Id("b"),
#                                 BinaryOp(
#                                     "*",
#                                     UnaryOp(
#                                         "-",
#                                         BinaryOp(
#                                             "+",
#                                             Id("a"),
#                                             Id("r")
#                                         )
#                                     ),
#                                     UnaryOp(
#                                         "-",
#                                         Id("c")
#                                     )
#                                 )
#                             )
#                         ]
#                     )
#                 )
#             ]
#         )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             348))
#
#     def test_49(self):
#         input = r"""
#         Var: x, y[1] = True, z[2][3] = {{1,2,"text"},{True,False,0xA}};
#         Function: main
#         Parameter: b, c, d[10][10]
#         Body:
#             Var: a = 1710165;
#             Var: r = 3.1415;
#             b = -(a + r) * -c;
#             d[1][1] = !(y[1] && z[1][0]);
#         EndBody.
#         """
#         expect = Program(
#             [
#                 VarDecl(
#                     Id("x"),
#                     [],
#                     None
#                 ),
#                 VarDecl(
#                     Id("y"),
#                     [1],
#                     BooleanLiteral(True)
#                 ),
#                 VarDecl(
#                     Id("z"),
#                     [2,3],
#                     ArrayLiteral(
#                         [
#                             ArrayLiteral(
#                                 [
#                                     IntLiteral(1),
#                                     IntLiteral(2),
#                                     StringLiteral("text")
#                                 ]
#                             ),
#                             ArrayLiteral(
#                                 [
#                                     BooleanLiteral(True),
#                                     BooleanLiteral(False),
#                                     IntLiteral(10)
#                                 ]
#                             )
#                         ]
#                     )
#                 ),
#                 FuncDecl(
#                     Id("main"),
#                     [
#                         VarDecl(
#                             Id("b"),
#                             [],
#                             None
#                         ),
#                         VarDecl(
#                             Id("c"),
#                             [],
#                             None
#                         ),
#                         VarDecl(
#                             Id("d"),
#                             [10,10],
#                             None
#                         )
#                     ],
#                     (
#                         [
#                             VarDecl(
#                                 Id("a"),
#                                 [],
#                                 IntLiteral(1710165)
#                             ),
#                             VarDecl(
#                                 Id("r"),
#                                 [],
#                                 FloatLiteral(3.1415)
#                             )
#                         ],
#                         [
#                             Assign(
#                                 Id("b"),
#                                 BinaryOp(
#                                     "*",
#                                     UnaryOp(
#                                         "-",
#                                         BinaryOp(
#                                             "+",
#                                             Id("a"),
#                                             Id("r")
#                                         )
#                                     ),
#                                     UnaryOp(
#                                         "-",
#                                         Id("c")
#                                     )
#                                 )
#                             ),
#                             Assign(
#                                 ArrayCell(
#                                     Id("d"),
#                                     [
#                                         IntLiteral(1),
#                                         IntLiteral(1)
#                                     ]
#                                 ),
#                                 UnaryOp(
#                                     "!",
#                                     BinaryOp(
#                                         "&&",
#                                         ArrayCell(
#                                             Id("y"),
#                                             [
#                                                 IntLiteral(1)
#                                             ]
#                                         ),
#                                         ArrayCell(
#                                             Id("z"),
#                                             [
#                                                 IntLiteral(1),
#                                                 IntLiteral(0)
#                                             ]
#                                         )
#                                     )
#                                 )
#                             )
#                         ]
#                     )
#                 )
#             ]
#         )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             349))
#
#     def test_50(self):
#         input = r"""
#         Var: x, y[1] = True, z[2][3] = {{1,2,"text"},{True,False,0xA}};
#         Function: main
#         Parameter: b, c, d[10][10]
#         Body:
#             Var: a = 1710165;
#             Var: r = 3.1415;
#             b = -(a + r) * -c;
#             d[1][1] = !(y[1] && z[1][0]);
#             If d[1][1] Then
#                 d[1][2] = {1,2,3};
#             EndIf.
#         EndBody.
#         """
#         expect = Program(
#             [
#                 VarDecl(
#                     Id("x"),
#                     [],
#                     None
#                 ),
#                 VarDecl(
#                     Id("y"),
#                     [1],
#                     BooleanLiteral(True)
#                 ),
#                 VarDecl(
#                     Id("z"),
#                     [2,3],
#                     ArrayLiteral(
#                         [
#                             ArrayLiteral(
#                                 [
#                                     IntLiteral(1),
#                                     IntLiteral(2),
#                                     StringLiteral("text")
#                                 ]
#                             ),
#                             ArrayLiteral(
#                                 [
#                                     BooleanLiteral(True),
#                                     BooleanLiteral(False),
#                                     IntLiteral(10)
#                                 ]
#                             )
#                         ]
#                     )
#                 ),
#                 FuncDecl(
#                     Id("main"),
#                     [
#                         VarDecl(
#                             Id("b"),
#                             [],
#                             None
#                         ),
#                         VarDecl(
#                             Id("c"),
#                             [],
#                             None
#                         ),
#                         VarDecl(
#                             Id("d"),
#                             [10,10],
#                             None
#                         )
#                     ],
#                     (
#                         [
#                             VarDecl(
#                                 Id("a"),
#                                 [],
#                                 IntLiteral(1710165)
#                             ),
#                             VarDecl(
#                                 Id("r"),
#                                 [],
#                                 FloatLiteral(3.1415)
#                             )
#                         ],
#                         [
#                             Assign(
#                                 Id("b"),
#                                 BinaryOp(
#                                     "*",
#                                     UnaryOp(
#                                         "-",
#                                         BinaryOp(
#                                             "+",
#                                             Id("a"),
#                                             Id("r")
#                                         )
#                                     ),
#                                     UnaryOp(
#                                         "-",
#                                         Id("c")
#                                     )
#                                 )
#                             ),
#                             Assign(
#                                 ArrayCell(
#                                     Id("d"),
#                                     [
#                                         IntLiteral(1),
#                                         IntLiteral(1)
#                                     ]
#                                 ),
#                                 UnaryOp(
#                                     "!",
#                                     BinaryOp(
#                                         "&&",
#                                         ArrayCell(
#                                             Id("y"),
#                                             [
#                                                 IntLiteral(1)
#                                             ]
#                                         ),
#                                         ArrayCell(
#                                             Id("z"),
#                                             [
#                                                 IntLiteral(1),
#                                                 IntLiteral(0)
#                                             ]
#                                         )
#                                     )
#                                 )
#                             ),
#                             If(
#                                 [
#                                     (
#                                         ArrayCell(
#                                             Id("d"),
#                                             [
#                                                 IntLiteral(1),
#                                                 IntLiteral(1)
#                                             ]
#                                         ),
#                                         [],
#                                         [
#                                             Assign(
#                                                 ArrayCell(
#                                                     Id("d"),
#                                                     [
#                                                         IntLiteral(1),
#                                                         IntLiteral(2)
#                                                     ]
#                                                 ),
#                                                 ArrayLiteral(
#                                                     [
#                                                         IntLiteral(1),
#                                                         IntLiteral(2),
#                                                         IntLiteral(3)
#                                                     ]
#                                                 )
#                                             )
#                                         ]
#                                     )
#                                 ],
#                                 (
#                                     [],
#                                     []
#                                 )
#                             )
#                         ]
#                     )
#                 )
#             ]
#         )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             350))
#
#     def test_51(self):
#         input = r"""
#         Var: x, y[1] = True, z[2][3] = {{1,2,"text"},{True,False,0xA}};
#         Function: main
#         Parameter: b, c, d[10][10]
#         Body:
#             Var: a = 1710165;
#             Var: r = 3.1415;
#             b = -(a + r) * -c;
#             d[1][1] = !(y[1] && z[1][0]);
#             If d[1][1] Then
#                 d[1][2] = {1,2,3};
#             ElseIf y[1] Then
#                 Return !y[1];
#             EndIf.
#         EndBody.
#         """
#         expect = Program(
#             [
#                 VarDecl(
#                     Id("x"),
#                     [],
#                     None
#                 ),
#                 VarDecl(
#                     Id("y"),
#                     [1],
#                     BooleanLiteral(True)
#                 ),
#                 VarDecl(
#                     Id("z"),
#                     [2,3],
#                     ArrayLiteral(
#                         [
#                             ArrayLiteral(
#                                 [
#                                     IntLiteral(1),
#                                     IntLiteral(2),
#                                     StringLiteral("text")
#                                 ]
#                             ),
#                             ArrayLiteral(
#                                 [
#                                     BooleanLiteral(True),
#                                     BooleanLiteral(False),
#                                     IntLiteral(10)
#                                 ]
#                             )
#                         ]
#                     )
#                 ),
#                 FuncDecl(
#                     Id("main"),
#                     [
#                         VarDecl(
#                             Id("b"),
#                             [],
#                             None
#                         ),
#                         VarDecl(
#                             Id("c"),
#                             [],
#                             None
#                         ),
#                         VarDecl(
#                             Id("d"),
#                             [10,10],
#                             None
#                         )
#                     ],
#                     (
#                         [
#                             VarDecl(
#                                 Id("a"),
#                                 [],
#                                 IntLiteral(1710165)
#                             ),
#                             VarDecl(
#                                 Id("r"),
#                                 [],
#                                 FloatLiteral(3.1415)
#                             )
#                         ],
#                         [
#                             Assign(
#                                 Id("b"),
#                                 BinaryOp(
#                                     "*",
#                                     UnaryOp(
#                                         "-",
#                                         BinaryOp(
#                                             "+",
#                                             Id("a"),
#                                             Id("r")
#                                         )
#                                     ),
#                                     UnaryOp(
#                                         "-",
#                                         Id("c")
#                                     )
#                                 )
#                             ),
#                             Assign(
#                                 ArrayCell(
#                                     Id("d"),
#                                     [
#                                         IntLiteral(1),
#                                         IntLiteral(1)
#                                     ]
#                                 ),
#                                 UnaryOp(
#                                     "!",
#                                     BinaryOp(
#                                         "&&",
#                                         ArrayCell(
#                                             Id("y"),
#                                             [
#                                                 IntLiteral(1)
#                                             ]
#                                         ),
#                                         ArrayCell(
#                                             Id("z"),
#                                             [
#                                                 IntLiteral(1),
#                                                 IntLiteral(0)
#                                             ]
#                                         )
#                                     )
#                                 )
#                             ),
#                             If(
#                                 [
#                                     (
#                                         ArrayCell(
#                                             Id("d"),
#                                             [
#                                                 IntLiteral(1),
#                                                 IntLiteral(1)
#                                             ]
#                                         ),
#                                         [],
#                                         [
#                                             Assign(
#                                                 ArrayCell(
#                                                     Id("d"),
#                                                     [
#                                                         IntLiteral(1),
#                                                         IntLiteral(2)
#                                                     ]
#                                                 ),
#                                                 ArrayLiteral(
#                                                     [
#                                                         IntLiteral(1),
#                                                         IntLiteral(2),
#                                                         IntLiteral(3)
#                                                     ]
#                                                 )
#                                             )
#                                         ]
#                                     ),
#                                     (
#                                         ArrayCell(
#                                             Id("y"),
#                                             [
#                                                 IntLiteral(1)
#                                             ]
#                                         ),
#                                         [],
#                                         [
#                                            Return(
#                                                UnaryOp(
#                                                    "!",
#                                                    ArrayCell(
#                                                        Id("y"),
#                                                        [
#                                                            IntLiteral(1)
#                                                         ]
#                                                     )
#                                                 )
#                                             )
#                                         ]
#                                     )
#                                 ],
#                                 (
#                                     [],
#                                     []
#                                 )
#                             )
#                         ]
#                     )
#                 )
#             ]
#         )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             351))
#
#     def test_52(self):
#         input = r"""
#         Var: x, y[1] = True, z[2][3] = {{1,2,"text"},{True,False,0xA}};
#         Function: main
#         Parameter: b, c, d[10][10]
#         Body:
#             Var: a = 1710165;
#             Var: r = 3.1415;
#             b = -(a + r) * -c;
#             d[1][1] = !(y[1] && z[1][0]);
#             If d[1][1] Then
#                 d[1][2] = {1,2,3};
#             ElseIf y[1] Then
#                 Return !y[1];
#             EndIf.
#         EndBody.
#         Function: foo
#         Body:
#         EndBody.
#         """
#         expect = Program(
#             [
#                 VarDecl(
#                     Id("x"),
#                     [],
#                     None
#                 ),
#                 VarDecl(
#                     Id("y"),
#                     [1],
#                     BooleanLiteral(True)
#                 ),
#                 VarDecl(
#                     Id("z"),
#                     [2,3],
#                     ArrayLiteral(
#                         [
#                             ArrayLiteral(
#                                 [
#                                     IntLiteral(1),
#                                     IntLiteral(2),
#                                     StringLiteral("text")
#                                 ]
#                             ),
#                             ArrayLiteral(
#                                 [
#                                     BooleanLiteral(True),
#                                     BooleanLiteral(False),
#                                     IntLiteral(10)
#                                 ]
#                             )
#                         ]
#                     )
#                 ),
#                 FuncDecl(
#                     Id("main"),
#                     [
#                         VarDecl(
#                             Id("b"),
#                             [],
#                             None
#                         ),
#                         VarDecl(
#                             Id("c"),
#                             [],
#                             None
#                         ),
#                         VarDecl(
#                             Id("d"),
#                             [10,10],
#                             None
#                         )
#                     ],
#                     (
#                         [
#                             VarDecl(
#                                 Id("a"),
#                                 [],
#                                 IntLiteral(1710165)
#                             ),
#                             VarDecl(
#                                 Id("r"),
#                                 [],
#                                 FloatLiteral(3.1415)
#                             )
#                         ],
#                         [
#                             Assign(
#                                 Id("b"),
#                                 BinaryOp(
#                                     "*",
#                                     UnaryOp(
#                                         "-",
#                                         BinaryOp(
#                                             "+",
#                                             Id("a"),
#                                             Id("r")
#                                         )
#                                     ),
#                                     UnaryOp(
#                                         "-",
#                                         Id("c")
#                                     )
#                                 )
#                             ),
#                             Assign(
#                                 ArrayCell(
#                                     Id("d"),
#                                     [
#                                         IntLiteral(1),
#                                         IntLiteral(1)
#                                     ]
#                                 ),
#                                 UnaryOp(
#                                     "!",
#                                     BinaryOp(
#                                         "&&",
#                                         ArrayCell(
#                                             Id("y"),
#                                             [
#                                                 IntLiteral(1)
#                                             ]
#                                         ),
#                                         ArrayCell(
#                                             Id("z"),
#                                             [
#                                                 IntLiteral(1),
#                                                 IntLiteral(0)
#                                             ]
#                                         )
#                                     )
#                                 )
#                             ),
#                             If(
#                                 [
#                                     (
#                                         ArrayCell(
#                                             Id("d"),
#                                             [
#                                                 IntLiteral(1),
#                                                 IntLiteral(1)
#                                             ]
#                                         ),
#                                         [],
#                                         [
#                                             Assign(
#                                                 ArrayCell(
#                                                     Id("d"),
#                                                     [
#                                                         IntLiteral(1),
#                                                         IntLiteral(2)
#                                                     ]
#                                                 ),
#                                                 ArrayLiteral(
#                                                     [
#                                                         IntLiteral(1),
#                                                         IntLiteral(2),
#                                                         IntLiteral(3)
#                                                     ]
#                                                 )
#                                             )
#                                         ]
#                                     ),
#                                     (
#                                         ArrayCell(
#                                             Id("y"),
#                                             [
#                                                 IntLiteral(1)
#                                             ]
#                                         ),
#                                         [],
#                                         [
#                                            Return(
#                                                UnaryOp(
#                                                    "!",
#                                                    ArrayCell(
#                                                        Id("y"),
#                                                        [
#                                                            IntLiteral(1)
#                                                         ]
#                                                     )
#                                                 )
#                                             )
#                                         ]
#                                     )
#                                 ],
#                                 (
#                                     [],
#                                     []
#                                 )
#                             )
#                         ]
#                     )
#                 ),
#                 FuncDecl(
#                     Id("foo"),
#                     [],
#                     (
#                         [],
#                         []
#                     )
#                 )
#             ]
#         )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             352))
#
#     def test_53(self):
#         input = r"""
#         Var: x, y[1] = True, z[2][3] = {{1,2,"text"},{True,False,0xA}};
#         Function: main
#         Parameter: b, c, d[10][10]
#         Body:
#             Var: a = 1710165;
#             Var: r = 3.1415;
#             b = -(a + r) * -c;
#             d[1][1] = !(y[1] && z[1][0]);
#             If d[1][1] Then
#                 d[1][2] = {1,2,3};
#             ElseIf y[1] Then
#                 Return !y[1];
#             EndIf.
#         EndBody.
#         Function: foo
#         Body:
#             For (i = 0, i < x+1, 1) Do
#                 For (j = i+1, j < x*10, 2) Do
#                     Continue;
#                 EndFor.
#             EndFor.
#         EndBody.
#         """
#         expect = Program(
#             [
#                 VarDecl(
#                     Id("x"),
#                     [],
#                     None
#                 ),
#                 VarDecl(
#                     Id("y"),
#                     [1],
#                     BooleanLiteral(True)
#                 ),
#                 VarDecl(
#                     Id("z"),
#                     [2,3],
#                     ArrayLiteral(
#                         [
#                             ArrayLiteral(
#                                 [
#                                     IntLiteral(1),
#                                     IntLiteral(2),
#                                     StringLiteral("text")
#                                 ]
#                             ),
#                             ArrayLiteral(
#                                 [
#                                     BooleanLiteral(True),
#                                     BooleanLiteral(False),
#                                     IntLiteral(10)
#                                 ]
#                             )
#                         ]
#                     )
#                 ),
#                 FuncDecl(
#                     Id("main"),
#                     [
#                         VarDecl(
#                             Id("b"),
#                             [],
#                             None
#                         ),
#                         VarDecl(
#                             Id("c"),
#                             [],
#                             None
#                         ),
#                         VarDecl(
#                             Id("d"),
#                             [10,10],
#                             None
#                         )
#                     ],
#                     (
#                         [
#                             VarDecl(
#                                 Id("a"),
#                                 [],
#                                 IntLiteral(1710165)
#                             ),
#                             VarDecl(
#                                 Id("r"),
#                                 [],
#                                 FloatLiteral(3.1415)
#                             )
#                         ],
#                         [
#                             Assign(
#                                 Id("b"),
#                                 BinaryOp(
#                                     "*",
#                                     UnaryOp(
#                                         "-",
#                                         BinaryOp(
#                                             "+",
#                                             Id("a"),
#                                             Id("r")
#                                         )
#                                     ),
#                                     UnaryOp(
#                                         "-",
#                                         Id("c")
#                                     )
#                                 )
#                             ),
#                             Assign(
#                                 ArrayCell(
#                                     Id("d"),
#                                     [
#                                         IntLiteral(1),
#                                         IntLiteral(1)
#                                     ]
#                                 ),
#                                 UnaryOp(
#                                     "!",
#                                     BinaryOp(
#                                         "&&",
#                                         ArrayCell(
#                                             Id("y"),
#                                             [
#                                                 IntLiteral(1)
#                                             ]
#                                         ),
#                                         ArrayCell(
#                                             Id("z"),
#                                             [
#                                                 IntLiteral(1),
#                                                 IntLiteral(0)
#                                             ]
#                                         )
#                                     )
#                                 )
#                             ),
#                             If(
#                                 [
#                                     (
#                                         ArrayCell(
#                                             Id("d"),
#                                             [
#                                                 IntLiteral(1),
#                                                 IntLiteral(1)
#                                             ]
#                                         ),
#                                         [],
#                                         [
#                                             Assign(
#                                                 ArrayCell(
#                                                     Id("d"),
#                                                     [
#                                                         IntLiteral(1),
#                                                         IntLiteral(2)
#                                                     ]
#                                                 ),
#                                                 ArrayLiteral(
#                                                     [
#                                                         IntLiteral(1),
#                                                         IntLiteral(2),
#                                                         IntLiteral(3)
#                                                     ]
#                                                 )
#                                             )
#                                         ]
#                                     ),
#                                     (
#                                         ArrayCell(
#                                             Id("y"),
#                                             [
#                                                 IntLiteral(1)
#                                             ]
#                                         ),
#                                         [],
#                                         [
#                                            Return(
#                                                UnaryOp(
#                                                    "!",
#                                                    ArrayCell(
#                                                        Id("y"),
#                                                        [
#                                                            IntLiteral(1)
#                                                         ]
#                                                     )
#                                                 )
#                                             )
#                                         ]
#                                     )
#                                 ],
#                                 (
#                                     [],
#                                     []
#                                 )
#                             )
#                         ]
#                     )
#                 ),
#                 FuncDecl(
#                     Id("foo"),
#                     [],
#                     (
#                         [],
#                         [
#                             For(
#                                 Id("i"),
#                                 IntLiteral(0),
#                                 BinaryOp("<",
#                                         Id("i"),
#                                         BinaryOp(
#                                             "+",
#                                             Id("x"),
#                                             IntLiteral(1)
#                                         )
#                                     ),
#                                 IntLiteral(1),
#                                 (
#                                     [],
#                                     [
#                                         For(
#                                             Id("j"),
#                                             BinaryOp(
#                                                     "+",
#                                                     Id("i"),
#                                                     IntLiteral(1)
#                                                 ),
#                                             BinaryOp("<",
#                                                     Id("j"),
#                                                     BinaryOp(
#                                                         "*",
#                                                         Id("x"),
#                                                         IntLiteral(10)
#                                                     )
#                                                 ),
#                                             IntLiteral(2),
#                                             (
#                                                 [],
#                                                 [
#                                                     Continue()
#                                                 ]
#                                             )
#                                         )
#                                     ]
#                                 )
#                             )
#                         ]
#                     )
#                 )
#             ]
#         )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             353))
#
#     def test_54(self):
#         input = r"""
#         Var: x, y[1] = True, z[2][3] = {{1,2,"text"},{True,False,0xA}};
#         Function: main
#         Parameter: b, c, d[10][10]
#         Body:
#             Var: a = 1710165;
#             Var: r = 3.1415;
#             b = -(a + r) * -c;
#             d[1][1] = !(y[1] && z[1][0]);
#             If d[1][1] Then
#                 d[1][2] = {1,2,3};
#             ElseIf y[1] Then
#                 Return !y[1];
#             Else
#                 While (test < 10) Do
#                     e = foo() || 1;
#                     Return foo();
#                 EndWhile.
#             EndIf.
#         EndBody.
#         Function: foo
#         Body:
#             For (i = 0, i < x+1, 1) Do
#                 For (j = i+1, j < x*10, 2) Do
#                     Continue;
#                 EndFor.
#             EndFor.
#         EndBody.
#         """
#         expect = Program(
#             [
#                 VarDecl(
#                     Id("x"),
#                     [],
#                     None
#                 ),
#                 VarDecl(
#                     Id("y"),
#                     [1],
#                     BooleanLiteral(True)
#                 ),
#                 VarDecl(
#                     Id("z"),
#                     [2,3],
#                     ArrayLiteral(
#                         [
#                             ArrayLiteral(
#                                 [
#                                     IntLiteral(1),
#                                     IntLiteral(2),
#                                     StringLiteral("text")
#                                 ]
#                             ),
#                             ArrayLiteral(
#                                 [
#                                     BooleanLiteral(True),
#                                     BooleanLiteral(False),
#                                     IntLiteral(10)
#                                 ]
#                             )
#                         ]
#                     )
#                 ),
#                 FuncDecl(
#                     Id("main"),
#                     [
#                         VarDecl(
#                             Id("b"),
#                             [],
#                             None
#                         ),
#                         VarDecl(
#                             Id("c"),
#                             [],
#                             None
#                         ),
#                         VarDecl(
#                             Id("d"),
#                             [10,10],
#                             None
#                         )
#                     ],
#                     (
#                         [
#                             VarDecl(
#                                 Id("a"),
#                                 [],
#                                 IntLiteral(1710165)
#                             ),
#                             VarDecl(
#                                 Id("r"),
#                                 [],
#                                 FloatLiteral(3.1415)
#                             )
#                         ],
#                         [
#                             Assign(
#                                 Id("b"),
#                                 BinaryOp(
#                                     "*",
#                                     UnaryOp(
#                                         "-",
#                                         BinaryOp(
#                                             "+",
#                                             Id("a"),
#                                             Id("r")
#                                         )
#                                     ),
#                                     UnaryOp(
#                                         "-",
#                                         Id("c")
#                                     )
#                                 )
#                             ),
#                             Assign(
#                                 ArrayCell(
#                                     Id("d"),
#                                     [
#                                         IntLiteral(1),
#                                         IntLiteral(1)
#                                     ]
#                                 ),
#                                 UnaryOp(
#                                     "!",
#                                     BinaryOp(
#                                         "&&",
#                                         ArrayCell(
#                                             Id("y"),
#                                             [
#                                                 IntLiteral(1)
#                                             ]
#                                         ),
#                                         ArrayCell(
#                                             Id("z"),
#                                             [
#                                                 IntLiteral(1),
#                                                 IntLiteral(0)
#                                             ]
#                                         )
#                                     )
#                                 )
#                             ),
#                             If(
#                                 [
#                                     (
#                                         ArrayCell(
#                                             Id("d"),
#                                             [
#                                                 IntLiteral(1),
#                                                 IntLiteral(1)
#                                             ]
#                                         ),
#                                         [],
#                                         [
#                                             Assign(
#                                                 ArrayCell(
#                                                     Id("d"),
#                                                     [
#                                                         IntLiteral(1),
#                                                         IntLiteral(2)
#                                                     ]
#                                                 ),
#                                                 ArrayLiteral(
#                                                     [
#                                                         IntLiteral(1),
#                                                         IntLiteral(2),
#                                                         IntLiteral(3)
#                                                     ]
#                                                 )
#                                             )
#                                         ]
#                                     ),
#                                     (
#                                         ArrayCell(
#                                             Id("y"),
#                                             [
#                                                 IntLiteral(1)
#                                             ]
#                                         ),
#                                         [],
#                                         [
#                                            Return(
#                                                UnaryOp(
#                                                    "!",
#                                                    ArrayCell(
#                                                        Id("y"),
#                                                        [
#                                                            IntLiteral(1)
#                                                         ]
#                                                     )
#                                                 )
#                                             )
#                                         ]
#                                     )
#                                 ],
#                                 (
#                                     [],
#                                     [
#                                         While(
#                                             BinaryOp(
#                                                 "<",
#                                                 Id("test"),
#                                                 IntLiteral(10)
#                                             ),
#                                             (
#                                                 [],
#                                                 [
#                                                     Assign(
#                                                         Id("e"),
#                                                         BinaryOp(
#                                                             "||",
#                                                             CallExpr(
#                                                                 Id("foo"),
#                                                                 []
#                                                             ),
#                                                             IntLiteral(1)
#                                                         )
#                                                     ),
#                                                     Return(
#                                                         CallExpr(
#                                                             Id("foo"),
#                                                             []
#                                                         )
#                                                     )
#                                                 ]
#                                             )
#                                         )
#                                     ]
#                                 )
#                             )
#                         ]
#                     )
#                 ),
#                 FuncDecl(
#                     Id("foo"),
#                     [],
#                     (
#                         [],
#                         [
#                             For(
#                                 Id("i"),
#                                 IntLiteral(0),
#                                 BinaryOp("<",
#                                         Id("i"),
#                                         BinaryOp(
#                                             "+",
#                                             Id("x"),
#                                             IntLiteral(1)
#                                         )
#                                     ),
#                                 IntLiteral(1),
#                                 (
#                                     [],
#                                     [
#                                         For(
#                                             Id("j"),
#                                             BinaryOp(
#                                                     "+",
#                                                     Id("i"),
#                                                     IntLiteral(1)
#                                                 ),
#                                             BinaryOp("<",
#                                                     Id("j"),
#                                                     BinaryOp(
#                                                         "*",
#                                                         Id("x"),
#                                                         IntLiteral(10)
#                                                     )
#                                                 ),
#                                             IntLiteral(2),
#                                             (
#                                                 [],
#                                                 [
#                                                     Continue()
#                                                 ]
#                                             )
#                                         )
#                                     ]
#                                 )
#                             )
#                         ]
#                     )
#                 )
#             ]
#         )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             354))
#
#     def test_55(self):
#         input = """
# Function: main
# Body:
#     **
#     *Student Name   : Huynh Pham Phuoc Linh
#     *Student ID     : 1710165
#     **
#     print(value);
#     Return;
# EndBody."""
#         expect = Program(
#             [
#                 FuncDecl(
#                     Id("main"),
#                     [],
#                     (
#                         [],
#                         [
#                             CallStmt(
#                                 Id("print"),
#                                 [
#                                     Id("value")
#                                 ]
#                             ),
#                             Return(None)
#                         ]
#                     )
#                 )
#             ]
#         )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             355))
#
#     def test_56(self):
#         input = """
# Function: main
# Body:
#     **
#     *Student Name   : Huynh Pham Phuoc Linh
#     *Student ID     : 1710165
#     **
#     print(value);
#     Return;
#     ** Comment **
# EndBody."""
#         expect = Program(
#             [
#                 FuncDecl(
#                     Id("main"),
#                     [],
#                     (
#                         [],
#                         [
#                             CallStmt(
#                                 Id("print"),
#                                 [
#                                     Id("value")
#                                 ]
#                             ),
#                             Return(None)
#                         ]
#                     )
#                 )
#             ]
#         )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             356))
#
#     def test_57(self):
#         input = """
# Function: main
# Body:
#     **
#     *Student Name   : Huynh Pham Phuoc Linh
#     *Student ID     : 1710165
#     **
#     print(value); ** print value of program **
#     Return value;
#     ** Comment **
# EndBody."""
#         expect = Program(
#             [
#                 FuncDecl(
#                     Id("main"),
#                     [],
#                     (
#                         [],
#                         [
#                             CallStmt(
#                                 Id("print"),
#                                 [
#                                     Id("value")
#                                 ]
#                             ),
#                             Return(
#                                 Id("value")
#                             )
#                         ]
#                     )
#                 )
#             ]
#         )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             357))
#
#     def test_58(self):
#         input = """
# Function: main
# Body:
#     **
#     *Student Name   : Huynh Pham Phuoc Linh
#     *Student ID     : 1710165
#     **
#     If checkFoo() Then
#         ** Comment 1 **
#         Return 1;
#     Else
#         ** Comment 2 **
#         Return 2;
#     EndIf.
# EndBody."""
#         expect = Program(
#             [
#                 FuncDecl(
#                     Id("main"),
#                     [],
#                     (
#                         [],
#                         [
#                             If(
#                                 [
#                                     (
#                                         CallExpr(
#                                             Id("checkFoo"),
#                                             []
#                                         ),
#                                         [],
#                                         [
#                                             Return(
#                                                 IntLiteral(1)
#                                             )
#                                         ]
#                                     )
#                                 ],
#                                 (
#                                     [],
#                                     [
#                                         Return(
#                                             IntLiteral(2)
#                                         )
#                                     ]
#                                 )
#                             )
#                         ]
#                     )
#                 )
#             ]
#         )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             358))
#
#     def test_59(self):
#         input = """
# Function: main
# Body:
#     **
#     *Student Name   : Huynh Pham Phuoc Linh
#     *Student ID     : 1710165
#     **
#     If checkFoo() == "verify" Then
#         ** Comment 1 **
#         Var: x[3] = {1,2,3};
#         Return x[0] + x[1] * x[2];
#     Else
#         ** Comment 2 **
#         Return 2;
#     EndIf.
# EndBody."""
#         expect = Program(
#             [
#                 FuncDecl(
#                     Id("main"),
#                     [],
#                     (
#                         [],
#                         [
#                             If(
#                                 [
#                                     (
#                                         BinaryOp(
#                                             "==",
#                                             CallExpr(
#                                                 Id("checkFoo"),
#                                                 []
#                                             ),
#                                             StringLiteral("verify")
#                                         ),
#                                         [
#                                             VarDecl(
#                                                 Id("x"),
#                                                 [3],
#                                                 ArrayLiteral(
#                                                     [
#                                                         IntLiteral(1),
#                                                         IntLiteral(2),
#                                                         IntLiteral(3)
#                                                     ]
#                                                 )
#                                             )
#                                         ],
#                                         [
#                                             Return(
#                                                 BinaryOp(
#                                                     "+",
#                                                     ArrayCell(
#                                                         Id("x"),
#                                                         [
#                                                             IntLiteral(0)
#                                                         ]
#                                                     ),
#                                                     BinaryOp(
#                                                         "*",
#                                                         ArrayCell(
#                                                             Id("x"),
#                                                             [
#                                                                 IntLiteral(1)
#                                                             ]
#                                                         ),
#                                                         ArrayCell(
#                                                             Id("x"),
#                                                             [
#                                                                 IntLiteral(2)
#                                                             ]
#                                                         )
#                                                     )
#                                                 )
#                                             )
#                                         ]
#                                     )
#                                 ],
#                                 (
#                                     [],
#                                     [
#                                         Return(
#                                             IntLiteral(2)
#                                         )
#                                     ]
#                                 )
#                             )
#                         ]
#                     )
#                 )
#             ]
#         )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             359))
#
#     def test_60(self):
#         input = """
# Function: main
# Body:
#     **
#     *Student Name   : Huynh Pham Phuoc Linh
#     *Student ID     : 1710165
#     **
#     If checkFoo() == "verify" Then
#         ** Comment 1 **
#         Var: x[3] = {1,2,3};
#         Return x[0] + x[1] * x[2];
#     Else
#         ** Comment 2 **
#         Return 2;
#     EndIf.
# EndBody.
# Var: x = 1;"""
#         expect = Program(
#             [
#                 FuncDecl(
#                     Id("main"),
#                     [],
#                     (
#                         [],
#                         [
#                             If(
#                                 [
#                                     (
#                                         BinaryOp(
#                                             "==",
#                                             CallExpr(
#                                                 Id("checkFoo"),
#                                                 []
#                                             ),
#                                             StringLiteral("verify")
#                                         ),
#                                         [
#                                             VarDecl(
#                                                 Id("x"),
#                                                 [3],
#                                                 ArrayLiteral(
#                                                     [
#                                                         IntLiteral(1),
#                                                         IntLiteral(2),
#                                                         IntLiteral(3)
#                                                     ]
#                                                 )
#                                             )
#                                         ],
#                                         [
#                                             Return(
#                                                 BinaryOp(
#                                                     "+",
#                                                     ArrayCell(
#                                                         Id("x"),
#                                                         [
#                                                             IntLiteral(0)
#                                                         ]
#                                                     ),
#                                                     BinaryOp(
#                                                         "*",
#                                                         ArrayCell(
#                                                             Id("x"),
#                                                             [
#                                                                 IntLiteral(1)
#                                                             ]
#                                                         ),
#                                                         ArrayCell(
#                                                             Id("x"),
#                                                             [
#                                                                 IntLiteral(2)
#                                                             ]
#                                                         )
#                                                     )
#                                                 )
#                                             )
#                                         ]
#                                     )
#                                 ],
#                                 (
#                                     [],
#                                     [
#                                         Return(
#                                             IntLiteral(2)
#                                         )
#                                     ]
#                                 )
#                             )
#                         ]
#                     )
#                 )
#                 ,
#                 VarDecl(
#                     Id("x"),
#                     [],
#                     IntLiteral(1)
#                 )
#             ]
#         )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             360))
#
#     def test_61(self):
#         input = r"""
#         Function: foo
#             Body:
#                 a[2][foo()][b[1]] = 5;
#             EndBody."""
#         expect = Program(
#                 [FuncDecl(Id("foo"),[],
#                           (
#                               [],
#                               [
#                                   Assign(
#                                     ArrayCell(
#                                         Id("a"),
#                                         [
#                                             IntLiteral(2),
#                                             CallExpr(
#                                                 Id("foo"),
#                                                 []
#                                             ),
#                                             ArrayCell(
#                                                 Id("b"),
#                                                 [
#                                                     IntLiteral(1)
#                                                 ]
#                                             )
#                                         ]
#                                     ),
#                                     IntLiteral(5)
#                                   )
#                               ]
#                           ))
#                 ]
#                 )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             361))
#
#     def test_62(self):
#         input = r"""
#         Function: foo
#             Body:
#                 foo1();
#                 Return foo();
#             EndBody."""
#         expect = Program(
#                 [
#                     FuncDecl(
#                         Id("foo"),
#                         [],
#                         (
#                             [],
#                             [
#                                 CallStmt(
#                                     Id("foo1"),
#                                     []
#                                 ),
#                                 Return(
#                                     CallExpr(
#                                         Id("foo"),
#                                         []
#                                     )
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             362))
#
#     def test_63(self):
#         input = r"""
#         Function: foo
#             Body:
#                 foo1();
#                 Return foo();
#                 ** Test comment **
#             EndBody."""
#         expect = Program(
#                 [
#                     FuncDecl(
#                         Id("foo"),
#                         [],
#                         (
#                             [],
#                             [
#                                 CallStmt(
#                                     Id("foo1"),
#                                     []
#                                 ),
#                                 Return(
#                                     CallExpr(
#                                         Id("foo"),
#                                         []
#                                     )
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             363))
#
#     def test_64(self):
#         input = r"""
#         Function: foo
#             Body:
#                 foo1();
#                 Return foo(fooo());
#                 ** Test comment **
#             EndBody."""
#         expect = Program(
#                 [
#                     FuncDecl(
#                         Id("foo"),
#                         [],
#                         (
#                             [],
#                             [
#                                 CallStmt(
#                                     Id("foo1"),
#                                     []
#                                 ),
#                                 Return(
#                                     CallExpr(
#                                         Id("foo"),
#                                         [
#                                             CallExpr(
#                                                 Id("fooo"),
#                                                 []
#                                             )
#                                         ]
#                                     )
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             364))
#
#     def test_65(self):
#         input = r"""
#         Function: foo
#             Body:
#                 foo1();
#                 Return foo(fooo({1,2,3}));
#                 ** Test comment **
#             EndBody."""
#         expect = Program(
#                 [
#                     FuncDecl(
#                         Id("foo"),
#                         [],
#                         (
#                             [],
#                             [
#                                 CallStmt(
#                                     Id("foo1"),
#                                     []
#                                 ),
#                                 Return(
#                                     CallExpr(
#                                         Id("foo"),
#                                         [
#                                             CallExpr(
#                                                 Id("fooo"),
#                                                 [
#                                                     ArrayLiteral(
#                                                         [
#                                                             IntLiteral(1),
#                                                             IntLiteral(2),
#                                                             IntLiteral(3)
#                                                         ]
#                                                     )
#                                                 ]
#                                             )
#                                         ]
#                                     )
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             365))
#
#     def test_66(self):
#         input = r"""
#         Function: foo
#             Body:
#                 foo1();
#                 Return foo(fooo({1,2,3} ** Text text text hide**));
#                 ** Test comment **
#             EndBody."""
#         expect = Program(
#                 [
#                     FuncDecl(
#                         Id("foo"),
#                         [],
#                         (
#                             [],
#                             [
#                                 CallStmt(
#                                     Id("foo1"),
#                                     []
#                                 ),
#                                 Return(
#                                     CallExpr(
#                                         Id("foo"),
#                                         [
#                                             CallExpr(
#                                                 Id("fooo"),
#                                                 [
#                                                     ArrayLiteral(
#                                                         [
#                                                             IntLiteral(1),
#                                                             IntLiteral(2),
#                                                             IntLiteral(3)
#                                                         ]
#                                                     )
#                                                 ]
#                                             )
#                                         ]
#                                     )
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             366))
#
#     def test_67(self):
#         input = r"""
#         Function: foo
#             Body:
#                 foo1({1,2,3}[3]);
#                 Return foo(fooo({1,2,3}));
#                 ** Test comment **
#             EndBody."""
#         expect = Program(
#                 [
#                     FuncDecl(
#                         Id("foo"),
#                         [],
#                         (
#                             [],
#                             [
#                                 CallStmt(
#                                     Id("foo1"),
#                                     [
#                                         ArrayCell(
#                                             ArrayLiteral(
#                                                 [
#                                                     IntLiteral(1),
#                                                     IntLiteral(2),
#                                                     IntLiteral(3)
#                                                 ]
#                                             ),
#                                             [
#                                                 IntLiteral(3)
#                                             ]
#                                         )
#                                     ]
#                                 ),
#                                 Return(
#                                     CallExpr(
#                                         Id("foo"),
#                                         [
#                                             CallExpr(
#                                                 Id("fooo"),
#                                                 [
#                                                     ArrayLiteral(
#                                                         [
#                                                             IntLiteral(1),
#                                                             IntLiteral(2),
#                                                             IntLiteral(3)
#                                                         ]
#                                                     )
#                                                 ]
#                                             )
#                                         ]
#                                     )
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             367))
#
#     def test_68(self):
#         input = r"""
#         Function: foo
#             Body:
#                 foo1({1,2,3}[3], 2*{1,2,3}[2]);
#                 Return foo(fooo({1,2,3}));
#                 ** Test comment **
#             EndBody."""
#         expect = Program(
#                 [
#                     FuncDecl(
#                         Id("foo"),
#                         [],
#                         (
#                             [],
#                             [
#                                 CallStmt(
#                                     Id("foo1"),
#                                     [
#                                         ArrayCell(
#                                             ArrayLiteral(
#                                                 [
#                                                     IntLiteral(1),
#                                                     IntLiteral(2),
#                                                     IntLiteral(3)
#                                                 ]
#                                             ),
#                                             [
#                                                 IntLiteral(3)
#                                             ]
#                                         ),
#                                         BinaryOp(
#                                             "*",
#                                             IntLiteral(2),
#                                             ArrayCell(
#                                                 ArrayLiteral(
#                                                     [
#                                                         IntLiteral(1),
#                                                         IntLiteral(2),
#                                                         IntLiteral(3)
#                                                     ]
#                                                 ),
#                                                 [
#                                                     IntLiteral(2)
#                                                 ]
#                                             )
#                                         )
#                                     ]
#                                 ),
#                                 Return(
#                                     CallExpr(
#                                         Id("foo"),
#                                         [
#                                             CallExpr(
#                                                 Id("fooo"),
#                                                 [
#                                                     ArrayLiteral(
#                                                         [
#                                                             IntLiteral(1),
#                                                             IntLiteral(2),
#                                                             IntLiteral(3)
#                                                         ]
#                                                     )
#                                                 ]
#                                             )
#                                         ]
#                                     )
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             368))
#
#     def test_69(self):
#         input = r"""
#         Function: foo
#         Parameter: x, y, z[1]
#             Body:
#                 foo1({1,2,3}[3], 2*{1,2,3}[2]);
#                 Return foo(fooo({1,2,3}));
#                 ** Test comment **
#             EndBody."""
#         expect = Program(
#                 [
#                     FuncDecl(
#                         Id("foo"),
#                         [
#                             VarDecl(
#                                 Id("x"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("y"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("z"),
#                                 [1],
#                                 None
#                             )
#                         ],
#                         (
#                             [],
#                             [
#                                 CallStmt(
#                                     Id("foo1"),
#                                     [
#                                         ArrayCell(
#                                             ArrayLiteral(
#                                                 [
#                                                     IntLiteral(1),
#                                                     IntLiteral(2),
#                                                     IntLiteral(3)
#                                                 ]
#                                             ),
#                                             [
#                                                 IntLiteral(3)
#                                             ]
#                                         ),
#                                         BinaryOp(
#                                             "*",
#                                             IntLiteral(2),
#                                             ArrayCell(
#                                                 ArrayLiteral(
#                                                     [
#                                                         IntLiteral(1),
#                                                         IntLiteral(2),
#                                                         IntLiteral(3)
#                                                     ]
#                                                 ),
#                                                 [
#                                                     IntLiteral(2)
#                                                 ]
#                                             )
#                                         )
#                                     ]
#                                 ),
#                                 Return(
#                                     CallExpr(
#                                         Id("foo"),
#                                         [
#                                             CallExpr(
#                                                 Id("fooo"),
#                                                 [
#                                                     ArrayLiteral(
#                                                         [
#                                                             IntLiteral(1),
#                                                             IntLiteral(2),
#                                                             IntLiteral(3)
#                                                         ]
#                                                     )
#                                                 ]
#                                             )
#                                         ]
#                                     )
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             369))
#
#     def test_70(self):
#         input = r"""
#         Function: foo
#         Parameter: x, y, z[1]
#             Body:
#                 ** Test If statement **
#                 Var: x = True, y = False;
#                 If True Then
#                 EndIf.
#             EndBody."""
#         expect = Program(
#                 [
#                     FuncDecl(
#                         Id("foo"),
#                         [
#                             VarDecl(
#                                 Id("x"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("y"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("z"),
#                                 [1],
#                                 None
#                             )
#                         ],
#                         (
#                             [
#                                 VarDecl(
#                                     Id("x"),
#                                     [],
#                                     BooleanLiteral(True)
#                                 ),
#                                 VarDecl(
#                                     Id("y"),
#                                     [],
#                                     BooleanLiteral(False)
#                                 )
#                             ],
#                             [
#                                 If(
#                                     [
#                                         (
#                                             BooleanLiteral(True),
#                                             [],
#                                             []
#                                         )
#                                     ],
#                                     (
#                                         [],
#                                         []
#                                     )
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             370))
#
#     def test_71(self):
#         input = r"""
#         Function: foo
#         Parameter: x, y, z[1]
#             Body:
#                 ** Test If statement **
#                 Var: x = True, y = False;
#                 If True Then
#                     zoo(1);
#                 EndIf.
#             EndBody."""
#         expect = Program(
#                 [
#                     FuncDecl(
#                         Id("foo"),
#                         [
#                             VarDecl(
#                                 Id("x"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("y"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("z"),
#                                 [1],
#                                 None
#                             )
#                         ],
#                         (
#                             [
#                                 VarDecl(
#                                     Id("x"),
#                                     [],
#                                     BooleanLiteral(True)
#                                 ),
#                                 VarDecl(
#                                     Id("y"),
#                                     [],
#                                     BooleanLiteral(False)
#                                 )
#                             ],
#                             [
#                                 If(
#                                     [
#                                         (
#                                             BooleanLiteral(True),
#                                             [],
#                                             [
#                                                 CallStmt(
#                                                     Id("zoo"),
#                                                     [
#                                                         IntLiteral(1)
#                                                     ]
#                                                 )
#                                             ]
#                                         )
#                                     ],
#                                     (
#                                         [],
#                                         []
#                                     )
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             371))
#
#     def test_72(self):
#         input = r"""
#         Function: foo
#         Parameter: x, y, z[1]
#             Body:
#                 ** Test 3 If statement **
#                 Var: x = True, y = False;
#                 If True Then
#                     zoo(1);
#                 ElseIf y Then
#                     print(0xA);
#                 EndIf.
#             EndBody."""
#         expect = Program(
#                 [
#                     FuncDecl(
#                         Id("foo"),
#                         [
#                             VarDecl(
#                                 Id("x"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("y"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("z"),
#                                 [1],
#                                 None
#                             )
#                         ],
#                         (
#                             [
#                                 VarDecl(
#                                     Id("x"),
#                                     [],
#                                     BooleanLiteral(True)
#                                 ),
#                                 VarDecl(
#                                     Id("y"),
#                                     [],
#                                     BooleanLiteral(False)
#                                 )
#                             ],
#                             [
#                                 If(
#                                     [
#                                         (
#                                             BooleanLiteral(True),
#                                             [],
#                                             [
#                                                 CallStmt(
#                                                     Id("zoo"),
#                                                     [
#                                                         IntLiteral(1)
#                                                     ]
#                                                 )
#                                             ]
#                                         ),
#                                         (
#                                             Id("y"),
#                                             [],
#                                             [
#                                                 CallStmt(
#                                                     Id("print"),
#                                                     [
#                                                         IntLiteral(10)
#                                                     ]
#                                                 )
#                                             ]
#                                         )
#                                     ],
#                                     (
#                                         [],
#                                         []
#                                     )
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             372))
#
#     def test_73(self):
#         input = r"""
#         Function: foo
#         Parameter: x, y, z[1]
#             Body:
#                 ** Test 4 If statement **
#                 Var: x = True, y = False;
#                 If True Then
#                     zoo(1);
#                 ElseIf y Then
#                     print(0xA);
#                 Else
#                     Var: z = {1,2,3};
#                     w = a && b;
#                 EndIf.
#             EndBody."""
#         expect = Program(
#                 [
#                     FuncDecl(
#                         Id("foo"),
#                         [
#                             VarDecl(
#                                 Id("x"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("y"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("z"),
#                                 [1],
#                                 None
#                             )
#                         ],
#                         (
#                             [
#                                 VarDecl(
#                                     Id("x"),
#                                     [],
#                                     BooleanLiteral(True)
#                                 ),
#                                 VarDecl(
#                                     Id("y"),
#                                     [],
#                                     BooleanLiteral(False)
#                                 )
#                             ],
#                             [
#                                 If(
#                                     [
#                                         (
#                                             BooleanLiteral(True),
#                                             [],
#                                             [
#                                                 CallStmt(
#                                                     Id("zoo"),
#                                                     [
#                                                         IntLiteral(1)
#                                                     ]
#                                                 )
#                                             ]
#                                         ),
#                                         (
#                                             Id("y"),
#                                             [],
#                                             [
#                                                 CallStmt(
#                                                     Id("print"),
#                                                     [
#                                                         IntLiteral(10)
#                                                     ]
#                                                 )
#                                             ]
#                                         )
#                                     ],
#                                     (
#                                         [
#                                             VarDecl(
#                                                 Id("z"),
#                                                 [],
#                                                 ArrayLiteral(
#                                                     [
#                                                         IntLiteral(1),
#                                                         IntLiteral(2),
#                                                         IntLiteral(3)
#                                                     ]
#                                                 )
#                                             )
#                                         ],
#                                         [
#                                             Assign(
#                                                 Id("w"),
#                                                 BinaryOp(
#                                                     "&&",
#                                                     Id("a"),
#                                                     Id("b")
#                                                 )
#                                             )
#                                         ]
#                                     )
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             373))
#
#     def test_74(self):
#         input = r"""
#         Function: foo
#         Parameter: x, y, z[1]
#             Body:
#                 ** Test 5 If statement **
#                 Var: x = True, y = False;
#                 If True Then
#                     zoo(1);
#                 ElseIf y Then
#                     print(0xA);
#                     ** Test 5 thoi! **
#                 Else
#                     Var: z = {1,2,3};
#                     w = a && b;
#                 EndIf.
#             EndBody."""
#         expect = Program(
#                 [
#                     FuncDecl(
#                         Id("foo"),
#                         [
#                             VarDecl(
#                                 Id("x"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("y"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("z"),
#                                 [1],
#                                 None
#                             )
#                         ],
#                         (
#                             [
#                                 VarDecl(
#                                     Id("x"),
#                                     [],
#                                     BooleanLiteral(True)
#                                 ),
#                                 VarDecl(
#                                     Id("y"),
#                                     [],
#                                     BooleanLiteral(False)
#                                 )
#                             ],
#                             [
#                                 If(
#                                     [
#                                         (
#                                             BooleanLiteral(True),
#                                             [],
#                                             [
#                                                 CallStmt(
#                                                     Id("zoo"),
#                                                     [
#                                                         IntLiteral(1)
#                                                     ]
#                                                 )
#                                             ]
#                                         ),
#                                         (
#                                             Id("y"),
#                                             [],
#                                             [
#                                                 CallStmt(
#                                                     Id("print"),
#                                                     [
#                                                         IntLiteral(10)
#                                                     ]
#                                                 )
#                                             ]
#                                         )
#                                     ],
#                                     (
#                                         [
#                                             VarDecl(
#                                                 Id("z"),
#                                                 [],
#                                                 ArrayLiteral(
#                                                     [
#                                                         IntLiteral(1),
#                                                         IntLiteral(2),
#                                                         IntLiteral(3)
#                                                     ]
#                                                 )
#                                             )
#                                         ],
#                                         [
#                                             Assign(
#                                                 Id("w"),
#                                                 BinaryOp(
#                                                     "&&",
#                                                     Id("a"),
#                                                     Id("b")
#                                                 )
#                                             )
#                                         ]
#                                     )
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             374))
#
#     def test_75(self):
#         input = r"""
#         Function: foo
#         Parameter: x, y, z[1]
#             Body:
#                 ** Test 6 If statement **
#                 Var: x = True, y = False;
#                 If True Then
#                     Var: d[1];
#                     zoo(1);
#                 ElseIf y Then
#                     print(0xA);
#                 Else
#                     Var: z = {1,2,3};
#                     w = a && b;
#                 EndIf.
#             EndBody."""
#         expect = Program(
#                 [
#                     FuncDecl(
#                         Id("foo"),
#                         [
#                             VarDecl(
#                                 Id("x"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("y"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("z"),
#                                 [1],
#                                 None
#                             )
#                         ],
#                         (
#                             [
#                                 VarDecl(
#                                     Id("x"),
#                                     [],
#                                     BooleanLiteral(True)
#                                 ),
#                                 VarDecl(
#                                     Id("y"),
#                                     [],
#                                     BooleanLiteral(False)
#                                 )
#                             ],
#                             [
#                                 If(
#                                     [
#                                         (
#                                             BooleanLiteral(True),
#                                             [
#                                                 VarDecl(
#                                                     Id("d"),
#                                                     [1],
#                                                     None
#                                                 )
#                                             ],
#                                             [
#                                                 CallStmt(
#                                                     Id("zoo"),
#                                                     [
#                                                         IntLiteral(1)
#                                                     ]
#                                                 )
#                                             ]
#                                         ),
#                                         (
#                                             Id("y"),
#                                             [],
#                                             [
#                                                 CallStmt(
#                                                     Id("print"),
#                                                     [
#                                                         IntLiteral(10)
#                                                     ]
#                                                 )
#                                             ]
#                                         )
#                                     ],
#                                     (
#                                         [
#                                             VarDecl(
#                                                 Id("z"),
#                                                 [],
#                                                 ArrayLiteral(
#                                                     [
#                                                         IntLiteral(1),
#                                                         IntLiteral(2),
#                                                         IntLiteral(3)
#                                                     ]
#                                                 )
#                                             )
#                                         ],
#                                         [
#                                             Assign(
#                                                 Id("w"),
#                                                 BinaryOp(
#                                                     "&&",
#                                                     Id("a"),
#                                                     Id("b")
#                                                 )
#                                             )
#                                         ]
#                                     )
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             375))
#
#     def test_76(self):
#         input = r"""
#         Function: foo
#         Parameter: x, y, z[1]
#             Body:
#                 ** Test 1 For Statement **
#                 For (x = 0, x < 5, 2) Do
#                 EndFor.
#             EndBody."""
#         expect = Program(
#                 [
#                     FuncDecl(
#                         Id("foo"),
#                         [
#                             VarDecl(
#                                 Id("x"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("y"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("z"),
#                                 [1],
#                                 None
#                             )
#                         ],
#                         (
#                             [],
#                             [
#                                 For(
#                                     Id("x"),
#                                     IntLiteral(0),
#                                     BinaryOp(
#                                         "<",
#                                         Id("x"),
#                                         IntLiteral(5)
#                                     ),
#                                     IntLiteral(2),
#                                     (
#                                         [],
#                                         []
#                                     )
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             376))
#
#     def test_77(self):
#         input = r"""
#         Function: foo
#         Parameter: x, y, z[1]
#             Body:
#                 ** Test 2 For Statement **
#                 For (x = 0, x < 5, 2) Do
#                     Var: abc[2] = {0x1, 0x2};
#                 EndFor.
#             EndBody."""
#         expect = Program(
#                 [
#                     FuncDecl(
#                         Id("foo"),
#                         [
#                             VarDecl(
#                                 Id("x"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("y"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("z"),
#                                 [1],
#                                 None
#                             )
#                         ],
#                         (
#                             [],
#                             [
#                                 For(
#                                     Id("x"),
#                                     IntLiteral(0),
#                                     BinaryOp(
#                                         "<",
#                                         Id("x"),
#                                         IntLiteral(5)
#                                     ),
#                                     IntLiteral(2),
#                                     (
#                                         [
#                                             VarDecl(
#                                                 Id("abc"),
#                                                 [2],
#                                                 ArrayLiteral(
#                                                     [
#                                                         IntLiteral(1),
#                                                         IntLiteral(2)
#                                                     ]
#                                                 )
#                                             )
#                                         ],
#                                         []
#                                     )
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             377))
#
#     def test_78(self):
#         input = r"""
#         Function: foo
#         Parameter: x, y, z[1]
#             Body:
#                 ** Test 3 For Statement **
#                 For (x = 0, x < 5, 2) Do
#                     Var: abc[2] = {0x1, 0x2};
#                     abc = {0,2,3}[1];
#                 EndFor.
#             EndBody."""
#         expect = Program(
#                 [
#                     FuncDecl(
#                         Id("foo"),
#                         [
#                             VarDecl(
#                                 Id("x"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("y"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("z"),
#                                 [1],
#                                 None
#                             )
#                         ],
#                         (
#                             [],
#                             [
#                                 For(
#                                     Id("x"),
#                                     IntLiteral(0),
#                                     BinaryOp(
#                                         "<",
#                                         Id("x"),
#                                         IntLiteral(5)
#                                     ),
#                                     IntLiteral(2),
#                                     (
#                                         [
#                                             VarDecl(
#                                                 Id("abc"),
#                                                 [2],
#                                                 ArrayLiteral(
#                                                     [
#                                                         IntLiteral(1),
#                                                         IntLiteral(2)
#                                                     ]
#                                                 )
#                                             )
#                                         ],
#                                         [
#                                             Assign(
#                                                 Id("abc"),
#                                                 ArrayCell(
#                                                     ArrayLiteral(
#                                                         [
#                                                             IntLiteral(0),
#                                                             IntLiteral(2),
#                                                             IntLiteral(3)
#                                                         ]
#                                                     ),
#                                                     [
#                                                         IntLiteral(1)
#                                                     ]
#                                                 )
#                                             )
#                                         ]
#                                     )
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             378))
#
#     def test_79(self):
#         input = r"""
#         Function: foo
#         Parameter: x, y, z[1]
#             Body:
#                 ** Test 4 For Statement **
#                 For (x = 0, x < 5, 2) Do
#                     Var: abc[2] = {0x1, 0x2};
#                     abc = {0,2,3}[1];
#                     ** Comment 4 **
#                 EndFor.
#             EndBody."""
#         expect = Program(
#                 [
#                     FuncDecl(
#                         Id("foo"),
#                         [
#                             VarDecl(
#                                 Id("x"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("y"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("z"),
#                                 [1],
#                                 None
#                             )
#                         ],
#                         (
#                             [],
#                             [
#                                 For(
#                                     Id("x"),
#                                     IntLiteral(0),
#                                     BinaryOp(
#                                         "<",
#                                         Id("x"),
#                                         IntLiteral(5)
#                                     ),
#                                     IntLiteral(2),
#                                     (
#                                         [
#                                             VarDecl(
#                                                 Id("abc"),
#                                                 [2],
#                                                 ArrayLiteral(
#                                                     [
#                                                         IntLiteral(1),
#                                                         IntLiteral(2)
#                                                     ]
#                                                 )
#                                             )
#                                         ],
#                                         [
#                                             Assign(
#                                                 Id("abc"),
#                                                 ArrayCell(
#                                                     ArrayLiteral(
#                                                         [
#                                                             IntLiteral(0),
#                                                             IntLiteral(2),
#                                                             IntLiteral(3)
#                                                         ]
#                                                     ),
#                                                     [
#                                                         IntLiteral(1)
#                                                     ]
#                                                 )
#                                             )
#                                         ]
#                                     )
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             379))
#
#     def test_80(self):
#         input = r"""
#         Function: foo
#         Parameter: x, y, z[1]
#             Body:
#                 ** Test 5 For Statement **
#                 For (x = 0, x < 5, 2) Do
#                     Var: abc[2] = {0x1, 0x2};
#                     abc = {0,2,3}[1];
#                     ** Comment 4 **
#                     For (i = 0, i, i) Do
#                     EndFor.
#                 EndFor.
#             EndBody."""
#         expect = Program(
#                 [
#                     FuncDecl(
#                         Id("foo"),
#                         [
#                             VarDecl(
#                                 Id("x"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("y"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("z"),
#                                 [1],
#                                 None
#                             )
#                         ],
#                         (
#                             [],
#                             [
#                                 For(
#                                     Id("x"),
#                                     IntLiteral(0),
#                                     BinaryOp(
#                                         "<",
#                                         Id("x"),
#                                         IntLiteral(5)
#                                     ),
#                                     IntLiteral(2),
#                                     (
#                                         [
#                                             VarDecl(
#                                                 Id("abc"),
#                                                 [2],
#                                                 ArrayLiteral(
#                                                     [
#                                                         IntLiteral(1),
#                                                         IntLiteral(2)
#                                                     ]
#                                                 )
#                                             )
#                                         ],
#                                         [
#                                             Assign(
#                                                 Id("abc"),
#                                                 ArrayCell(
#                                                     ArrayLiteral(
#                                                         [
#                                                             IntLiteral(0),
#                                                             IntLiteral(2),
#                                                             IntLiteral(3)
#                                                         ]
#                                                     ),
#                                                     [
#                                                         IntLiteral(1)
#                                                     ]
#                                                 )
#                                             ),
#                                             For(
#                                                 Id("i"),
#                                                 IntLiteral(0),
#                                                 Id("i"),
#                                                 Id("i"),
#                                                 (
#                                                     [],
#                                                     []
#                                                 )
#                                             )
#                                         ]
#                                     )
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             380))
#
#     def test_81(self):
#         input = r"""
#         Function: foo
#         Parameter: x, y, z[1]
#             Body:
#                 ** Test 6 For Statement **
#                 For (x = 0, x < 5, 2) Do
#                     Var: abc[2] = {0x1, 0x2};
#                     abc = {0,2,3}[1];
#                     ** Comment 4 **
#                     For (i = 0, i, i) Do
#                         ** Comment 5 **
#                     EndFor.
#                 EndFor.
#             EndBody."""
#         expect = Program(
#                 [
#                     FuncDecl(
#                         Id("foo"),
#                         [
#                             VarDecl(
#                                 Id("x"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("y"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("z"),
#                                 [1],
#                                 None
#                             )
#                         ],
#                         (
#                             [],
#                             [
#                                 For(
#                                     Id("x"),
#                                     IntLiteral(0),
#                                     BinaryOp(
#                                         "<",
#                                         Id("x"),
#                                         IntLiteral(5)
#                                     ),
#                                     IntLiteral(2),
#                                     (
#                                         [
#                                             VarDecl(
#                                                 Id("abc"),
#                                                 [2],
#                                                 ArrayLiteral(
#                                                     [
#                                                         IntLiteral(1),
#                                                         IntLiteral(2)
#                                                     ]
#                                                 )
#                                             )
#                                         ],
#                                         [
#                                             Assign(
#                                                 Id("abc"),
#                                                 ArrayCell(
#                                                     ArrayLiteral(
#                                                         [
#                                                             IntLiteral(0),
#                                                             IntLiteral(2),
#                                                             IntLiteral(3)
#                                                         ]
#                                                     ),
#                                                     [
#                                                         IntLiteral(1)
#                                                     ]
#                                                 )
#                                             ),
#                                             For(
#                                                 Id("i"),
#                                                 IntLiteral(0),
#                                                 Id("i"),
#                                                 Id("i"),
#                                                 (
#                                                     [],
#                                                     []
#                                                 )
#                                             )
#                                         ]
#                                     )
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             381))
#
#     def test_82(self):
#         input = r"""
#         Function: foo
#         Parameter: x, y, z[1]
#             Body:
#                 ** Test 6 For Statement **
#                 For (x = 0, x < 5, 2) Do
#                     Var: abc[2] = {0x1, 0x2};
#                     abc = {0,2,3}[1];
#                     ** Comment 4 **
#                     For (i = 0, i, i) Do
#                         ** Comment 5 **
#                         abc = foo();
#                     EndFor.
#                 EndFor.
#             EndBody."""
#         expect = Program(
#                 [
#                     FuncDecl(
#                         Id("foo"),
#                         [
#                             VarDecl(
#                                 Id("x"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("y"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("z"),
#                                 [1],
#                                 None
#                             )
#                         ],
#                         (
#                             [],
#                             [
#                                 For(
#                                     Id("x"),
#                                     IntLiteral(0),
#                                     BinaryOp(
#                                         "<",
#                                         Id("x"),
#                                         IntLiteral(5)
#                                     ),
#                                     IntLiteral(2),
#                                     (
#                                         [
#                                             VarDecl(
#                                                 Id("abc"),
#                                                 [2],
#                                                 ArrayLiteral(
#                                                     [
#                                                         IntLiteral(1),
#                                                         IntLiteral(2)
#                                                     ]
#                                                 )
#                                             )
#                                         ],
#                                         [
#                                             Assign(
#                                                 Id("abc"),
#                                                 ArrayCell(
#                                                     ArrayLiteral(
#                                                         [
#                                                             IntLiteral(0),
#                                                             IntLiteral(2),
#                                                             IntLiteral(3)
#                                                         ]
#                                                     ),
#                                                     [
#                                                         IntLiteral(1)
#                                                     ]
#                                                 )
#                                             ),
#                                             For(
#                                                 Id("i"),
#                                                 IntLiteral(0),
#                                                 Id("i"),
#                                                 Id("i"),
#                                                 (
#                                                     [],
#                                                     [
#                                                         Assign(
#                                                             Id("abc"),
#                                                             CallExpr(
#                                                                 Id("foo"),
#                                                                 []
#                                                             )
#                                                         )
#                                                     ]
#                                                 )
#                                             )
#                                         ]
#                                     )
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             382))
#
#     def test_83(self):
#         input = r"""
#         Function: foo
#         Parameter: x, y, z[1]
#             Body:
#                 While (True) Do
#                     ** Test 1 While Statement **
#                 EndWhile.
#             EndBody."""
#         expect = Program(
#                 [
#                     FuncDecl(
#                         Id("foo"),
#                         [
#                             VarDecl(
#                                 Id("x"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("y"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("z"),
#                                 [1],
#                                 None
#                             )
#                         ],
#                         (
#                             [],
#                             [
#                                 While(
#                                     BooleanLiteral(True),
#                                     (
#                                         [],
#                                         []
#                                     )
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             383))
#
#     def test_84(self):
#         input = r"""
#         Function: foo
#         Parameter: x, y, z[1]
#             Body:
#                 While (x < y + z[1]) Do
#                     ** Test 2 While Statement **
#                 EndWhile.
#             EndBody."""
#         expect = Program(
#                 [
#                     FuncDecl(
#                         Id("foo"),
#                         [
#                             VarDecl(
#                                 Id("x"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("y"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("z"),
#                                 [1],
#                                 None
#                             )
#                         ],
#                         (
#                             [],
#                             [
#                                 While(
#                                     BinaryOp(
#                                         "<",
#                                         Id("x"),
#                                         BinaryOp(
#                                             "+",
#                                             Id("y"),
#                                             ArrayCell(
#                                                 Id("z"),
#                                                 [
#                                                     IntLiteral(1)
#                                                 ]
#                                             )
#                                         )
#                                     ),
#                                     (
#                                         [],
#                                         []
#                                     )
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             384))
#
#     def test_85(self):
#         input = r"""
#         Function: foo
#         Parameter: x, y, z[1]
#             Body:
#                 While (x < y + z[1]) Do
#                     ** Test 3 While Statement **
#                     Var: e = 0xA;
#                 EndWhile.
#             EndBody."""
#         expect = Program(
#                 [
#                     FuncDecl(
#                         Id("foo"),
#                         [
#                             VarDecl(
#                                 Id("x"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("y"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("z"),
#                                 [1],
#                                 None
#                             )
#                         ],
#                         (
#                             [],
#                             [
#                                 While(
#                                     BinaryOp(
#                                         "<",
#                                         Id("x"),
#                                         BinaryOp(
#                                             "+",
#                                             Id("y"),
#                                             ArrayCell(
#                                                 Id("z"),
#                                                 [
#                                                     IntLiteral(1)
#                                                 ]
#                                             )
#                                         )
#                                     ),
#                                     (
#                                         [
#                                             VarDecl(
#                                                 Id("e"),
#                                                 [],
#                                                 IntLiteral(10)
#                                             )
#                                         ],
#                                         []
#                                     )
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             385))
#
#     def test_86(self):
#         input = r"""
#         Function: foo
#         Parameter: x, y, z[1]
#             Body:
#                 While (x < y + z[1]) Do
#                     ** Test 4 While Statement **
#                     Var: e = 0xA;
#                     While True Do
#                     EndWhile.
#                 EndWhile.
#             EndBody."""
#         expect = Program(
#                 [
#                     FuncDecl(
#                         Id("foo"),
#                         [
#                             VarDecl(
#                                 Id("x"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("y"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("z"),
#                                 [1],
#                                 None
#                             )
#                         ],
#                         (
#                             [],
#                             [
#                                 While(
#                                     BinaryOp(
#                                         "<",
#                                         Id("x"),
#                                         BinaryOp(
#                                             "+",
#                                             Id("y"),
#                                             ArrayCell(
#                                                 Id("z"),
#                                                 [
#                                                     IntLiteral(1)
#                                                 ]
#                                             )
#                                         )
#                                     ),
#                                     (
#                                         [
#                                             VarDecl(
#                                                 Id("e"),
#                                                 [],
#                                                 IntLiteral(10)
#                                             )
#                                         ],
#                                         [
#                                             While(
#                                                 BooleanLiteral(True),
#                                                 (
#                                                     [],
#                                                     []
#                                                 )
#                                             )
#                                         ]
#                                     )
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             386))
#
#     def test_87(self):
#         input = r"""
#         Function: foo
#         Parameter: x, y, z[1]
#             Body:
#                 While (x < y + z[1]) Do
#                     ** Test 5 While Statement **
#                     Var: e = 0xA;
#                     While True Do
#                         While True Do
#                         EndWhile.
#                     EndWhile.
#                 EndWhile.
#             EndBody."""
#         expect = Program(
#                 [
#                     FuncDecl(
#                         Id("foo"),
#                         [
#                             VarDecl(
#                                 Id("x"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("y"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("z"),
#                                 [1],
#                                 None
#                             )
#                         ],
#                         (
#                             [],
#                             [
#                                 While(
#                                     BinaryOp(
#                                         "<",
#                                         Id("x"),
#                                         BinaryOp(
#                                             "+",
#                                             Id("y"),
#                                             ArrayCell(
#                                                 Id("z"),
#                                                 [
#                                                     IntLiteral(1)
#                                                 ]
#                                             )
#                                         )
#                                     ),
#                                     (
#                                         [
#                                             VarDecl(
#                                                 Id("e"),
#                                                 [],
#                                                 IntLiteral(10)
#                                             )
#                                         ],
#                                         [
#                                             While(
#                                                 BooleanLiteral(True),
#                                                 (
#                                                     [],
#                                                     [
#                                                         While(
#                                                             BooleanLiteral(True),
#                                                             (
#                                                                 [],
#                                                                 []
#                                                             )
#                                                         )
#                                                     ]
#                                                 )
#                                             )
#                                         ]
#                                     )
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             387))
#
#     def test_88(self):
#         input = r"""
#         Function: foo
#         Parameter: x, y, z[1]
#             Body:
#                 While (x < y + z[1]) Do
#                     ** Test 5 While Statement **
#                     Var: e = 0xA;
#                     While True Do
#                         While True Do
#                             While True Do
#                             EndWhile.
#                         EndWhile.
#                     EndWhile.
#                 EndWhile.
#             EndBody."""
#         expect = Program(
#                 [
#                     FuncDecl(
#                         Id("foo"),
#                         [
#                             VarDecl(
#                                 Id("x"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("y"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("z"),
#                                 [1],
#                                 None
#                             )
#                         ],
#                         (
#                             [],
#                             [
#                                 While(
#                                     BinaryOp(
#                                         "<",
#                                         Id("x"),
#                                         BinaryOp(
#                                             "+",
#                                             Id("y"),
#                                             ArrayCell(
#                                                 Id("z"),
#                                                 [
#                                                     IntLiteral(1)
#                                                 ]
#                                             )
#                                         )
#                                     ),
#                                     (
#                                         [
#                                             VarDecl(
#                                                 Id("e"),
#                                                 [],
#                                                 IntLiteral(10)
#                                             )
#                                         ],
#                                         [
#                                             While(
#                                                 BooleanLiteral(True),
#                                                 (
#                                                     [],
#                                                     [
#                                                         While(
#                                                             BooleanLiteral(True),
#                                                             (
#                                                                 [],
#                                                                 [
#                                                                     While(
#                                                                         BooleanLiteral(True),
#                                                                         (
#                                                                             [],
#                                                                             []
#                                                                         )
#                                                                     )
#                                                                 ]
#                                                             )
#                                                         )
#                                                     ]
#                                                 )
#                                             )
#                                         ]
#                                     )
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             388))
#
#     def test_89(self):
#         input = r"""
#         Function: foo
#         Parameter: x, y, z[1]
#             Body:
#                 While (x < y + z[1]) Do
#                     ** Test 5 While Statement **
#                     Var: e = 0xA;
#                     While True Do
#                         While True Do
#                             While True Do
#                                 While True Do
#                                     print("a");
#                                 EndWhile.
#                             EndWhile.
#                         EndWhile.
#                     EndWhile.
#                 EndWhile.
#             EndBody."""
#         expect = Program(
#                 [
#                     FuncDecl(
#                         Id("foo"),
#                         [
#                             VarDecl(
#                                 Id("x"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("y"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("z"),
#                                 [1],
#                                 None
#                             )
#                         ],
#                         (
#                             [],
#                             [
#                                 While(
#                                     BinaryOp(
#                                         "<",
#                                         Id("x"),
#                                         BinaryOp(
#                                             "+",
#                                             Id("y"),
#                                             ArrayCell(
#                                                 Id("z"),
#                                                 [
#                                                     IntLiteral(1)
#                                                 ]
#                                             )
#                                         )
#                                     ),
#                                     (
#                                         [
#                                             VarDecl(
#                                                 Id("e"),
#                                                 [],
#                                                 IntLiteral(10)
#                                             )
#                                         ],
#                                         [
#                                             While(
#                                                 BooleanLiteral(True),
#                                                 (
#                                                     [],
#                                                     [
#                                                         While(
#                                                             BooleanLiteral(True),
#                                                             (
#                                                                 [],
#                                                                 [
#                                                                     While(
#                                                                         BooleanLiteral(True),
#                                                                         (
#                                                                             [],
#                                                                             [
#                                                                                 While(
#                                                                                     BooleanLiteral(True),
#                                                                                     (
#                                                                                         [],
#                                                                                         [
#                                                                                             CallStmt(
#                                                                                                 Id("print"),
#                                                                                                 [
#                                                                                                     StringLiteral("a")
#                                                                                                 ]
#                                                                                             )
#                                                                                         ]
#                                                                                     )
#                                                                                 )
#                                                                             ]
#                                                                         )
#                                                                     )
#                                                                 ]
#                                                             )
#                                                         )
#                                                     ]
#                                                 )
#                                             )
#                                         ]
#                                     )
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             389))
#
#     def test_90(self):
#         input = r"""
#         Function: foo
#         Parameter: x, y, z[1]
#             Body:
#                 While (x < y + z[1]) Do
#                     ** Test 6 While Statement **
#                     Var: e = 0xA;
#                     While True Do
#                         While True Do
#                             While True Do
#                                 While True Do
#                                     print("a");
#                                     Return(False);
#                                 EndWhile.
#                             EndWhile.
#                         EndWhile.
#                     EndWhile.
#                 EndWhile.
#             EndBody."""
#         expect = Program(
#                 [
#                     FuncDecl(
#                         Id("foo"),
#                         [
#                             VarDecl(
#                                 Id("x"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("y"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("z"),
#                                 [1],
#                                 None
#                             )
#                         ],
#                         (
#                             [],
#                             [
#                                 While(
#                                     BinaryOp(
#                                         "<",
#                                         Id("x"),
#                                         BinaryOp(
#                                             "+",
#                                             Id("y"),
#                                             ArrayCell(
#                                                 Id("z"),
#                                                 [
#                                                     IntLiteral(1)
#                                                 ]
#                                             )
#                                         )
#                                     ),
#                                     (
#                                         [
#                                             VarDecl(
#                                                 Id("e"),
#                                                 [],
#                                                 IntLiteral(10)
#                                             )
#                                         ],
#                                         [
#                                             While(
#                                                 BooleanLiteral(True),
#                                                 (
#                                                     [],
#                                                     [
#                                                         While(
#                                                             BooleanLiteral(True),
#                                                             (
#                                                                 [],
#                                                                 [
#                                                                     While(
#                                                                         BooleanLiteral(True),
#                                                                         (
#                                                                             [],
#                                                                             [
#                                                                                 While(
#                                                                                     BooleanLiteral(True),
#                                                                                     (
#                                                                                         [],
#                                                                                         [
#                                                                                             CallStmt(
#                                                                                                 Id("print"),
#                                                                                                 [
#                                                                                                     StringLiteral("a")
#                                                                                                 ]
#                                                                                             ),
#                                                                                             Return(
#                                                                                                 BooleanLiteral(False)
#                                                                                             )
#                                                                                         ]
#                                                                                     )
#                                                                                 )
#                                                                             ]
#                                                                         )
#                                                                     )
#                                                                 ]
#                                                             )
#                                                         )
#                                                     ]
#                                                 )
#                                             )
#                                         ]
#                                     )
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             390))
#
#     def test_91(self):
#         input = r"""
#         Function: foo
#         Parameter: x, y, z[1]
#             Body:
#                 Do
#                     ** Test 1 Dowhile Statement **
#                 While True EndDo.
#             EndBody."""
#         expect = Program(
#                 [
#                     FuncDecl(
#                         Id("foo"),
#                         [
#                             VarDecl(
#                                 Id("x"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("y"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("z"),
#                                 [1],
#                                 None
#                             )
#                         ],
#                         (
#                             [],
#                             [
#                                 Dowhile(
#                                     (
#                                         [],
#                                         []
#                                     ),
#                                     BooleanLiteral(True)
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             391))
#
#     def test_92(self):
#         input = r"""
#         Function: foo
#         Parameter: x, y, z[1]
#             Body:
#                 Do
#                     ** Test 1 Dowhile Statement **
#                     Do
#                     While True EndDo.
#                 While True EndDo.
#             EndBody."""
#         expect = Program(
#                 [
#                     FuncDecl(
#                         Id("foo"),
#                         [
#                             VarDecl(
#                                 Id("x"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("y"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("z"),
#                                 [1],
#                                 None
#                             )
#                         ],
#                         (
#                             [],
#                             [
#                                 Dowhile(
#                                     (
#                                         [],
#                                         [
#                                             Dowhile(
#                                                 (
#                                                     [],
#                                                     []
#                                                 ),
#                                                 BooleanLiteral(True)
#                                             )
#                                         ]
#                                     ),
#                                     BooleanLiteral(True)
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             392))
#
#     def test_93(self):
#         input = r"""
#         Function: foo
#         Parameter: x, y, z[1]
#             Body:
#                 Do
#                     ** Test 2 Dowhile Statement **
#                     Do
#                         Do
#                         While True EndDo.
#                     While True EndDo.
#                 While True EndDo.
#             EndBody."""
#         expect = Program(
#                 [
#                     FuncDecl(
#                         Id("foo"),
#                         [
#                             VarDecl(
#                                 Id("x"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("y"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("z"),
#                                 [1],
#                                 None
#                             )
#                         ],
#                         (
#                             [],
#                             [
#                                 Dowhile(
#                                     (
#                                         [],
#                                         [
#                                             Dowhile(
#                                                 (
#                                                     [],
#                                                     [
#                                                         Dowhile(
#                                                             (
#                                                                 [],
#                                                                 []
#                                                             ),
#                                                             BooleanLiteral(True)
#                                                         )
#                                                     ]
#                                                 ),
#                                                 BooleanLiteral(True)
#                                             )
#                                         ]
#                                     ),
#                                     BooleanLiteral(True)
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             393))
#
#     def test_94(self):
#         input = r"""
#         Function: foo
#         Parameter: x, y, z[1]
#             Body:
#                 Do
#                     ** Test 3 Dowhile Statement **
#                     Do
#                         Do
#                             Do
#                             While True EndDo.
#                         While True EndDo.
#                     While True EndDo.
#                 While True EndDo.
#             EndBody."""
#         expect = Program(
#                 [
#                     FuncDecl(
#                         Id("foo"),
#                         [
#                             VarDecl(
#                                 Id("x"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("y"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("z"),
#                                 [1],
#                                 None
#                             )
#                         ],
#                         (
#                             [],
#                             [
#                                 Dowhile(
#                                     (
#                                         [],
#                                         [
#                                             Dowhile(
#                                                 (
#                                                     [],
#                                                     [
#                                                         Dowhile(
#                                                             (
#                                                                 [],
#                                                                 [
#                                                                     Dowhile(
#                                                                         (
#                                                                             [],
#                                                                             []
#                                                                         ),
#                                                                         BooleanLiteral(True)
#                                                                     )
#                                                                 ]
#                                                             ),
#                                                             BooleanLiteral(True)
#                                                         )
#                                                     ]
#                                                 ),
#                                                 BooleanLiteral(True)
#                                             )
#                                         ]
#                                     ),
#                                     BooleanLiteral(True)
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             394))
#
#     def test_95(self):
#         input = r"""
#         Function: foo
#         Parameter: x, y, z[1]
#             Body:
#                 Do
#                     ** Test 3 Dowhile Statement **
#                     Do
#                         Do
#                             Do
#                                 While True Do
#                                 EndWhile.
#                             While True EndDo.
#                         While True EndDo.
#                     While True EndDo.
#                 While True EndDo.
#             EndBody."""
#         expect = Program(
#                 [
#                     FuncDecl(
#                         Id("foo"),
#                         [
#                             VarDecl(
#                                 Id("x"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("y"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("z"),
#                                 [1],
#                                 None
#                             )
#                         ],
#                         (
#                             [],
#                             [
#                                 Dowhile(
#                                     (
#                                         [],
#                                         [
#                                             Dowhile(
#                                                 (
#                                                     [],
#                                                     [
#                                                         Dowhile(
#                                                             (
#                                                                 [],
#                                                                 [
#                                                                     Dowhile(
#                                                                         (
#                                                                             [],
#                                                                             [
#                                                                                 While(
#                                                                                     BooleanLiteral(True),
#                                                                                     (
#                                                                                         [],
#                                                                                         []
#                                                                                     )
#                                                                                 )
#                                                                             ]
#                                                                         ),
#                                                                         BooleanLiteral(True)
#                                                                     )
#                                                                 ]
#                                                             ),
#                                                             BooleanLiteral(True)
#                                                         )
#                                                     ]
#                                                 ),
#                                                 BooleanLiteral(True)
#                                             )
#                                         ]
#                                     ),
#                                     BooleanLiteral(True)
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             395))
#
#     def test_96(self):
#         input = r"""
#         Function: foo
#         Parameter: x, y, z[1]
#             Body:
#                 Do
#                     ** Test 4 Dowhile Statement **
#                     Do
#                         Do
#                             Do
#                                 While True Do
#                                     While True Do
#                                     EndWhile.
#                                 EndWhile.
#                             While True EndDo.
#                         While True EndDo.
#                     While True EndDo.
#                 While True EndDo.
#             EndBody."""
#         expect = Program(
#                 [
#                     FuncDecl(
#                         Id("foo"),
#                         [
#                             VarDecl(
#                                 Id("x"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("y"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("z"),
#                                 [1],
#                                 None
#                             )
#                         ],
#                         (
#                             [],
#                             [
#                                 Dowhile(
#                                     (
#                                         [],
#                                         [
#                                             Dowhile(
#                                                 (
#                                                     [],
#                                                     [
#                                                         Dowhile(
#                                                             (
#                                                                 [],
#                                                                 [
#                                                                     Dowhile(
#                                                                         (
#                                                                             [],
#                                                                             [
#                                                                                 While(
#                                                                                     BooleanLiteral(True),
#                                                                                     (
#                                                                                         [],
#                                                                                         [
#                                                                                             While(
#                                                                                                 BooleanLiteral(True),
#                                                                                                 (
#                                                                                                     [],
#                                                                                                     []
#                                                                                                 )
#                                                                                             )
#                                                                                         ]
#                                                                                     )
#                                                                                 )
#                                                                             ]
#                                                                         ),
#                                                                         BooleanLiteral(True)
#                                                                     )
#                                                                 ]
#                                                             ),
#                                                             BooleanLiteral(True)
#                                                         )
#                                                     ]
#                                                 ),
#                                                 BooleanLiteral(True)
#                                             )
#                                         ]
#                                     ),
#                                     BooleanLiteral(True)
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             396))
#
#     def test_97(self):
#         input = r"""
#         Function: foo
#         Parameter: x, y, z[1]
#             Body:
#                 Do
#                     ** Test 4 Dowhile Statement **
#                     Do
#                         Do
#                             Do
#                                 While True Do
#                                     While True Do
#                                         If True Then
#                                         EndIf.
#                                     EndWhile.
#                                 EndWhile.
#                             While True EndDo.
#                         While True EndDo.
#                     While True EndDo.
#                 While True EndDo.
#             EndBody."""
#         expect = Program(
#                 [
#                     FuncDecl(
#                         Id("foo"),
#                         [
#                             VarDecl(
#                                 Id("x"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("y"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("z"),
#                                 [1],
#                                 None
#                             )
#                         ],
#                         (
#                             [],
#                             [
#                                 Dowhile(
#                                     (
#                                         [],
#                                         [
#                                             Dowhile(
#                                                 (
#                                                     [],
#                                                     [
#                                                         Dowhile(
#                                                             (
#                                                                 [],
#                                                                 [
#                                                                     Dowhile(
#                                                                         (
#                                                                             [],
#                                                                             [
#                                                                                 While(
#                                                                                     BooleanLiteral(True),
#                                                                                     (
#                                                                                         [],
#                                                                                         [
#                                                                                             While(
#                                                                                                 BooleanLiteral(True),
#                                                                                                 (
#                                                                                                     [],
#                                                                                                     [
#                                                                                                         If(
#                                                                                                             [
#                                                                                                                 (
#                                                                                                                     BooleanLiteral(True),
#                                                                                                                     [],
#                                                                                                                     []
#                                                                                                                 )
#                                                                                                             ],
#                                                                                                             (
#                                                                                                                 [],
#                                                                                                                 []
#                                                                                                             )
#                                                                                                         )
#                                                                                                     ]
#                                                                                                 )
#                                                                                             )
#                                                                                         ]
#                                                                                     )
#                                                                                 )
#                                                                             ]
#                                                                         ),
#                                                                         BooleanLiteral(True)
#                                                                     )
#                                                                 ]
#                                                             ),
#                                                             BooleanLiteral(True)
#                                                         )
#                                                     ]
#                                                 ),
#                                                 BooleanLiteral(True)
#                                             )
#                                         ]
#                                     ),
#                                     BooleanLiteral(True)
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             397))
#
#     def test_98(self):
#         input = r"""
#         Function: foo
#         Parameter: x, y, z[1]
#             Body:
#                 Do
#                     ** Test 4 Dowhile Statement **
#                     Do
#                         Do
#                             Do
#                                 While True Do
#                                     While True Do
#                                         If True Then
#                                         Else
#                                             For(i = 0,i < 10, 1) Do
#                                             EndFor.
#                                         EndIf.
#                                     EndWhile.
#                                 EndWhile.
#                             While True EndDo.
#                         While True EndDo.
#                     While True EndDo.
#                 While True EndDo.
#             EndBody."""
#         expect = Program(
#                 [
#                     FuncDecl(
#                         Id("foo"),
#                         [
#                             VarDecl(
#                                 Id("x"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("y"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("z"),
#                                 [1],
#                                 None
#                             )
#                         ],
#                         (
#                             [],
#                             [
#                                 Dowhile(
#                                     (
#                                         [],
#                                         [
#                                             Dowhile(
#                                                 (
#                                                     [],
#                                                     [
#                                                         Dowhile(
#                                                             (
#                                                                 [],
#                                                                 [
#                                                                     Dowhile(
#                                                                         (
#                                                                             [],
#                                                                             [
#                                                                                 While(
#                                                                                     BooleanLiteral(True),
#                                                                                     (
#                                                                                         [],
#                                                                                         [
#                                                                                             While(
#                                                                                                 BooleanLiteral(True),
#                                                                                                 (
#                                                                                                     [],
#                                                                                                     [
#                                                                                                         If(
#                                                                                                             [
#                                                                                                                 (
#                                                                                                                     BooleanLiteral(True),
#                                                                                                                     [],
#                                                                                                                     []
#                                                                                                                 )
#                                                                                                             ],
#                                                                                                             (
#                                                                                                                 [],
#                                                                                                                 [
#                                                                                                                     For(
#                                                                                                                         Id("i"),
#                                                                                                                         IntLiteral(0),
#                                                                                                                         BinaryOp(
#                                                                                                                             "<",
#                                                                                                                             Id("i"),
#                                                                                                                             IntLiteral(10)
#                                                                                                                         ),
#                                                                                                                         IntLiteral(1),
#                                                                                                                         (
#                                                                                                                             [],
#                                                                                                                             []
#                                                                                                                         )
#                                                                                                                     )
#                                                                                                                 ]
#                                                                                                             )
#                                                                                                         )
#                                                                                                     ]
#                                                                                                 )
#                                                                                             )
#                                                                                         ]
#                                                                                     )
#                                                                                 )
#                                                                             ]
#                                                                         ),
#                                                                         BooleanLiteral(True)
#                                                                     )
#                                                                 ]
#                                                             ),
#                                                             BooleanLiteral(True)
#                                                         )
#                                                     ]
#                                                 ),
#                                                 BooleanLiteral(True)
#                                             )
#                                         ]
#                                     ),
#                                     BooleanLiteral(True)
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             398))
#
#     def test_99(self):
#         input = r"""
#         Function: foo
#         Parameter: x, y, z[1]
#             Body:
#                 Do
#                     ** Test 4 Dowhile Statement **
#                     Do
#                         Do
#                             Do
#                                 While True Do
#                                     While True Do
#                                         If True Then
#                                         Else
#                                             For(i = 0,i < 10, 1) Do
#                                                 print("Successful");
#                                             EndFor.
#                                         EndIf.
#                                     EndWhile.
#                                 EndWhile.
#                             While True EndDo.
#                         While True EndDo.
#                     While True EndDo.
#                 While True EndDo.
#             EndBody."""
#         expect = Program(
#                 [
#                     FuncDecl(
#                         Id("foo"),
#                         [
#                             VarDecl(
#                                 Id("x"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("y"),
#                                 [],
#                                 None
#                             ),
#                             VarDecl(
#                                 Id("z"),
#                                 [1],
#                                 None
#                             )
#                         ],
#                         (
#                             [],
#                             [
#                                 Dowhile(
#                                     (
#                                         [],
#                                         [
#                                             Dowhile(
#                                                 (
#                                                     [],
#                                                     [
#                                                         Dowhile(
#                                                             (
#                                                                 [],
#                                                                 [
#                                                                     Dowhile(
#                                                                         (
#                                                                             [],
#                                                                             [
#                                                                                 While(
#                                                                                     BooleanLiteral(True),
#                                                                                     (
#                                                                                         [],
#                                                                                         [
#                                                                                             While(
#                                                                                                 BooleanLiteral(True),
#                                                                                                 (
#                                                                                                     [],
#                                                                                                     [
#                                                                                                         If(
#                                                                                                             [
#                                                                                                                 (
#                                                                                                                     BooleanLiteral(True),
#                                                                                                                     [],
#                                                                                                                     []
#                                                                                                                 )
#                                                                                                             ],
#                                                                                                             (
#                                                                                                                 [],
#                                                                                                                 [
#                                                                                                                     For(
#                                                                                                                         Id("i"),
#                                                                                                                         IntLiteral(0),
#                                                                                                                         BinaryOp(
#                                                                                                                             "<",
#                                                                                                                             Id("i"),
#                                                                                                                             IntLiteral(10)
#                                                                                                                         ),
#                                                                                                                         IntLiteral(1),
#                                                                                                                         (
#                                                                                                                             [],
#                                                                                                                             [
#                                                                                                                                 CallStmt(
#                                                                                                                                     Id("print"),
#                                                                                                                                     [
#                                                                                                                                         StringLiteral("Successful")
#                                                                                                                                     ]
#                                                                                                                                 )
#                                                                                                                             ]
#                                                                                                                         )
#                                                                                                                     )
#                                                                                                                 ]
#                                                                                                             )
#                                                                                                         )
#                                                                                                     ]
#                                                                                                 )
#                                                                                             )
#                                                                                         ]
#                                                                                     )
#                                                                                 )
#                                                                             ]
#                                                                         ),
#                                                                         BooleanLiteral(True)
#                                                                     )
#                                                                 ]
#                                                             ),
#                                                             BooleanLiteral(True)
#                                                         )
#                                                     ]
#                                                 ),
#                                                 BooleanLiteral(True)
#                                             )
#                                         ]
#                                     ),
#                                     BooleanLiteral(True)
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         self.assertTrue(TestAST.checkASTGen(
#             input,
#             expect,
#             399))
