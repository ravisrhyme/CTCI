"""
I like parentheticals (a lot).
Sometimes (when I nest them (my parentheticals) too much (like this (and this)))
they get confusing.

Write a function that, given a sentence like the one above, along with the 
position of an opening parenthesis, finds the corresponding closing parenthesis.

Example: if the example string above is input with the number 10 (position of the
first parenthesis), the output should be 79 (position of the last parenthesis).

"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Interviewcake.com"]
__status__  = "Prototype"


def count_paranthesis(string,initial_position):
	
	i = initial_position + 1
	length = len(string)
	count = 1
	while i <  length:
		if string[i] == '(':
			count += 1
		elif string[i] == ')':
			count -= 1
	
		if count == 0:
			return i
		i += 1

	return None


if __name__=='__main__':
	string = 'Ravikiran (is an((( idiot))))'
	print(count_paranthesis(string,11))
