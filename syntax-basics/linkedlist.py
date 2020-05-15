class linkedlist:
    class Node:
        __slots__ = "_value", "_next"

        def __init__( self, v, n ):
            self._value = v
            self._next = n
    def __init__(self, val):
        self._head = None
        self._tail = None
        self._size = 0

    def __iter__(self):
        current = self._head
        while current is not None:
            yield str(current._value)
            current = current._next
	
    def push(self, val):
        newNode = self.Node(val, self._head)
        self._head = newNode
        if self._tail is None:
            self._tail = self._head
        self._size += 1

    def pop( self ):
        if self._head is not None:
            popped = self._head._value
            self._head = self._head._next
            self._size -= 1
            return popped
        if self._head is None:
            self._tail = None


        
        
	
