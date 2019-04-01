#Add method to find the height of binary search tree. Provide test cases.

import tree as t1

class height(t1.BST):
    
    
    def __init__(self):
        super().__init__() 
        
    #Add method to find the height of binary search tree

    def maxDepth(self):
        if not self.isEmpty():
            count=self.height1(self.root)
            print("Height:")
            return count
	
    def height1(self,node):
        if node is None:
            return 0
        else:
            return max(self.height1(node.left), self.height1(node.right))+1


if __name__ == '__main__':

    h = height()
    h.add_node(4)
    h.add_node(5)
    h.add_node(2)
    h.add_node(8)
    h.add_node(3)
    h.add_node(6)
    h.add_node(1)
    h.add_node(0)
    h.add_node(7)
    h.add_node(9)
    height=h.maxDepth()
    print(height)