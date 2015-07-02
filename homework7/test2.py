def buildmapStructure(node,neighbor,cost,map):
    if not node in map:
        map[node] = {neighbor : cost } 
    else:
        map[node].append({neighbor : cost })
        
def dist(x1,y1,x2,y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def build_graph() :
    
    map = dict()
    node= dict()
    
    with open('usa.txt') as file_in :
        linecount = 1
        nodecount = 0  
        
        for line in file_in : 
            #print linecount 
            x = line.split()
            
            if linecount == 1 : 
                linecount = linecount + 1
                continue
            
            elif linecount <= 87576 : 
                linecount = linecount + 1
                node.update(int(x[1],int(x[2])               
                  
            else :
                linecount = linecount + 1
                node1 = int(x[0])
                node2 = int(x[1])
                
                buildmapStructure(node1,node2,dist(),map):
            

if __name__ == "__main__" :
    #import sys;sys.argv = ['', 'Test.testName']
    #unittest.main()
    graph = {'s': {'a': 2, 'b': 1},
            'a': {'s': 3, 'b': 4, 'c':8},
            'b': {'s': 4, 'a': 2, 'd': 2},
            'c': {'a': 2, 'd': 7, 't': 4},
            'd': {'b': 1, 'c': 11, 't': 5},
            't': {'c': 3, 'd': 5}}
    
    build_graph()
    print "map :" , map

