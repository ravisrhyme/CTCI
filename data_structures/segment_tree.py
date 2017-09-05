"""
Implementation of Segment Tree

Operations : Update and query

Time Complexity:
"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Algorithm Design Manual"]
__status__  = "Prototype"


class segment_tree:
	def __init__(self,element_list):
		self.size_of_list = len(element_list)
		self.size_of_tree = (2 * len(element_list)) - 1 #Need to do some thinking on this !!
		self.tree = [0] * (self.size_of_tree + 1)
		self.element_list = element_list


	def build(self,current_index = 1,start = 0,end = 7):
		""" Builds a segment tree
		"""
		if (start == end):
			self.tree[current_index] = self.element_list[start]
			return 
		else:
			mid = (start + end) // 2

			self.build(2*current_index,start,mid)
			self.build(2*current_index + 1,mid+1,end)
			
			self.tree[current_index] = max(self.tree[2*current_index], self.tree[2*current_index+1])


	def update(self,new_element,index):
		print(self.tree)


	def query(self,query_start_index,query_end_index,tree_index = 1,list_start_index =0 ,list_end_index = 7):
		""" Queries a segment tree
		list_start_index, list_end_index correspond to start and end indexes of 
		tree_index.
		"""
		# If query segment is part of list index range
		if (query_start_index <= list_start_index and query_end_index >= list_end_index):
			return self.tree[tree_index]

		if (query_start_index > list_end_index or query_end_index < list_start_index):
			return 0

		mid = list_start_index + list_end_index // 2
		p1 = self.query(query_start_index,query_end_index,2* tree_index,list_start_index,mid)
		p2 = self.query(query_start_index,query_end_index,2* tree_index+1,mid+1,list_end_index)

		return max(p1,p2)
		

if __name__ == "__main__":

	element_list = [4,5,6,7,8,9,10,11]
	st = segment_tree(element_list)
	st.build()
	st.update(1,1)
	print(st.query(1,4))
