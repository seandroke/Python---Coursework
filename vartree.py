class VarTree:
    class Node:
        __slots__ = "_left","_value","_right","_variable"
        def __init__(self, l, v, n, r):
            self._left = l
            self._variable = v
            self._value = n
            self._right = r

    def __init__(self):
        self._root = None

    def _search(self, here, var):
        if here is None:
            here = self._insert(here, var, str(0))
            return '0'
        elif var == here._variable:
            return here._value
        elif var > here._variable:
            return self._search(here._right,var)
        elif var < here._variable:
            return self._search(here._left, var)

    def _insert(self, here, var, value):
        if here is None:
            return self.Node(None, var, value, None)
        elif var == here._variable:
            here._value = value
            return here
        elif var < here._variable:
            here._left = self._insert(here._left, var, value)
            return here
        elif var > here._variable:
            here._right = self._insert(here._right, var, value)
            return here
        else:
            return here

    def assign(self, var, value):
        if self._root is None:
            self._root = self.Node(None, var, value, None)
        else:
            self._root = self._insert(self._root, var, value)

    def lookup(self, var):
        return self._search(self._root, var)

            
            
            
