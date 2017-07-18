"""
Implementation of hashtable
"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Brian Jordan"]
__status__  = "Prototype"


table_size = 1000

class hash_table:
	""" Implementation of simple hash table
	"""
	def __init__(self):
		# made value of table as list to handle collisions
		self.table = [[None]] * table_size

	def insert(self,string):
		""" Inserts a string after getting its hash value in to table.
		"""
		index = self.find_hash(string)
		print('index is ', index)
		# Appending string to list of values at index
		self.table[index].append(string)

	def lookup(self,string):
		""" Returns a boolean basing on presence or absence of string at index
		"""
		index = self.find_hash(string)
		print('index is ', index)
		if string in self.table[index]:
			return True
		else:
			return False 

	def find_hash(self,string):
		""" Computes and returns hash index for a given string.
		Has two components : 
		1. calculating hash code(unbounded i.e h)
		2. calculating compressed index i.e h % tablesize
		
		Using shift and add algorithm for #1 below
		"""	
		h = ord(string[0])
		length_of_string = len(string)

		for i in range(1,length_of_string):
			h = (h << 4) + ord(string[i])

		print('h is', h)
		return h % table_size


if __name__=='__main__':

	ht = hash_table()
	ht.insert('ravi')
	print(ht.lookup('ravi'))

