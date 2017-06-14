"""
Write a function to find the 2nd largest element in a binary search tree 
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
		
def find_largest_recursive(root):
	""" Recurcively finds the largest element in the Binary Search Tree
	"""
	if root.right_child:
		return find_largest(root.right_child)
	return root.data

def find_largest_iterative(root):
	
	node = root
	
	while node:
		if not node.right_child:
			return node.data
		node = node.right_child


def find_second_largest_iterative(root):
	current = root
	parent_data = None
	
	if (current is None) or (current.right_child is None and current.left_child is None):
		return parent_data

	while current:
		if current.right_child:
			parent_data = current.data

		else:
			if current.left_child is not None:
				return find_largest_iterative(current.left_child)
			else:
				return parent_data

		current = current.right_child

def find_second_largest_recursive(root,parent_data = None):
	""" Recursively returns the second largest element in the BST
	"""

	if root.right_child is None: # No right child
		if root.left_child is not None: 
			return find_largest(root.left_child)
		else :  # leaf node i.e both left and right children are None
			return parent_data

	else: # Have a right child
		parent_data = root.data
		return find_second_largest(root.right_child,parent_data)
		
	


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
	print(find_largest_iterative(root))
	print(find_second_largest_iterative(root))
