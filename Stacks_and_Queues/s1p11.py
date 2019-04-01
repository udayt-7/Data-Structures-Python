#rotate function for queue


class flexiqueue:
	
	defualt_capacity = 2
	def __init__(self):
		self.data = [None]*flexiqueue.defualt_capacity
		self.front = 0
		self.size = 0
	
	def isqEmpty(self):
		return self.size == 0
	
	def qlength(self):
		return self.size
	
	def qcapacity(self):
		return len(self.data)
	
	def qfirst_element(self):
		if not self.isqEmpty():
			return self.data[self.front]

	def qdequeue(self):
		if not self.isqEmpty():
			element = self.data[self.front]
			self.data[self.front]=None
			self.front = (self.front+1)%len(self.data)
			self.size-=1
			if 0<self.size<len(self.data)//4:
				self.resize(len(self.data)//2)
				return element
			else:
				return element
			return element

	def qenqueue(self,ele):
		if self.size == len(self.data):
			self.resize(2*len(self.data))
		new_pos = (self.front+self.size)%len(self.data)
		self.data[new_pos]= ele
		self.size+=1



	def rotate(self):
		c = self.size
		while(c != 0):
			if not self.isqEmpty():
				element = self.data[self.front]
				print("Dequeued ele: ",element)
				self.data[self.front]=None
				self.front = (self.front+1)%len(self.data)
				#self.size-=1
				if 0<self.size<len(self.data)//4:
					self.resize(len(self.data)//2)
				
			if self.size == len(self.data):
				self.resize(2*len(self.data))
			new_pos = (self.front+self.size)%len(self.data)
			self.data[new_pos]= element
			#self.size+=1
			c -=1

	
		
	
	def resize(self,capacity):
		old_data = self.data
		walk = self.front

		self.data = [None] * capacity
		for k in range(len(old_data)):
			if(old_data[walk]!=None):

				self.data[k] = old_data[walk]
				#print(self.data[k],old_data[walk])
				walk = (walk+1)%len(old_data)
		self.front = 0

	def displayqueue(self):
		if not self.isqEmpty():
			l = []
			for ch in self.data:
				if ch != None:
					l.append(ch)
		print(l)
			
    	


if __name__ == '__main__':

	q = flexiqueue()
	q.qenqueue(1)
	q.qenqueue(2)
	q.qenqueue(3)
	q.qenqueue(4)
	q.qenqueue(5)
	q.qenqueue(6)
	q.qenqueue(7)
	q.qenqueue(8)
	q.rotate()
	
	q.displayqueue()
	











