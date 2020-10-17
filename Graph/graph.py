from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, s, S=set()):  # s is starting point of the Graph
        S, Q = set(s), [s]
        while Q:
            u = Q.pop()
            S.add(u)
            for v in reversed(self.graph[u]):
                if v not in S:
                    Q.append(v)

        return S


def dfs(G, s, S=set()):  # s is starting point of the Graph
    S, Q = set(s), [s]
    while Q:
        u = Q.pop()
        S.add(u)
        for adj in reversed(G[u]):
            if adj not in S:
                Q.append(adj)

    return S


def bfs(G, s):
    visited, Q = set(s), deque([s])
    while Q:
        u = Q.popleft()
        print(u, end=" ")
        for adj in G[u]:
            if adj not in visited:
                Q.append(adj)
                visited.add(adj)

    return visited


def topsort(G):
    S, res = set(), []

    def recurse(v):
        if v in S:
            return
        S.add(v)
        for s in G[v]:
            recurse(s)
        res.append(v)
    for u in G:
        recurse(u)
    res.reverse()
    return res


if __name__ == "__main__":
    G = Graph()
    G.addEdge("A", "B")
    G.addEdge("A", "E")
    G.addEdge("B", "F")
    G.addEdge("C", "G")
    G.addEdge("D", "E")
    G.addEdge("D", "H")
    G.addEdge("E", "H")
    G.addEdge("E", "D")
    G.addEdge("F", "I")
    G.addEdge("I", "H")

    G = {
        "A": ["B", "C", "D"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B", "D"],
        "E": ["B", "F"],
        "F": ["C", "E", "G"],
        "G": ["F"],
    }

    # n = dfs(G, "A")
    # print("DFS SEARCH is in GRAPH", n)
    # a = bfs(G, "A")
    # print("BFS SEARCH is in GRAPH", a)
    print(topsort(G))
