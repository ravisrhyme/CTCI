"""
You have a stack of n boxes, with width w(i),height h(i), depth d(i). The boxes
cannot be rotated and can only be stacked on top of one another if each box in 
the stack is strictly larger than the box above it in width,height and depth.

Implement a method to build the tallest stack possible,where the height of stack 
is the sum of the heights of each box.

Time Complexity  :
Space Complexity :   
"""

__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Cracking The coding interview"]
__status__  = "Prototype"



def find_tallest_stack(boxes, bottom):
	""" Returns the tallest stack
	"""
	max_height = 0
	max_stack = []
	for box in boxes:
		if (is_valid(box,bottom)):
			current_stack = find_tallest_stack(boxes, box)
			current_height = len(current_stack)	
			
			if current_height > max_height:
				max_height = current_height
				max_stack = current_stack

	if len(bottom):
		max_stack.append(bottom)

	return max_stack

def is_valid(box,bottom):
	if len(bottom) == 0:
		return True

	elif box[0] > bottom[0] and \
		 box[1] > bottom[1] and \
		 box[2] > bottom[2]:
		return True

	else:
		return False

if __name__=='__main__':

	boxes = [[1,2,3]
			 [4,5,6]
			]
