"""
Implement an algorithm to print all valid combinations of n-pairs of parenthesis

Example:
Input : 2
output : ()() (()) 
"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Cracking The coding interview"]
__status__  = "Prototype"


combos = []
def find_valid_parenthesis(left_count,right_count,current_string=""):

	if left_count < 0 or right_count < left_count:
		return

	if right_count == 0 and left_count == 0:
		combos.append(current_string)
		current_string = ""
		return

	else:
		if left_count > 0:
			#current_string += '('
			find_valid_parenthesis(left_count-1,right_count,current_string+'(')

		if right_count > left_count:
			#current_string += ')'
			find_valid_parenthesis(left_count,right_count-1,current_string+')')


if __name__=='__main__':
	number = 2
	find_valid_parenthesis(2,2)
	print(combos)
