#Write a method to reverse the elements in the same list.


import link1 as l1

class reverse(l1.Llist):
	
	def __init__(self):
		super().__init__()

	def rev(self):
		
		cur = self.head
		prev = None
		fut = cur.next
		while not cur is None and not fut is None:
			cur.next=prev
			prev=cur
			cur=fut
			fut=cur.next
		else:
			cur.next=prev
			
		self.head=cur
		

		

		
	
if __name__ == '__main__':

	r = reverse()
	r.addfirst(1)
	r.addfirst(11)
	r.addlast(33)
	r.addlast(43)
	r.addlast(53)
	r.addlast(63)
	r.displaylist()
	r.rev()
	print("after reversing:")
	r.displaylist()

