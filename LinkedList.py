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
    li.add_node(8)
    print(li.__str__())