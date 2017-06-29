"""
I figured out how to get rich: online poker.
I suspect the online poker game I'm playing shuffles cards by doing a single 
"riffle"

To prove this, let's write a function to tell us if a full deck of cards 
shuffled_deck is a single riffle of two other halves half1 and half2.

We'll represent a stack of cards as a list of integers in the range 
1..52 (since there are 52 distinct cards in a deck).

"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Interviewcake.com"]
__status__  = "Prototype"

def is_single_riffle(shuffled_deck, half1,half2):
	"""Checks if it is a single riffle.
	Time Complexity  = O(n)
	Space Complexity = O(1)
	"""
	i = 0
	j = 0
	
	if len(half1) + len(half2) != len(shuffled_deck):
		return False

	for card in shuffled_deck:
		if i < len(half1)  and card == half1[i]:
			i += 1
		elif j < len(half2) and card == half2[j]:
			j += 1
		else:
			return False

	return True

def is_single_riffle_recursive(shuffled_deck, half1,half2):
	""" Checks if it is a single riffle.
	Time Complexity = O(n^2) i.e n stack calls + O(n) operation for each slicing
	Space Complexity = O(n^2) i.e O(n) space per call to copy slice and O(N) calls
	"""	
	if len(shuffled_deck) == 0:
		return True

	if len(half1) != 0 and shuffled_deck[0] == half1[0]:
		return is_single_riffle_recursive(shuffled_deck[1:], half1[1:],half2)
	
	elif len(half2) != 0 and shuffled_deck[0] == half2[0]:
		return is_single_riffle_recursive(shuffled_deck[1:], half1,half2[1:])

	return False

def is_single_riffle_recursive_simplified(shuffled_deck, half1,half2, index_shuffled = 0,index_half1 = 0,index_half2 = 0):
	"""Checks if it is a single riffle
	Time Complexity  : O(n)
	Space Complexity : O(n)
	Time and space complexity reduced as slicing operation is removed and indexes are used !
	"""
	if index_shuffled == len(shuffled_deck):
		return True

	if index_half1 < len(half1) and shuffled_deck[index_shuffled] == half1[index_half1]:
		return is_single_riffle_recursive_simplified(shuffled_deck, half1,half2, (index_shuffled+1),(index_half1+1),index_half2)
	
	elif index_half2 < len(half2) and shuffled_deck[index_shuffled] == half2[index_half2]:
		return is_single_riffle_recursive_simplified(shuffled_deck, half1,half2, (index_shuffled+1),index_half1,(index_half2+1))

	return False

if __name__=='__main__':
	shuffled_deck= [1,4,2,5,3,6]
	half1 = [1,2,3]
	half2 = [4,5,6]
	print(is_single_riffle(shuffled_deck, half1,half2))
	print(is_single_riffle_recursive(shuffled_deck, half1,half2))
	print(is_single_riffle_recursive_simplified(shuffled_deck, half1,half2))

