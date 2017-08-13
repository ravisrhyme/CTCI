# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(T):
	"""
	"""
	number_of_cities = len(T)
	output = [0] * (len(T)-1)
    
	# This helps in reducing the time complexity 
	# by increasing space complexity to O(m)
	parents = [[] for i in range(0,number_of_cities)]

	# Populating parents
	for i in range(0,number_of_cities):
		if (i != T[i]):
			parents[T[i]].append(i)
		else:
			capital = i
            
	previous = [capital]
    
	total = 1
	for i in range(0,len(output)):
		output[i],previous = find_neighbours(T,previous,parents)
		total += output[i]
		if total == (number_of_cities):
			break
  
	return output
    
def find_neighbours(T,previous,parents):
	current = []
	count = 0
	for city in previous:
		temp = parents[city]
		if len(temp) > 0:
			count += len(temp)
			current.extend(temp)
            
        #for i in range(0,len(T)):
            #if T[i] == city and i != city:
                #count += 1
                #current.append(i)
                    
	return count, current


if __name__=='__main__':
	T = [9,1,4,9,0,4,8,9,0,1]
	print(solution(T))
