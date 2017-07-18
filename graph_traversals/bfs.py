"""
Breadth first search Traversal of graph

Will keep appending as I improve on traversal implementations
"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Steven Skiena","Guido van Rossum"]
__status__  = "Prototype"

def bfs_iterative(graph,start):
	""" Prints all the reachable nodes from the start by BFS traversal
	"""
	visited = set()
	watched = set()
	nodes_queue = [start] # List that helps as queue
	watched.add(start)
	
	while nodes_queue:
		current_node = nodes_queue.pop(0)

		print("visiting",current_node)
		visited.add(current_node)
		
		for adjacent_node in graph[current_node]:
			if (adjacent_node not in watched) and (adjacent_node not in visited):
				nodes_queue.append(adjacent_node)
				path.add(adjacent_node)


def find_path_bfs(graph,start,path = []):
	
	return path


	
if __name__ == '__main__':

	graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

	bfs_iterative(graph,'E')
