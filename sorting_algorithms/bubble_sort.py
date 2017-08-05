"""
Implementation of bubble sort

Time Complexity : O(n^2) in worst and average case
				  O(n) in best case
Space Complexity : O(1)
"""

__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Algorithm Design Manual","mycodeschool channel"]
__status__  = "Prototype"


def bubble_sort(element_list):
	"""Sorts by using bubble sort algorithm
	In every iteration in inner loop, we bubble up the largest element to right
	placing it in right position.
	"""
	length_of_list = len(element_list)

	for i in range(length_of_list-1,-1,-1):
		flag = 0 # using flag to optimise in case of already sorted array
 		for j in range(0,i):
			if element_list[j] > element_list[j+1]:
				swap(element_list,j,j+1)
				flag = 1

		if flag == 0: # Array is already sorted. No need of further iterations
			break



def swap(element_list,i,j):
	""" Swaps the elements position i and j in list
	"""
	temp = element_list[i]
	element_list[i] = element_list[j]
	element_list[j] = temp

if __name__=='__main__':
	element_list = [9,8,7,2,3,6]
	bubble_sort(element_list)
	print(element_list)

