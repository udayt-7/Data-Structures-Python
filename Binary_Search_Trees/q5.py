#Add method to count the number of terminal nodes in BST. Provide test cases.


import tree as t1

class terminal(t1.BST):
    
    
    def __init__(self):
        super().__init__() 

    def leaf_nodes(self):
        if not self.isEmpty():
            self._leaf_nodes(self.root)
            print('Terminal Nodes:',self.leaf_count)

    def _leaf_nodes(self,node):
        if not node is None:
            if node.left == None and node.right == None:
                self.leaf_count+=1
                return
            else:
                self._leaf_nodes(node.left)
                self._leaf_nodes(node.right)

if __name__ == '__main__':
    
    
    t = terminal()
    t.add_node(4)
    t.add_node(5)
    t.add_node(2)
    t.add_node(8)
    t.add_node(3)
    t.add_node(6)
    t.add_node(1)
    t.add_node(0)
    t.add_node(7)
    t.add_node(9)
    
    t.leaf_nodes()