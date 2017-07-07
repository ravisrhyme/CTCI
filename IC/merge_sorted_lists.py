"""
In order to win the prize for most cookies sold, my friend Alice and I are going
to merge our Girl Scout Cookies orders and enter as one unit.

Each order is represented by an "order id" (an integer).

We have our lists of orders sorted numerically already, in lists. 

Write a function to merge our lists of orders into one sorted list.

For example:

my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

print merge_lists(my_list, alices_list)
# prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]

Time Complexity = O(n)
Space Complexity = O(n)

"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Interviewcake.com"]
__status__  = "Prototype"


def merge_lists(list1,list2):
	"""Returns the sorted merged list of two sorted list.
	"""

	length1 = len(list1)
	length2 = len(list2)

	sorted_index = length1 + length2 # Traverse atlease one 
	i = 0
	j = 0
	k = 0
	sorted_list = []

	while i < sorted_index:

		if j >= length1 :
			sorted_list.extend(list2[k:])
			break;

		elif k >= length2:
			sorted_list.extend(list2[j:])
			break;

		else:
			if list1[j] < list2[k]:
				sorted_list.append(list1[j])
				j += 1
			else: 
				sorted_list.append(list2[k])
				k += 1
		i += 1

	return sorted_list


if __name__== '__main__':
	list1 = [1,5]
	list2 = [2,4,6] 
	print(merge_lists(list1,list2))
