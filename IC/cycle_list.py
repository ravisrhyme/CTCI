"""
You have a singly-linked list and want to check if it contains a cycle.
A singly-linked list is built with nodes, where each node has

node.next—the next node in the list.
node.value—the data held in the node. For example, if our linked list stores 
people in line at the movies, node.value might be the person's name.

Cycle occurs when a node’s next points back to a previous node in the list. The
linked list is no longer linear with a beginning and end—instead, it cycles 
through a loop of nodes.

Write a function contains_cycle() that takes the first node in a singly-linked 
list and returns a boolean indicating whether the list contains a cycle.
	
"""

__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Interviewcake.com"]
__status__  = "Prototype"


class linked_list():
	def __init__(self,value):
		self.data = value
		self.next = None


def contains_cycle(node):
	
	fast_pointer = node
	slow_pointer = node
	
	while fast_pointer is not None and fast_pointer.next is not None:
		slow_pointer = slow_pointer.next
		fast_pointer = fast_pointer.next.next

		if fast_pointer is slow_pointer:
			return True


	return False


if __name__=="__main__":

	a = linked_list(1)
	b = linked_list(2)
	c = linked_list(3)
	d = linked_list(4)


	a.next = b
	b.next = c
	c.next = d
	d.next = a

	print(contains_cycle(a))


