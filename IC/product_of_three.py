"""
Problem Statement:
Given a list of integers, find the highest product you can get from three of the
integers.

The input list_of_ints will always have at least three integers.
Time Complexity  : O(n)
space Complexity : O(1)
"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Interviewcake.com"]
__status__  = "Prototype"


def product_of_three(given_list):
	""" Returns highest product of three integers 
	"""

	if len(given_list) < 3:
		raise Exception("List should have atleast 3 members")

	highest_1 = highest_2 = highest_3 = 0
	lowest_1 = lowest_2 = 0

	for number in given_list:
		if number > highest_1:
			highest_3 = highest_2
			highest_2 = highest_1
			highest_1 = number
		elif number > highest_2:
			highest_3 = highest_2
			highest_2 = number
		elif number > highest_3:
			highest_3 = number


		if number < lowest_2:
			lowest_1 = lowest_2
			lowest_2 = number
		elif number < lowest_1:
			lowest_1 = number

	product_lowest = lowest_1 * lowest_2
	product_highest = highest_3 * highest_2 * highest_1

	if product_lowest * highest_3 > product_highest:
		return product_lowest * highest_1
	else:
		return product_highest
			


if __name__== '__main__':
	given_list = [1,10,-5,1,-100]
	print(product_of_three(given_list))
