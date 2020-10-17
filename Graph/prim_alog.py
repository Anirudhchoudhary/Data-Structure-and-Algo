from collections import defaultdict
import heapq

inf = float("inf")


def relax(W, u, v, D, P):
    '''
    W is weight of Graph
    u is Edge of Graph
    v is Edge of Graph
    D is distance from the Graph
    P is Postion 
    '''
    d = D.get(u, inf) + W[u][v]
    if d < D.get(v, inf):
        D[v], P[v] = d, u
        return True


class Graph:

    def __init__(self):
        self.edges = defaultdict()

    def addEdge(self, u, v, w):
        if u in self.edges.keys():
            d1 = {v: w}
            self.edges[u].update(d1)
        else:
            self.edges[u] = {v: w}

    def printgraph(self):
        for u in self.edges.keys():
            print(self.edges[u])

    def prim_algo(self, s):
        mst = defaultdict(set)
        visited = set([s])
        Q = [
            (cost, s, to) for to, cost in self.edges[s].items()
        ]
        heapq.heapify(Q)
        while Q:
            cost, frm, to = heapq.heappop(Q)
            if to not in visited:
                visited.add(to)
                mst[frm].add(to)
                for to_next, cost in self.edges[to].items():
                    if to_next not in visited:
                        heapq.heappush(Q, (cost, to, to_next))

        return mst

    def find(self, C, u):
        if C[u] != u:
            C[u] = self.find(C, C[u])  # path compression
        return C[u]

    def union(self, C, R, u, v):
        u, v = self.find(C, u), self.find(C, v)
        if R[u] > R[v]:
            C[v] = u
        else:
            C[u] = v
        if R[u] == R[v]:
            R[v] += 1

    def krushkal(self):
        E = [(self.edges[u][v], u, v)
             for u in self.edges for v in self.edges[u]]
        T = set()
        C, R = {u: u for u in self.edges}, {u: 0 for u in self.edges}
        for _, u, v in sorted(E):
            if self.find(C, u) != self.find(C, v):
                T.add((u, v))
                self.union(C, R, u, v)

        return T


def create_spanning_tree(graph, starting_vertex):
    mst = defaultdict(set)
    visited = set([starting_vertex])
    edges = [
        (cost, starting_vertex, to)
        for to, cost in graph[starting_vertex].items()
    ]
    heapq.heapify(edges)

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst[frm].add(to)
            for to_next, cost in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (cost, to, to_next))

    return mst


def dijstra(G, start, end):
    heap = [(0, start)]
    heapq.heapify(heap)
    visited = set()
    while heap:
        cost, u = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        if u == end:
            return cost
        for v, c in G[u].items():
            if v in visited:
                continue
            _next = c + cost
            heapq.heappush(heap, (_next, v))

    return -1


def bellman_ford(G, s):
    D, P = {s: 0}, {}
    for rnd in G:
        changed = False
        for u in G:
            for v in G[u]:
                if relax(G, u, v, D, P):
                    changed = True

        if not changed:
            break
    else:
        raise ValueError("Negative Cycle")
    return D, P


example_graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1, 'E': 4},
    'C': {'A': 3, 'B': 1, 'F': 5},
    'D': {'B': 1, 'E': 1},
    'E': {'B': 4, 'D': 1, 'F': 1},
    'F': {'C': 5, 'E': 1, 'G': 1},
    'G': {'F': 1},
}

print(dijstra(example_graph, "A", "G"))
print("__________________LPPOL_________________________")
print(bellman_ford(example_graph, "A"))
# dict(create_spanning_tree(example_graph, 'A'))
# print(create_spanning_tree(example_graph, "A"))


if __name__ == "__main__":
    G = Graph()
    G.addEdge("A", "B", 4)
    G.addEdge("A", "D", 10)
    G.addEdge("B", "A", 4)
    G.addEdge("B", "C", 5)
    G.addEdge("C", "B", 4)
    G.addEdge("C", "D", 10)
    G.addEdge("D", "A", 1)
    G.addEdge("D", "C", 10)
    # print(G.krushkal())
