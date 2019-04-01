#  Implement LeakyStack. This stack should be of fixed size. When push is invoked with the stack at 
#full capacity, rather than throwing a Full exception, 
#accept the pushed element at the top while “leaking” the oldest element 
#from the bottom of the stack to make a room.


class leaky_stack:
	capacity = 5
	
	def __init__(self):
		self.data = []
		self.count = 0
	
	def isstackempty(self):
		return self.count == 0
	
	def isstackfull(self):
		return self.count == leaky_stack.capacity
	
	def stacklength(self):
		return self.count

	def stackpeek(self):
		if not self.isstackempty():
			return self.data[-1]

	def stackpush(self,ele):
		if self.isstackfull():
			
			self.data.pop(0)
			self.count-=1 

		self.data.append(ele)
		self.count+=1
			

	def stackpop(self):
		if not self.isstackempty():
			self.count-=1
			return self.data.pop()
			
			
	def displaystack(self):
		print(self.data)

if __name__ == '__main__':
	s1 = leaky_stack()
	s1.stackpush(1)
	s1.stackpush(2)
	s1.stackpush(3)
	s1.stackpush(4)
	s1.stackpush(5)
	s1.stackpush(6)
	s1.stackpush(7)
	s1.stackpush(8)
	s1.displaystack()
	

	

	
