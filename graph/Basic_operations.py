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

    def check_edge(self,v1,v2):

        if v1 in self.graph and v2 in self.graph:


            if v1 in self.graph[v2]:

                print("edge exist")
            else:

                print("edge not exist")
        else:

            print("check vertex")

    def get_neighbor(self,vertex):

        if vertex in self.graph:
            
            print("Neighbors of", vertex," : ",self.graph[vertex])
        
        else:

            print("check vertex")


    def get_degree(self,vertex):

        if vertex in self.graph:

            print("Degree of", vertex,":",len(self.graph[vertex]))
        else:
            print("check vertex")



    def display(self):

        for i in self.graph:

            print(i, " : ",self.graph[i])

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
g.remove_vertex('A')
g.remove_edge('D','C')
g.check_edge('D','E')
g.get_neighbor('D')
g.get_degree('E')
g.display()

