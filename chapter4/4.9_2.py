"""
You are given a binary tree in which each node contains a value. Design an
algorithm to print all paths which sum to a given value. 

#2 : The path need not to start at the root and need not to end at leaf.

check 4_9.0.py 4.9_1.py and 4.9_3.py for other cases

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

	path = path+ [root.data]
	temp_sum = 0
	for i in range ((len(path))-1,-1,-1):
		temp_sum += path[i]
		if needed_sum == temp_sum:
			print_path(path,i,len(path)-1)

	# Check across left and right subtree
	find_paths(root.left,needed_sum,path)
	find_paths(root.right,needed_sum,path)

def print_path(path,start,end):
	for i in range(start,end + 1):
		print(path[i],end=' ')
	print()


if __name__== "__main__":

	a = node(1)
	a.left = node(2)
	a.right = node(3)
	a.left.left = node(4)
	a.left.right = node(5)
	a.right.left = node(6)
		
	needed_sum = 7
	print('needed_sum :',needed_sum)
	find_paths(a,needed_sum)

