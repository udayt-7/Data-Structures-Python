#Add method to count number of nodes in the left sub tree and number of nodes in right sub tree. 
#Provide test cases.
	
import tree as t1
class leftright(t1.BST):
    
    
    def __init__(self):
        super().__init__()     
    
    def count_nodes(self,key):
        if not self.isEmpty():
            current =self.root
            while current!=None:
                if current.data>key:
                    current=current.left
                elif current.data<key:
                    current=current.right
                else:
                    break
            if current.data==key:
                if not current.left == None:
                    self._count_nodes(current.left)
                    print(self.lcount)
            if not current.right == None:
                self.lcount=0
                self._count_nodes(current.right)
                print(self.lcount)

            else:
                return False

    def _count_nodes(self,node):
        if not node is None:
            self._count_nodes(node.left)
            self.lcount+=1
            self._count_nodes(node.right)

if __name__ == '__main__':
    
    
    lr = leftright()
    lr.add_node(4)
    lr.add_node(5)
    lr.add_node(2)
    lr.add_node(7)
    lr.add_node(3)
    lr.add_node(6)
    lr.add_node(1)
    lr.add_node(0)
    lr.add_node(8)
    lr.add_node(9)
    lr.count_nodes(4)
    