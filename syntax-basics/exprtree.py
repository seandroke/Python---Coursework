from abc import ABCMeta,abstractmethod
from vartree import VarTree

class ExprTree(metaclass=ABCMeta):
    """Abstract class for expression"""
    def __str__(self):
        return ' '.join( str(x) for x in iter(self) )
    #   All of the derived class mus implement these functions
    @abstractmethod
    def __iter__(self):
        """an inorder iterator for this tree node, for display"""
        pass
    @abstractmethod
    def evaluate(self, variables):
        """evaluate using the existing variables"""
        pass
    @abstractmethod
    def postfix(self):
        """a post-order iterator to create a postfix expression"""
        pass


class Var(ExprTree):
    """A variable leaf"""
    def __init__(self, n):
        self._name = n
    def __iter__(self):
        yield self._name
    def evaluate(self, variables):
        return variables.lookup(self._name)
    def postfix(self):
        yield self._name

class Value(ExprTree):
    """A value leaf"""
    def __init__(self, v):
        self._value = v
    def __iter__(self):
        yield self._value
    def evaluate(self, variables):
        return self._value
    def postfix(self):
        yield self._value
    
    

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
        
    def evaluate(self,variables):
        if self._expr == "=":
            variables.assign(self._left._name,self._right.evaluate(variables))
            return self._right.evaluate(variables)
        else:
            return eval(str(self._left.evaluate(variables))+ self._expr + str(self._right.evaluate(variables)))
    def postfix(self):
        yield from self._left.postfix()
        yield from self._right.postfix()
        yield self._expr
        
    
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
    def evaluate(self,variables):
        if self._test.evaluate(variables):
            return str(self._true.evaluate(variables))
        else:
            return str(self._false.evaluate(variables))
    def postfix(self):
        yield from self._test.postfix()
        yield from self._true.postfix()
        yield from self._false.postfix()
        yield "?",":" 

