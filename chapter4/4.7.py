"""
Design an algorithm and write code to find the first common ancestor of two
nodes in a binary tree. Avoid storing additional nodes in a data structure.

Note: This is not a BST.
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

def find_fca(root,p,q):
	""" Returns the first common ancestor of two nodes with
	p,q as keys/data. Works only if both p and q are present in tree or
	if both p,q are not present in tree.
	Won't work if one is present and other is absent.
	"""
	
	if root is None:
		return None

	# If given node is either of p/q, return to previous stack indicating
	# p/q is part of that specific left/right subtree
	if root.data == p or root.data == q:
		return root
	
	# Look for keys in left and right subtree
	left_fca = find_fca(root.left,p,q)
	right_fca = find_fca(root.right,p,q)

	# If both returns non-None, it definitely means one is present in one subtree
	# and other is present in other subtree
	if left_fca and right_fca:
		return root

	# check whether left or right subtree need to traversed
	return left_fca if left_fca is not None else right_fca


def find_lca_utility(root,p,q,present):

	if root is None:
		return None
	
	if root.data == p:
		present[0] = True
		return root

	if root.data == q:
		present[1] = True
		return root


	left_fca = find_lca_utility(root.left,p,q,present)
	right_fca = find_lca_utility(root.right,p,q,present)

	if left_fca and right_fca:
		return root

	return left_fca if left_fca is not None else right_fca


def find(root,key):

	if root is None:
		return False

	elif root.data == key:
		return True

	else:
		return (find(root.left,key) or  find(root.right,key))


def find_lca_complete(root,p,q):

	""" Returns the first common ancestor of two nodes with
	p,q as keys/data.
	Will work if one is present and other is absent with the help of find()
	"""

	present = [False,False]

	node = find_lca_utility(root,p,q,present)

	if node is None: # Both p,q not part of tree
		return None

	if (present[0] and present[1]) or (present[0] and find(root,q)) or \
		(present[1] and find(root,p)): 
			return node.data
	else:
		return None


if __name__=='__main__':

	a = node(1)
	b = node(2)
	c = node(3)
	d = node(4)
	e = node(5)
	f = node(6)
	g = node(7)

	a.left = b
	a.right = c
	
	b.left = d
	b.right = e

	c.left = f
	c.right = g

	#print(find_fca(a,2,4).data)

	print(find_lca_complete(a,4,8))
	
