"""
Implementation of binary heap(min)

A complete binary tree can be stored by using single List
  
                    Insert      extract_min  find_min  search  delete
Time Complexity  :  O(log(n))   O(log(n))    O(1)      O(n)    O(log(n))

Space Complexity : O(n)
"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Algorithm Design Manual","interactivepython.org"]
__status__  = "Prototype"


class binary_heap:
	""" Implementation of binary heap
	"""
	def __init__(self):
		self.heaplist = [0]
		self.current_size = 0

	def insert(self,key):
		""" Inserts an element in to heap
		"""
		self.heaplist.append(key)
		self.current_size += 1
		self.bubble_up(self.current_size)

	def bubble_up(self,i):
		""" Utility for insert() function.
		Bubbles up till top making sure heap-order property is restored
		"""		
		while i // 2 > 0: # // Used for integer division in python3
			if self.heaplist[i] < self.heaplist[i // 2]:
				temp = self.heaplist[i]
				self.heaplist[i] = self.heaplist[i // 2]
				self.heaplist[i // 2] = temp
			i = i // 2

	def extract_min(self):
		""" Returns the minimum value from the heap
		"""
		min_value = self.heaplist[1]
		self.heaplist[1] = self.heaplist[self.current_size]
		self.current_size -= 1
		self.heaplist.pop()
		self.bubble_down(1) # Bubble down
		return min_value


	def bubble_down(self,i):
		""" Utility for extract_min() function
		Bubbles down the top element till heap-order property is restored 
		"""
		while i * 2 < self.current_size:
			min_child_index = self.find_min_child_index(i)

			if self.heaplist[i] > self.heaplist[min_child_index]:
				temp = self.heaplist[i]
				self.heaplist[i] = self.heaplist[min_child_index]
				self.heaplist[min_child_index] = temp

			i = min_child_index

	def find_min_child_index(self,i):

		if i * 2 + 1 > self.current_size:
			return i * 2

		if self.heaplist[i * 2] < self.heaplist[(i * 2) + 1]:
			return 2 * i
		else:
			return (2 * i) + 1

	def build_heap(self,element_list):
		""" Builds heap 
		"""
		# Takes O(nlog(n)) time	
		#for element in element_list:
			#self.insert(element)

		# Takes O(n) time
		self.current_size = len(element_list)
		i = self.current_size // 2
		self.heaplist.extend(element_list)

		# Interesting observation and Idea !! :)
		# half the elements will be leafs at max in complete
		# binary trees like heaps. So traversing across the first half and 
		# bubbling down each element  
		while i > 0:
			self.bubble_down(i)
			i -= 1			
		
		 
if __name__== '__main__':

	element_list = [3,2,1]

	h = binary_heap()

	h.build_heap(element_list)
	print(h.extract_min())
