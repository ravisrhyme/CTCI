"""
Depth first search Traversal of graph

Will keep appending as I improve on traversals
"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Steven Skiena","Guido van Rossum"]
__status__  = "Prototype"


def dfs_iterative(graph,start):
    """ Prints all reachable nodes from the start in the order of visiting.
    Implemented Iteratively.
    """	
    # Stack to help traversing in DFS fashion in LIFO.
    node_stack = [start] 
    # Using sets to distinguish between in stack and visited nodes.
    # Using sets() as O(1) access
    visited = set()
    watched = set()

    # Traverses in LIFO order
    while node_stack:
        current_node = node_stack.pop()
        visited.add(current_node)
        watched.add(current_node)

        print ("visiting ",current_node)
        for adjacent_node in graph[current_node]:
            # Helps in avoiding cycles
            if (adjacent_node not in watched) and (adjacent_node not in visited):
                node_stack.append(adjacent_node)
                watched.add(adjacent_node)


def dfs_recursive(graph,node,visited=set(),watched=set()):
    """Prints all reachable nodes from the start in the order of visiting.
    Implemented recursvely.
    """

    if node is None:
        return
    if node in visited:
        return

    print("Visiting ", node)
    visited.add(node)

    for adjacent_node in graph[node]:
        if (adjacent_node not in watched) and (adjacent_node not in visited):
            watched.add(adjacent_node)
            dfs_recursive(graph,adjacent_node,visited,watched)



if __name__== '__main__':

    graph = {'A': ['B', 'C'],
            'B': ['C', 'D'],
            'C': ['D'],
            'D': ['C'],
            'E': ['F'],
            'F': ['C']}
    print("Traversing Recursively")
    dfs_recursive(graph,"A")
    print("Traversing Iteratively")
    dfs_iterative(graph,"A")
