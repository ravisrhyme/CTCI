"""
You're working with an intern that keeps coming to you with JavaScript code that
won't run because the braces, brackets, and parentheses are off. To save you both
some time, you decide to write a braces/brackets/parentheses validator.

Let's say:

'(', '{', '[' are called "openers."
')', '}', ']' are called "closers."
Write an efficient function that tells us whether or not an input string's 
openers and closers are properly nested.
"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Interviewcake.com"]
__status__  = "Prototype"

openers = ['{','[','(']
closers = ['}',']',')']

def check_matching(string):
	
	stack = []
	for char in string:
		if char in openers:
			stack.append(char) # Push the open bracket to stack
		elif char in closers:
			temp = stack.pop() # Pop the top element from stack

			open_index = openers.index(temp)
			close_index = closers.index(char)
			if open_index != close_index:
				return False

	if len(stack) != 0:
		 return False
	else:
		return True



if __name__=='__main__':

	string = '{[abc]xyz(hhgg)}'
	print(check_matching(string))
