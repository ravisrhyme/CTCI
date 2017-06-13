"""
Write a function to see if a binary tree is "superbalanced".
A tree is "superbalanced" if the difference between the depths of any two leaf 
nodes is no greater than one.
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


def is_superbalanced(root):
	""" DFS implemented in iterative way
	depth to every leaf is tracked in the below logic.
	if there are more than two different depths to leafs,this fuction returns False
	Also if the absolute difference between two depths is greater than one,
	it will return False. 
	"""
	depths = []
	
	depth = 0 
	node_list = [(root,depth)]

	while (len(node_list) != 0):
		node, depth = node_list.pop()
		
		if node.left_child == None and node.right_child == None:
			
			if depth not in depths:
				depths.append(depth)
			
			if (len(depths) > 2 or(len(depths) == 2 and  (abs(depths[0]-depths[1]) > 1))):
				return False

		else:
			if node.left_child is not None:
				node_list.append((node.left_child,depth + 1))
			if node.right_child is not None:
				node_list.append((node.right_child,depth + 1))
				
	return True	


if __name__=="__main__":

	#Positive test case
	root = Node(1)
	root.left_child = Node(2)
	root.right_child = Node(3)
	root.left_child.left_child = Node(4)
	root.left_child.right_child = Node(5)
	root.right_child.left_child = Node(6)
	root.right_child.right_child = Node(7)
	print(is_superbalanced(root))
	
	#Negatve test case
	root = Node(1)
	root.left_child = Node(2)
	root.right_child = Node(3)
	root.left_child.left_child = Node(4)
	root.left_child.right_child = Node(5)
	root.left_child.left_child.left_child = Node(6)
	root.left_child.left_child.right_child = Node(7)
	print(is_superbalanced(root))
