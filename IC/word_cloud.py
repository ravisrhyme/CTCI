"""
You want to build a word cloud, an infographic where the size of a word 
corresponds to how often it appears in the body of text.
To do this, you'll need data. 

Write code that takes a long string and builds its word cloud data in a 
dictionary , where the keys are words and the values are the number of times the
words occurred.

Think about capitalized words. For example, look at these sentences:

'After beating the eggs, Dana read the next step:'
'Add milk and eggs, then add flour and sugar.'

What do we want to do with "After", "Dana", and "add"? In this example, your 
final dictionary should include one "Add" or "add" with a value of 22. Make
reasonable (not necessarily perfect) decisions about cases like "After" and 
"Dana".

Assume the input will only contain words and standard punctuation.

Time Complexity  : O(n)
Space Complexity : O(n)

Open ended question. Need to get back !!

"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Interviewcake.com"]
__status__  = "Prototype"

def build_word_cloud(string):

	"""Returns a Dictionary with keys as words and count as values.
	"""

	words = split_words(string)
	word_count = build_word_count(words)

	return word_count


def split_words(sentence):
	""" Splits the given sentence in to words and returns the words
	"""	
	words = []
	current_word = []
	i = 0
	for char in sentence:

		if char == ' ':
			words.append(''.join(current_word))
			current_word = []

		elif char.isalpha():
			current_word.append(char)

	return words

def build_word_count(words):
	"""Builds the count of words and returns the dictionary
	"""

	word_count = {}
	for word in words:
		if word in word_count:
			word_count[word] += 1
		else:
			word_count[word] = 1

	return word_count


if __name__ == '__main__':
	string = 'ravi kiran is a MS student '
	print(build_word_cloud(string))
