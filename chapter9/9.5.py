"""
Compute all permutations of a string.

Time complexity : O(n!)
Space Complexity : O(n!)

cannot do better than this ! :(
"""

__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Cracking The coding interview"]
__status__  = "Prototype"


def find_permutations(string,n):
	""" Returns all permutations of a given string
	Implemented using base case and build approach.
	i.e Recurse till the last character of string is reached and
	start building permutations of each string from that point by moving across
	the stack below and adding a new character at all places in each string from
	previous stack
	"""	
	if n == 0:
		return [string[0]]

	last_character = string[n]
	list_of_permutations = find_permutations(string,n-1)

	new_permutations = []
	for permutation in list_of_permutations:
		for position in range(0, len(permutation)+1):
			new_string = permutation[position:] + last_character + permutation[:position]
			new_permutations.append(new_string)

	return new_permutations 

if __name__=='__main__':
	string = 'ravi'
	print(find_permutations(string,len(string)-1))
