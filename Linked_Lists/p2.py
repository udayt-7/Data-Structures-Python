#2. Add methods to Q1 to find maximum and minimum elements in the list.


import link1 as l1

class minmax(l1.Llist):
	
	def __init__(self):
		super().__init__()

	def maxmin(self):
			
		cur = self.head
		max1 = self.head.data
		min1 =self.head.data
		
		while(cur != None):

			if max1 < cur.data:
				max1 = cur.data
			cur = cur.next
			


			if min1 > cur.data:
				min1 = cur.data
			cur = cur.next
		
		print("Min element:",max1)
		print("max element:",min1)



if __name__ == '__main__':


	m = minmax()
	m.addfirst(1)
	m.addfirst(11)
	m.addlast(33)
	m.addlast(43)
	m.addlast(53)
	m.addlast(63)
	m.displaylist()
	m.maxmin()



