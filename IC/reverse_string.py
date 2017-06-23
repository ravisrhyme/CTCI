"""
Write a function to reverse a string in-place

Time Complexity  = O(n)
Space Complexity = O(1)
"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Interviewcake.com"]
__status__  = "Prototype"


def reverse_string(string):

	# Converting to list of characters as string is Immutable in python 	
	string_list = list(string)
	
	first_pointer = 0
	last_pointer = len(string) - 1

	while first_pointer < last_pointer: # swapping characters
		temp = string_list[first_pointer]
		string_list[first_pointer] = string_list[last_pointer]
		string_list[last_pointer] = temp
		first_pointer += 1
		last_pointer  -= 1

	return ''.join(string_list)


if __name__=='__main__':
	string = 'ravikiran'
	print(reverse_string(string))
