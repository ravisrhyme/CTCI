"""
Implementation of Trie Data Structure.
"""

__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Inventor of Trie"]
__status__  = "Prototype"


class Trie:
	def __init__(self):
		self.root_node = {}

	def check_and_add(self,word):
	
		current_node = self.root_node
		is_new_word = False
	
		for char in word:
			if char not in current_node:
				is_new_word = True
				current_node[char] = {}
			current_node = current_node[char]

		if 'EON' not in current_node:
			is_new_word = True
			current_node['EON'] = {}
	
		return is_new_word


if __name__== "__main__":

	trie_object = Trie()
	print(trie_object.root_node)
	print(trie_object.check_and_add('ravi'))
	print(trie_object.check_and_add('ravi'))
	print(trie_object.root_node)
	print(trie_object.check_and_add('ravikiran'))
	print(trie_object.root_node)
