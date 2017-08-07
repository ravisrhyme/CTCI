"""
Given a sorted array of strings which is interspersed with empty strings,
Write a method to find the location of a given string.

Time Complexity : O(log(n))
Space Complexity : O(1)
"""

__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Cracking The coding interview"]
__status__  = "Prototype"



def find_string(string_list,string):
	""" Returns the index of the string, if string is present in sorted string_list
	passed as input
	"""

	start = 0
	end = len(string_list)-1

	# Doing Binary search	
	while (start <= end):
		mid = (start + end) // 2

		# If string at mid is empty string,  we either move left or right to point 
		# to non empty string
		if not string_list[mid]:
			left = mid -1
			right = mid + 1
			while True:
				if (left < start) and ( right > end):
					return None
				elif string_list[right] and right <= end: 
					mid = right
					break;
				elif string_list[left]  and left>= start:
					mid = left
					break;
				
				right += 1
				left -= 1
				
		
		if string == string_list[mid]:
			return mid;

		elif string < string_list[mid]:
			#Move left
			end = mid -1

		elif string > string_list[mid]:
			#Move right
			start = mid + 1



if __name__=='__main__':
	string_list =['ravi','rbvi','','rcvi','rdvi']
	print(find_string(string_list,'rdvi'))


