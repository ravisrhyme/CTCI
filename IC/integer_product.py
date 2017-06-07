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


#test cases
#if __init__ == "__main__":
list = [1,7,3,4,10,12,14]
print(integer_product(list))

