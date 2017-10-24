"""
Print the following list in Hirearchy
locations = [
		{"id":1,"name":"San Francisco Bay Area","parent_id":None},
		{"id":2,"name":"San Jose","parent_id":3},
		{"id":3,"name":"South Bay","parent_id":1},
		{"id":4,"name":"San Francisco","parent_id":1},
		{"id":5,"name":"Manhattan","parent_id":6},
		{"id":6,"name":"New York","parent_id":None}
			]

i.e parent with no dash, Immediate child with one dash etc.

New York
-Manhattan
San Francisco Bay Area
-San Francisco
-South Bay
--San Jose
Note: Should be in sorted order
"""
import sys, json


def build_graph(locations):

    """ Builds a graph from a given set of locations.
    """
    roots = []
    graphs = {}

    for location in locations:
  
        if location['parent_id'] == None: #root
            roots.append(location)
            if location['id'] not in graphs:
                graphs[location['id']] = []
    
        elif location['parent_id'] not in graphs:
            graphs[location['parent_id']] = [location]
    
        else:
            graphs[location['parent_id']].append(location)

    return roots,graphs
    
def bfs(root,graphs):

    """ BFS implementation to traverse across the graph.
    Not using any exoicit visited() set as there is no cycle.

    """

    queue = [(root['id'],root['name'],0)]
    
  
    while len(queue) != 0:
        print_string = '' 
        iid,name,depth = queue.pop(0)
        
        print_string += '-' * depth
        print_string += name
        print(print_string)

        if iid in graphs:
            graphs[iid] = sorted(graphs[iid], key=lambda x: x['name'])
            for value in graphs[iid]:
                queue.append((value['id'],value['name'],depth+1))


if __name__=='__main__':

    locations = [{"id":1,"name":"San Francisco Bay Area","parent_id":None},{"id":2,"name":"San Jose","parent_id":3}, \
            {"id":3,"name":"South Bay","parent_id":1},{"id":4,"name":"San Francisco","parent_id":1},\
            {"id":5,"name":"Manhattan","parent_id":6},{"id":6,"name":"New York","parent_id":None}]

    roots,graphs = build_graph(locations)
    roots = sorted(roots, key=lambda x: x['name'])

    #print(roots)
    #print(graphs)

    for root in roots:
        bfs(root,graphs)
