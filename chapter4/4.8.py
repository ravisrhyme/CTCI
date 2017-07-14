"""
You have two very large binary  trees. T1 with millions of nodes and T2 with
hundreds of nodes. Implement an algorithm to decide if T2 is a subtree of T1.

Idea1 : can be solved by making sure that inorder and pre order traversals of T2
		Subset of inorder and preorder traversals of T1.
		Time Complexity = O(n)
		Space Complexity = O(m+n) as we need to save traversal strings of both T1 
		and T2

Idea2 : Is to traverse across tree and check for match when ever both are equal.
		Time Complexity : O(n*m)
		Space Complexity : O(log(m)) as we are doing DFS. we store the max of log(m)
						   nodes if t2 is balanced or worst case of m nodes.
							 

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


def is_subtree(t1,t2):
	""" Traverses across T1. And calls find_match() when ever 
	t1 is equal to t2
	"""
	if t1 is None or t2 is None:
		return False

	if t1.data == t2.data:
		return find_match(t1,t2)
	else:
		return (is_subtree(t1.left,t2) or is_subtree(t1.right,t2))

def find_match(t1,t2):
	""" Returns True if T2 is subtree of T1.
	Else returns False 
	"""
	t2_node_stack = [t2]
	t1_node_stack = [t1]
	
	# Will do DFS iteratively and checks if T2 is subtree of T1
	# by comparing each node
	while t2_node_stack and t1_node_stack:

		current_t1 = t1_node_stack.pop()
		current_t2 = t2_node_stack.pop()
		
		if current_t1.data != current_t2.data:
			return False

		# Adds children of T1 to stack holding nodes of T1
		if current_t1.left is not None:
			t1_node_stack.append(current_t1.left)
		if current_t1.right is not None:
            t1_node_stack.append(current_t1.right)

		# Adds children of T2 to stack holding nodes of T2
		if current_t2.left is not None:
			t2_node_stack.append(current_t2.left)
		if current_t2.right is not None:
			t2_node_stack.append(current_t2.right)

	#if t2 has more nodes than the passed subtree of T1
	if len(t2_node_stack) != 0:
		return False
	
	# T2 is subtree of T1
	return True

	
if __name__== '__main__':

	# Tree T1
	a = node(1)
	a.left = node(2)
	a.right = node(3)
	a.left.left = node(4)
	a.left.right = node(5)
	a.right.left = node(6)
	a.right.right = node(7)

	# Tree T2
	b = node(2)
	b.left = node(4)
	b.right = node(6)

	print(is_subtree(a,b))
