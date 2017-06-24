"""
Write an efficient function that checks whether any permutation of an input 
string is a palindrome.

You can assume the input string only contains lowercase letters.

Examples:

"civic" should return True
"ivicc" should return True
"civil" should return False
"livci" should return False
"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Interviewcake.com"]
__status__  = "Prototype"


def is_permutation_palindrome(string):
	""" Returns True if any permutation of a given string is a palindrome
	Else returns False
	"""	
	unpaired_characters = set()
	for char in string:
		if char in unpaired_characters:
			unpaired_characters.remove(char)
		else:
			unpaired_characters.add(char)

	if len(unpaired_characters) > 1:
		return False
	else:
		return True


if __name__=='__main__':
	string = 'raviiv'
	print(is_permutation_palindrome(string))
