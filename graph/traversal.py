class Graph:

    def __init__(self):
        self.graph = {}
    
    def add_vertex(self,vertex):

        if vertex not in self.graph:

            self.graph[vertex] = []

        else:

            print("vertex already exist")
    def add_edge(self,v1,v2):

        if v1 in self.graph and v2 in self.graph:
           
            if v2 not in self.graph[v1]:
                self.graph[v1].append(v2)
            if v1 not in self.graph[v2]:
                self.graph[v2].append(v1)

        else:

            print("vertex not available")
    
    def remove_vertex(self,vertex):

        if vertex in self.graph:

            for i in self.graph:
                if vertex in self.graph[i]:

                    self.graph[i].remove(vertex)
            del self.graph[vertex]
        else:
            print("check vertex")

    def remove_edge(self,v1,v2):

        if v1 in self.graph and v2 in self.graph:

            if v1 in self.graph[v2]:

                self.graph[v2].remove(v1)

            if v2 in self.graph[v1]:

                self.graph[v1].remove(v2)


        else:
            print("check vertex")


    def display(self):

        for i in self.graph:

            print(i, " : ",self.graph[i])

    def dfs_itr(self,start):

        stack = [start]
        visited = set()
        result = []

        while stack:

            current = stack.pop()

            if current not in visited:

                visited.add(current)
                result.append(current)
                
                for i in reversed(self.graph[current]):

                    stack.append(i)

        return result

    def bfs(self,start):

        visited = set()

        queue = [start]
        visited.add(start)

        while queue:

            current = queue.pop(0)

            for i in self.graph[current]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)


        print(visited)                




        
g = Graph()

g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_vertex('E')
g.add_edge('A','B')
g.add_edge('A','C')
g.add_edge('A','D')
g.add_edge('C','D')
g.add_edge('B','D')
g.add_edge('B','E')
g.add_edge('E','D')


g.display()
g.dfs_itr('A')
g.bfs('A')
