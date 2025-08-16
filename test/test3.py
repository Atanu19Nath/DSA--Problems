def dfs(start, graph, visited):
    
    parent = -1 
    stack = [(start,parent)]
    while stack:

        current, parent = stack.pop()

        if current not in visited:

            visited.add(current)
            
            for i in reversed(graph[current]):
                    
                    if i not in visited:
                        
                        stack.append((i,current))
                        
                    elif i != parent :

                        return True

    return False



def get_component(edge):

    # STEP1: CREATE A GRAPH USING EDGE

    graph = {}

    for u,v in edge:

        if u not in graph:

            graph[u] =[]

        if v not in graph:

            graph[v] = []

        graph[u].append(v)
        graph[v].append(u)
    
    for i in graph:

        print(i, " : ",graph[i])


    #STEP 2 : GET COMPONENTS

    visited = set()

    for node in graph:

        if node not in visited:

            result = dfs(node,graph,visited)

            if result:
                return result 

    return False

# edge = [[0,1],[0,2],[0,3],[4,5],[5,6]]

edge = [[0,1],[1,2],[2,3],[3,0]]

print(get_component(edge))
