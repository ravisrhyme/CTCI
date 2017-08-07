"""
You are given two sorted arrays, A and B, where A has a large enough buffer at 
the end to hold B. Write a method to merge B into A in sorted order.

Time Complexity : O(m+n)
Space Complexity : O(1)

Key idea : Start from end of 2 arrays !! 
 
"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Cracking The coding interview"]
__status__  = "Prototype"


def sort_lists(a,b):

	indexb = len(b) - 1
	indexa = len(a) - len(b) -1
	index_merged = len(a) - 1 # assuming k to be i + j

	while indexb >= 0 and indexa >= 0:
		if a[indexa] > b [indexb]:
			a[index_merged] = a[indexa]
			indexa -= 1

		else:
			a[index_merged] = b[indexb]
			indexb -= 1
		
		index_merged -= 1

	# Need to take care of this only for b, as 'a' will have items in place
	while indexb >= 0:
		a [index_merged] = b[indexb]
		indexb -= 1
		index_merged -= 1


if __name__=='__main__':
	a = [1,6,10,0,0,0]
	b = [2,7,11]
	sort_lists(a,b)
	print(a)
