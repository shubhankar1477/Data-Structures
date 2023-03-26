import random

class Node(object):
    __slots__ = ['value','left','right']

    def __init__(self,value,left = None, right = None) -> None:
        self.value = value
        self.right = right
        self.left = left
        
class BST:
    def inorder(self,node):
        if node is None:
            return []
        return self.inorder(node.left)+[node.value]+self.inorder(node.right)
    
    def insertion(self,node,value):
        
        if node is None:
            return Node(value)
        else:
            if value == node.value:
                return node
            elif value < node.value:
                node.left = self.insertion(node.left,value)
            else:
                node.right = self.insertion(node.right,value)
        return node
    def getMinvalue(self,node):
        curr = node
        while (curr.left) is not None:
            curr = curr.left
        return curr 
    
    def deletion(self,node,value):
        if node is None:
            return node

        if value < node.value:
            node.left = self.deletion(node.left,value)
        elif value > node.value:
            node.right = self.deletion(node.right,value)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            if node.right is None:
                temp = node.left
                node = None
                return temp
            
            temp = self.getMinvalue(node.right)

            node.value =  temp.value

            node.right = self.deletion(node.right,temp.value)
        return node
            
    



if __name__ == '__main__':
    node = Node(3)
    bst = BST()
    for i in [0,1,2,5,15,20]:
        node = bst.insertion(node,i)
    print(bst.inorder(node))
    print(bst.getMinvalue(node))
    node = bst.deletion(node,2)
    print(bst.inorder(node))
