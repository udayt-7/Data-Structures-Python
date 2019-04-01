#Add methods to find max and min element in BST. Provide test cases.


import tree as t1

class minmax(t1.BST):
    
    
    def __init__(self):
        super().__init__() 
    
    def findMin(self,node):
        if node.left is None:
            return node
        else:
            return self.findMin(node.left)
        #print(node.data)

    def findMax(self,node):
        if node.right is None:
            return node
        else:
            return self.findMax(node.right)
        #print(node.data)


if __name__ == '__main__':
    
    
    m = minmax()
    m.add_node(4)
    m.add_node(5)
    m.add_node(2)
    m.add_node(7)
    m.add_node(3)
    m.add_node(6)
    m.add_node(1)
    m.add_node(0)
    m.add_node(8)
    m.add_node(9)
    print(m.findMin(m.root).data)
    print(m.findMax(m.root).data)
    #m.findMax()
    
	