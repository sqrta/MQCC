import ply.yacc as yacc
from qasmlex import tokens

def p_S(p):
    '''S : Head Declarations Operations
        | Head Declarations'''
    p[0] = '\n'.join(p[2:])

def p_Head(p):
    '''Head : QASM Float SemiColon Include DQuotation ID DeciPoint ID DQuotation SemiColon'''
    p[0] = p[5]

def p_Operations_Op(p):
    '''
    Operations : Op
    '''
    p[0] = p[1]+'\n'

def p_Operations_list(p):
    '    Operations : Operations Op'
    p[0] = ''.join(p[1:])

def p_Op1(p):
    '''Op : ID ArgList SemiColon '''
    p[0] = p[1] +'(' + p[2] + ');'

def p_Op2(p):
    'Op : ID LParen ExpList RParen ArgList SemiColon'
    p[0] = p[1]+'(' + p[3] +',' + p[5] + ');'

def p_Arglist(p):
    '''ArgList : Arg
                | ArgList Comma Arg'''
    p[0] = ''.join(p[1:])

def p_Arg(p):
    '''Arg : ID
            | ID LBracket CExp RBracket'''
    p[0] = ''.join(p[1:])

def p_ExpList(p):
    '''ExpList : CExp
                | ExpList Comma CExp'''
    p[0] = ''.join(p[1:])

def p_Declarations_Decl(p):
    '''Declarations : Decl 
                    | Declarations Decl'''
    p[0] = '\n'.join(p[1:])
    # except:
    #     print('sd', p[1:t])
    # if len(p)>2:
    #     p[0] = p[1] +p[2]
    # else:
    #     p[0] = p[1]


def p_Decl_Reg(p):
    '''Decl : RegDecl SemiColon'''
    p[0] = p[1]+p[2]

def p_RegDecl(p):
    '''RegDecl : QREG ArrayDecls 
                | CREG ArrayDecls '''
    p[0] = p[1] + ' ' + p[2]


def p_ArrayDecls(p):
    'ArrayDecls : ID LBracket Integer RBracket'
    p[0] = p[1] + p[2] + p[3] + p[4]

def p_ArrayDecls_decl(p):
    'ArrayDecls : ArrayDecl'
    p[0] = [p[1]]

def p_ArrayDecl(p):
    'ArrayDecl : ID LBracket Int RBracket'
    p[0] = p[1]  + '[' + str(p[4]) + '];'

def p_Int(p):
    'Int : Integer'
    p[0] = int(p[1])

def p_IntSet(p):
    '''IntSet : IntSet Comma Int'''
    p[0] = p[1]+[p[3]]


def p_IntSet_Int(p):
    'IntSet : Int'
    p[0] = [p[1]]

def p_CExp(p):
    '''CExp : Integer
            | Float
            | CExp Plus CExp
            | CExp Minus CExp
            | CExp Times CExp
            | CExp Divide CExp
            | CExp Mod CExp
            | Minus CExp
            | LParen CExp RParen'''
    p[0] = ''.join(p[1:])

def p_empty(p):
    'Empty :'
    pass

def p_error(p):
    tmp = p
    print(p)
    msg = ''
    count=0
    while tmp:
        msg+=str(tmp.value)
        tmp = parser.token()
        if tmp.type == 'SemiColon':
            count+=1
            if count>3:
                break
    print('Syntax error! Before the statement: "' + msg + '"')
    exit(0)
parser = yacc.yacc(start="S")
path = "test"
with open(path,'r') as f:
    s = f.read()
    result = parser.parse(s, tracking=True)
    print(result)