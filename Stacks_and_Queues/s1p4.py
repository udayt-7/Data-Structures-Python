#Implement a transfer function and two temporary stacks, 
##to replace the contents of a given stack S with those same elements, but in reverse order.

import stack1

s1 = stack1.LimitedStack()
s2 = stack1.LimitedStack()
s3 = stack1.LimitedStack()

m = int(input("Size of stack:"))


for ch in range(m):
	ele = int(input("enter element:"))
	s1.stackpush(ele)
print(s1.data)

def transfer(s1,s2):

	for ch in range(m):
		s2.stackpush(s1.stackpop())
		print(s2.data)
		s3.stackpush(s2.stackpop())
	
	print(s3.data)

transfer(s1,s2)