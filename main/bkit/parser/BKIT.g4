/**
    Student ID 1710165;
*/
grammar BKIT;


@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
	language=Python3;
}

program: main+ EOF;

main: var_declare | func_declare;
var_declare: var_list;// var_list?;
var_list: var_normal SEMI;
//var_list: VAR COLON var_vt SEMI BODY COLON var_single+ ENDBODY DOT;
//var_list: body_declare;//BODY COLON stmt* ENDBODY DOT;
var_normal: VAR COLON var_normal_list (COMMA var_normal_list)*;
var_normal_list: scalar_var_int (EQ (array_lit | all_lit ))? ;
//var_vt: scalar_var (COMMA scalar_var)*;
//var_vp: array_cell
//      | scalar_var
//      | exp;
//array_cell: LCB (var_vp (COMMA var_vp)*)? RCB;

array_lit_cell: array_lit
              | all_lit;
array_lit: LCB (array_lit_cell (COMMA array_lit_cell)*)? RCB;
/**
 * 6 Statements and Control Flow
 */
//body: stmt_notfunc | stmt_spe;
body: var_declare* stmt*;
stmt: stmt_notfunc | stmt_spe;
//stmt_decl: var_declare | func_declare;
stmt_notfunc: if_stmt
            | for_stmt
            | while_stmt
            | doWhile_stmt
            ;
stmt_spe: assign_stmt SEMI
        | break_stmt
        | continue_stmt
        | return_stmt
        | call_stmt;
// body declare
body_declare: BODY COLON body ENDBODY DOT;

//assign statement
assign_stmt: ID op_index* EQ exp;
//assign_part: exp;
//assign_part: (scalar_var | ((func_call | STRINGLIT | array_cell)) index_var*);
// function declare
func_declare: FUNCTION COLON ID parameter_func? body_declare;

// parameter declare
parameter_func: PARAMETER COLON scalar_var_int (COMMA scalar_var_int)*;

// if-elseif-else statement
if_stmt: IF exp THEN body elseif_stmt* else_stmt? ENDIF DOT;
elseif_stmt: ELSEIF exp THEN body;
else_stmt: ELSE body;

// for statement
for_stmt: FOR LP ID EQ exp COMMA conditionExpr COMMA updateExpr RP DO body ENDFOR DOT;

//scalar-variable
scalar_var: ID index_var*;
index_var: LSB exp RSB;

//scalar-var-assign
scalar_var_int: ID index_var_int*;
index_var_int: LSB INTLIT RSB;

//condition expression
conditionExpr: exp;

//update expression
updateExpr: exp;

// while statement
while_stmt: WHILE exp DO body ENDWHILE DOT;

// Do-while statement
doWhile_stmt: DO body WHILE exp ENDDO DOT;

//Break statement
break_stmt: BREAK SEMI;

//Continue statement
continue_stmt: CONTINUE SEMI;

//Return statement
return_stmt: RETURN exp? SEMI;

//Call statment
//func_call: ID LP ((exp | var_vp) (COMMA (exp | var_vp))*)? RP;
func_call: ID LP func_call_cell? RP;
func_call_cell: exp (COMMA exp)*;
// func_call_cell: var_vp (COMMA var_vp)*;
call_stmt: func_call SEMI;

//expression
exp: exp1 RELATIONAL exp1 | exp1 ;
exp1: exp1 ( AND | OR ) exp2 | exp2;
exp2: exp2 (ADD | SUB | ADDDOT | SUBDOT) exp3 | exp3;
exp3: exp3 ( MUL | DIV | MOD | MULDOT | DIVDOT) exp4 | exp4;
exp4: (NOT) exp4 | exp5;
exp5: (SUB | SUBDOT) exp5 | exp6;
exp6: exp6 op_index | operands;
op_index: LSB exp RSB;
operands: LP exp RP
        | func_call
        | all_lit
        | LCB all_lit (COMMA all_lit)* RCB
        | ID
        ;

//operand: all_literal | func_call_exp | var_id | LP expression RP ;
bool_lit: TRUE | FALSE;
int_lit: INTLIT;
float_lit: FLOATLIT;
string_lit: STRINGLIT;
all_lit: int_lit | float_lit | string_lit | bool_lit;

RELATIONAL: RELATIONAL_FLOAT | RELATIONAL_INT;
RELATIONAL_INT:  EQINT | NEQINT | GTINT | LTINT | GTEINT | LTEINT ;
RELATIONAL_FLOAT: EQINT | NEQF | GTF | LTF | GTEF | LTEF ;

fragment DIGIT: [0-9];
fragment DEC:   '0' | [1-9] DIGIT*;
fragment HEX:   [0][xX][1-9A-F][0-9A-F]*;
fragment OCT:   [0][oO][1-7][0-7]*;
fragment EXP:   [eE];
fragment EXPONENT: EXP [+-]? DIGIT+;

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
BCMT: ('**' .*? '**') -> skip; // Block comment

// 3.3.2 Keywords
//keywords: BODY | BREAK | CONTINUE | DO | ELSE | ELSEIF | ENDBODY
//        | ENDIF | ENDFOR | ENDWHILE | FOR | FUNCTION | IF | PARAMETER
//        | RETURN | THEN | VAR | WHILE | TRUE | FALSE | ENDDO;

//Method
FUNCTION: 'Function';// 'F' U N C T I O N;
PARAMETER: 'Parameter';//'P' A R A M E T E R;
//Scope
BODY: 'Body';//'B' O D Y;
ENDBODY: 'EndBody';//'E' N D B O D Y;
//Flow Statement
IF: 'If';//'I' F;
THEN: 'Then';//'T' H E N;
ELSEIF: 'ElseIf';//'E' L S E I F;
ELSE: 'Else';//'E' L S E;
ENDIF: 'EndIf';//'E' N D I F;
//Loop Statement
FOR: 'For';//'F' O R;
ENDFOR: 'EndFor';//'E' N D F O R;
DO: 'Do';//'D' O;
ENDDO: 'EndDo';//'E' N D D O;
WHILE: 'While';//'W' H I L E;
ENDWHILE: 'EndWhile';//'E' N D W H I L E;
//Stop Statement
RETURN: 'Return';//'R' E T U R N;
BREAK: 'Break';//'B' R E A K;
CONTINUE: 'Continue';//'C' O N T I N U E;
//Value
TRUE: 'True';//'T' R U E;
FALSE: 'False';//'F' A L S E;
//Others
VAR: 'Var';//'V' A R;

/**
// 3.3.3 Operator
*/

//OPERATORRRR: BOOL_OPERATOR | ARITHMETIC_OPERATOR | RELATIONAL_OPERATOR;

// Boolean operators
//BOOL_OPERATOR: NOT | AND | OR;

NOT: '!';
AND: '&&';
OR: '||';

// Arithmetic operators
//ARITHMETIC_OPERATOR: ADD | SUB | MUL | DIV | MOD | ADDDOT | SUBDOT | MULDOT | DIVDOT;
// Integer

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '\\';
MOD: '%';

// Float

ADDDOT: ADD DOT;
SUBDOT: SUB DOT;
MULDOT: MUL DOT;
DIVDOT: DIV DOT;

// Relational operators
//RELATIONAL_OPERATOR: RELATIONAL_OPERATOR_INT | RELATIONAL_OPERATOR_FLOAT;

// Integer
//RELATIONAL_OPERATOR_INT: EQINT | NEQINT | LTINT | LTEINT | GTINT | GTEINT;
EQ: '=';

EQINT: EQ EQ;
NEQINT: NOT EQ;
LTINT : '<' ;
LTEINT: LTINT EQ;
GTINT : '>' ;
GTEINT: GTINT EQ;

// Float
//RELATIONAL_OPERATOR_FLOAT: NEQF | LTF | LTEF | GTF| GTEF;

NEQF: EQ '/' EQ;
LTF: LTINT DOT;
LTEF: LTINT EQ DOT;
GTF: GTINT DOT;
GTEF: GTINT EQ DOT;

// 3.3.4 SEPARATOR:  '('|')'|'['|']'|':'|'.'|','|';'|'{'|'}';
LP: '('; // Left Parenthesis
RP: ')'; // Right Parenthesis
LCB: '{'; // Left Curly Bracket
RCB: '}'; // Right Curly Bracket
LSB: '['; // Left Square Bracket
RSB: ']'; // Right Square Bracket
SEMI: ';' ;
COLON: ':' ;
COMMA: ',';
DOT: '.';

// 3.3.5 Literals

// Integer
INTLIT: DEC | HEX | OCT;

// FLoat
FLOATLIT: DEC DOT (EXPONENT | DIGIT+ EXPONENT?)?
        | DEC EXPONENT
        ;

// 3.3.1 Identifiers
ID: [a-z][_a-zA-Z0-9]* ;


ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL
	{
		value = str(self.text)
		raise IllegalEscape(value[1:])
	}
	;
UNCLOSE_STRING: '"' STR_CHAR* ([\n\f\r\b\t\\] | '\'"' | EOF)
	{
		value = str(self.text)
		possible = ['\b', '\t', '\n', '\f', '\r', '\'"', '\\']
		if value[-1] in possible:
			raise UncloseString(value[1:-1])
		else:
			raise UncloseString(value[1:])
	}
	;
UNTERMINATED_COMMENT: '**' UNT_CMT* '*'?
    {
        raise UnterminatedComment()
    };

// String
STRINGLIT: '"' STR_CHAR* '"'
    {
		value = str(self.text)
		self.text = value[1:-1]
	};

ERROR_CHAR: .
	{
		raise ErrorToken(self.text)
	}
	;

fragment STR_CHAR: ~[\b\f\r\n\t'"\\] | ESC_SEQ ;
fragment ESC_SEQ: '\\' [bfrnt'\\] | '\'"' ;
fragment ESC_ILLEGAL: '\\' ~[bfrnt'\\] | '\'' | '\'' ~["];
fragment UNT_CMT: ~[*] ;
//grammar BKIT;
//
//@lexer::header {
//from lexererr import *
//}
//
//@lexer::members {
//def emit(self):
//    tk = self.type
//    result = super().emit()
//    if tk == self.UNCLOSE_STRING:
//        raise UncloseString(result.text)
//    elif tk == self.ILLEGAL_ESCAPE:
//        raise IllegalEscape(result.text)
//    elif tk == self.ERROR_CHAR:
//        raise ErrorToken(result.text)
//    elif tk == self.UNTERMINATED_COMMENT:
//        raise UnterminatedComment()
//    else:
//        return result;
//}
//
//options{
//	language=Python3;
//}
//
//program  : VAR COLON ID SEMI EOF ;
//
//ID: [a-z]+ ;
//
//SEMI: ';' ;
//
//COLON: ':' ;
//
//VAR: 'Var' ;
//
//WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
//
//
//ERROR_CHAR: .;
//UNCLOSE_STRING: .;
//ILLEGAL_ESCAPE: .;
//UNTERMINATED_COMMENT: .;
