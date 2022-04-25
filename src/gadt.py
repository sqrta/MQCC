from functools import reduce
debug = False
connect = ' + \n'
def Debug(*args):
    if debug:
        print(args)

def expValid(varLabels, exp):
    for item in varLabels:
        exec(item[0].varName() + '=' + str(item[1]))
    return eval(exp)


def z3decl(varName):
    return varName + '= Int("' + varName + '")'


def z3Var(varDict):
    # [(varName, range)]
    decls = []
    ranges = []
    for key in varDict.keys():
        decls.append(z3decl(key))
        ranges.append(
            'Or(' + ','.join([key + '==' + str(v) for v in varDict[key]]) + ')')
    return decls, ranges


def numStr(n):
    if isinstance(n, int):
        return str(n)
    elif isinstance(n, float):
        return format(n, '.3f')
    else:
        return str(n)


class Register:
    def __init__(self, name, index, type):
        self.name = name
        self.index = index
        self.type = type
        
    def getIndex(self):
        return int(self.index)

    def getName(self):
        return self.name

    def __str__(self):
        return self.name+'['+str(self.index)+']'

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.name == other.name and self.index == other.index

    def __hash__(self):
        return hash((self.name, self.index))


def conStr(var, label, mode='default'):
    if mode == 'z3':
        return 'If('+str(var)+'=='+str(label)+',1.0,0.0)'
    else:
        return '['+str(var) + ',' + str(label)+']'


class Var:
    def __init__(self, value, inType=None):
        self.value = value
        self.type = inType

    def varName(self):
        return self.value

    def __str__(self):
        return str((self.type, self.value))

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.value == other.value and self.type == other.type

    def __hash__(self):
        return hash((self.type, self.value))


class ConPair:
    def __init__(self, attr, var=None, label=None):
        # attr is an Attr instance
        self.conVar = {} if not var else {var: label}
        self.attr = attr

    def getConVar(self):
        result = []
        for key in self.conVar.keys():
            var = key
            if var.type == 'fcho':
                result.append(var.varName())
        return result

    def addConVar(self, var, label):
        if var in self.conVar.keys():
            if self.conVar[var] != label:
                return -1
        else:
            self.conVar[var] = label
        return 0

    def varStr(self, mode='default'):
        exps = []
        varList = list(self.conVar.items())
        varList.sort(key=lambda x: x[0].varName())
        if mode == 'valid':
            for var in varList:
                if var[0].type == 'fcho':
                    exps.append(conStr(var[0].varName(), var[1], mode))
        else:
            for var in varList:
                tmp = conStr(var[0].varName(), var[1], mode)
                exps.append(tmp)
        labelStr = '' if len(exps) == 0 else '*'.join(exps)
        return labelStr

    def globalVarStr(self, varDict):
        exps = []
        selfDict = {key.varName() : value for key,value in self.conVar.items() if key.type=='fcho'}
        varList = list(varDict.keys())
        varList.sort()
        for var in varList:
            if var in selfDict.keys():
                exps.append([conStr(var, selfDict[var])])
            else:
                exps.append([conStr(var, value)
                             for value in varDict[var]])
        return reduce(lambda a, b: [i+'*'+j for i in a for j in b], exps)

    def valid(self):
        freeVar = []
        limitVar = []
        for var, label in self.conVar.items():
            if var.type == 'fcho':
                freeVar.append((var, label))
            else:
                limitVar.append((var, label))
        for var in limitVar:
            name = var[0].varName()
            exp = name + '==' + str(var[1])
            if not expValid(freeVar, exp):
                return False
        return True

    def expression(self, mode='default'):
        attrStr = numStr(self.attr.value())
        choiceStr = self.varStr(mode)
        if choiceStr == '':
            return attrStr
        return choiceStr + '*' + attrStr

    def z3exp(self):
        decls = []
        cons = []
        # each com is a (var, label) tuple like (('fcho', 'c1'), '0')
        for var, label in self.conVar.items():
            name = var.varName()
            cons.append(str(name) + '==' + str(label))
            if var.type == 'fcho':
                decls.append(z3decl(name))

        return decls, cons

    def __str__(self):
        return str((self.varStr(), self.attr))

    def __repr__(self):
        return str(self)

    def __cmp__(self, other):
        return self.attr.__cmp__(other.attr)


class Attr:
    def __init__(self):
        self.empty()

    def empty(self):
        pass

    def op(self, opID, regs, args):
        pass

    def case(self, group, var):
        pass

    def value(self):
        return 0

    def __str__(self):
        return str(self.value())

    def __repr__(self):
        return str(self)


class AttrWrap:
    def __init__(self, attrType):
        self.attrType = attrType

    def expression(self, mode=None, reqs=None):
        pass

    def choice(self, var, group):
        pass

    def canOpt(self):
        return ''

    def validate(self):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        return str(self)


class additive(AttrWrap):
    def __init__(self, attrType):
        self.attrType = attrType
        self.conList = []  # list of (AttrWrap, var, label)
        self.insList = []  # list of ConPair

    def empty(self):
        ins = self.attrType()
        ins.empty()
        self.insList = [ConPair(ins)]

    def op(self, gate, regs, args=None):
        self.insList[-1].attr.op(gate, regs, args)
        #print(gate, self.insList)

    def case(self, attrGroup, var=None):
        group = [(item[0], item[1].insList[0].attr) for item in attrGroup]
        self.insList[0].attr.case(group, var)

    def choice(self, var, group):
        for item in group:
            label = item[0]
            attr = item[1]
            self.conList.append((attr, var, label))
        # self.empty()

    def expression(self, mode='default'):
        if mode == 'backend':
            return ''.join([ins.attr.value() for ins in self.insList])
        scale = numStr(sum([ins.attr.value() for ins in self.insList]))
        exps = []
        if len(self.conList) == 0:
            return scale
        for item in self.conList:
            var = item[1].varName()
            label = item[2]
            exps.append(conStr(var, label, mode) +
                        '*' + item[0].expression(mode))
        exp = connect.join(exps) if scale == '0' else scale + \
            connect + connect.join(exps)
        return '(' + exp + ')'

    def canOpt(self):
        return 'add'

    def maxValue(self):
        scale = sum([ins.attr.value() for ins in self.insList])
        terms = 0
        for item in self.conList:
            terms += item[0].maxValue()
        return scale + terms

    def append(self, other):
        self.insList += other.insList

    def __str__(self):
        return str((self.conList, self.insList))


class generalWrap(AttrWrap):
    def __init__(self, attrType):
        self.attrType = attrType
        self.insList = []

    def empty(self):
        ins = self.attrType()
        ins.empty()
        self.insList = [ConPair(ins)]  # list of ConPair

    def op(self, gate, regs, args=None):
        for ins in self.insList:
            ins.attr.op(gate, regs, args)

    def case(self, attrGroup, var=None):
        
        length = len(self.insList)
        Debug(attrGroup)
        for i in range(length):
            group = [(item[0], item[1].insList[i].attr) for item in attrGroup]
            self.insList[i].attr.case(group, var)
        '''
        length = len(self.insList)
        print(attrGroup)
        for i in range(length):
            terms = []
            for item in attrGroup:
                k = len(item[1].insList) / length
                terms.append([item.insList[i*k + j] for j in range(k)])
            def threadMerge(a,b):
                if len(a)==1 and len(b) ==1:
                    return [[a[0],b[0]]]
                
            group = [(item[0], item[1].insList[i].attr) for item in attrGroup]
            self.insList[i].attr.case(group, var)
        '''

    def addCon(self, var, label):
        newList = []
        for ins in self.insList:
            tmp = ins.addConVar(var, label)
            if tmp == 0:
                newList.append(ins)
        self.insList = newList

    def choice(self, var, group):
        attrs = []
        for item in group:
            label = item[0]
            attr = item[1]
            attr.addCon(var, label)
            attrs.append(attr)

        def attrUnion(a, b):
            a.insList += b.insList
            return a
        self.insList = reduce(attrUnion, attrs).insList

    def union(self, other):
        self.insList += other.insList

    def getI(self, i):
        return self.insList[i]

    def length(self):
        return len(self.insList)

    def validate(self):
        newList = []
        for item in self.insList:
            if item.valid():
                newList.append(item)
        self.insList = newList

    def expression(self, mode=None, reqs=None):
        return connect.join([ins.expression('valid') for ins in self.insList])

    def __str__(self):
        return str([i for i in self.insList])

    def __repr__(self):
        return str(self)
