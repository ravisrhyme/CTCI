"""
Write a function for doing an in-place shuffle of a list.
The shuffle must be "uniform," meaning each item in the original list must have
the same probability of ending up in each spot in the final list.

Assume that you have a function get_random(floor, ceiling) for getting a random
integer that is >= floor and <= ceiling.

Time Complexity  = O(n)
Space Complexity = O(1)
"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Interviewcake.com"]
__status__  = "Prototype"

import random

def get_random(floor,ceiling):
	return random.randrange(floor, ceiling+1)

def shuffle(item_list):
	
	length = len(item_list)
	
	if length <= 1:
		return item_list
	
	last_element_index = length - 1 # pointing to last element in the list 

	for current_starting_index in range(0,last_element_index):
		random_index = get_random(current_starting_index, last_element_index)

		if random_index != current_starting_index:
			item_list[current_starting_index], item_list[random_index] = item_list[random_index], \
																		  item_list[current_starting_index]

	return item_list

if __name__ == '__main__':
	item_list = [1,2,3,4,5,6]
	print(item_list)
	print(shuffle(item_list))
														
