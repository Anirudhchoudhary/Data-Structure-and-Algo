from collections import defaultdict


"This is comment paet"


class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)

    # Function to add an edge to graph
    def addEdge(self, v, w):
        self.graph[v].append(w)  # Add w to v_s list
        self.graph[w].append(v)  # Add v to w_s list

    def isCyclicUtil(self, v, visited, parent):

        # Mark the current node as visited
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            # If the node is not visited then recurse on it
            if visited[i] == False:
                if(self.isCyclicUtil(i, visited, v)):
                    return True
            # If an adjacent vertex is visited and not parent of current vertex,
            # then there is a cycle
            elif parent != i:
                return True

        return False

    # Returns true if the graph contains a cycle, else false.

    def isCyclic(self):
        # Mark all the vertices as not visited
        visited = [False]*(self.V)
        # Call the recursive helper function to detect cycle in different
        # DFS trees
        for i in range(self.V):
            if visited[i] == False:  # Don't recur for u if it is already visited
                if(self.isCyclicUtil(i, visited, -1)) == True:
                    return True

        return False


if __name__ == "__main__":
    g = Graph(5)
    g.addEdge(1, 0)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(0, 3)
    g.addEdge(3, 4)

    if g.isCyclic():
        print("Cycle is present in Graph")
    else:
        print("NO Cycle is presnt")
