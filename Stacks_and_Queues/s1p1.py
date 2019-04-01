#Implement a function with signature transfer(S,T) that transfers all elements from Stack S onto Stack T,
  #so that that elements that starts at the top of S is the first to be inserted into T, and element at the bottom of S ends up at the top of T.




import stack1

s = stack1.LimitedStack()
t = stack1.LimitedStack()

m = int(input("Size of stack:"))

def signtransfer(s,t):

	for ch in range(m):
		t.stackpush(s.stackpop())
	print(t.data)

for ch in range(m):
	ele = int(input("enter element"))
	s.stackpush(ele)
print(s.data)

signtransfer(s,t)
