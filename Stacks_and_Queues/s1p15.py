'''15.   Design an ADT for a two-color, double-stack ADT that consists of two stacks – one “red” and one “blue” – and has as its operations 
#color-coded versions of the regular stack ADT operations. For example, this ADT should support both a red push operation and a blue push operation.
#Give an efficient implementation of this ADT 
#using single array whose capacity is set at some value N that is assumed to always be larger than the sizes of 
the red and blue stacks combined.'''

class limitedStack:
	capacity=10
	def __init__(self):
		self.data=[None] * limitedStack.capacity
		self.count1=0
		self.count2=limitedStack.capacity//2

	def redstackempty(self):
		return self.count1 == 0 

	def bluestackempty(self):
		return self.count2 == 0 


	def redstackfull(self):
		return self.count1 == limitedStack.capacity//2

	def bluestackfull(self):
		return self.count2 == limitedStack.capacity

	def redstacklength(self):
		return self.count1

	def bluestacklength(self):
		return self.count2

	def redstackpeek(self):
		if not self.isstackempty():
			return self.data[self.count1-1]

	def bluestackpeek(self):
		if not self.isstackempty():
			return self.data[-1]

	def redstackpush(self,ele):
		if not self.redstackfull():
			self.data.append(ele)
			self.count1 += 1

	def bluestackpush(self,ele):
		if not self.bluestackfull():
			#print(self.data)
			self.data[self.count2] = ele
			self.count2 += 1


	def redstackpop(self):
		if not self.redstackempty():
			red = self.data.pop()
			self.count1 -= 1
			return red

	def bluestackpop(self):
		if not self.bluestackempty():
			blue = self.data.pop(self.count2-1)
			self.count2 -= 1
			return blue


	def displayredstack(self):
		temp=self.count1
		while temp !=0:
			print(self.data[temp])
			temp -= 1

		print(self.data)

	def displaybluestack(self):
		temp=self.count2
		while temp !=0:
			print(self.data[temp])
			temp -= 1

if __name__ == "__main__":
	so=limitedStack()
	while True:
		print("enter 1.Redpush 2.BluePush 3.RedPop 4.BluePop 5.Red display 6.Blue display 7.exit")
		ch=int(input())
		if (ch == 1):
			ele=input("enter the element:  ")
			so.redstackpush(ele)	
		elif (ch == 2):
			ele=input("enter the element:  ")
			so.bluestackpush(ele)
		elif (ch == 3):
			so.redstackpop()
		elif (ch == 4):
			so.bluestackpop()
		elif (ch == 5):
			so.displayredstack()
		elif (ch == 6):
			so.displaybluestack()
		else:
			break
	#so.displaystack()
