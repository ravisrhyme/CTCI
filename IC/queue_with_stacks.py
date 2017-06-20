"""
Implement a queue with 2 stacks. Your queue should have an enqueue and a dequeue
function and it should be "first in first out" (FIFO).
Optimize for the time cost of mm function calls on your queue. These can be any
mix of enqueue and dequeue calls.

Assume you already have a stack implementation and it gives O(1) time push and 
pop.
"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Interviewcake.com"]
__status__  = "Prototype"


class queue_with_two_stacks:
	def __init__(self):
		# Assuming the size of queue to be infinity
		self.s1 = []
		self.s2 = []

	def enqueue(self,value):
		self.s1.append(value)
	
	def dequeue(self):
		if len(self.s2) == 0:
			length = len(self.s1)
			if length == 0:
				raise IndexError("Queue is Empty")
			while (length > 0):
				self.s2.append(self.s1.pop())
				length -= 1
		return self.s2.pop()



if __name__=="__main__":
	q = queue_with_two_stacks()
	q.enqueue(1)
	q.enqueue(2)
	q.enqueue(3)
	print(q.dequeue())
	print(q.dequeue())
	print(q.dequeue())
	print(q.dequeue())
