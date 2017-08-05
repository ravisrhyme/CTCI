"""
Implementation of Selection sort

Time Complexity : O(n^2)
Space Complexity : O(1)
"""

__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Algorithm Design Manual","mycodeschool channel"]
__status__  = "Prototype"


def selection_sort(element_list):
	""" Sorts by using selection sort algorithm
	In every iteration, find the minimum and start swapping with element from
	index starting at 0. 
	"""
	for i in range(0, len(element_list)-1):
		minimum_element = element_list[i]
		minimal_index = i

		for j in range(i+1, len(element_list)):
			if element_list[j] < minimum_element:
				minimum_element = element_list[j]
				minimal_index = j

		swap(element_list,i,minimal_index)


def swap(element_list,i,j):
	""" Swaps the elements position i and j in list
	"""
	temp = element_list[i]
	element_list[i] = element_list[j]
	element_list[j] = temp

if __name__=='__main__':
	element_list = [9,8,7,2,3,6]
	selection_sort(element_list)
	print(element_list)

