"""
Write a recursive function for generating all permutations of an input string. 
Return them as a set.

"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Interviewcake.com"]
__status__  = "Prototype"


def find_permutations(string):

	if len(string) <= 1:
		return set([string])


	all_except_last_character = string[:-1]
	last_character = string[-1]

	permutations_of_string = find_permutations(all_except_last_character)
	
	permutations = set()
	for permutation_of_string in permutations_of_string:
		for position in range(len(all_except_last_character)+1):
			permutation = permutation_of_string[position:] + last_character + permutation_of_string[:position]
			permutations.add(permutation)

	return permutations


if __name__ == '__main__':
	string = 'ravikiran'
	print(find_permutations(string))
