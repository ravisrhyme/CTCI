"""
You are given a binary tree in which each node contains a value. Design an
algorithm to print all paths which sum to a given value. 

#0 : The path need to start at the root and end at leaf

check 4.9_1,4.9_2 and 4.9_3 for other cases

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
	# Check for path sum at every leaf node
	if root.left is None and root.right is None:

		# Checks if current path till leaf node leads to needed sum
		# subtracting root.data is required to make sure of current data
		if (needed_sum - root.data) == 0:
			print(path + [root.data])
		return

	# Check across left and right subtree. Conditions are necesessary to take
	# care of node with only one child.
	if root.left:
		find_paths(root.left,(needed_sum-root.data),path+[root.data])
	if root.right :
		find_paths(root.right,(needed_sum-root.data),path+[root.data])


if __name__== "__main__":

	a = node(1)
	a.left = node(2)
	a.right = node(3)
	a.left.left = node(4)
	a.left.right = node(5)
	a.right.left = node(6)

	find_paths(a,7)

