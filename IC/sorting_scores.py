"""
You created a game that is more popular than Angry Birds.

Each round, players receive a score between 0 and 100, which you use to rank them
from highest to lowest. So far you're using an algorithm that sorts in O(nlog(n)) 
time, but players are complaining that their rankings aren't updated fast enough.
You need a faster sorting algorithm.

Write a function that takes:

a list of unsorted_scores
the highest_possible_score in the game
and returns a sorted list of scores in less than O(nlgn) time.

For example:

unsorted_scores = [37, 89, 41, 65, 91, 53]
HIGHEST_POSSIBLE_SCORE = 100

sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE)
# returns [91, 89, 65, 53, 41, 37]

Time complexity = O(n)
Space Complexity = O(n)

Implemented Counting sort
"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Interviewcake.com"]
__status__  = "Prototype"

def sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE):
	
	count_scores = [0] * (HIGHEST_POSSIBLE_SCORE + 1) # List to save the occurances of scores
	sorted_scores = [] #list to return the sorted scores

	#Counting the occurances/frequencies of each score
	for score in unsorted_scores:
			count_scores[score] += 1

	# Traversing across the frequencies from the end to get scores in descending order
	for score in range(HIGHEST_POSSIBLE_SCORE,-1,-1):
		count = count_scores[score]
		
		# Repeating the frequencies for the occured number of times
		for times in range(count):
			sorted_scores.append(score)

	return sorted_scores

if __name__=='__main__':
	unsorted_scores = [37, 89, 41, 65, 91, 53]
	print(sort_scores(unsorted_scores, 100))
