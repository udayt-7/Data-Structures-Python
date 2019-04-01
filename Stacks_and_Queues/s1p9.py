##Design a double-ended queue using two stacks as instance variables.


import stack1 as s

class denqueue():
	
	def __init__(self):
		self.data1 = s.LimitedStack()
		self.data2 = s.LimitedStack()
	
	def isEmpty(self):
		return self.data1.isstackempty() or self.data2.isstackempty()


	def qlength(self):
		s1 = self.data1.stacklength()
		s2 = self.data2.stacklength()
		return s1+s2

	def enqueue_from_back(self,ele):
		self.data1.stackpush(ele)


	def dequeue_from_back(self):
		self.data1.stackpop()

	def enqueue_from_front(self,ele):
		while not self.data1.isstackempty():
			self.data2.stackpush(self.data1.stackpop())

		self.data2.stackpush(ele)
		
		while not self.data2.isstackempty():
			self.data1.stackpush(self.data2.stackpop())

	def dequeue_from_front(self):
		while not self.data1.isstackempty():
			self.data2.stackpush(self.data1.stackpop())

		self.data2.stackpop()

		while not self.data2.isstackempty():
			self.data1.stackpush(self.data2.stackpop())

	def displayqueue(self):
		self.data1.displaystack()

if __name__ == '__main__':
	

	d = denqueue()
	d.enqueue_from_front(1)
	d.enqueue_from_front(2)
	d.enqueue_from_front(3)
	d.enqueue_from_front(4)
	d.enqueue_from_back(5)
	d.enqueue_from_back(6)
	d.dequeue_from_front()
	d.dequeue_from_back()
	d.displayqueue()







