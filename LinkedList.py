class Node:
    def __init__(self,value,next_node=None,prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

    def __str__(self) -> str:
        return str(self.value)
class LinkedList:
    def __init__(self,values = None) -> None:
        self.head = None
        self.tail = None
        self._len= 0

        if values is not None:
            self.add_multiple_nodes(values)
    def __str__(self):
        return ' -> '.join([str(node) for node in self])
    
    def __len__(self):
        count = 0
        node = self.head
        while node:
            count+=1
            node = node.next
        return count

    def add_node(self,value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        self._len+=1
        return self.tail

    def add_multiple_nodes(self,values):
        for value in values:
            self.add_node(value)

    def add_node_as_head(self,value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            self.head = Node(value,self.head)
        return self.head
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
    @property
    def values(self):
        return [node.value for node in self]
    
    def _find_value(self,curr, prev,value):
        while curr:
            if curr.value == value:
                return curr,prev,True
            prev = curr
            curr = curr.next
        return curr, prev , False
    def __contains__(self, value):
        _, _, found = self._find_value(self.head, None, value)
        return found
    
    def remove(self,value):
        node, prev, found = self._find_value(self.head, None, value)
        if not node:
            raise ValueError()
        if prev :
            prev.next = node.next
        else:
            self.head = node.next 
        if not node.next:
            self.tail = prev
        self._len-=1

    def reverse(self):
        curr = self.head
        prev = None
        while curr:
            self._next  = curr.next
            curr.next = prev
            prev = curr
            curr = self._next
        self.head = prev
        return self.head
    
    def sort(self):
        curr  = self.head
        index = None

        if curr is None:
            return 
        else:
            while curr:
                index = curr.next
                while index:
                    if curr.value > index.value:
                        temp = curr.value
                        curr.value = index.value
                        index.value = temp
                    index = index.next
                curr = curr.next



    
class DoublyLinkedList(LinkedList):
    def add_node(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value, None, self.tail)
            self.tail = self.tail.next
        return self
    def add_node_as_head(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            current_head = self.head
            self.head = Node(value, current_head)
            current_head.prev = self.head
        return self.head
    
    
if __name__ == '__main__':
    li = LinkedList()
    li.add_node(1)
    li.add_node(0)
    li.add_node(9)

    # print(li.__contains__(5))
    # print(li.__str__())
    # print(li.remove(8))
    print(li.__str__())
    print(li.sort())
    print(li.__str__())

