"""
Users on longer flights like to start a second movie right when their first one 
ends, but they complain that the plane usually lands before they can see the 
ending. So you're building a feature for choosing two movies whose total runtimes
will equal the exact flight length.

Write a function that takes an integer flight_length (in minutes) and a list of 
integers movie_lengths (in minutes) and returns a boolean indicating whether there 
are two numbers in movie_lengths whose sum equals flight_length.

When building your function:

Assume your users will watch exactly two movies
Don't make your users watch the same movie twice
Optimize for runtime over memory

"""

__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Interviewcake.com"]
__status__  = "Prototype"

def can_two_movies_fill_flight(movie_lengths, flight_length):
	""" Returns True if there are two movies that can be watched
	within one flight duration
	"""	
	movie_lengths_set = set()

	for length in movie_lengths:
		remaining_length = flight_length - length
		if remaining_length in movie_lengths_set:
			return True
		else:
			movie_lengths_set.add(length)

	return False


if __name__=='__main__':
	
	movie_lengths = [1,2,3,5,6] 
	print(can_two_movies_fill_flight(movie_lengths, 12))
