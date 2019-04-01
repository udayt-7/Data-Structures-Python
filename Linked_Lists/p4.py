
#4.Modify Q1 such that one can delete any specified element from the list.


import link1 as l1

class delatany(l1.Llist):
	
	def __init__(self):
		super().__init__()

	def delatany(self,val):

		cur = self.head

		i = 0

		if not self.isempty():
			while(cur != None and cur.next.data != val):
				cur = cur.next

			temp = cur.next
			cur.next = temp.next
			temp.next = None
				
		print("\n\nAfter deleting:",temp.data)
		
		
if __name__ == '__main__':


	d = delatany()
	d.addfirst(1)
	d.addfirst(11)
	d.addlast(33)
	d.addlast(43)
	d.addlast(53)
	d.addlast(63)
	d.displaylist()
	
	d.delatany(33)
	d.displaylist()