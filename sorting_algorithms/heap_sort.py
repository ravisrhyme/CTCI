"""
Implementation of heap sort

Time complexity : O(nlog(n))
space complexity : O(n)

"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Algorithm Design Manual"]
__status__  = "Prototype"

from binary_heap import binary_heap


def heap_sort(min_heap):
	for i in range(1,min_heap.current_size + 1):
		print(min_heap.extract_min())

if __name__== '__main__':

	element_list = [9,8,7,1,2,3,6,5,4]
	h = binary_heap()
	h.build_heap(element_list)
	heap_sort(h)
