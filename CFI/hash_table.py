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
		index = self.shift_and_add_hash(string)
		print('index is ', index)
		# Appending string to list of values at index
		self.table[index].append(string)

	def lookup(self,string):
		""" Returns a boolean basing on presence or absence of string at index
		"""
		index = self.shift_and_add_hash(string)
		print('index is ', index)
		if string in self.table[index]:
			return True
		else:
			return False

	def additive_hash(self,string):
		"""Implementation of additive hash
		"""
		h = ord(string[0])
		length_of_string = len(string)

		for i in range(1,length_of_string):
			h +=  ord(string[i])
		
		return h % table_size

	def xor_hash(self,string):
		""" Implementation of XOR hashing algorithm
		"""
		h = ord(string[0])
		length_of_string = len(string)
		
		for i in range(1,length_of_string):
			h ^=  ord(string[i])
		
		return h % table_size

	def rotating_hash(self,string):
		"""Implementation of rotating hashing algorithm
		"""
		h = ord(string[0])
		length_of_string = len(string)

		for i in range(1,length_of_string):
			h =  (h << 4) ^ (h >> 28) ^ ord(string[i])

		return h % table_size

	def bernstein_hash(self,string):
		"""Implementation of bernstein hashing algorithm
		"""
		h = ord(string[0])
		length_of_string = len(string)

		for i in range(1,length_of_string):
			h = 33 * h + p[i];

		return h % table_size

	def modified_bernstein_hash(self,string):
		"""Implementation of modified bernstein hashing algorithm
		"""
		h = ord(string[0])
		length_of_string = len(string)

		for i in range(1,length_of_string):
			h = 33 * h ^ ord(string[i]);

		return h % table_size

	def shift_add_xor_hash(self,string):
		"""Implementation of shift-add-XOR hashing algorithm
		"""
		h = ord(string[0])
		length_of_string = len(string)

		for i in range(1,length_of_string):
			h ^= (h << 5) + (h >> 2) + ord(string[i]);

		return h % table_size

	def shift_and_add_hash(self,string):
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

