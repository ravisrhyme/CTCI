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

if __name__=='__main__':
	shuffled_deck= [1,4,2,5,3,6]
	half1 = [1,2,3]
	half2 = [4,5,6]
	print(is_single_riffle(shuffled_deck, half1,half2))
