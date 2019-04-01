#Add methods to display the traversal in ascending and descending order.


 
import tree as t1

class incdec(t1.BST):
    
    
    def __init__(self):
        super().__init__()    
    
    def inorder(self):
        if not self.isEmpty():
            self._inorder_(self.root)
            

    def _inorder_(self,node):
        if not node is None:
            self._inorder_(node.left)
            print(node.data)
            self._inorder_(node.right)

    def deorder(self):
        if not self.isEmpty():
            self._deorder_(self.root)
            

    def _deorder_(self,node):
        if not node is None:
            self._deorder_(node.right)
            print(node.data)
            self._deorder_(node.left)

if __name__ == '__main__':

    id = incdec()
    id.add_node(4)
    id.add_node(5)
    id.add_node(2)
    id.add_node(8)
    id.add_node(3)
    id.add_node(6)
    id.add_node(1)
    id.add_node(0)
    id.add_node(7)
    id.add_node(9)
    id.inorder()
    id.deorder()