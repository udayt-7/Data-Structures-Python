#Write a method which creates the intersection of elements from two lists.



import link1

l1 = link1.Llist()
l2 = link1.Llist()


l1.addfirst(3)
l1.addfirst(1)
l1.addlast(5)
l1.addlast(7)
l1.addlast(6)
l1.addlast(4)
print("LIST 1")
l1.displaylist()

l2.addfirst(1)
l2.addfirst(3)
l2.addlast(9)
l2.addlast(10)
l2.addlast(11)
l2.addlast(6)
print("LIST 2")
l2.displaylist()


def intersection(l1,l2):
	l=[]
	cur1 = l1.head
	cur2 = l2.head
	
	while (cur1 != None and cur2 != None):
		if (cur1.data != cur2.data):
			cur1 = cur1.next
		else:
			l.append(cur1.data)
			cur1=cur1.next

			

	#list1.append(cur.data)		
	#print(cur.data,end = '\t')			
	# list1 = set(list1)
	# list1 = list(list1)
	# print(list1)

intersection(l1,l2)
