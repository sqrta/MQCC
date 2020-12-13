import ply.yacc as yacc
from preLex import tokens
from adt import qubit

text=[]
index=0
# unitList
def p_unitList_unit(p):
    'unitList : gateDeclare unitList'
    p[0] = [p[1]] + p[2]


def p_unitList(p):
    ''' unitList : Block '''
    global text
    p[0]=[('block',''.join(text[index:]))]
    text=''


# gateDeclare
def p_gateDeclare(p):
    'gateDeclare : GATE ID LPAREN VarList RPAREN LBRACE Block RBRACE '
    global text,index
    p[0]='#define ' + p[2] + '(' +','.join(p[4])+ ') ' + text[index]
    index+=1


# VarList
def p_VarList(p):
    'VarList : vardef Comma VarList'
    p[0] = [p[1]] + p[3]


def p_VarList_var(p):
    'VarList : vardef'
    p[0] = [p[1]]


# vardef
def p_vardef_ID(p):
    'vardef : ID'
    p[0] = p[1]


#Block
def p_Block(p):
    'Block : error Block'
    p[0] = p[1].value + p[2]
    #print(p[1].value)

def p_Block_empty(p):
    'Block : empty'
    p[0]='end'

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        tmp=p.value
        while True:
            tok=parser.token()
            if not tok or tok.type == 'RBRACE':
                break
            tmp += tok.value
        parser.errok()
        text.append(tmp)
        print('text:\t',text)
        return tok 
    
parser = yacc.yacc()
with open('pretest', 'r') as f:
    s = f.read()
    print(s)
    result = parser.parse(s)
    for i in result:
        print(i)
