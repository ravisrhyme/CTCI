"""
Write a function fib() that a takes an integer nn and returns the nnth fibonacci
number.

This is a very good simple problem to understand the magic of efficient algorithm
Following are the execution times of three implementations on my machine.
RAM       : 8GB
Processor : i3
OS        : Ubuntu 16.04

1. Recursive without memoization
	real	1m36.028s
	user	1m36.020s
	sys	    0m0.000s

2. Recursive with memoization
	real	0m0.037s
	user	0m0.032s
	sys	    0m0.004s


3. Iterative with memoization
	real	0m0.032s
	user	0m0.028s
	sys	    0m0.000s

There is Drastic difference between with and without memoization.
I tested for number 40.

Basically O(2^40=102334155) calls reduced O(40) !! 

"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Interviewcake.com"]
__status__  = "Prototype"

f = {}

def fib_recursive(n):
	"""Returns the nth Fibanacci number
	Time complexity : O(2^n)
	"""
	
	if n < 0:
		raise Exception("Negative number. Not valid !!")
	if n in [0,1]:
		return n
	else:
		return fib_recursive(n-1) + fib_recursive(n-2)

def fib_memoized_recursive(n):
	""" Returns the nth Fibanacci number
	Time  complexity : O(n)
	Space complexity : O(n)
	"""
	global f
	if n < 0:
		raise Exception("Negative number. Not valid !!")
	if n in [0,1]:
		return n
	if n in f:
		return f[n]

	f[n] = fib_memoized_recursive(n-1) + fib_memoized_recursive(n-2)
	

	return f[n]

def fib_memoized_iterative(n):
	""" Returns the nth Fibanacci number
	Time complexity  : O(n)
	Space complexity : O(1)
	"""
	global f
	if n < 0:
		raise Exception("Negative number. Not valid !!")
	if n in [0,1]:
		return n
	previous_two = 0
	previous_one = 1
	current = None
	i = 2
	while (i <= n):
		current = previous_one + previous_two
		previous_two = previous_one
		previous_one = current
		i += 1
	return current



if __name__=="__main__":

	#print(fib_recursive(40))
	#print(fib_memoized_recursive(40))
	print(fib_memoized_iterative(40))
