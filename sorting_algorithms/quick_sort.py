"""
Implementation of quick sort algorithm

Time Complexity : O(nlog(n)) in Average case
				  O(n^2) in worst case

Space Complexity : O(1)

One of the In-place sorting algorithms

Reference: https://youtu.be/COk73cpQbFQ?list=PL2_aWCzGMAwKedT2KfDMB9YA5DgASZb3U
"""

__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Algorithm Design Manual","mycodeschool channel"]
__status__  = "Prototype"


def quick_sort(element_list,start,end):
	"""
	Implementation of Quick sort algorithm.
	"""
	if (start >=  end): # Base case
		return

	# Find pivot and makes sure that all elements to left of pivot are smaller
	# and all elements to right are larger than pivot. Returns the index of 
	# pivot 
	pivot_index = find_pivot_index(element_list,start,end)

	# Applies quick sort on left and right subproblems from the given list
	quick_sort(element_list,start,pivot_index-1)
	quick_sort(element_list,pivot_index+1,end)


def find_pivot_index(element_list,start,end):
	""" Returns pivot index and makes sure that all elements to left of pivot 
	are smaller and all elements to right are larger than pivot.
	"""
	pivot = element_list[end]
	pivot_index = start

	for i in range(start,end):
		if element_list[i] < pivot:
			#Swap elements 
			swap(element_list,pivot_index,i)
			pivot_index += 1
			#print(element_list)

	swap(element_list,pivot_index,end)
	
	return pivot_index


def swap(element_list,pivot_index,i):
	""" swaps element at index i and pivot_index
	"""
	temp = element_list[pivot_index]
	element_list[pivot_index] = element_list[i]
	element_list[i] = temp

if __name__=='__main__':

	element_list = [9,8,7,2,3,6]
	print('Given list :', element_list)
	quick_sort(element_list,0,len(element_list)-1)
	print('Sorted list :',element_list)
