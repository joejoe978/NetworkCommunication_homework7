import pdb
"""
The Bellman-Ford algorithm

Graph API:

    iter(graph) gives all nodes
    iter(graph[u]) gives neighbours of u
    graph[u][v] gives weight of edge (u, v)
"""
 
# Step 1: For each node prepare the destination and predecessor
def initialize(graph, source):
    #print "hi"
    d = {} # Stands for destination
    p = {} # Stands for predecessor
    for node in graph:
        d[node] = float('Inf') # We start admiting that the rest of nodes are very very far
        p[node] = None
    d[source] = 0 # For the source we know how to reach
    return d, p
 
def relax(node, neighbour, graph, d, p):
    # If the distance between the node and the neighbour is lower than the one I have now
    if d[neighbour] > d[node] + graph[node][neighbour]:
        # Record this lower distance
        d[neighbour]  = d[node] + graph[node][neighbour]
        p[neighbour] = node
 
def bellman_ford(graph, source):
    d, p = initialize(graph, source)
    for i in range(len(graph)-1): #Run this until is converges
        #print i
        for u in graph:
            for v in graph[u]: #For each neighbour of u
                relax(u, v, graph, d, p) #Lets relax it
 
    # Step 3: check for negative-weight cycles
    for u in graph:
        for v in graph[u]:
            assert d[v] <= d[u] + graph[u][v]
 
    return d, p
 
 
def test():
    graph = {
        'a': {'b': 5 , 'h': 8 , 'e': 9},
        'b': {'c': 12 , 'h': 4 , 'd': 15},
        'c': {'d': 3 , 'g': 11},
        'd': {'g': 9 },
        'e': {'h': 5 , 'f': 4 , 'g' : 20},
        'f': {'c': 1 , 'g': 13 },
        'g': {},
        'h': {'f': 6 , 'c': 7 , }
        }
    
    path = []
    dist, p = bellman_ford(graph, 'a')
    cost = dist['g']
    
    pre = 'g'
    while pre is not None :
        path.append(pre)
        pre = p[pre]
    path.reverse()
    
    print cost,path
    
    
if __name__ == '__main__': test()