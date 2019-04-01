
class Llist:
	class _Node:
		def __init__(self,ele):
			self.data = ele
			self.next = None
	def __init__(self):
		self.head = None
		self.tail = None
		self.count = 0

	def displaylist(self):
		cur = self.head
		i = 0
		print("Linked List:\n")
		while cur != None:			
			print(cur.data,end = '\t')
			cur  = cur.next
			i += 1

		print('\n')
		print("Total no of elements:",i)


	def isempty(self):
		return self.count == 0
	
	def addfirst(self,val):
		new_node = self._Node(val)
		if not self.isempty():
			new_node.next = self.head
			self.head = new_node
		else:
			self.head = self.tail = new_node
		self.count += 1

	def addlast(self,val):
		new_node =self._Node(val)
		if not self.isempty():
			self.tail.next = new_node
			self.tail = new_node
		else:
			self.head = self.tail = new_node
		self.count += 1

			
	def delfirst(self):
		if not self.isempty():
			self.head = self.head.next
		if self.head == None:
			self.tail = None
		self.count -= 1

	def dellast(self):
		if not self.isempty():
			if self.head == self.tail:
				self.head = self.tail = None
			else:
				tail = self.tail
				cur = self.head
			while cur.next != tail:
				cur = cur.next
			self.tail = cur
			cur.next = None
			self.count -= 1

	def lookup(self):
		 	
		opt = int(input("select:\n 1.search from data\n 2.search from node\n"))
		while(opt == 1 or opt == 2):
			
			if (opt == 1):
				val = int(input("enter element to be searched:"))
				cur = self.head
				i = 0
				while(cur != None):
					if cur.data == val:
						print(val,"is in Node:",i)
						exit(0)
					cur = cur.next
					i += 1

				else:
					print("element not found")

			elif(opt == 2):
				key = int(input("enter node to be searched:"))
				i = 0
				cur = self.head
				while(i < key and cur != None):
					cur = cur.next
					i += 1
				else:
					if cur != None:
						print("Node",key ,"is:",cur.data)

					else:
						print("key not found")
					break
		else:
			print("invalid option")

	def addany(self,pos,ele):
		
		new_node = self._Node(ele)
		i = 0
		if not self.isempty():
			temp = self.head

			while(i<pos-1 and temp != None):
				temp = temp.next
				i += 1

		new_node.next = temp.next
		temp.next = new_node
		print("\n\nAdding",ele,"at position", pos)


if __name__ == '__main__':

	l1 = Llist()
	l1.addfirst(1)
	l1.addfirst(11)
	l1.addlast(33)
	l1.addlast(43)
	l1.addlast(53)
	l1.addlast(63)
	l1.displaylist()
	#l1.lookup()
	l1.addany(2,45)
	l1.displaylist()
	l1.addany(6,95)
	l1.displaylist()
