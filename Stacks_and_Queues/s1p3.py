##Modify ArrayStack implementation so that the stack’s capacity is limited to maxlen elements. 
#If push is called when the stack is at full capacity, throw a Full exception.

import sys

class LimitedStack:
	capacity = 10
	

	def __init__(self):
		self.data = []
		self.count = 0
		self.value = []

	def isstackempty(self):
		return self.count == 0

	def isstackfull(self):
		
		return self.count == LimitedStack.capacity

	def stacklength(self):
		return self.count

	def stackpeek(self):
		if not self.isstackempty():
			return self.data[-1]

	def stackpush(self,ele):
		#if not self.isstackfull():
			try:
				if(self.count != LimitedStack.capacity):
					self.data.append(ele)
					self.count += 1
				else:
					raise Exception("stack overflow !!!")
			
			except Exception as e:
				print(e)
				sys.exit()
			
	def stackpop(self):
		if not self.isstackempty():
			self.count -= 1
			return self.data.pop()
			
	def displaystack(self):
		print(self.data)

if __name__ == '__main__':

	l1 = LimitedStack()
	
	opt = int(input("Press 1 to push"))
	c =0	

	while(opt == 1):
			
		if (opt == 1):
			capacity = int(input("Max capacity is 10, enter 10 to input numbers:"))
			while(capacity != 0):
				#if (c>=capacity):	
				ele = input("enter the elements:\n")
				l1.stackpush(ele)
				c += 1
		
		l1.displaystack()