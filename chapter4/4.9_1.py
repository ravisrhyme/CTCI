"""
You are given a binary tree in which each node contains a value. Design an
algorithm to print all paths which sum to a given value. 

#1 : The path need to start at the root and need not to end at leaf.

check 4.9_0.py 4.9_2.py and 4.9_3.py for other cases

Time Complexity : O(n)
Space Complexity : O(log(n)) for balanced tree
				   else O(n) in worst case

"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Gayle McDowell"]
__status__  = "Prototype"


class node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

def find_paths(root,needed_sum, path = []):

	""" Prints all the paths starting from root to nodes, that lead to
	given sum
	"""
	if root is None:
		return 
	# Checks if current path till current node leads to needed sum
	# subtracting root.data is required to make sure of current data
	# else it will be printed only when chekcing for either children
	# and will be printed twice	
	if (needed_sum - root.data) == 0:
		print(path + [root.data])

	# Check across left and right subtree
	find_paths(root.left,(needed_sum-root.data),path+[root.data])
	find_paths(root.right,(needed_sum-root.data),path+[root.data])



if __name__== "__main__":

	a = node(1)
	a.left = node(2)
	a.right = node(6)
	a.left.left = node(4)
	a.left.right = node(5)
	a.right.left = node(7)

	find_paths(a,7)

