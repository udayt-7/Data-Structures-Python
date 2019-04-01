#Suppose you have three nonempty stacks R, S and T. Describe a sequence of operations that results in 
##S storing all elements originally in T below of S’s original elements, with both sets of those elements in their original configuration. 
###For example, if R = [1,2,3], S = [4, 5] and T = [6, 7, 8, 9], the final configuration should have R = [1, 2, 3] and S = [6, 7, 8,  9, 4, 5].


import stack1

s1 = stack1.LimitedStack()
s2 = stack1.LimitedStack()
s3 = stack1.LimitedStack()

m = int(input("Size of stack 1:"))
n = int(input("Size of stack 2:"))
o = int(input("Size of stack 3:"))


for ch1 in range(m):
	ele1 = int(input("enter elements of s1:"))
	s1.stackpush(ele1)


for ch2 in range(n):
	ele2 = int(input("enter elements of s2:"))
	s2.stackpush(ele2)


for ch3 in range(o):
	ele3 = int(input("enter elements of s3:"))
	s3.stackpush(ele3)

print(s1.data)
print(s2.data)
print(s3.data)

def seq(s1,s2,s3):

	cont = s1.stacklength()

	while not s2.isstackempty():
		s1.stackpush(s2.stackpop())

	while not s3.isstackempty():
		s1.stackpush(s3.stackpop())
	
	while s1.stacklength()>cont:
		s2.stackpush(s1.stackpop())
	
	
	print("\n\n",s1.data)
	print(s2.data)
	
	
seq(s1,s2,s3)