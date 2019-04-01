#9.      Create single list such that it should always contain unique elements. Care should be taken that, 
##if element is already present in the list, you should not add it again.

class Llist:
	class _Node:
		def __init__(self,ele):
			self.data = ele
			self.next = None
	def __init__(self):
		self.head = None
		self.tail = None
		self.count = 0
		self.list1 = []

	def displaylist(self):
		cur = self.head
		i = 0
		list1 = []

		print("Linked List:\n")
		while cur != None:	
			list1.append(cur.data)		
			print(cur.data,end = '\t')
			cur  = cur.next
			i += 1			
		print('\n')
		print("Total no of elements:",i)
		print('\n')

	def isempty(self):
		return self.count == 0
	
	def addfirst(self,val):
		if not self.lookup(val):
			new_node = self._Node(val)
			if not self.isempty():
				new_node.next = self.head
				self.head = new_node
			else:
				self.head = self.tail = new_node
			self.count += 1

	def addlast(self,val):
		if not self.lookup(val):
			new_node =self._Node(val)
			if not self.isempty():
				self.tail.next = new_node
				self.tail = new_node
			else:
				self.head = self.tail = new_node
			self.count += 1


	def addany(self,pos,ele):
		if not self.lookup(ele):
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


	def lookup(self,val):
		 	
		#val = int(input("enter element to be add:"))
		cur1 = self.head
		
		i = 0
		while(cur1 != None):
			if cur1.data == val:
				print("Cannot add",val,"already in list")
				return True
			cur1 = cur1.next
	
			i += 1

		else:
			print("The number",val,"can be added!!")

			

if __name__ == '__main__':

	l1 = Llist()
	l1.addfirst(1)
	l1.addfirst(11)
	l1.addlast(33)
	l1.addlast(43)
	l1.addlast(53)
	l1.addlast(63)
	l1.displaylist()
	l1.addany(2,43)
	l1.addany(2,45)
	l1.displaylist()
	l1.addfirst(1)
	l1.addfirst(9)
	l1.displaylist()
