from z3 import *
from gadt import *

flag = True


class hashExp:
    def __init__(self, attr, goal, varDict=None):
        # attr is an AttrWrap class
        if varDict:
            self.scope = {}
            for pair in attr.insList:
                exps = pair.globalVarStr(varDict)
                for exp in exps:
                    self.scope[exp] = pair.attr.value()
        else:
            self.scope = {pair.varStr('valid'): pair.attr.value()
                          for pair in attr.insList}

        self.goal = goal

    def sat(self, model):
        exps = []
        for item in model:
            exps.append((str(item), str(model[item])))
        exps.sort(key=lambda x: x[0])
        cons = '*'.join([conStr(x[0], x[1]) for x in exps])
        value = self.scope[cons]
        satExp = str(value) + self.goal
        return eval(satExp)

    def conPairSat(self, conpair):
        cons = conpair.varStr('valid')
        value = self.scope[cons]
        satExp = str(value) + self.goal
        return eval(satExp)


def conVarsSat(decls, cons, conVars=None):
    s = Solver()
    decl = decls[0]
    ranges = decls[1]
    for item in decl:
        exec(item)
    exec('s.add(' + ','.join(ranges) + ')')
    if conVars:
        constraints = conVars.z3exp()[1]
        exec('s.add(' + ','.join(constraints) + ')')
    for con in cons:
        exec('s.add(' + con + ')')
    if s.check() == sat:
        return s.model()
    else:
        return None
    '''
    if conVars.getAttr().getValue()==23:
        print(s,s.check())
    '''


def indirectSat(model, indirectCons, conPair=None):
    if conPair:
        for item in indirectCons:
            if not item.conPairSat(conPair):
                return False
        return True
    else:
        for item in indirectCons:
            if not item.sat(model):
                return False
        return True


def z3_add(name, f):
    return name + '.add(' + f + ')'


def directSolve(decls, goalAttr, goal, directCons, indirectCons):
    goalexp = goalAttr.expression('z3')
    if goal == 'min':
        low = - goalAttr.maxValue()
        high = 0
        goalexp = '-' + goalexp
    else:
        low = 0
        high = goalAttr.maxValue()
    accuracy = goalAttr.maxValue()/1000
    mid = (high + low) / 2
    # define z3 var
    s = Solver()
    decl = decls[0]
    ranges = decls[1]
    for item in decl:
        exec(item)
    for item in ranges:
        exec(z3_add('s', item))
    fitModel = None
    exec(z3_add('s', ','.join(directCons)))
    while high - low > accuracy:
        s.push()
        goalCons = z3_add('s', goalexp + '>' + str(mid))
        exec(goalCons)

        while s.check() == sat:
            model = s.model()
            if indirectSat(model, indirectCons):
                fitModel = model
                break
            else:

                s.add(Or([d() != model[d] for d in model]))
        if s.check() == sat:
            low = mid
        else:
            high = mid
        mid = (high + low) / 2
        s.pop()
    if fitModel:
        return abs(mid), fitModel
    else:
        return (None, None)


def OptSolve(decls, goalAttr, goal, directCons, indirectCons):
    terms = goalAttr.insList
    if goal == 'min':
        terms.sort(key=lambda a: a.attr.value())
    else:
        terms.sort(key=lambda a: a.attr.value(), reverse=True)
    for best in terms:
        #print(best, best.attr.value())
        model = conVarsSat(decls, directCons, best)
        if model and indirectSat(model, indirectCons, best):
            value = best.attr.value()
            return value, model
    return (None, None)


def z3solve(varDict, exps, goals):
    directCons = []
    indirectCons = []
    goalAttr = None
    decls = z3Var(varDict)
    for i in range(len(exps)):
        if goals[i] == 'min' or goals[i] == 'max':
            goalAttr = exps[i]
            goal = goals[i]
    if goalAttr.canOpt() == 'add':
        globalVar = varDict
    else:
        globalVar = None
    for i in range(len(exps)):
        if goals[i] != 'min' and goals[i] != 'max':
            if exps[i].canOpt() == 'add':
                directCons.append(exps[i].expression('z3') + goals[i])
            else:
                indirectCons.append(hashExp(exps[i], goals[i], globalVar))
    if not goalAttr:
        print('No goal object')
        exit(0)
    if goalAttr.canOpt() == 'add':
        return directSolve(decls, goalAttr, goal, directCons, indirectCons)
    else:
        return OptSolve(decls, goalAttr, goal, directCons, indirectCons)


def lchoValue(fchoValue, exp):
    #print(fchoValue, exp)
    for key, value in fchoValue.items():
        exec(key + '=' + str(value))
    return int(eval(exp))
