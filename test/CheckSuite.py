import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):
    def test_0(self):
        # FuncDecl(Id("main"),[],([],[]))
        input = Program([FuncDecl(Id("main"),[],([],[CallStmt(Id("foo"),[])]))])
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_1(self):
        input = Program([
                VarDecl(
                    Id("x"),
                    [],
                    None
                )
            ])
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_2(self):
        input = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),FuncDecl(Id("main"),[],([],[]))])
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_3(self):
        input = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[1],None),FuncDecl(Id("main"),[],([],[]))])
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_4(self):
        input = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[1],IntLiteral(1)),FuncDecl(Id("main"),[],([],[]))])
        expect = str(TypeCannotBeInferred(VarDecl(Id("y"),[1],IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_5(self):
        input = Program([VarDecl(Id("x"),[],BooleanLiteral(True)),FuncDecl(Id("main"),[],([],[]))])
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_6(self):
        input = Program([VarDecl(Id("x"),[],BooleanLiteral(False)),FuncDecl(Id("main"),[],([],[]))])
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,406))
    
    def test_7(self):
        input = Program([VarDecl(Id("x"),[],StringLiteral("True")),FuncDecl(Id("main"),[],([],[]))])
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,407))
    
    def test_8(self):
        input = Program([VarDecl(Id("x"),[],FloatLiteral(1.2)),FuncDecl(Id("main"),[],([],[]))])
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,408))
    
    def test_9(self):
        input = Program(
            [
                VarDecl(
                    Id("x"),
                    [1],
                    FloatLiteral(1.2)
                ),
                FuncDecl(Id("main"),[],([],[]))
            ]
        )
        expect = str(TypeCannotBeInferred(VarDecl(Id("x"),[1],FloatLiteral(1.2))))
        self.assertTrue(TestChecker.test(input,expect,409))
    
    def test_10(self):
        input = Program(
            [
                VarDecl(
                    Id("x"),
                    [1,2,3],
                    None
                ),
                VarDecl(
                    Id("y"),
                    [2,2],
                    ArrayLiteral(
                        [
                            ArrayLiteral(
                                [
                                    IntLiteral(1),
                                    IntLiteral(2)
                                ]
                            ),
                            ArrayLiteral(
                                [
                                    IntLiteral(10),
                                    IntLiteral(20)
                                ]
                            )
                        ]
                    )
                ),
                FuncDecl(Id("main"),[],([],[]))
            ]
        )
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,410))
    
    def test_11(self):
        input = Program(
            [
                VarDecl(
                    Id("x"),
                    [],
                    IntLiteral(3)
                ),
                VarDecl(
                    Id("y"),
                    [],
                    IntLiteral(3)
                ),
                FuncDecl(Id("main"),[],([],[]))
            ]
        )
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,411))
    
    def test_12(self):
        input =  Program(
            [
                VarDecl(
                    Id("x"),
                    [],
                    FloatLiteral(1000.0)
                ),
                VarDecl(
                    Id("y"),
                    [5],
                    ArrayLiteral(
                        [
                            IntLiteral(2),
                            IntLiteral(4),
                            IntLiteral(100),
                            IntLiteral(24),
                            IntLiteral(9)
                        ]
                    )
                ),
                VarDecl(
                    Id("z"),
                    [],
                    FloatLiteral(2000.0)
                ),
                FuncDecl(Id("main"),[],([],[]))
            ]
        )
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,412))
    
    def test_13(self):
        input = Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            CallStmt(
                                Id("foo"),
                                []
                            )
                        ]
                    )
                )
            ]
        )
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,413))
    
    def test_14(self):
        input = Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [
                            VarDecl(Id("id"),[2,3],None),
                            VarDecl(Id("id"),[2,8],None)
                        ],
                        [
                            
                        ]
                    )
                )
            ]
        )
        expect = str(Redeclared(Variable(),"id"))
        self.assertTrue(TestChecker.test(input,expect,414))
    
    def test_15(self):
        input = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],None)],([],[]))])
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,415))
    
    def test_16(self):
        input = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],None)],([],[]))])
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,416))
    
    def test_17(self):
        input = Program(
                    [
                        VarDecl(Id("x"),[],None),
                        FuncDecl(Id("main"),
                                 [
                                     VarDecl(Id("x"),[],None),
                                     VarDecl(Id("y"),[5,2],None)
                                 ],
                                    (
                                        [],
                                        []
                                    )
                                 )
                    ])
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,417))
    
    def test_18(self):
        input = Program(
                    [
                        VarDecl(Id("x"),[],None),
                        FuncDecl(Id("main"),
                                 [
                                     VarDecl(Id("x"),[],None),
                                     VarDecl(Id("y"),[5,2],None)
                                 ],
                                    (
                                        [
                                            VarDecl(Id("r"),[],FloatLiteral(3.14)),
                                            VarDecl(Id("e"),[],FloatLiteral(2.7e1))
                                        ],
                                        []
                                    )
                                 )
                    ])
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,408))
    
    def test_19(self):
        input = Program(
                    [
                        VarDecl(Id("x"),[],None),
                        FuncDecl(Id("main"),
                                 [
                                     VarDecl(Id("x"),[],None),
                                     VarDecl(Id("y"),[5,2],None)
                                 ],
                                    (
                                        [
                                            VarDecl(Id("r"),[],FloatLiteral(3.14)),
                                            VarDecl(Id("e"),[],FloatLiteral(2.7e1))
                                        ],
                                        [
                                            Assign
                                            (
                                                Id("a"),
                                                Id("x")
                                            )
                                        ]
                                    )
                                 )
                    ])
        expect = str(Undeclared(Identifier(),"a"))
        self.assertTrue(TestChecker.test(input,expect,419))
    
    def test_20(self):
        input = Program(
                [
                    FuncDecl(Id("foo"),[],
                          (
                              [],
                              [
                                  Assign(
                                    Id("a"),
                                    IntLiteral(1)
                                  )
                              ]
                          )
                          ),
                    FuncDecl(Id("main"),[],([],[]))
                    
                ])
        expect = str(Undeclared(Identifier(),"a"))
        self.assertTrue(TestChecker.test(input,expect,420))
    
    def test_21(self):
        input = Program(
                [FuncDecl(Id("main"),[],
                          (
                              [
                                VarDecl(
                                    Id("a"),
                                    [4],
                                    None
                                )  
                                ],
                              [
                                  Assign(
                                    Id("a"),
                                    ArrayLiteral(
                                        [
                                        IntLiteral(1),
                                        IntLiteral(3),
                                        IntLiteral(5),
                                        IntLiteral(7)
                                        ]
                                    )
                                  )
                              ]
                          ))
                ]
                )
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,421))
    
    def test_22(self):
        input = Program(
                [FuncDecl(Id("main"),[],
                          (
                              [
                                  VarDecl(
                                    Id("a"),
                                    [4],
                                    None
                                )  
                               ],
                              [
                                  Assign(
                                    ArrayCell(
                                        Id("a"),
                                        [IntLiteral(2)]
                                    ),
                                    IntLiteral(5)
                                  )
                              ]
                          ))
                ]
                )
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,422))
    
    def test_23(self):
        input = Program(
                [FuncDecl(Id("main"),
                          [
                              
                              ],
                          (
                              [VarDecl(
                                    Id("a"),
                                    [],
                                    None
                                )  ],
                              [
                                  If(
                                      [
                                       (
                                        BooleanLiteral(True),
                                        [],
                                        [
                                            CallStmt(Id("main"),[])
                                        ]
                                        ),
                                        (
                                        BooleanLiteral(False),
                                        [],
                                        [
                                           
                                        ]
                                        ),
                                        (
                                        BinaryOp("<",Id("a"),IntLiteral(2)),
                                        [
                                            VarDecl(Id("x"),[],None)
                                        ],
                                        []
                                        )
                                      ],
                                      (
                                          [
                                              VarDecl(Id("x"),[],IntLiteral(3))
                                          ],
                                          [
                                              Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))
                                          ]
                                      )
                                  )
                              ]
                          ))
                ]
                )
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,423))
    
    def test_24(self):
        input = Program(
            [FuncDecl(
                Id("main"),
                [],
                (
                    [
                        VarDecl(
                                    Id("i"),
                                    [],
                                    None
                                )  ],
                    [
                        For(
                            Id("i"),
                            IntLiteral(0),
                            BinaryOp("<",
                                     Id("i"),
                                     IntLiteral(5)),
                            IntLiteral(1),
                            (
                                [],
                                [
                                    CallStmt(Id("print"),[Id("i")])
                                ]
                            )
                        )
                    ]
                )
            )
            ]
        )
        expect = str(TypeMismatchInStatement(CallStmt(Id("print"),[Id("i")])))
        self.assertTrue(TestChecker.test(input,expect,424))
    
    def test_25(self):
        input = Program([
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[
                        CallExpr(Id("read"),[IntLiteral(4)])
                        ])]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,425))
    
    def test_26(self):
        input = Program([
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,426))
    
    def test_27(self):
        input = Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [
                            VarDecl(
                                    Id("i"),
                                    [],
                                    None
                                )  
                            ],
                        [
                            While(
                                BinaryOp(
                                    ">",
                                    Id("i"),
                                    IntLiteral(10)
                                ),
                                (
                                    [],
                                    [
                                        Assign(
                                            Id("i"),
                                            BinaryOp(
                                                "-",
                                                Id("i"),
                                                IntLiteral(1)
                                            )
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,427))
    
    def test_28(self):
        input = Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [
                            VarDecl(
                                    Id("i"),
                                    [],
                                    None
                                )      
                        ],
                        [
                            While(
                                BinaryOp(
                                    "<",
                                    Id("i"),
                                    IntLiteral(10)
                                ),
                                (
                                    [
                                        VarDecl(Id("x"),[],IntLiteral(10))
                                    ],
                                    [
                                        Assign(
                                            Id("i"),
                                            BinaryOp(
                                                "+",
                                                Id("x"),
                                                IntLiteral(1)
                                            )
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,428))
    
    def test_29(self):
        input = Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [
                            VarDecl(
                                    Id("i"),
                                    [],
                                    None
                                )      
                        ],
                        [
                            Dowhile(
                                (
                                    [],
                                    [
                                        Assign(
                                            Id("i"),
                                            BinaryOp("*",Id("i"),IntLiteral(2))
                                        ),
                                        Break()
                                    ]
                                ),
                                BinaryOp("<",Id("i"),IntLiteral(10))
                            )
                        ]
                    )
                )
            ]
        )
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,429))
    
    def test_30(self):
        input = Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [
                            VarDecl(
                                Id("x"),
                                [],
                                StringLiteral("1710165")
                            ),
                            VarDecl(
                                Id("y"),
                                [],
                                IntLiteral(1710165)
                            )
                        ],
                        [
                            If(
                                [
                                    (
                                        BinaryOp("==",Id("y"),IntLiteral(1710165)),
                                        [],
                                        [
                                            Return(None)
                                        ]
                                    ),
                                    (
                                        BinaryOp("!=",Id("y"),IntLiteral(1710165)),
                                        [],
                                        [
                                            Assign(
                                                Id("x"),
                                                StringLiteral("Phuoc Linh")
                                            )
                                        ]
                                    )
                                ],
                                (
                                    [],
                                    [
                                        Return(None)
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,430))
    
    def test_31(self):
        input = Program(
            [
                VarDecl(
                    Id("x"),
                    [],
                    None
                ),
                VarDecl(
                    Id("y"),
                    [],
                    BooleanLiteral(True)
                ),
                VarDecl(
                    Id("z"),
                    [2,3],
                    ArrayLiteral(
                        [
                            ArrayLiteral(
                                [
                                    IntLiteral(1),
                                    IntLiteral(2),
                                    IntLiteral(2)  
                                ]
                            ),
                            ArrayLiteral(
                                [
                                    IntLiteral(2),
                                    IntLiteral(2),
                                    IntLiteral(10)
                                ]
                            )
                        ]
                    )
                ),
                FuncDecl(
                    Id("main"),
                    [
                        VarDecl(
                            Id("b"),
                            [],
                            None
                        ),
                        VarDecl(
                            Id("c"),
                            [],
                            None
                        ),
                        VarDecl(
                            Id("d"),
                            [10,10],
                            None
                        )
                    ],
                    (
                        [
                            VarDecl(
                                Id("a"),
                                [],
                                IntLiteral(1710165)
                            )
                        ],
                        []
                    )
                )
            ]
        )
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,431))
    
    def test_32(self):
        input = Program(
            [
                VarDecl(
                    Id("x"),
                    [],
                    None
                ),
                VarDecl(
                    Id("y"),
                    [],
                    BooleanLiteral(True)
                ),
                VarDecl(
                    Id("z"),
                    [2,3],
                    ArrayLiteral(
                        [
                            ArrayLiteral(
                                [
                                    IntLiteral(1),
                                    IntLiteral(2),
                                    IntLiteral(2)  
                                ]
                            ),
                            ArrayLiteral(
                                [
                                    IntLiteral(2),
                                    IntLiteral(2),
                                    IntLiteral(10)
                                ]
                            )
                        ]
                    )
                ),
                FuncDecl(
                    Id("main"),
                    [
                        VarDecl(
                            Id("b"),
                            [],
                            None
                        ),
                        VarDecl(
                            Id("c"),
                            [],
                            None
                        ),
                        VarDecl(
                            Id("d"),
                            [10,10],
                            None
                        )
                    ],
                    (
                        [
                            VarDecl(
                                Id("a"),
                                [],
                                IntLiteral(1710165)
                            ),
                            VarDecl(
                                Id("r"),
                                [],
                                IntLiteral(3)
                            )
                        ],
                        [
                            Assign(
                                Id("b"),
                                BinaryOp(
                                    "*",
                                    UnaryOp(
                                        "-",
                                        BinaryOp(
                                            "+",
                                            Id("a"),
                                            Id("r")
                                        )
                                    ),
                                    UnaryOp(
                                        "-",
                                        Id("c")
                                    )
                                )
                            )
                        ]
                    )
                )
            ]
        )
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,432))
    
    def test_33(self):
        input = Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            CallStmt(
                                Id("foo"),
                                []
                            )
                        ]
                    )
                )
            ]
        )
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,433))
    
    def test_34(self):
        input = Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [
                            VarDecl(Id("id"),[2,3],None),
                            VarDecl(Id("id"),[2,8],None)
                        ],
                        [
                            
                        ]
                    )
                )
            ]
        )
        expect = str(Redeclared(Variable(),"id"))
        self.assertTrue(TestChecker.test(input,expect,434))
    
    def test_35(self):
        input = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],None)],([],[]))])
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,435))
    
    def test_36(self):
        input = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],None)],([],[]))])
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,436))
    
    def test_37(self):
        input = Program(
                    [
                        VarDecl(Id("x"),[],None),
                        FuncDecl(Id("main"),
                                 [
                                     VarDecl(Id("x"),[],None),
                                     VarDecl(Id("y"),[5,2],None)
                                 ],
                                    (
                                        [],
                                        []
                                    )
                                 )
                    ])
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,437))
    
    def test_38(self):
        input = Program(
                    [
                        VarDecl(Id("x"),[],None),
                        FuncDecl(Id("main"),
                                 [
                                     VarDecl(Id("x"),[],None),
                                     VarDecl(Id("y"),[5,2],None)
                                 ],
                                    (
                                        [
                                            VarDecl(Id("r"),[],FloatLiteral(3.14)),
                                            VarDecl(Id("e"),[],FloatLiteral(2.7e1))
                                        ],
                                        []
                                    )
                                 )
                    ])
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,438))
    
    def test_39(self):
        input = Program(
                    [
                        VarDecl(Id("x"),[],None),
                        FuncDecl(Id("main"),
                                 [
                                     VarDecl(Id("x"),[],None),
                                     VarDecl(Id("y"),[5,2],None)
                                 ],
                                    (
                                        [
                                            VarDecl(Id("r"),[],FloatLiteral(3.14)),
                                            VarDecl(Id("e"),[],FloatLiteral(2.7e1))
                                        ],
                                        [
                                            Assign
                                            (
                                                Id("a"),
                                                Id("x")
                                            )
                                        ]
                                    )
                                 )
                    ])
        expect = str(Undeclared(Identifier(),"a"))
        self.assertTrue(TestChecker.test(input,expect,439))
        
    def test_40(self):
        # FuncDecl(Id("main"),[],([],[]))
        input = Program([FuncDecl(Id("main"),[],([],[CallStmt(Id("foo"),[])]))])
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_41(self):
        input = Program([
                VarDecl(
                    Id("x"),
                    [],
                    None
                )
            ])
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_42(self):
        input = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),FuncDecl(Id("main"),[],([],[]))])
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_43(self):
        input = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[1],None),FuncDecl(Id("main"),[],([],[]))])
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_44(self):
        input = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[1],IntLiteral(1)),FuncDecl(Id("main"),[],([],[]))])
        expect = str(TypeCannotBeInferred(VarDecl(Id("y"),[1],IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_45(self):
        input = Program([VarDecl(Id("x"),[],BooleanLiteral(True)),FuncDecl(Id("main"),[],([],[]))])
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_46(self):
        input = Program([VarDecl(Id("x"),[],BooleanLiteral(False)),FuncDecl(Id("main"),[],([],[]))])
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,446))
    
    def test_47(self):
        input = Program([VarDecl(Id("x"),[],StringLiteral("True")),FuncDecl(Id("main"),[],([],[]))])
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,447))
    
    def test_48(self):
        input = Program([VarDecl(Id("x"),[],FloatLiteral(1.2)),FuncDecl(Id("main"),[],([],[]))])
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,448))
    
    def test_49(self):
        input = Program(
            [
                VarDecl(
                    Id("x"),
                    [1],
                    FloatLiteral(1.2)
                ),
                FuncDecl(Id("main"),[],([],[]))
            ]
        )
        expect = str(TypeCannotBeInferred(VarDecl(Id("x"),[1],FloatLiteral(1.2))))
        self.assertTrue(TestChecker.test(input,expect,449))
    
    def test_50(self):
        input = Program(
            [
                VarDecl(
                    Id("x"),
                    [1,2,3],
                    None
                ),
                VarDecl(
                    Id("y"),
                    [2,2],
                    ArrayLiteral(
                        [
                            ArrayLiteral(
                                [
                                    IntLiteral(1),
                                    IntLiteral(2)
                                ]
                            ),
                            ArrayLiteral(
                                [
                                    IntLiteral(10),
                                    IntLiteral(20)
                                ]
                            )
                        ]
                    )
                ),
                FuncDecl(Id("main"),[],([],[]))
            ]
        )
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,450))
    
    def test_51(self):
        input = Program(
            [
                VarDecl(
                    Id("x"),
                    [],
                    IntLiteral(3)
                ),
                VarDecl(
                    Id("y"),
                    [],
                    IntLiteral(3)
                ),
                FuncDecl(Id("main"),[],([],[]))
            ]
        )
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,451))
    
    def test_52(self):
        input =  Program(
            [
                VarDecl(
                    Id("x"),
                    [],
                    FloatLiteral(1000.0)
                ),
                VarDecl(
                    Id("y"),
                    [5],
                    ArrayLiteral(
                        [
                            IntLiteral(2),
                            IntLiteral(4),
                            IntLiteral(100),
                            IntLiteral(24),
                            IntLiteral(9)
                        ]
                    )
                ),
                VarDecl(
                    Id("z"),
                    [],
                    FloatLiteral(2000.0)
                ),
                FuncDecl(Id("main"),[],([],[]))
            ]
        )
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,452))
    
    def test_53(self):
        input = Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            CallStmt(
                                Id("foo"),
                                []
                            )
                        ]
                    )
                )
            ]
        )
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,453))
    
    def test_54(self):
        input = Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [
                            VarDecl(Id("id"),[2,3],None),
                            VarDecl(Id("id"),[2,8],None)
                        ],
                        [
                            
                        ]
                    )
                )
            ]
        )
        expect = str(Redeclared(Variable(),"id"))
        self.assertTrue(TestChecker.test(input,expect,454))
    
    def test_55(self):
        input = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],None)],([],[]))])
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,455))
    
    def test_56(self):
        input = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],None)],([],[]))])
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,456))
    
    def test_57(self):
        input = Program(
                    [
                        VarDecl(Id("x"),[],None),
                        FuncDecl(Id("main"),
                                 [
                                     VarDecl(Id("x"),[],None),
                                     VarDecl(Id("y"),[5,2],None)
                                 ],
                                    (
                                        [],
                                        []
                                    )
                                 )
                    ])
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,457))
    
    def test_58(self):
        input = Program(
                    [
                        VarDecl(Id("x"),[],None),
                        FuncDecl(Id("main"),
                                 [
                                     VarDecl(Id("x"),[],None),
                                     VarDecl(Id("y"),[5,2],None)
                                 ],
                                    (
                                        [
                                            VarDecl(Id("r"),[],FloatLiteral(3.14)),
                                            VarDecl(Id("e"),[],FloatLiteral(2.7e1))
                                        ],
                                        []
                                    )
                                 )
                    ])
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,458))
    
    def test_59(self):
        input = Program(
                    [
                        VarDecl(Id("x"),[],None),
                        FuncDecl(Id("main"),
                                 [
                                     VarDecl(Id("x"),[],None),
                                     VarDecl(Id("y"),[5,2],None)
                                 ],
                                    (
                                        [
                                            VarDecl(Id("r"),[],FloatLiteral(3.14)),
                                            VarDecl(Id("e"),[],FloatLiteral(2.7e1))
                                        ],
                                        [
                                            Assign
                                            (
                                                Id("a"),
                                                Id("x")
                                            )
                                        ]
                                    )
                                 )
                    ])
        expect = str(Undeclared(Identifier(),"a"))
        self.assertTrue(TestChecker.test(input,expect,459))
    
    def test_60(self):
        input = Program(
                [
                    FuncDecl(Id("foo"),[],
                          (
                              [],
                              [
                                  Assign(
                                    Id("a"),
                                    IntLiteral(1)
                                  )
                              ]
                          )
                          ),
                    FuncDecl(Id("main"),[],([],[]))
                    
                ])
        expect = str(Undeclared(Identifier(),"a"))
        self.assertTrue(TestChecker.test(input,expect,460))
    
    def test_61(self):
        input = Program(
                [FuncDecl(Id("main"),[],
                          (
                              [
                                VarDecl(
                                    Id("a"),
                                    [4],
                                    None
                                )  
                                ],
                              [
                                  Assign(
                                    Id("a"),
                                    ArrayLiteral(
                                        [
                                        IntLiteral(1),
                                        IntLiteral(3),
                                        IntLiteral(5),
                                        IntLiteral(7)
                                        ]
                                    )
                                  )
                              ]
                          ))
                ]
                )
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,461))
    
    def test_62(self):
        input = Program(
                [FuncDecl(Id("main"),[],
                          (
                              [
                                  VarDecl(
                                    Id("a"),
                                    [4],
                                    None
                                )  
                               ],
                              [
                                  Assign(
                                    ArrayCell(
                                        Id("a"),
                                        [IntLiteral(2)]
                                    ),
                                    IntLiteral(5)
                                  )
                              ]
                          ))
                ]
                )
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,462))
    
    def test_63(self):
        input = Program(
                [FuncDecl(Id("main"),
                          [
                              
                              ],
                          (
                              [VarDecl(
                                    Id("a"),
                                    [],
                                    None
                                )  ],
                              [
                                  If(
                                      [
                                       (
                                        BooleanLiteral(True),
                                        [],
                                        [
                                            CallStmt(Id("main"),[])
                                        ]
                                        ),
                                        (
                                        BooleanLiteral(False),
                                        [],
                                        [
                                           
                                        ]
                                        ),
                                        (
                                        BinaryOp("<",Id("a"),IntLiteral(2)),
                                        [
                                            VarDecl(Id("x"),[],None)
                                        ],
                                        []
                                        )
                                      ],
                                      (
                                          [
                                              VarDecl(Id("x"),[],IntLiteral(3))
                                          ],
                                          [
                                              Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))
                                          ]
                                      )
                                  )
                              ]
                          ))
                ]
                )
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,463))
    
    def test_64(self):
        input = Program(
            [FuncDecl(
                Id("main"),
                [],
                (
                    [
                        VarDecl(
                                    Id("i"),
                                    [],
                                    None
                                )  ],
                    [
                        For(
                            Id("i"),
                            IntLiteral(0),
                            BinaryOp("<",
                                     Id("i"),
                                     IntLiteral(5)),
                            IntLiteral(1),
                            (
                                [],
                                [
                                    CallStmt(Id("print"),[Id("i")])
                                ]
                            )
                        )
                    ]
                )
            )
            ]
        )
        expect = str(TypeMismatchInStatement(CallStmt(Id("print"),[Id("i")])))
        self.assertTrue(TestChecker.test(input,expect,464))
    
    def test_65(self):
        input = Program([
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[
                        CallExpr(Id("read"),[IntLiteral(4)])
                        ])]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,465))
    
    def test_66(self):
        input = Program([
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,466))
    
    def test_67(self):
        input = Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [
                            VarDecl(
                                    Id("i"),
                                    [],
                                    None
                                )  
                            ],
                        [
                            While(
                                BinaryOp(
                                    ">",
                                    Id("i"),
                                    IntLiteral(10)
                                ),
                                (
                                    [],
                                    [
                                        Assign(
                                            Id("i"),
                                            BinaryOp(
                                                "-",
                                                Id("i"),
                                                IntLiteral(1)
                                            )
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,467))
    
    def test_68(self):
        input = Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [
                            VarDecl(
                                    Id("i"),
                                    [],
                                    None
                                )      
                        ],
                        [
                            While(
                                BinaryOp(
                                    "<",
                                    Id("i"),
                                    IntLiteral(10)
                                ),
                                (
                                    [
                                        VarDecl(Id("x"),[],IntLiteral(10))
                                    ],
                                    [
                                        Assign(
                                            Id("i"),
                                            BinaryOp(
                                                "+",
                                                Id("x"),
                                                IntLiteral(1)
                                            )
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,468))
    
    def test_69(self):
        input = Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [
                            VarDecl(
                                    Id("i"),
                                    [],
                                    None
                                )      
                        ],
                        [
                            Dowhile(
                                (
                                    [],
                                    [
                                        Assign(
                                            Id("i"),
                                            BinaryOp("*",Id("i"),IntLiteral(2))
                                        ),
                                        Break()
                                    ]
                                ),
                                BinaryOp("<",Id("i"),IntLiteral(10))
                            )
                        ]
                    )
                )
            ]
        )
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,469))
    
    def test_70(self):
        # FuncDecl(Id("main"),[],([],[]))
        input = Program([FuncDecl(Id("main"),[],([],[CallStmt(Id("foo"),[])]))])
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_71(self):
        input = Program([
                VarDecl(
                    Id("x"),
                    [],
                    None
                )
            ])
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_72(self):
        input = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),FuncDecl(Id("main"),[],([],[]))])
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_73(self):
        input = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[1],None),FuncDecl(Id("main"),[],([],[]))])
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_74(self):
        input = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[1],IntLiteral(1)),FuncDecl(Id("main"),[],([],[]))])
        expect = str(TypeCannotBeInferred(VarDecl(Id("y"),[1],IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_75(self):
        input = Program([VarDecl(Id("x"),[],BooleanLiteral(True)),FuncDecl(Id("main"),[],([],[]))])
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_76(self):
        input = Program([VarDecl(Id("x"),[],BooleanLiteral(False)),FuncDecl(Id("main"),[],([],[]))])
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,476))
    
    def test_77(self):
        input = Program([VarDecl(Id("x"),[],StringLiteral("True")),FuncDecl(Id("main"),[],([],[]))])
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,477))
    
    def test_78(self):
        input = Program([VarDecl(Id("x"),[],FloatLiteral(1.2)),FuncDecl(Id("main"),[],([],[]))])
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,478))
    
    def test_79(self):
        input = Program(
            [
                VarDecl(
                    Id("x"),
                    [1],
                    FloatLiteral(1.2)
                ),
                FuncDecl(Id("main"),[],([],[]))
            ]
        )
        expect = str(TypeCannotBeInferred(VarDecl(Id("x"),[1],FloatLiteral(1.2))))
        self.assertTrue(TestChecker.test(input,expect,479))
    
    def test_80(self):
        input = Program(
            [
                VarDecl(
                    Id("x"),
                    [1,2,3],
                    None
                ),
                VarDecl(
                    Id("y"),
                    [2,2],
                    ArrayLiteral(
                        [
                            ArrayLiteral(
                                [
                                    IntLiteral(1),
                                    IntLiteral(2)
                                ]
                            ),
                            ArrayLiteral(
                                [
                                    IntLiteral(10),
                                    IntLiteral(20)
                                ]
                            )
                        ]
                    )
                ),
                FuncDecl(Id("main"),[],([],[]))
            ]
        )
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,480))
    
    def test_81(self):
        input = Program(
            [
                VarDecl(
                    Id("x"),
                    [],
                    IntLiteral(3)
                ),
                VarDecl(
                    Id("y"),
                    [],
                    IntLiteral(3)
                ),
                FuncDecl(Id("main"),[],([],[]))
            ]
        )
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,481))
    
    def test_82(self):
        input =  Program(
            [
                VarDecl(
                    Id("x"),
                    [],
                    FloatLiteral(1000.0)
                ),
                VarDecl(
                    Id("y"),
                    [5],
                    ArrayLiteral(
                        [
                            IntLiteral(2),
                            IntLiteral(4),
                            IntLiteral(100),
                            IntLiteral(24),
                            IntLiteral(9)
                        ]
                    )
                ),
                VarDecl(
                    Id("z"),
                    [],
                    FloatLiteral(2000.0)
                ),
                FuncDecl(Id("main"),[],([],[]))
            ]
        )
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,482))
    
    def test_83(self):
        input = Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            CallStmt(
                                Id("foo"),
                                []
                            )
                        ]
                    )
                )
            ]
        )
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,483))
    
    def test_84(self):
        input = Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [
                            VarDecl(Id("id"),[2,3],None),
                            VarDecl(Id("id"),[2,8],None)
                        ],
                        [
                            
                        ]
                    )
                )
            ]
        )
        expect = str(Redeclared(Variable(),"id"))
        self.assertTrue(TestChecker.test(input,expect,484))
    
    def test_85(self):
        input = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],None)],([],[]))])
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,485))
    
    def test_86(self):
        input = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],None)],([],[]))])
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,486))
    
    def test_87(self):
        input = Program(
                    [
                        VarDecl(Id("x"),[],None),
                        FuncDecl(Id("main"),
                                 [
                                     VarDecl(Id("x"),[],None),
                                     VarDecl(Id("y"),[5,2],None)
                                 ],
                                    (
                                        [],
                                        []
                                    )
                                 )
                    ])
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,487))
    
    def test_88(self):
        input = Program(
                    [
                        VarDecl(Id("x"),[],None),
                        FuncDecl(Id("main"),
                                 [
                                     VarDecl(Id("x"),[],None),
                                     VarDecl(Id("y"),[5,2],None)
                                 ],
                                    (
                                        [
                                            VarDecl(Id("r"),[],FloatLiteral(3.14)),
                                            VarDecl(Id("e"),[],FloatLiteral(2.7e1))
                                        ],
                                        []
                                    )
                                 )
                    ])
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,488))
    
    def test_89(self):
        input = Program(
                    [
                        VarDecl(Id("x"),[],None),
                        FuncDecl(Id("main"),
                                 [
                                     VarDecl(Id("x"),[],None),
                                     VarDecl(Id("y"),[5,2],None)
                                 ],
                                    (
                                        [
                                            VarDecl(Id("r"),[],FloatLiteral(3.14)),
                                            VarDecl(Id("e"),[],FloatLiteral(2.7e1))
                                        ],
                                        [
                                            Assign
                                            (
                                                Id("a"),
                                                Id("x")
                                            )
                                        ]
                                    )
                                 )
                    ])
        expect = str(Undeclared(Identifier(),"a"))
        self.assertTrue(TestChecker.test(input,expect,489))
    
    def test_90(self):
        input = Program(
                [
                    FuncDecl(Id("foo"),[],
                          (
                              [],
                              [
                                  Assign(
                                    Id("a"),
                                    IntLiteral(1)
                                  )
                              ]
                          )
                          ),
                    FuncDecl(Id("main"),[],([],[]))
                    
                ])
        expect = str(Undeclared(Identifier(),"a"))
        self.assertTrue(TestChecker.test(input,expect,490))
    
    def test_91(self):
        input = Program(
                [FuncDecl(Id("main"),[],
                          (
                              [
                                VarDecl(
                                    Id("a"),
                                    [4],
                                    None
                                )  
                                ],
                              [
                                  Assign(
                                    Id("a"),
                                    ArrayLiteral(
                                        [
                                        IntLiteral(1),
                                        IntLiteral(3),
                                        IntLiteral(5),
                                        IntLiteral(7)
                                        ]
                                    )
                                  )
                              ]
                          ))
                ]
                )
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,491))
    
    def test_92(self):
        input = Program(
                [FuncDecl(Id("main"),[],
                          (
                              [
                                  VarDecl(
                                    Id("a"),
                                    [4],
                                    None
                                )  
                               ],
                              [
                                  Assign(
                                    ArrayCell(
                                        Id("a"),
                                        [IntLiteral(2)]
                                    ),
                                    IntLiteral(5)
                                  )
                              ]
                          ))
                ]
                )
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,492))
    
    def test_93(self):
        input = Program(
                [FuncDecl(Id("main"),
                          [
                              
                              ],
                          (
                              [VarDecl(
                                    Id("a"),
                                    [],
                                    None
                                )  ],
                              [
                                  If(
                                      [
                                       (
                                        BooleanLiteral(True),
                                        [],
                                        [
                                            CallStmt(Id("main"),[])
                                        ]
                                        ),
                                        (
                                        BooleanLiteral(False),
                                        [],
                                        [
                                           
                                        ]
                                        ),
                                        (
                                        BinaryOp("<",Id("a"),IntLiteral(2)),
                                        [
                                            VarDecl(Id("x"),[],None)
                                        ],
                                        []
                                        )
                                      ],
                                      (
                                          [
                                              VarDecl(Id("x"),[],IntLiteral(3))
                                          ],
                                          [
                                              Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))
                                          ]
                                      )
                                  )
                              ]
                          ))
                ]
                )
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,493))
    
    def test_94(self):
        input = Program(
            [FuncDecl(
                Id("main"),
                [],
                (
                    [
                        VarDecl(
                                    Id("i"),
                                    [],
                                    None
                                )  ],
                    [
                        For(
                            Id("i"),
                            IntLiteral(0),
                            BinaryOp("<",
                                     Id("i"),
                                     IntLiteral(5)),
                            IntLiteral(1),
                            (
                                [],
                                [
                                    CallStmt(Id("print"),[Id("i")])
                                ]
                            )
                        )
                    ]
                )
            )
            ]
        )
        expect = str(TypeMismatchInStatement(CallStmt(Id("print"),[Id("i")])))
        self.assertTrue(TestChecker.test(input,expect,494))
    
    def test_95(self):
        input = Program([
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[
                        CallExpr(Id("read"),[IntLiteral(4)])
                        ])]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,495))
    
    def test_96(self):
        input = Program([
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,496))
    
    def test_97(self):
        input = Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [
                            VarDecl(
                                    Id("i"),
                                    [],
                                    None
                                )  
                            ],
                        [
                            While(
                                BinaryOp(
                                    ">",
                                    Id("i"),
                                    IntLiteral(10)
                                ),
                                (
                                    [],
                                    [
                                        Assign(
                                            Id("i"),
                                            BinaryOp(
                                                "-",
                                                Id("i"),
                                                IntLiteral(1)
                                            )
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,497))
    
    def test_98(self):
        input = Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [
                            VarDecl(
                                    Id("i"),
                                    [],
                                    None
                                )      
                        ],
                        [
                            While(
                                BinaryOp(
                                    "<",
                                    Id("i"),
                                    IntLiteral(10)
                                ),
                                (
                                    [
                                        VarDecl(Id("x"),[],IntLiteral(10))
                                    ],
                                    [
                                        Assign(
                                            Id("i"),
                                            BinaryOp(
                                                "+",
                                                Id("x"),
                                                IntLiteral(1)
                                            )
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,498))
    
    def test_99(self):
        input = Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [
                            VarDecl(
                                    Id("i"),
                                    [],
                                    None
                                )      
                        ],
                        [
                            Dowhile(
                                (
                                    [],
                                    [
                                        Assign(
                                            Id("i"),
                                            BinaryOp("*",Id("i"),IntLiteral(2))
                                        ),
                                        Break()
                                    ]
                                ),
                                BinaryOp("<",Id("i"),IntLiteral(10))
                            )
                        ]
                    )
                )
            ]
        )
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,499))