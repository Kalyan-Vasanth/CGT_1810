#include <stdio.h>
#include <stdbool.h>
#include <limits.h>

#define MAX_V 100

int graph[MAX_V][MAX_V];
bool visited[MAX_V];
int V;

void DFS(int v) {
    visited[v] = true;
    for (int u = 0; u < V; u++) {
        if (graph[v][u] && !visited[u]) {
            DFS(u);
        }
    }
}

bool isConnected() {
    for (int i = 0; i < V; i++) visited[i] = false;

    int start = -1;
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            if (graph[i][j]) {
                start = i;
                break;
            }
        }
        if (start != -1) break;
    }

    if (start == -1) return true;

    DFS(start);

    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            if (graph[i][j] && !visited[i]) return false;
        }
    }

    return true;
}

int vertexConnectivity() {
    int min_cut = INT_MAX;

    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) visited[j] = false;
        visited[i] = true;

        int count = 0;
        for (int j = 0; j < V; j++) {
            if (!visited[j]) {
                DFS(j);
                count++;
                if (count > 1) break;
            }
        }

        if (count > 1) min_cut = i;
    }

    return min_cut;
}

int edgeConnectivity() {
    return 0;
}

int main() {
    printf("Enter the number of vertices: ");
    scanf("%d", &V);

    printf("Enter the adjacency matrix of the graph:\n");
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            scanf("%d", &graph[i][j]);
        }
    }

    if (!isConnected()) {
        printf("The graph is disconnected.\n");
        return 0;
    }

    int v_connectivity = vertexConnectivity();
    int e_connectivity = edgeConnectivity();

    printf("Vertex Connectivity: %d\n", v_connectivity);
    printf("Edge Connectivity: %d\n", e_connectivity);
    printf("K-Connected value: %d\n", v_connectivity);

    return 0;
}