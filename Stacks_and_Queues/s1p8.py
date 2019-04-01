# Design a queue using two stacks as instance variables,
# such that all queue operations execute in amortized O(1) time.

import stack1 as s

class queue:
	
	def __init__(self):
		self.data1 = s.LimitedStack()
		self.data2 = s.LimitedStack()
		self.front = 0
		self.size = 0 
	def isqEmpty(self):
		return self.data2.isstackempty()


	
	def qlength(self):
		return self.data2.stacklength()
	
	
	
	def qfirst_element(self):
		self.data2.stackpeek()

	def qdequeue(self):
		if not self.isqEmpty():
			self.data2.stackpop()
			



	def qenqueue(self,ele):
		self.data2.stackpush(ele)
	
		

		

	def displayqueue(self):
		if not self.isqEmpty():
			self.data2.displaystack()
		

if __name__ == '__main__':

	q = queue()
	q.qenqueue(1)
	q.qenqueue(2)
	q.qenqueue(3)
	q.qenqueue(4)
	q.qenqueue(5)
	q.qenqueue(6)
	q.qenqueue(7)
	q.qenqueue(8)
	

	for ch in range(q.data1.stacklength()):
		if not q.data1.isstackempty():
			
			q.data2.stackpush(q.data1.stackpop())
	
	q.qdequeue()
	q.qdequeue()
	q.displayqueue()

