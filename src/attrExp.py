from numpy.lib.shape_base import array_split
from hdwspec import getNoiseMap
from functools import reduce
import math
from gadt import Attr
name = 'hdwspec'
noiseMap = getNoiseMap(name)

reserved = {'measure'}
pseudo = {'release', 'barrier'}


def calDepth(stamp):
    return 0 if len(stamp) == 0 else max(stamp.values())


def calError(gate, regs):
    global noiseMap

    def numRound(number, digit):
        return int(number*10**digit) / 10**digit
    if len(regs) == 1:
        index = regs[0].getIndex()
        return numRound(noiseMap[index, index], 3)
    elif len(regs) == 2:
        index0 = regs[0].getIndex()
        index1 = regs[1].getIndex()
        return numRound(noiseMap[index0, index1], 3)
    else:
        index0 = regs[0].getIndex()
        index1 = regs[1].getIndex()
        index2 = regs[2].getIndex()
        error = 3*noiseMap[index1, index2] + 2 * \
            noiseMap[index0, index1] + noiseMap[index1, index2]
        return numRound(error, 3)


def calAQV(startDict, depth):
    return sum([depth - value for value in startDict.values()])


def calCross(gateList):
    BoeblingenDict = {(6, 7): [(0, 1), (1, 2)], (3, 4): [(8, 9)], (7, 12): [
        (11, 16)], (13, 18): [(11, 12), (16, 17)], (18, 19): [16, 17]}
    error = 0
    for layer in gateList:
        regPairs = [tuple(sorted([i.getIndex() for i in item[1]]))
                    for item in layer if len(item[1]) > 1]
        for regPair in regPairs:
            if regPair in BoeblingenDict.keys():
                for other in regPairs:
                    if other in BoeblingenDict[regPair]:
                        error += 1
    return error


def dictMerge(a, b, f):
    return {k: f(a[k], b[k]) if k in a.keys() and k in b.keys() else a.get(k, b.get(k))
            for k in a.keys() | b.keys()}


class Depth(Attr):

    def empty(self):
        self.depthDict = {}

    def op(self, opID, regs, args):
        if opID == 'barrier':
            cur = calDepth(self.depthDict)
            for reg in regs:
                self.depthDict[reg] = cur
        elif opID == 'CRZ_N':
            self.depthDict[regs[0]] = args[0]+1
        elif opID not in pseudo:
            share = set(self.depthDict.keys()) & set(regs)
            next = calDepth({k: self.depthDict[k] for k in share}) + 1
            for reg in regs:
                self.depthDict[reg] = next

    def value(self):
        # return (calDepth(self.depthDict),self.depthDict)
        return calDepth(self.depthDict)

    def case(self, groups, reg):
        self.depthDict = reduce(lambda a, b: dictMerge(
            a, b, max), [i[1].depthDict for i in groups])

    def __str__(self):
        return str(self.depthDict)

class Accuracy(Attr):
    def empty(self):
        self.error = 0

    def op(self, opID, regs, args):
        '''
        opID : string
        regs : list of registers
            register.getName()  -> get the array name
            register.getIndex() -> get the index
        args : list of real numbers
        '''
        if opID == 'CRZ_N':
            self.error += 1/2**args[0] # 1/2^h_j

    def case(self, groups, reg):
        '''
        groups : Each item in groups is a tuple (Int, Noise) or ('default', Noise)
        reg : the register on which the case statement depends
        '''
        pass

    def value(self):
        return self.error

class AQV(Attr):

    def empty(self):
        self.depthDict = {}
        self.store = 0
        self.startDict = {}

    def op(self, opID, regs, args):

        if opID == 'release':
            for reg in regs:
                if reg in self.depthDict.keys():
                    self.store += self.depthDict.pop(reg) - \
                        self.startDict.pop(reg)
        else:
            share = set(regs) & set(self.depthDict.keys())
            startTime = calDepth({k: self.depthDict[k] for k in share})
            for reg in regs:
                self.depthDict[reg] = startTime + 1
                self.startDict[reg] = self.startDict.get(reg, startTime)
            #print(opID, self.startDict, self.depthDict)

    def value(self):
        depth = calDepth(self.depthDict)
        aqv = self.store + calAQV(self.startDict, depth)
        # return str((aqv, self.store, self.startDict, self.depthDict, depth))
        return aqv

    def case(self, group, reg):
        self.store = max([i[1].store for i in group])

        self.depthDict = reduce(lambda a, b: dictMerge(
            a, b, max), [i[1].depthDict for i in group])
        self.startDict = reduce(lambda a, b: dictMerge(
            a, b, min), [i[1].startDict for i in group])

    def __str__(self):
        return str((self.startDict, self.depthDict))


class Noise(Attr):

    def empty(self):
        self.error = 0

    def op(self, opID, regs, args):
        if opID not in pseudo:
            self.error += calError(opID, regs)

    def value(self):
        return self.error

    def case(self, groups, reg):
        self.error = max([p[1].error for p in groups])


class gateNum(Attr):

    def empty(self):
        self.num = 0

    def op(self, opID, regs, args):
        if opID not in pseudo:
            self.num += 1

    def union(self, other):
        self.num += other.num

    def case(self, groups, reg):
        self.num = max([p[1].num for p in groups])


class crossTalk(Attr):
    def empty(self):
        self.depthDict = {}
        self.gateList = [[]]

    def op(self, opID, regs, args):
        if opID == 'barrier':
            cur = calDepth(self.depthDict)
            for reg in regs:
                self.depthDict[reg] = cur
        elif opID not in pseudo:
            share = set(regs) & set(self.depthDict.keys())
            next = calDepth({k: self.depthDict[k] for k in share}) + 1
            for reg in regs:
                self.depthDict[reg] = next
            if next >= len(self.gateList):
                self.gateList.append([])
            self.gateList[next].append((opID, regs))

    def value(self):
        ratio = 0
        alpha = 0.01
        decoherence = 1 - math.exp(-alpha * calDepth(self.depthDict))
        crosstalk = calCross(self.gateList)
        return crosstalk + ratio * decoherence

    def case(self, groups, reg):
        maxCross = max([i[1] for i in groups], key=lambda x: x.value())
        self.gateList = maxCross.gateList
        self.depthDict = maxCross.depthDict


class OpenQASM(Attr):
    def empty(self):
        # 'OPENQASM 2.0;\ninclude "qelib1.inc";\nqreg q[20];\ncreg c[20];\n'
        self.text = ''

    def value(self):
        return self.text

    def op(self, opID, regs, args):
        if opID == 'measure':
            self.text += 'measure ' + \
                str(regs[0]) + '->' + str(regs[1]) + ';\n'
        else:
            if args:
                opStr = opID + '(' + ','.join([str(i) for i in args]) + ') '
            else:
                opStr = opID + ' '
            self.text += opStr + ','.join([str(i) for i in regs]) + ';\n'

    def case(self, group, reg):
        for item in group:
            label = item[0]
            block = item[1]
            self.text += 'if(' + str(reg) + '==' + \
                str(label) + '){\n' + block.text + '\n}\n'


class MQCC(Attr):
    def empty(self):
        # 'OPENQASM 2.0;\ninclude "qelib1.inc";\nqreg q[20];\ncreg c[20];\n'
        self.text = ''

    def value(self):
        return self.text

    def op(self, opID, regs, args):
        if args:
            opStr = opID + \
                '(' + ','.join([str(i) for i in args]) + \
                ',' + ','.join([str(i) for i in regs])+');\n'
        else:
            opStr = opID + '(' + ','.join([str(i) for i in regs])+');\n'
        self.text += opStr

    def case(self, group, reg):
        self.text += 'case(' + str(reg) + '){\n'
        for item in group:
            label = item[0]
            block = item[1].text
            if block == '':
                block = 'pass\n'
            self.text += str(label) + ':\n' + block
        self.text += '}\n'

class Fidelity(Attr):
    def empty(self):
        self.fidelity = 0

    def op(self, opID, regs, args):
        from math import log
        if opID not in pseudo:
            self.fidelity += log(1-calError(opID, regs))

    def value(self):
        return self.fidelity

    def case(self, groups, reg):
        self.fidelity = min([p[1].fidelity for p in groups])    