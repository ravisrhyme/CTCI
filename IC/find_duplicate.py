"""
Find a duplicate, Space Edition.

Need to optimise for space.

i.e required space complexity is : O(1)
Time complexity : O(nlogn)

It's a wonderful idea of applying binary search by using range of values instead
of size of the list :) 

"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Interviewcake.com"]
__status__  = "Prototype"


def find_duplicate(item_list):
	""" Returns first duplicate element in the list
	"""
	floor = 1
	ceiling = len(item_list) - 1

	while floor < ceiling :

		mid = (floor + ceiling)//2 # '//' for integer division. 
								   # Division returns float by default in python3
		lower_range_floor, lower_range_ceiling = floor, mid
		upper_range_floor, upper_range_ceiling = mid + 1, ceiling
		actual_lower_range_count = 0

		for number in item_list:
			if number >= lower_range_floor and number <= lower_range_ceiling:
				 actual_lower_range_count += 1

		expected_lower_range_count = (lower_range_ceiling - lower_range_floor) + 1

		if actual_lower_range_count > expected_lower_range_count:
			floor, ceiling = lower_range_floor, lower_range_ceiling

		else:
			floor, ceiling = upper_range_floor, upper_range_ceiling


	return item_list[floor-1]


if __name__ == '__main__':

	item_list = [1,2,3,4,5,6,7,3]
	print(find_duplicate(item_list))
