"""
A magic index in an array A[1...n-1] is defined to be an index such that A[i] = i
Given a sorted array of distinct integers, write a method to find a magic index, 
if one exists, in an array.

Follow up:

What if the values are not distinct

Time complexity : O(n) in brute force.
				  O(log(n)) if binary search is applied


Space complexity : O(1) 
"""

def find_magic_binary_distinct(sorted_array):
	""" Returns the magic number by performing a binary search
	"""
	start = 0
	end = len(sorted_array) - 1
	
	while start <= end:
		mid = int((start + end)/2)
		
		if sorted_array[mid] == mid:
			return mid
		
		elif sorted_array[mid] < mid : # Search right half if key < index
			start = mid + 1
		else: # search left half
			end = mid - 1

	return -1

def find_magic_binary_not_distinct(sorted_array,start,end):
	""" If elements are not distinct, we cannot eliminate one half of tree
	as in binary search. We traverse both left and right subtree. We can 
	jump to indices of mid_value as that is the minimum possibility of having 
	the magic index condition.
	"""
	if (end < start) or (start < 0) or (end >= len(sorted_array)):
		return -1	

	mid_index = int((start + end)/2)
	mid_value = sorted_array[mid_index]

	if mid_index == mid_value:
		return mid_index

	left_index = min(mid_index-1,mid_value)
	left_found = find_magic_binary_not_distinct(sorted_array,start,left_index)
	
	if left_found >= 0:
		return left_found

	right_index = max(mid_index+1,mid_value)
	right_found = find_magic_binary_not_distinct(sorted_array,right_index,end)

	return right_found

def find_magic_brute_force(sorted_array):
	""" Returns the magic index. 
	Time complexity : O(n)
	space complexity : O(1)
	"""
	for i in range (0,len(sorted_array)):
		if i == sorted_array[i]:
			return i

	
if __name__=='__main__':

	distinct_sorted_array = [-40,-20,-1,1,2,3,5,7,9,12,13]
	not_distinct_sorted_array = [-40,-20,2,2,2,3,5,7,9,12,13]
	print(find_magic_brute_force(distinct_sorted_array))
	print(find_magic_binary_distinct(distinct_sorted_array))
	print(find_magic_binary_not_distinct(not_distinct_sorted_array,0,len(not_distinct_sorted_array)-1))
