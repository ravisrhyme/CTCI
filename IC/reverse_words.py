"""
Write a function to reverse words in a sentence in-place

Time Complexity  = O(n)
Space Complexity = O(1)
"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Interviewcake.com"]
__status__  = "Prototype"


def reverse_string(string_list):
	
	first_pointer = 0
	last_pointer = len(string_list) - 1

	while first_pointer < last_pointer: # swapping characters
		temp = string_list[first_pointer]
		string_list[first_pointer] = string_list[last_pointer]
		string_list[last_pointer] = temp
		first_pointer += 1
		last_pointer  -= 1

	return ''.join(string_list)

def reverse_words(string):
	words_list = list(string)
	words = []

	i = 0
	j = len(words_list) - 1
	
	while i < j :
		temp = words_list[i]
		words_list[i] = words_list[j]
		words_list[j] = temp
		i += 1
		j -= 1

	i = 0
	j = 0
	length = len(words_list)
	
	while j < length:
		if words_list[j] == ' ':
			words.append(reverse_string(words_list[i:j+1]))
			words.append(' ')
			i = j+ 1
		j += 1

	words.append(reverse_string(words_list[i:j+1])) # Takes care of last word
	return ''.join(words)

if __name__=='__main__':
	string = 'ravikiran is MS student'
	print(reverse_words(string))
