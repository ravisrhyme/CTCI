"""
Write a method to return all subsets of a set.

Time Complexity = O(2 ^ n)
Space Complexity = O(2 ^ n)

Logic : As for combinotorial problems, we vary the number of items from 0-n
	    to solve this.

		i.e we find the number of subsets with one item i.e list[0]
		next we find number of subsets with 2 items. And it turns out 
		to be number_of_subsets[0] + list[1].

		using this logic we recurse from n to 0 and backk track to n from 0
"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Cracking The coding interview"]
__status__  = "Prototype"


#subsets = []
def find_subsets(given_set,n):
	""" Returns all the subsets of a given set
	"""
	if n == 0:
		return [[given_set[n]]]

	temp_lists = []
	current_item = given_set[n]
	subsets.extend(find_subsets(given_set,n-1))

	for subset in subsets:
		temp_lists.append(subset + [current_item])

	temp_lists.append([current_item])
	
	if n == len(given_set)-1 :
		subsets.extend(temp_lists)
		return subsets
	else:
		return temp_lists

def find_subsets_v2(given_set,n):
	""" Returns all the subsets of a given set.
	A cleaner implementation.

	"""	
	if n == 0:
		return [[given_set[n]]]

	current_item = given_set[n]
	temp_sets = []
	subsets = find_subsets_v2(given_set,n-1)

	for subset in subsets:
		temp_set = subset + [current_item]
		temp_sets.append(temp_set)
		
	temp_sets.append([current_item])
	subsets.extend(temp_sets)

	return subsets

if __name__=='__main__':
	given_set = [1,2,3,4]
	print (find_subsets_v2(given_set,len(given_set)-1))
