def dfs(start, graph, visited):


    stack = [start]

    result = []
  
    while stack:

        current = stack.pop()

        if current not in visited:

            visited.add(current)
            result.append(current)

            for i in reversed(graph[current]):
                    
                    stack.append(i)

    return result



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
    component = []

    for node in graph:

        if node not in visited:



            result = dfs(node,graph,visited)

            component.append(result)

    return component

edge = [0,1],[0,2],[0,3],[4,5],[5,6]

print(get_component(edge))
