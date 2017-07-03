"""
Demo to understand closures in python.

"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Dive in to Python3"]
__status__  = "Prototype"


import re


"""patterns = \
(
('[sxz]$','$', 'es'),
('[^aeioudgkprt]h$', '$', 'es'),
('(qu|[^aeiou])y$', 'y$', 'ies'),
('$', '$', 's')
)"""

def build_match_and_apply_functions(pattern,search,replace):

	def matches_rule(word):
		return re.search(pattern,word)

	def apply_rule(word):
		return re.sub(search,replace,word)

	return (matches_rule,apply_rule)



#Generator Function
def rules(rules_filename):
	with open(rules_filename,encoding='utf-8') as pattern_file:
		for line in pattern_file:
			pattern, search, replace = line.split(None, 3)
			yield build_match_and_apply_functions(pattern,search,replace)
			

def plural(word, rules_filename='plural_rules.txt'):

	#Generator function can be called in for loop
	for matches_rule,apply_rule in rules(rules_filename):
		if matches_rule(word):
			return apply_rule(word)


if __name__=='__main__':
	
	word = 'name'
	print(plural(word))
	print(plural('cake'))	
