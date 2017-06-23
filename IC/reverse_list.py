"""
Hooray! It's opposite day. Linked lists go the opposite way today.
Write a function for reversing a linked list. Do it in-place.

Your function will have one input: the head of the list.

Your function should return the new head of the list.

Time complexity  : O(n)
space complexity : O(1)
"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Interviewcake.com"]
__status__  = "Prototype"

class linked_list:
	def __init__(self,value):
		self.data = value
		self.next = None


def reverse_list(head):
	"""
	Returns the head of list after reversing passed list.
	"""

	previous_node = None
	current_node  = head
	
	# Reverses one link at a time starting from head
	while current_node is not None:
		temp = current_node.next #Copying the next node before changing the pointer
		current_node.next = previous_node # changing pointer to previous
		previous_node = current_node # Marking current node as previous for next iteration
		current_node = temp # Marking next node as current for next iteration

	return previous_node # Return the head of reversed list


def print_list(head):

	while head is not None:
		print(head.data)
		head = head.next



if __name__=='__main__':

	a = linked_list(1)
	b = linked_list(2)
	c = linked_list(3)
	d = linked_list(4)
	
	a.next = b
	b.next = c
	c.next = d

	print("Actual List")
	print_list(a)
	x = reverse_list(a)
	print("\nReversed list")
	print_list(x)
