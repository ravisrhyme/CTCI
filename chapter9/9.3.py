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

	start = 0
	end = len(sorted_array) - 1
	
	while start <= end:
		mid = int((start + end)/2)
		
		if sorted_array[mid] == mid:
			return mid
		
		elif sorted_array[mid] < mid : # Search right half if key < index
			start = mid + 1
		else: # search left half
			end = mid -1

def find_magic_binary_not_distinct(sorted_array):
	start = 0
	end = len(sorted_array) - 1

	while start <= end:
		mid = int((start + end)/2)

		if 


if __name__=='__main__':

	distinct_sorted_array = [-40,-20,-1,1,2,3,5,7,9,12,13]
	#print(find_magic_brute_force(sorted_array))
	print(find_magic_binary_distinct(sorted_array))
