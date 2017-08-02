"""
Implementation of merge sort.

Time Complexity  : O(nlog(n))
Space Complexity : O(n)
"""

__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Algorithm Design Manual"]
__status__  = "Prototype"



def merge_sort(element_list):
	""" Sorts a given list in Ascending order
	"""
	length_of_list = len(element_list)

	if (length_of_list < 2):
		return
	
	mid = int(length_of_list/2)
		
	left_half = element_list[:mid]
	right_half  = element_list[mid:]

	#print(left_half)
	#print(right_half)	
	merge_sort(left_half)
	merge_sort(right_half)

	merge(left_half,right_half,element_list)



def merge(left_half,right_half,element_list):
	""" Merges the given halfs in increasing order
	"""
	length_of_left = len(left_half)
	length_of_right = len(right_half)

	i = 0
	j = 0
	k = 0
	
	while i < length_of_left and j < length_of_right:
		if left_half[i] <= right_half[j]:
			element_list[k] = left_half[i]
			i += 1
		else:
			element_list[k] = right_half[j]
			j += 1
		k += 1

	while i < length_of_left:
		element_list[k] = left_half[i]
		i += 1
		k += 1

	while j < length_of_right:
		element_list[k] = right_half[j]
		j += 1
		k += 1


if __name__=='__main__':
	element_list = [9,8,7,6,5,4]
	length_of_array = len(element_list)
	merge_sort(element_list)
	print(element_list)
