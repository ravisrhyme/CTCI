"""
I opened up a dictionary to a page in the middle and started flipping through, 
looking for words I didn't know. I put each word I didn't know at increasing 
indices in a huge list I created in memory. When I reached the end of the 
dictionary, I started from the beginning and did the same thing until I reached 
the page I started at.

Now I have a list of words that are mostly alphabetical, except they start 
somewhere in the middle of the alphabet, reach the end, and then start from the 
beginning of the alphabet. In other words, this is an alphabetically ordered list 
that has been "rotated." 

Time complexity = O(logn)
space complexity = O(1)
"""

__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Interviewcake.com"]
__status__  = "Prototype"

def find_rotation_point(words):
	""" Returns the rotation index from the list of words
	This function will do a altered binary search :)
	"""
	i = 0
	j = len(words)-1
	while i < j :
	
		mid = int((i + j)/2)
		
		if (words[mid] <  words[mid+1] and \
			words[mid] <  words[mid-1]) :
				# Found the rotation point 
				return mid
	
		elif words[mid] <  words[i]:
			#Move Left
			j = mid - 1

		else:
			#Move right
			i = mid
	return None

if __name__ == "__main__":
	words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
	'Yankie',
	'zebra',
    'asymptote', # <-- rotates here!
	'aviation'
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage']
	print(find_rotation_point(words))
