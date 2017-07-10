"""
Given a sorted array with unique integer elements, write an algorithm to create
a binary search tree with minimal height.

Time Complexity : O(n)
Space Complexity : O(n)
"""

__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Gayle McDowell"]
__status__  = "Prototype"


class node:
	def __init__(self,value):
		self.data = value
		self.left = None
		self.right = None

def build_bst_from_sorted_array(sorted_array, i,j):
	
	if (j == i):
		return node(sorted_array[i])

	if (j < i):
		return None

	mid = int((i + j)/2)
	
	current_node = node(sorted_array[mid])

	current_node.left = build_bst_from_sorted_array(sorted_array,i,mid-1)
	current_node.right = build_bst_from_sorted_array(sorted_array,mid+1,j)

	return current_node


def inorder_traversal(root):

	if root is None:
		return

	inorder_traversal(root.left)
	print(root.data)
	inorder_traversal(root.right)


if __name__=='__main__':
	
	array = [1,2,3,4,5,6]

	root = build_bst_from_sorted_array(array,0,len(array)-1)
	inorder_traversal(root)
