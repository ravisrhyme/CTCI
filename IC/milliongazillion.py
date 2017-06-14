"""
wrote a crawler that visits web pages, stores a few keywords in a database, and 
follows links to other web pages. I noticed that my crawler was wasting a lot 
of time visiting the same pages over and over, so I made a set, visited, where 
I'm storing URLs I've already visited. Now the crawler only visits a URL if it 
hasn't already been visited.

Thing is, the crawler is running on my old desktop computer in my parents' basement 
(where I totally don't live anymore), and it keeps running out of memory because 
visited is getting so huge.

How can I trim down the amount of space taken up by visited?

Answer : By using Trie
"""

__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Interviewcake.com"]
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
