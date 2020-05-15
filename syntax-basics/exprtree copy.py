from abc import ABCMeta, abstractmethod
from vartree import VarTree

class ExprTree(metaclass=ABCMeta):
    def __str__(self):
        return ' '.join( str(x) for x in iter(self) )

    @abstractmethod
    def __iter__(self):
        """an inorder iterator for this tree node, for display"""
        pass

    @abstractmethod
    def postfix(self):
        """a post-order iterator to create a postfix expression"""
        pass

    @abstractmethod
    def evaluate(self, variables, functions):
        """evaluate using the existing variables"""
        pass

class Var(ExprTree):
    
    def __init__(self, n):
        self._name = n
        
    def __iter__(self):
        yield self._name
        
    def postfix(self):
        yield self._name
        
    def evaluate(self, variables, functions):
        #print(self._name)
        return variables.lookup(self._name)

class Oper(ExprTree):
    
    def __init__(self,val1,operate,val2):
        self._left = val1
        self._right = val2
        self._expr = operate

    def __iter__(self):
        yield "("
        yield from self._left
        yield self._expr
        yield from self._right
        yield ")" 

    def postfix(self):
        yield from self._left.postfix()
        yield from self._right.postfix()
        yield self._expr

    def evaluate(self,variables,functions):
        if self._expr == "=":
            variables.assign(self._left._name,self._right.evaluate(variables,functions))
            return self._right.evaluate(variables,functions)
        else:
            return eval(str(self._left.evaluate(variables,functions))+ self._expr + str(self._right.evaluate(variables,functions)))

class Value(ExprTree):
    
    def __init__(self, v):
        self._value = v

    def __iter__(self):
        yield self._value

    def postfix(self):
        yield self._value

    def evaluate(self, variables,functions):
        return self._value

class Cond(ExprTree):
    
    def __init__(self,test,true,false):
        self._test = test
        self._true = true
        self._false = false

    def __iter__(self):
        yield "("
        yield from self._test
        yield ")"
        yield "?"
        yield "("
        yield from self._true
        yield ")"
        yield ":"
        yield "("
        yield from self._false
        yield ")"

    def postfix(self):
        yield from self._test.postfix()
        yield from self._true.postfix()
        yield from self._false.postfix()
        yield "?",":" 

    def evaluate(self,variables,functions):
        if self._test.evaluate(variables,functions):
            return str(self._true.evaluate(variables,functions))
        else:
            return str(self._false.evaluate(variables,functions))

class Functioncall(ExprTree):

    def __init__(self, n, p):
        self._name = n
        self._parameter = p

    def __iter__(self):
        yield self._name
        yield "("
        yield from self._parameter
        yield ")"

    def postfix(self):
        pass

    def evaluate(self, variables, functions):
        x = functions.lookup(self._name)
        y = VarTree()
        for i in range(len(x[0])):
            y.assign(x[0][i], self._parameter[i].evaluate(variables, functions))
        return x[1].evaluate(y, functions)

    



