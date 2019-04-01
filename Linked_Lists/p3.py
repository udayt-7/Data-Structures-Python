#Modify Q1 such that one can add a new element after any specified element.


import link1 as l1

class addafterele(l1.Llist):
	
	def __init__(self):
		super().__init__()

	def addafterele(self,val,ele):
		
		new_node = self._Node(ele)
		cur = self.head
		i = 0
		if not self.isempty():
			while(cur != None):
				if cur.data == val:
					
					temp = cur
					new_node.next = temp.next
					temp.next = new_node
					break

				cur = cur.next
				i += 1
			print("\n\nAdding",ele,"after", val)

if __name__ == '__main__':


	a = addafterele()
	a.addfirst(1)
	a.addfirst(11)
	a.addlast(33)
	a.addlast(43)
	a.addlast(53)
	a.addlast(63)
	a.displaylist()
	a.addafterele(63,99)
	a.displaylist()
