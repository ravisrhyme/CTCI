"""
Find a duplicate, Space Edition™ BEAST MODE

Time complexity  : O(n)
Space Complexity : O(1)

Lot of wonderful observations and new derivations !
Ideas that need to be derived and shaped while solving problems.

The interpretation of list as linked list and interpretation of node
and content of node as the indication of another pointer is the first step.

"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Interviewcake.com"]
__status__  = "Prototype"

def find_duplicate(number_list):
	""" Returns the duplicate element in the given list
	"""

	length_of_list = len(number_list)
	current_position = length_of_list
	# Traverse for n times in the list to stop at some element inside cycle
	for _ in range(length_of_list):
		current_position = number_list[current_position - 1]

	#find cycle length in list
	length_of_cycle = find_cycle_length(number_list,current_position)
	#print(length_of_cycle)

	# Find head position of cycle
	head_position = find_head_of_cycle(number_list,length_of_cycle)
	
	return head_position
	
def find_cycle_length(number_list,current_position):
	""" Returns the length of cycle given the given the cycle and 
	position of any element in the cycle
	index = position - 1
	"""

	initial_position = current_position
	current_position = number_list[current_position-1]
	length_of_cycle = 1
	
	while initial_position != current_position:
		current_position = number_list[current_position-1]
		length_of_cycle += 1

	return length_of_cycle

def find_head_of_cycle(number_list,length_of_cycle):
	""" Returns the position of head of cycle given list and 
	length of cycle. 
	index = position - 1 
	"""
	
	i = 1
	length_of_list = len(number_list)
	second_pointer = number_list[length_of_list-1]
	first_pointer = number_list[second_pointer-1] 
	
	while first_pointer != second_pointer:
		if i > length_of_cycle:
			second_pointer = number_list[second_pointer-1]
		
		first_pointer = number_list[first_pointer-1]
		i += 1
		
	return first_pointer 

if __name__ == '__main__':
	number_list = [1,2,3,4,5,6,4]
	print(find_duplicate(number_list))
