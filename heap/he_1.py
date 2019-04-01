# 1. Build maximum heap with required methods. It should support the behaviors like adding
# element, getting maximum element, extracting maximum element, count number of elements
# # and to check the method to test the heap order property.



class max_heap:
	def __init__(self,mylist = []):
		self.data = mylist
		self._buildheap()
	def isempty(self):
		return len(self.data) == 0
	
	def _length(self):
		return len(self.data)
	
	def _parent(self,j):
		return (j-1)//2 
	
	def _leftchild(self,j):
		return (2*j+1)
	
	def _rightchild(self,j):
		return(2*j+2)
	
	def _swap(self,i,j):
		self.data[i],self.data[j]=self.data[j],self.data[i]
	
	def _upheap(self,j):
		parent = self._parent(j)

		if j>0 and self.data[j] > self.data[parent]:

			self._swap(j,parent)
			self._upheap(parent)


	def _downheap(self,j,size):
		if self._leftchild(j)< size:
			left = self._leftchild(j)
			largechild = left
			if self._rightchild(j) < size:
				right = self._rightchild(j)
				if self.data[right] > self.data[left]:
					largechild = right


			if self.data[largechild]> self.data[j]:
				self._swap(largechild,j)
				self._downheap(largechild,size)


	def _buildheap(self):
		start = (self._length()-2)//2
		for i in range(start,-1,-1):
			self._downheap(i,self._length())


	def heap_add(self,ele):
		self.data.append(ele)
		self._upheap(self._length()-1)
	
	def ascOrder(self):
		length=self._length()
		for i in range(self._length()-1, -1, -1):
			self._swap(0,i)
			# self._downheap(0,length-2)
			self._downheap(0,i)
	def printheap(self):
		print(self.data)

	def get_max(self):
		return self.data[0]
	def extract_max(self):
		
		self._swap(0,self._length()-1)
		print(self.data.pop())
		self._buildheap()

if __name__ == '__main__':
	m = max_heap([15,6,10,7,17,12])
	#m.heap_add(10)
	m.ascOrder()
	m.printheap()
	# print(m.get_max())
	# m.extract_max()
	# m.printheap()
