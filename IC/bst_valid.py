"""
Write a function to check that a binary tree is a valid binary search tree
Time Complexity = O(n) 
Space complexity = O(log(n)) if tree is balanced/ O(h) else where 'h' is height
"""

__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Interviewcake.com"]
__status__  = "Prototype"


class Node:
	def __init__(self,value):
		self.data = value
		self.left_child = None
		self.right_child = None


def is_bst_valid(root):
	""" Checking whether a given BST is valid
	keep track of lower_bound and upper_bound for everynode
	Interesting pattern !!
	"""

	if root is None:
		return True

	node_and_bounds_stack = [(root,-float('inf'),float('inf'))]

	while len(node_and_bounds_stack) != 0:
		
		node,lower_bound,upper_bound = node_and_bounds_stack.pop()
		if node.data < lower_bound or node.data > upper_bound:
			return False
		
		if node.left_child is not None:
			node_and_bounds_stack.append((node.left_child,lower_bound,node.data))
		if node.right_child is not None:
			node_and_bounds_stack.append((node.right_child,node.data,upper_bound))

	return True

def is_bst_valid_recursive(root,lower_bound=-float('inf'),upper_bound=float('inf')):
	"""Implementation of is_bst_valid() fucntion recursively
	with same logic.Recursion takes care of stack here and no need to use stack 
	explicitly
	""" 
	if not root:
		return True

	if root.data < lower_bound or root.data > upper_bound:
		return False

	return is_bst_valid_recursive(root.left_child,lower_bound,root.data) \
			and is_bst_valid_recursive(root.right_child,root.data,upper_bound)
		


if __name__ == "__main__":

	#Positive test case
	root = Node(50)
	root.left_child = Node(30)
	root.right_child = Node(80)
	root.left_child.left_child = Node(20)
	root.left_child.right_child = Node(40)
	root.right_child.left_child = Node(70)
	root.right_child.right_child = Node(90)
	print(is_bst_valid(root))
	print(is_bst_valid_recursive(root))

	#Negative test case
	root = Node(1)
	root.left_child = Node(2)
	root.right_child = Node(3)
	root.left_child.left_child = Node(4)
	root.left_child.right_child = Node(5)
	root.right_child.left_child = Node(6)
	root.right_child.right_child = Node(7)
	print(is_bst_valid(root))
	print(is_bst_valid_recursive(root))
