#1.Create a single list with methods to add and delete elements from head and tail positions. 
##Provide method to check whether an element is present in the list. Count number of elements in the list.

import link1

l1 = link1.Llist()



l1.addfirst(1)
l1.addfirst(11)
l1.addlast(33)
l1.addlast(43)
l1.addlast(53)
l1.addlast(63)
l1.displaylist()

l1.addany(2,45)
l1.displaylist()
l1.addany(6,95)
l1.displaylist()

l1.delfirst()
print("\n\nAfter deleting first element:")
l1.displaylist()

l1.dellast()
print("\n\nAfter deleting last element:")
l1.displaylist()
