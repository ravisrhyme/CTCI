"""
You have a linked list and want to find the kth to last node.

Write a function kth_to_last_node() that takes an integer kk and the head_node of
a singly linked list, and returns the kth to last node in the list.

Time  Complexity = O(n)
Space Complexity : O(1)
Done in a single pass

"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Interviewcake.com"]
__status__  = "Prototype"

class linked_list:
	def __init__(self,value):
		self.data = value
		self.next = None

def kth_to_last_node(head,k):
	""" Returns the Kth element from last node
	"""
	
	first_pointer  = head
	second_pointer = head
	i = 0

	while first_pointer :

		if ( i >  k ):
			second_pointer = second_pointer.next
		
		first_pointer = first_pointer.next
		i += 1
	
	if (i <= k):
		raise Exception("Length of list less than k")
	else :
		return second_pointer

if __name__=='__main__':

	a = linked_list(1)
	b = linked_list(2)
	c = linked_list(3)
	d = linked_list(4)

	a.next = b
	b.next = c
	c.next = d

	node = kth_to_last_node(a,0)
	print(node.data)
