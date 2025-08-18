import heapq

def dijkstra(edges,n,start):

    #STEP1: CREATE A GRAPH 

    graph = {}

    for u,v,w in edges:

        if u not in graph:

            graph[u] = []
        if v not in graph:

            graph[v] = []
        
        graph[u].append([v,w])
        graph[v].append([u,w])

    
    for node in graph:

        print(node, " : ", graph[node])

    distance = {}
    for node in graph:
        distance[node] = float('inf')

    distance[start] = 0

    queue = [(0,start)]
    
    while queue:

        current_dis, current_node= heapq.heappop(queue)

        for neighnour,weight in graph[current_node]:

            new_distance = current_dis + weight
            if new_distance < distance[neighnour]:

                distance[neighnour] = new_distance

                heapq.heappush(queue,(new_distance,neighnour))

    return distance

edges = [
    (0, 1, 4),
    (0, 2, 1),
    (2, 1, 2),
    (1, 3, 1),
    (2, 3, 5),
    (3, 4, 3)
]
print("Shortest distances from node 0:", dijkstra(edges, 5, 0))