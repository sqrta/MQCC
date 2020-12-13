from src.gadt import Attr

class EmptyObject(Attr):
    def empty(self):
        pass

    def op(self, opID, regs, args):
        '''
        opID : string
        regs : list of registers
            register.getName()  -> get the array name
            register.getIndex() -> get the index
        args : list of real numbers
        '''
        pass

    def case(self, groups, reg):
        '''
        groups : Each item in groups is a tuple (Int, Noise) or ('default', Noise)
        reg : the register on which the case statement depends
        '''
        pass

    def value(self):
        return 0