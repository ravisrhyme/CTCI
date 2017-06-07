"""
Problem Statement:
Your company built an in-house calendar tool called HiCal. 
You want to add a feature to see the times in a day when everyone is available.

To do this, you’ll need to know when any team is having a meeting. In HiCal, 
a meeting is stored as tuples of integers (start_time, end_time). These 
integers represent the number of 30-minute blocks past 9:00am

(2, 3) # meeting from 10:00 – 10:30 am
(6, 9) # meeting from 12:00 – 1:30 pm

Write a function merge_ranges() that takes a list of meeting time ranges and 
returns a list of condensed ranges

[(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)] => [(0, 1), (3, 8), (9, 12)]

Complexity : O(nlogn)

"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Interviewcake.com"]
__status__  = "Prototype"

start = 0
end = 1

def merge_ranges(slots):
	global start,end
	slots.sort(key=lambda tup:tup[0])
	print(slots)
	length = len(slots)
	result = [list(slots[0])]
	k = 0
	i = 1
	while i < length:
		if 	slots[i][start] <= result[k][end]:
			if slots[i][end] > result[k][end]:
				result[k][end] = slots[i][end]
			#else:
				# Do nothing
		else:			
			k = k+1;
			result.append(list(slots[i]))
		i = i + 1
	return result


if __name__== "__main__":
	slots = [(0, 2),(1,1.5),(3, 5), (4, 8), (10, 12), (9, 10)]
	print(merge_ranges(slots))
