"""
Problem : Implement a function to check whether a given binary tree is balanced

"""

__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Gayle McDowell"]
__status__  = "Prototype"


class node:
    def __init__(self,data):
        self.lchild = None
        self.rchild = None
        self.data   =  data

def is_tree_balanced(root):
	"""
	Returns hight difference at each level
	"""
	if root is None:
		return 0

	left_height = is_tree_balanced(root.lchild)
	if left_height == -1:
		return -1
	
	right_height = is_tree_balanced(root.rchild)
	if right_height == -1:
		return -1

	height_diff = left_height - right_height

	if abs(height_diff) > 1:
		return -1
	else:
		return max(left_height,right_height) + 1


def check_balance(root):
	"""
	Returns True if tree is balanced. Else returns False
	"""
	height_diff = is_tree_balanced(root)
	if height_diff == -1:
		return False
	else:
		return True

def inorder_print(root):
	if root is None:
		return
	inorder_print(root.lchild)
	print(root.data)
	inorder_print(root.rchild)


if __name__ == "__main__":

    #Test case : 1
    r = node(6)
    r.lchild = node(4)
    r.rchild = node(9)
    r.lchild.lchild = node(2)
    r.lchild.rchild = node(5)
    r.rchild.lchild = node(7)
    r.rchild.rchild = node(10)
    #inorder_print(r)
    is_balanced = check_balance(r)
    print(is_balanced)


    #Testcase 2
    s = node(6)
    s.lchild = node(4)
    s.lchild.lchild = node(2)
    s.lchild.lchild = node(5)
    print(check_balance(s))
