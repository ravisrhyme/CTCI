"""
Delete a node from a singly-linked list,given only a variable pointing to that 
node
Time complexity = O(1) with "Side Effect"

"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Interviewcake.com"]
__status__  = "Prototype"


class linked_list_node:
	def __init__(self,value):
		self.data = value
		self.next = None

def print_list(node):
	
	while node:
		print(node.data)
		node = node.next

def delete_node(node):

	next_node = node.next

	if next_node:
		node.data = next_node.data
		node.next = next_node.next
	
	else:
		raise Exception("can't delete the last node with this method")


if __name__=="__main__":
	a = linked_list_node(2)
	b = linked_list_node(3)
	c = linked_list_node(4)
	d = linked_list_node(5)

	a.next = b
	b.next = c
	c.next = d
	
	print("Before Deletion:")	
	print_list(a)
	delete_node(b)
	print("After deletion:")
	print_list(a)

