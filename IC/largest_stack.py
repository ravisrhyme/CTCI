"""
You want to be able to access the largest element in a stack.

Implement a new class MaxStack with a function get_max() that returns the largest
element in the stack. get_max() should not remove the item.
"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Interviewcake.com"]
__status__  = "Prototype"


class max_stack:
	def __init__(self):
		self.stack = []
		self.largest = -1

	def push(self,item):
		self.stack.append((item,self.largest))
		if item > self.largest:
			self.largest = item

	def pop(self):
		item, next_largest = self.stack.pop()
		
		if (item == self.largest):
			self.largest = next_largest
		return item

	def get_max(self):
		return self.largest


if __name__=='__main__':
	ms = max_stack()
	ms.push(1)
	ms.push(2)
	ms.push(3)
	print(ms.get_max())
	print(ms.pop())
	print(ms.get_max())
	print(ms.pop())
	print(ms.get_max())
	print(ms.pop())
	print(ms.get_max())
