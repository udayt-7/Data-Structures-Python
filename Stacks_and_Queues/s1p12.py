#Give an array based implementation of double-ended queue supporting behaviors 
#like len (), add_first(), add_last(), delete_first(), delete_last(), first() and last().
# Double-ended queue should be of fixed capacity. 
#When queue is full, inserting element from 
#one end should cause an element to be lost from the opposite side.

class queue:
	
	defualt_capacity = 5
	def __init__(self):
		self.data = [None]*queue.defualt_capacity
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

	def qdequeue_first(self):
		if not self.isqEmpty():
			element = self.data[self.front]
			self.data[self.front]=None
			self.front = (self.front+1)%len(self.data)
			self.size-=1
		return element
	def qenqueue_last(self,ele):
		#print(self.front)
		if self.size == len(self.data):
			self.data[self.front] = None
			self.front = (self.front+1)%len(self.data) 
			self.size-=1

		#print(self.front,self.size)	
		new_pos = (self.front+self.size)%len(self.data)
		self.data[new_pos]= ele
		self.size+=1
		#print(self.front,self.size)
	def qenqueue_first(self,ele):
		if self.qlength() == 0:
			print(self.front)
			self.data[self.front] = ele
			print(self.data)
			self.size+=1
		else:
	

			new_pos = (self.front-1)%len(self.data)
			self.data[new_pos]= ele
			self.size+=1
		#print(new_pos,self.front)

	
	

	def displayqueue(self):
		if not self.isqEmpty():
			print(self.data)
		
			
    	


if __name__ == '__main__':

	q = queue()
	#q.qenqueue_last(1)
	#q.qenqueue_last(2)
	#q.qenqueue_last(3)
	#q.qenqueue_last(4)
	#q.qenqueue_last(5)
	#q.qenqueue_last(6)
	#q.qenqueue_last(7)
	q.qenqueue_first(8)
	q.qenqueue_first(9)
	#r = q.qdequeue()
	#print(r)
	#q.qdequeue_first()
	q.displayqueue()
	print(q.qlength())