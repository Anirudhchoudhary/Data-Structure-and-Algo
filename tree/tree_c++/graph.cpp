#include <bits/stdc++.h>

using namespace std;

void addEdge(vector<int> adj[], int u, int v)
{
    adj[u].push_back(v);
    adj[v].push_back(u);
}

void printGraph(vector<int> adj[], int V)
{
    for (int v = 0; v < V; v++)
    {
        cout << "\nAjacency List of Vextex  " << v << "\n head";
        for (auto x : adj[v])
        {
            cout << "->" << x;
        }
        cout << "\n";
    }
}

vector<bool> bfs(vector<int> adj[], int V)
{
    vector<bool> visited(adj->size(), false);
    queue<int> track;
    visited[V] = true;
    track.push(V);
    while (!track.empty())
    {

        size_t vertex = track.front();
        track.pop();
        for (auto x : adj[V])
        {
            if (!visited[x])
            {
                visited[x] = true;
                track.push(x);
            }
        }
    }
    return visited;
}

int main()
{
    int V = 5;
    vector<int> adj[V];
    addEdge(adj, 0, 1);
    addEdge(adj, 0, 4);
    addEdge(adj, 1, 2);
    addEdge(adj, 1, 3);
    addEdge(adj, 1, 4);
    addEdge(adj, 2, 3);
    addEdge(adj, 3, 4);

    vector<bool> n = bfs(adj, 0);
    for (auto i : bfs(adj, 0))
    {
        cout << i;
    }
    return 0;
}