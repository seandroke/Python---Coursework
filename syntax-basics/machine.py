from vartree import VarTree
class Instruction:
    """Simple instructions representative of a RISC machine

    These instructions are mostly immutable -- once constructed,
    they will not be changed -- only displayed and executed
    """
    def __init__(self, t):      # default constructor
        self._temp = t  # every instruction has a register
    def get_temp(self):         # which holds its answer
        return self._temp

class Print(Instruction):
    """A simple non-RISC output function to display a value"""
    def __str__(self):
        return "print T" + str(self._temp)
    def execute(self,temps,stack,pc,sp):
        print( temps[int(self._temp)] ) 

class Initialize(Instruction):
    def __init__(self,t,v):
        self._temp = t  # every instruction has a register
        self._values = v
    def __str__(self):
        return "T"+str(self._temp)+"="+str(self._values)      
    def execute(self,temps,stack,pc,sp):
        temps[int(self._temp)] = self._values  
    
class Load(Instruction): #stack[0]= T1
    def __init__ (self,t,i):
        self._temp= t
        self.index = i
    def __str__(self):
        return "stack["+str(self.index)+"] = T" + str(self._temp)
    def execute(self,temps,stack,pc,sp):
        stack[int(self.index)] = temps[int(self._temp)]
class Store(Instruction): #T1 = stack[0]
    def __init__ (self,t,i):
        self._temp= t
        self.index = i
    def __str__(self):
        return 'T'+str(self._temp)+"= stack["+str(self.index)+']'
    def execute(self,temps,stack,pc,sp):
        temps[int(self._temp)] = stack[int(self.index)]
class Compute(Instruction): #T1 = T2 + T3
    def __init__(self,t,t2,oper,t3):
        self._temp= t
        self._temp2 = t2
        self._temp3 = t3
        self.oper = oper
    def __str__(self):
        return 'T'+str(self._temp)+'='+'T'+str(self._temp2)+str(self.oper)+'T'+str(self._temp3)
    def execute(self,temps,stack,pc,sp):
        temps[int(self._temp)] = str(eval(str(temps[int(self._temp2)])+str(self.oper)+str(temps[int(self._temp3)])))
        
            
