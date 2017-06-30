"""
A child is running up in a staircase with n steps, and can hop either 1 step, 
2steps or 3 steps at a time. Implement a method to count how many possible ways
the child can run up the stairs

Time Complexity  = O(n)
space Complexity = O(n)
"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Cracking The coding interview"]
__status__  = "Prototype"


def find_total_ways(number_of_steps):

	fib = [0,1,2,3]
	for temp in range(4,number_of_steps+1):
		fib.append(fib[temp-1] + fib[temp-2])

	return fib[number_of_steps]



if __name__=='__main__':
	number_of_steps = 5
	print(find_total_ways(number_of_steps))
