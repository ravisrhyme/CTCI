"""
Implementation of insertion sort

Time Complexity : O(n^2)
Space Complexity : O(1)
"""

__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Algorithm Design Manual","mycodeschool channel"]
__status__  = "Prototype"


def insertion_sort(element_list):
	""" Sorts by using insertion sort algorithm
	In every iteration w.r.t outer loop, we compare it with all
	previous elements, one at a time, a keep shifting left if element_list[i]
	is less than previous element.(Important to note that we swap one element at
	a time startign with immediate previous element. 
	"""
	for i in range(1, len(element_list)): # Traverse across all elements
		for j in range(i,0,-1): # Traverse across all previous elements.
			if element_list[j] < element_list[j-1]: # Swap if current is less than previous
				swap(element_list,j,j-1)


def swap(element_list,i,j):
	""" Swaps the elements position i and j in list
	"""
	temp = element_list[i]
	element_list[i] = element_list[j]
	element_list[j] = temp

if __name__=='__main__':
	element_list = [9,8,7,2,3,6]
	print('Initial list:',element_list)
	insertion_sort(element_list)
	print("Sorted list :",element_list)

