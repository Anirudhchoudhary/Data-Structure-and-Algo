
edges = [[0, 6], [1, 2], [1, 4], [1, 6], [3, 0],
         [3, 4], [5, 1], [7, 0], [7, 1]]


def graph_(edges):
    graph = dict((i, []) for i in range(len(edges)-1))
    for src, des in edges:
        print(graph)
        if src in graph:
            graph[src] += [des]
        else:
            graph[src] = [des]
    return graph


def topsort(edges):
    graph = graph_(edges)
    S = set()
    res = []

    def recurse(u):
        if u in S:
            return
        S.add(u)
        for v in graph[u]:
            recurse(v)
        res.append(u)
    for u in graph:
        recurse(u)
    res.reverse()
    return res


print(topsort(edges))
