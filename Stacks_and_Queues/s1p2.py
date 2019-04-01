#Implement a function that reverses a list of elements 
##by pushing them onto a stack in one order, and write them back to the list in reversed order.

import stack1

s = stack1.LimitedStack()
t = stack1.LimitedStack()

m = int(input("Size of stack:"))

def reverse(s,t):

	for ch in range(m):
		t.stackpush(s.stackpop())
	print(t.data)

for ch in range(m):
	ele = int(input("enter element:"))
	s.stackpush(ele)
print(s.data)

reverse(s,t)
