class stack:
    def __init__(self) -> None:
        self.__index = []

    def __len__(self):
        return len(self.__index)
    
    def push(self,value):
        self.__index.insert(0,value)

    def peek(self):
        if len(self) == 0:
            raise Exception("Stack is Empty")
        return self.__index[0]
    def pop(self):
        if len(self) == 0:
            raise Exception("Stack is Empty")
        return self.__index.pop(0)
    
    def __str__(self) -> str:
        return str(self.__index)

def main():
    s = stack()
    s.push(5)
    s.push(10)
    s.push([100,100])
    s.push("test")
    print(str(s))
    s.pop()
    print(s.peek())
main()



class MyQueue(object): 
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.push_stack = []
        self.pop_stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.push_stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty(): return
        if len(self.pop_stack):
            return self.pop_stack.pop()
        else:
            while len(self.push_stack):
                self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.empty(): return
        if len(self.pop_stack):
            return self.pop_stack[-1]
        else:
            while len(self.push_stack):
                self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.push_stack)==False and len(self.pop_stack) == False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()