#6.  Create two separate single lists. Check two list are same. 
##If the two lists have the same number of elements in the same order, then they are treated as same.

import link1

l1 = link1.Llist()
l2 = link1.Llist()


l1.addfirst(1)
l1.addfirst(11)
l1.addlast(33)
l1.addlast(43)
l1.addlast(53)
l1.addlast(63)
print("LIST 1")
l1.displaylist()

l2.addfirst(1)
l2.addfirst(11)
l2.addlast(33)
l2.addlast(43)
l2.addlast(53)
l2.addlast(63)
print("LIST 2")
l2.displaylist()

def lcheck(l1,l2):

	cur1 = l1.head
	cur2 = l2.head
	
	while (cur1 != None and cur2 != None):			
		
		if cur1.data != cur2.data:
			print("\nDifferent Linked lists")
			break
		else:
			cur1  = cur1.next
			cur2  = cur2.next
			
	else:
		print("\nlists are equal")
		

lcheck(l1,l2)



