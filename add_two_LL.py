class Node:
    def __init__(self,value,next_node=None,prev_node=None):
        self.value = value
        self.next = next_node

    def __str__(self) -> str:
        return str(self.value)
    

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    
    def add_node(self,value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail


    def addTwoList(self,first,second):
        prev = None
        temp = None
        carry = 0


        while (first is not None or second is not None ):
            fdata = 0  if first is None else 