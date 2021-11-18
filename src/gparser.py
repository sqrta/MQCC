import ply.yacc as yacc
from lex import tokens
from gadt import generalWrap, additive, Var, Register
from attrExp import Depth, crossTalk, AQV, Noise
import copy
from attrExp import MQCC
from tool import z3solve, lchoValue
import collections

import os, sys
curdir = os.path.dirname(os.path.realpath(__file__))
parentDir = os.path.dirname(curdir)
sys.path.append(parentDir)    
from Attr import ObjectSet

#ObjectSet = {'Depth': (Depth, '<=4'), 'cross': (crossTalk, '<1'), 'Noise': (Noise, 'min', 'add')}

passMode = 'exp'
attrMode = 'general'
state_stack = []
lchoDict = {}
fchoDecl = {}
fchoDict = {}
fchoValue = {}

anonymous = '__c'
anonyCount = 0
attrType = None

precedence = (
    ('left', 'Plus', 'Minus'),
    ('left', 'Times', 'Divide'),
)

def Error(line, msg=None):
    print('Error in ' + str(line)+' : ' + msg)
    exit(0)

# Each p_ fucntion is a production rule

def p_S(p):
    '''S : Declarations Operations'''
    p[0] = (p[1], p[2])


def p_Declarations_Decl(p):
    '''Declarations : Decl
                    | Declarations Decl'''
    if (len(p) == 2):
        p[0] = p[1]
    elif (len(p) == 3):
        p[0] = p[1] + p[2]


def p_Decl_Reg(p):
    '''Decl : RegDecl SemiColon'''
    p[0] = p[1]

def p_Decl_Var(p):
    'Decl : ConDecl SemiColon'
    p[0] = []


def p_RegDecl(p):
    '''RegDecl : QREG ArrayDecls 
                | CREG ArrayDecls '''
    p[0] = [p[1] + ' ' + ','.join(p[2])]

def p_ArrayDecls(p):
    'ArrayDecls : ArrayDecls Comma ArrayDecl'
    p[0] = p[1] + [p[3]]

def p_ArrayDecls_decl(p):
    'ArrayDecls : ArrayDecl'
    p[0] = [p[1]]

def p_ArrayDecl(p):
    'ArrayDecl : ID LBracket Int RBracket'
    p[0] = p[1]  + '[' + str(p[4]) + '];'

def p_Condecl_free(p):
    'ConDecl : FCHO ID Assign IntRange'
    
    fchoDecl[p[2]] = p[4]
    p[0] = [('fcon', p[2], p[4])]

def p_Condecls_free(p):
    'ConDecl : FCHO IDList Assign IntRange'
    args = []
    for i in p[2]:
        args.append(('fcon', i, p[4]))
        fchoDecl[i] = p[4]
    p[0] = args
   

def p_IntRange(p):
    'IntRange : LBrace IntSet RBrace'
    p[0] = p[2]

def p_IntRange_interval(p):
    'IntRange : LBracket Int Comma Int RBracket'
    p[0] = list(range(p[2], p[4]+1))

def p_IDList_ID(p):
    'IDList : ID'
    p[0] = [p[1]]

def p_IDList(p):
    'IDList : IDList Comma ID'
    p[1].append(p[3])
    p[0] = p[1]


def p_Condecl_limit(p):
    'ConDecl : LCHO ID Assign CExp'

    lchoDict[p[2]] = p[4]
    p[0] = [('lcon', p[2], p[4])]



def p_IntSet(p):
    '''IntSet : IntSet Comma Int'''
    p[0] = p[1]+[p[3]]


def p_IntSet_Int(p):
    'IntSet : Int'
    p[0] = [p[1]]

def p_CExp(p):
    '''CExp : Integer
            | CExp Plus CExp
            | CExp Minus CExp
            | CExp Times CExp
            | CExp Divide CExp
            | CExp Mod CExp
            | Minus CExp
            | LParen CExp RParen'''
    p[0] = ''.join(p[1:])

'''
'''
def p_CExp_ID(p):
    'CExp : ID'
    if p[1] in fchoDecl.keys():
        p[0] = p[1]
    else:
        Error(p.lineno(1), 'Variable ' + p[1] +' is undefined')
# ExpList


def p_ExpList_list(p):
    'ExpList : ExpList Comma Exp'
    p[0] = p[1] + [p[3]]


def p_ExpList_Exp(p):
    'ExpList : Exp'
    p[0] = [p[1]]


# ArgList
def p_ArgList(p):
    'ArgList : ArgList Comma Arg'
    p[0] = p[1] + [p[3]]


def p_ArgList_var(p):
    'ArgList : Arg'
    p[0] = [p[1]]


# Arg
def p_Arg_ID(p):
    'Arg : ID'
    p[0] = Var(p[1], 'fcho')


def p_Arg_ID_array(p):
    'Arg : ID LBracket Exp RBracket'
    p[0] = Register(p[1], p[3])


def p_Exp_Plus(p):
    'Exp : Exp Plus Exp'
    p[0] = p[1] + p[3]


def p_Exp_Minus_two(p):
    'Exp : Exp Minus Exp'
    p[0] = p[1] - p[3]

def p_Exp_Minus(p):
    'Exp : Minus Exp'
    p[0] = - p[2]


def p_Exp_Exp(p):
    'Exp : Int'
    p[0] = p[1]

def p_Exp_Float(p):
    'Exp : Float'
    p[0] = float(p[1])

def p_Exp_Times(p):
    'Exp : Exp Times Exp'
    p[0] = p[1] * p[3]


def p_Exp_div(p):
    'Exp : Exp Divide Exp'
    p[0] = p[1] / p[3]


def p_factor_expr(p):
    'Exp : LParen Exp RParen'
    p[0] = p[2]

'''
def p_empty(p):
    'empty :'
    pass
'''

def p_operations(p):
    'Operations : SKIP Program'
    p[0] = state_stack[-1]

def p_SKIP(p):
    'SKIP : '
    #
    if attrMode == 'add':
        tmp = additive(attrType)
    else:
        tmp = generalWrap(attrType)
    tmp.empty()
    state_stack.append(tmp)
    global anonyCount
    anonyCount = 0

def p_program(p):
    'Program : Unit'
    pass

def p_program_op(p):
    'Program : Program Unit'
    pass

def p_Unit_empty(p):
    'Unit : SemiColon'
    pass

def p_unit_op(p):
    'Unit : ID LParen ArgList RParen SemiColon'
    #print(state_stack[-1])
    for item in p[3]:
        if not isinstance(item, Register):
            Error(p.lineno(1), "Operation on not register type")
    state_stack[-1].op(p[1],p[3])

def p_unit_op_exp(p):
    'Unit : ID LParen ExpList Comma ArgList RParen SemiColon'
    #print(state_stack[-1])
    for item in p[5]:
        if not isinstance(item, Register):
            Error(p.lineno(1), "Operation on not register type")
    state_stack[-1].op(p[1],p[5],p[3])
    
def p_unit_case(p):
    'Unit : CASE LParen Arg rscope RParen LBrace BranchList RBrace'
    state_stack[-1].case(p[7],p[3])

def p_rscope(p):
    'rscope : '
    pass
    #state_stack[-1].op('barrier', [p[-1]])

def p_carg_arg(p):
    'CArg : Arg'
    p[0] = p[1]

def p_carg_range(p):
    'CArg : IntRange'
    global anonyCount
    name = anonymous + str(anonyCount)
    anonyCount += 1
    fchoDecl[name] = p[1]
    p[0] = Var(name, 'fcho')

def p_unit_choice(p):
    'Unit : CHOICE LParen CArg RParen LBrace CBranchList RBrace'
    varName = p[3].varName()
    if passMode == 'backend':
        if varName in lchoDict.keys():
            fixValue = lchoValue(fchoValue, lchoDict[varName])
        else:
            fixValue = fchoValue[varName]
        defaultTerm = None
        for item in p[6]:
            if item[0]=='default':
                defaultTerm = item[1]

            elif item[0]==fixValue:
                state_stack[-1] = item[1]
                defaultTerm=None
                break
        if defaultTerm:
            state_stack[-1] = defaultTerm
    else:
        if varName in lchoDict.keys():
            var = Var(lchoDict[varName],'lcho')
            for item in p[6]:
                if item[0]=='default':
                    Error(p.lineno(1), 'Default in limit choice statement')
            group = p[6]
        else:
            var = p[3]
            fchoDict[varName] = fchoDecl[varName]
            varRange = set(fchoDict[varName])
            group = []
            defaultTerm = None
            for item in p[6]:
                num = item[0]
                if num!='default':
                    try:
                        varRange.remove(num)
                    except KeyError:
                        Error(p.lineno(3), 'Range error: ' + str(num) + ' not in ' + varName + '\'s range')
                    group.append(item)
                else:
                    defaultTerm = item[1]
            if defaultTerm:
                for label in varRange:
                    group.append((label, defaultTerm))
        state_stack[-1].choice(var, group)


def p_BranchList(p):
    'BranchList : BranchList scope Branch'
    p[0] = p[1] + [p[3]]

def p_scope(p):
    'scope : '
    if passMode == 'backend':
        tmp = additive(attrType)
        tmp.empty()
        state_stack.append(tmp)
    else:        
        state_stack.append(copy.deepcopy(state_stack[-1]))

def p_CBranchList_Branch(p):
    'CBranchList : cscope Branch'
    p[0] = [p[2]]

def p_CBranchList(p):
    'CBranchList : CBranchList cscope Branch'
    p[0] = p[1] + [p[3]]

def p_cscope(p):
    'cscope : '
    if attrMode == 'add':
        tmp = additive(attrType)
        tmp.empty()
        state_stack.append(tmp)
    else:
        state_stack.append(copy.deepcopy(state_stack[-1]))

def p_BranchList_Branch(p):
    'BranchList : scope Branch'
    p[0] = [p[2]]

def p_Int(p):
    'Int : Integer'
    p[0] = int(p[1])

def p_Branch(p):
    'Branch : Int Colon Program'
    p[0] = (p[1], state_stack.pop())

def p_Branch_pass(p):
    'Branch : Int Colon PASS'
    p[0] = (p[1], state_stack.pop())

def p_Branch_default(p):
    'Branch : DEFAULT Colon PASS'
    p[0] = ('default', state_stack.pop())

def p_Branch_default_pass(p):
    'Branch : DEFAULT Colon Program'
    p[0] = ('default', state_stack.pop())

def p_error(p):
    tmp = p
    
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

if __name__ == '__main__':
    parser = yacc.yacc()
    path = sys.argv[1]
    z3SolveBool = bool(sys.argv[2]=="True")
    exampleID = sys.argv[3]
    if exampleID!='0':
        if exampleID == '10':
            ObjectSet = {'Depth': (Depth, 'min'), 'crosstalk': (crossTalk, '<1')}
        elif exampleID == '1':
            ObjectSet = {'Depth': (Depth, 'min'), 'Noise': (Noise, '<0.15', 'add')}
        elif exampleID == '2':
            ObjectSet = {'crosstalk': (crossTalk, 'min'), 'Depth' : (Depth, '<12')}
        elif exampleID == '3':
            ObjectSet = {'AQV': (AQV, 'min')}
    
    with open(path, 'r') as f:
        s = f.read()
        # print(s)
        import time
        print('parse start')
        start=time.time()
        exps = []
        name = []
        attrReq = []
        minAttr = 0
        goalName = None
        # generate cost expressions
        for key, value in ObjectSet.items():
            name.append(key)
            attrType = value[0]
            attrReq.append(value[1])
            if value[1] == 'min' or value[1] == 'max':
                goalName = key
            if len(value)>=3:
                attrMode = value[2]
            else:
                attrMode = 'general'
            print('Generating expression for "'+key + '"')
            result = parser.parse(s, tracking=True)
            result[1].validate()
            exps.append(result[1])
        print('parse end. Expressions have been written into file "Expressions"')

        #print(result[0])
        with open('../Expressions', 'w+') as wexp:
            for i in range(len(exps)):
                wexp.write(name[i] + ': ' + exps[i].expression() + '\n\n')
        if z3SolveBool:
            print('\nStart to solve with z3\n')
            varList = list(fchoDict.keys())
            value, model = z3solve(fchoDict, exps, attrReq)

            if model:
                backendSet = {'MQCC' : (MQCC, '../Fixed-choice_MQCC')}
                if anonyCount==0:
                    print('Solution Model:', model)
                else:
                    print("Find solution successfully. Program uses anonymous choice variable, so cannot print out solution model")
                print('Final value of "' + goalName + '" is: ' + str(value))
                print('Result program has been written into file "Fixed-choice_MQCC"')
                for item in model:
                    fchoValue[str(item)] = model[item]
                passMode = 'backend'
                for key, value in backendSet.items():
                    attrMode = 'general'
                    attrType = value[0]
                    result = parser.parse(s, tracking=True)
                    with open(value[1], 'w+') as wr:
                        wr.write('\n'.join(result[0]) + '\n')
                        wr.write(result[1].expression('backend'))                
            else:
                print("\nNo satisfied model")
        end=time.time()
        print("Totally use {0}s".format(end-start))


        