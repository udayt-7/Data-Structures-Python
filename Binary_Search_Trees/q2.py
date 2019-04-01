#Add methods to in-order, pre-order, post-order and level-order traversals
    
import tree as t1

class orders(t1.BST):
    
    
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

	
    def pre_order(self):
        
        if not self.isEmpty():
            self._preorder(self.root)


    def _preorder(self,node):
        if not node is None:
            print(node.data)
            self._preorder(node.left)
            self._preorder(node.right)

    def postorder(self):
        if not self.isEmpty():
            self._postorder(self.root)

    def _postorder(self,node):
        if not node is None:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.data)
    
    # def level_order(self,data):
	# 	if not self.isEmpty:
	# 		q= queue1.flexiqueue()
	# 		self.q.enqueue(self.root)
	# 		for i in range(q):
	# 			if not self.q.isEmpty():
	# 				print(self.q.dequeue())
	# 				if not current.left is None:
	# 					self.q.enqueue(current.left)
	# 				if not current.right is None:
	# 					self.q.enqueue(current.right)
    # 


if __name__ == '__main__':

    o = orders()
    o.add_node(4)
    o.add_node(5)
    o.add_node(2)
    o.add_node(10)
    o.add_node(3)
    o.add_node(6)
    o.add_node(1)
    o.add_node(0)
    o.add_node(12)
    o.add_node(9)

    print('In-Order')
    o.inorder()
    print('Pre-Order')
    o.pre_order()
    print('Post-Order')
    o.postorder()
    #o.level_order()

