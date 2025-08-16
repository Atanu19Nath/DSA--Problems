# Function to perform Iterative DFS
def dfs_iterative(graph, start, visited):
    stack = [start]      # start DFS from this node
    component = []       # to store nodes in this component

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)        # mark visited
            component.append(node)   # add to current component

            # push all neighbors
            for nei in graph[node]:
                stack.append(nei)

    return component


# Main function
def find_connected_components(edges):
    graph = {}

    # Step 1: Build adjacency list
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)   # undirected

    visited = set()
    components = []

    # Step 2: Run DFS for unvisited nodes
    for node in graph:
        if node not in visited:
            comp = dfs_iterative(graph, node, visited)
            print("ans = ",comp)
            components.append(comp)

    return components


# Driver code
edges = [[0,1],[2,3],[3,4]]
components = find_connected_components(edges)
print("Connected Components:", components)
