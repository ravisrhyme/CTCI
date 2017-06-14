"""
Suppose we had a list of n integers sorted in ascending order. 
How quickly could we check if a given integer is in the list?

Answer : As list is in Ascending order, Use binary search
Time complexity : O(log(n))
Space complexity : O(1)
"""


def binary_search(list_of_numbers,number):
	
	i = 0
	j = len(list_of_numbers)-1
	
	while (i < j):
		mid = int((i + j) /2)
		
		if (number == list_of_numbers[mid]):
			return mid
		elif number > list_of_numbers[mid]:
			i = mid + 1
		else:
			j = mid - 1

	return None

if __name__ == "__main__":

	temp = [0,1,2,3,4,5,6]
	print(binary_search(temp,5))
