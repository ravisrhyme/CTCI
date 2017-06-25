"""
Write a class TempTracker with these methods:

insert()—records a new temperature
get_max()—returns the highest temp we've seen so far
get_min()—returns the lowest temp we've seen so far
get_mean()—returns the mean ↴ of all temps we've seen so far
get_mode()—returns a mode ↴ of all temps we've seen so far
Optimize for space and time. Favor speeding up the getter functions 
(get_max(), get_min(), get_mean(), and get_mode()) over speeding up 
the insert() function.

"""

__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Interviewcake.com"]
__status__  = "Prototype"

class TempTracker:
	"""class to track temperatures
	Follows Ahead fof time approach for this usecase instead of
	intime approach.
	Every get_* operation happens in O(1) time complexity
	"""
	def __init__(self):

		# To hold max and min
		self.max = None
		self.min = None

		#To hold sum and number of recordings
		self.sum = 0.0
		self.no_of_samples = 0
		self.mean = None

		#To hold frequencies for mode
		self.frequency = [0] * 111
		self.max_frequency = 0
		self.mode = None
	
	def insert(self,temp):

		#Keeping track of mode
		self.frequency[temp] += 1
		if self.max_frequency < self.frequency[temp]:
			self.max_frequency = self.frequency[temp]
			self.mode = temp

		#Keeping track of Max
		if (self.max is None) or (self.max < temp):
			self.max = temp

		#Keeping track of min
		if (self.min is None) or (self.min > temp):
			self.min = temp
		
		#keeping track of mean
		self.sum += temp
		self.no_of_samples +=1
		self.mean = (self.sum/self.no_of_samples)

	def get_max(self):
		return self.max
	
	def get_min(self):
		return self.min

	def get_mean(self):
		return self.mean

	def get_mode(self):
		return self.mode


if __name__=="__main__":
	obj = TempTracker()
	obj.insert(10)
	obj.insert(20)
	print(obj.get_max())
	print(obj.get_min())
	print(obj.get_mean())
	print(obj.get_mode())
	
