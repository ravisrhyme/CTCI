"""
Write an algorithm to find the 'next' node (i.e in-order successor) of a given
node in a binary search tree. You may assume that each node has a link to its
parent.

There are three cases one can think of for this problems:

1. If 'n' has the right subtreei, then return the left most element of right 
   subtree

2. If 'n' doesn't have right subtree and is the left child of its parent(q). We
   should return 'q' in such case

3. If 'n' doesn't have right subtree and is the right child of its parent(q).We
   need to traverse up the parent of q till we reach the node for which we are 
   left sub-tree. 

These cases make this problem tricky to write code !!

Three function takes care of the three cases. Felt it to be more cleaner way.

Time complexity : O(logn) for a balanced BST, else can go to O(n)
Space Complexity : O(logn) for a balanced BST, else can go to O(n)

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
		self.parent = None

def find_in_order_successor(node):
	""" Returns the in-order successor of a node in a
	given binary search tree
	"""
	# Case 1	
	if node.right:
		return find_left_most_child(node.right)
	#Case 2
	elif node == node.parent.left:
		return node.parent
	#Case 3
	else:
		return find_parent_with_node_as_left_child(node)



def find_left_most_child(node):

	if node.left:
		return find_left_most_child(node.left)

	else:
		return node

def find_parent_with_node_as_left_child(node):
	
	if node.parent is None:
		return None

	elif node == node.parent.left:
		return node.parent

	else:
		return find_parent_with_node_as_left_child(node.parent)


if __name__=='__main__':

	a = node(4)
	b = node(2)
	c = node(1)
	d = node(3)
	e = node(6)
	f = node(5)
	g = node(7)
	h = node(10)

	i = node(16)


	a.left = b
	a.right = e
	a.parent = h


	b.left = c
	b.right = d
	b.parent = a

	c.parent = b
	d.parent = b
	
	e.parent = a
	#root node
	h.left = a
	h.right = i
	
	i.parent = h

	print(find_in_order_successor(e).data)

