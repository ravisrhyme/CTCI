"""
Given a sorted array of n integers that has been rotated an unknown number of
times, write code to find an element in the array. You may assume that the array
was originally in increasing order.

Time Complexity  : O(log(n)) if all elements are distinct
Space Complexity : O(1)
"""

__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Cracking The coding interview"]
__status__  = "Prototype"



def find_element(element_list,element):
	start = 0
	end  = len(element_list) - 1 

	while (start <= end):
		mid = (start + end) // 2 # Integer division in python3
	
		if element == element_list[mid]:
			return mid
		
		# Key thought here is either the left or right half is always normal. 
		# i.e Ascending. Using that observation to decide to move left or right
		elif element_list[start] <= element_list[mid]: # Left half is normal and ascending
			if element >= element_list[start] and element < element_list[mid]:
				#move left
				end = mid - 1
			else:
				# Move right
				start = mid + 1

		elif element_list[start] > element_list[mid]: #Right half is normal and ascending
			if element <= element_list[end] and element > element_list[mid]:
				#Move right
				start = mid + 1
			else :
				# Move left
				end = mid - 1
			
				
	return None


if __name__=='__main__':
	element_list = [10,15,20,0,5]
	print(find_element(element_list,5))
