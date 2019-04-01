#Design a BST class with methods to add element, search element, number of elements 
#and delete requested element. 
#Provide test cases.


class BST:
	class _TreeNode:
		def __init__(self,ele):
			self.data=ele
			self.left=None
			self.right=None

	def __init__(self):
		self.root=None
		self.count=0
		self.lcount=0
		self.rcount=0
		self.leaf_count=0

	def add_node(self,ele):
		current=parent=self.root
		while current is not None and current.data!=ele:
			parent=current
			if ele<current.data:
				current=current.left
			elif ele>current.data:
				current=current.right
		if current is None:
			new_node=self._TreeNode(ele)
			if parent is None:
				self.root=new_node
			elif ele < parent.data:
				parent.left=new_node
			elif ele>parent.data:
				parent.right=new_node
			self.count+=1

	def node_count(self):
		return self.count

	def isEmpty(self):
		return self.count==0

	def lookup(self,key):
		if not self.isEmpty():
			current =self.root
			while current!=None:
				if current.data>key:
					current=current.left
				elif current.data<key:
					current=current.right
				else:
					break
				return current!=None

	def findMin(self,node):
		if node.left is None:
			return node
		else:
			return self.findMin(node.left)


	def delete_node(self,key):#delete terminal node
		if not self.isEmpty():
			self.root=self._delete_(self.root,key)

	def _delete_(self,node,key):
		if node is None:
			return node
		elif key<node.data:
			node.left=self._delete_(node.left,key)
		elif key>node.data:
			node.right=self._delete_(node.right,key)
		elif(node.left and node.right):
			temp=self.findMin(node.right)
			node.data=temp.data
			node.right= self._delete_(node.right,node.data)
		else:
			if node.left is None:
				node=node.right
			else:
				node=node.left
			self.count-=1
		return node


if __name__ == '__main__':
	
	
	b=BST()
	b.add_node(12)
	b.add_node(44)
	b.add_node(23)
	b.add_node(10)
	b.add_node(31)
	b.add_node(56)
	b.add_node(7)
	b.add_node(30)
	b.add_node(12)
	b.add_node(9)
	b.lookup(12)
	b.delete_node(12)
	b.lookup(12)