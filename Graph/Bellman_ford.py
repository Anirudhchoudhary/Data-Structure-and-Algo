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


if __name__ == "__main__":
    G = {
        'A': {'B': 2, 'C': 3},
        'B': {'A': 2, 'C': 1, 'D': 1, 'E': 4},
        'C': {'A': 3, 'B': 1, 'F': 5},
        'D': {'B': 1, 'E': 1},
        'E': {'B': 4, 'D': 1, 'F': 1},
        'F': {'C': 5, 'E': 1, 'G': 1},
        'G': {'F': 1},
    }
