"""
I have a list of n + 1 numbers. Every number in the range 1...n appears once 
except for one number that appears twice.

Write a function for finding the number that appears twice.

Time Complexity  = O(n)
Space Complexity = O(1)
"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Interviewcake.com"]
__status__  = "Prototype"

def appears_twice(number_list):

	length = len(number_list)-1	
	sum_of_list = 0

	#counting the sum of all numbers
	for number in number_list:
		sum_of_list += number

	#Finding the sum of n natural numbers
	sum_of_n_numbers = (length * (length +1))/2

	# Returns the number that appeared twice
	return (sum_of_list - sum_of_n_numbers)


if __name__ == '__main__':
	number_list = [1,2,3,4,5,6,7,8,9,10,10]
	print(appears_twice(number_list))
