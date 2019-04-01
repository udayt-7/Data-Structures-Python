#class of stack


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
		if not self.isstackfull():
			self.data.append(ele)
			self.count += 1

	def stackpop(self):
		if not self.isstackempty():
			self.count -= 1
			return self.data.pop()
			
	def displaystack(self):
		print(self.data)

if __name__ == '__main__':

	l1 = LimitedStack()
	
	opt = int(input(" enter option \n 1.Push\n 2.Pop\n Any other key to exit\n"))
		

	while(opt == 1 or opt == 2):
			
		if (opt == 1):
			r = int(input("enter no of elements:"))
			while(r != 0):
				ele = input("enter the elements:\n")
				l1.stackpush(ele)
				r -= 1
				#self.data.append(ele)

		elif(opt == 2):
			l1.stackpop()


		else:
			print("invalid option")

		l1.displaystack()
		opt = int(input(" enter option \n 1.Push\n 2.Pop\n Any other key to exit\n"))
	

