#STEP2: CYCLIC DETECTION IN DIRECTED GRAPH:

def dfs(start,visited, graph,current_path):


    visited.add(start)

    current_path.add(start)

    for neighbour in graph[start]:

        if neighbour not in visited:

            if dfs(neighbour,visited,graph,current_path):

                return True
            
        elif neighbour in current_path:

            return True
    
    current_path.remove(start)

    return False

            


def cyclic_dectection_directed_graph(edge):
    

    #STEP1 : CREATE A GRAPH USING EDGE

    graph = {}

    for u,v in edge:

        if u not in graph:

            graph[u] = []

        if v not in graph:

            graph[v] = []

        graph[u].append(v)    


    for node in graph:

        print(node, " : ", graph[node])


    #STEP2: COMPONETS IN GRAPH

    visited = set()

    for node in graph:
        
        
        if node not in visited:
    
            current_path = set()

            if dfs(node,visited,graph,current_path):
                
                return True
        
    return False




edge = [[1,2],[2,8],[8,9],[9,10],[10,8],[2,3],[7,3],[5,7],[5,6],[3,4],[4,5]]



print("total cycle = ",cyclic_dectection_directed_graph(edge))

