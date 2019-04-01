##7.      Write a method which creates the union of elements from two lists.



import link1

l1 = link1.Llist()
l2 = link1.Llist()


l1.addfirst(1)
l1.addlast(2)
l1.addlast(3)
l1.addlast(4)
l1.addlast(5)
l1.addlast(6)
print("LIST 1")
l1.displaylist()

l2.addfirst(7)
l2.addlast(8)
l2.addlast(9)
l2.addlast(10)
l2.addlast(11)
l2.addlast(12)
print("LIST 2")
l2.displaylist()


def union(l1,l2):

	cur1 = l1.head
	cur2 = l2.head
	list1 = []



	l1.tail.next = l2.head
	l1.tail = l2.tail

	list1.append(cur1.data)
				
	list1 = set(list1)
	list1 = list(list1)

	print("Union of lists:")
	l1.displaylist()


union(l1,l2)




