#Design a stack using a single queue as an instance variable, 
#and only constant additional local memory within the method bodies.

import queue1 as q

class Stack:
	
	def __init__(self):
		self.data = q.flexiqueue()
	
	def isstackempty(self):
		return self.data.isqEmpty()
	
	
	def stacklength(self):
		return self.data.qlength()

	
	def stackpush(self,ele):
		c = []
		for ch in range(self.data.qlength()):
			k = self.data.qdequeue()
			c.append(k)

		print(c)


		self.data.qenqueue(ele)

		for ch in c:
			self.data.qenqueue(ch)
	
	def stackpop(self):
		if not self.isstackempty():
			self.data.qdequeue()
			
			
	def displaystack(self):
		self.data.displayqueue()
		

if __name__ == '__main__':


	s1 = Stack()
	s1.stackpush(1)
	s1.stackpush(2)
	s1.stackpush(3)
	s1.stackpush(4)
	s1.stackpush(4)
	s1.stackpush(5)
	s1.stackpush(6)
	s1.stackpop()
	s1.stackpop()
	s1.displaystack()
