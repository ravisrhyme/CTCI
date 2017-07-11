"""
Given a binary tree,design an algorithm which creates a linked list of all the
nodes at each depth. 

Eg : If you have tree of depth D, you will have D linkedlists)

Time complexity = O(n)
Space Complexity = O(n)
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

node_list = [[]]
def make_list(root):

	node_queue = [(root,0)]

	while node_queue:
		current_node,depth = node_queue.pop(0)

		insert_node_in_list(current_node.data,depth)
		
		if current_node.left:
			node_queue.append((current_node.left,depth+1))

		if current_node.right:
			node_queue.append((current_node.right,depth+1))

def insert_node_in_list(value,index):

	#print(value," ",index)

	if index > len(node_list)-1:
		node_list.append([])

	node_list[index].append(value)



if __name__ == "__main__":

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

	make_list(a)

	print(node_list)
