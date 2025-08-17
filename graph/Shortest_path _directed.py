from collections import deque

def bfs(start,visited,graph,target):

    path = [start]

    queue = deque([(start,path)])

    visited.add(start)

    while queue:

        current,path = queue.popleft()

        if current == target:

            return path

        for neighbour in graph[current]:

            if neighbour not in visited:

                visited.add(neighbour)

                queue.append((neighbour, path + [neighbour]))

        
    return None          


def bfs_shortest_path_directed(edges, start, target):


    #STEP 1: CONVERT EDGES TO GRAPH

    graph = {}

    for u,v in edges:

        if u not in graph:

            graph[u] = []

        if v not in graph:

            graph[v] = []
        
        graph[u].append(v)
   

    
    for i in graph:

        print(i," : ",graph[i])
    
    if start not in graph or target not in graph:

        return None

    visited = set()
              
    return bfs(start,visited,graph,target)

edges = [[0,1],[0,2],[1,3],[2,3]]
print("Shortest path (",0,"->",3,"):", bfs_shortest_path_directed(edges, 0, 3))
