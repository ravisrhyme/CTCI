"""
Problem Statement:
You have a list of integers, and for each index you want to find the product 
of every integer except the integer at that index.
"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Interviewcake.com"]
__status__  = "Prototype"


def integer_product(arg):
	""" This function computes the above defined problem statement
	in O(n) time complexity using two additional lists
	"""
	length = len(arg)
	# List to store forward product
	temp1 = [1]
	#list to store backward product
	temp2 = [0]* length
	temp2[length-1] = 1
	result = []
	
	# forward product  
	for i in range(1,length):
		temp1.append(arg[i-1] * temp1[i-1])
	# Backward product
	for j in range (length-1,0,-1):
		temp2[j-1] = arg[j] * temp2[j]

	#final result
	for k in range(0,length):
		result.append(temp1[k] * temp2[k])
	return result

def integer_product_improved(given_list):
	""" This is an improved version of integer_product().
	we use only one list to compute in O(n) time instead of 
	three in integer_product(). We only store the products 
	before each index.
	"""

	if len(given_list) < 2:
		raise IndexError('Getting the product of numbers at other indices requires at least 2 numbers')

	list_of_product_before_index = []
	product_before = 1

	for i in range(0,len(given_list)):
		list_of_product_before_index.append(product_before)
		product_before *= given_list[i]

	product_after = 1
	for i in range(len(given_list)-1,-1,-1):
		list_of_product_before_index[i] *= product_after
		product_after *= given_list[i]

		
	return list_of_product_before_index


#test cases
if __name__ == "__main__":
	integer_list = [1,7,2,4]
	print(integer_list)
	print(integer_product_improved(integer_list))

