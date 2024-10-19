import random
import heapq

def print_matrix(matrix):
    """Prints the adjacency matrix."""
    print("\nAdjacency Matrix assigned random weights (0 indicates no edge):\n")
    n = len(matrix)
    print("    ", end="")
    for i in range(n):
        print(f"({i}) ", end="")
    print()
    for i, row in enumerate(matrix):
        print(f"({i}) ", end="")
        for val in row:
            print(f"  {val} ", end="")
        print()

def havel_hakimi(deg_seq):
    """Checks if the degree sequence is graphical using the Havel-Hakimi algorithm."""
    while True:
        deg_seq.sort(reverse=True)
        if deg_seq[0] == 0:
            return True
        d = deg_seq.pop(0)
        if d > len(deg_seq):
            return False
        for i in range(d):
            deg_seq[i] -= 1
            if deg_seq[i] < 0:
                return False

def construct_graph(deg_seq):
    """Constructs the adjacency matrix for a graphical degree sequence."""
    n = len(deg_seq)
    matrix = [[0] * n for _ in range(n)]
    nodes = [(deg_seq[i], i) for i in range(n)]
    while nodes:
        nodes.sort(reverse=True, key=lambda x: x[0])
        if nodes[0][0] == 0:
            break
        d, u = nodes.pop(0)
        if d > len(nodes):
            print("Error: Degree sequence is not handled correctly.")
            return None
        for i in range(d):
            v = nodes[i][1]
            matrix[u][v] = matrix[v][u] = random.randint(1, 10)  # Random weight assigned
            nodes[i] = (nodes[i][0] - 1, nodes[i][1])
    return matrix

def dijkstra(matrix, start):
    """Implements Dijkstra's algorithm to find the shortest paths from the start vertex."""
    n = len(matrix)
    distances = [float('inf')] * n  # Initialize distances to infinity
    distances[start] = 0  # Distance to start node is 0
    pq = [(0, start)]  # Priority queue to store (distance, node)

    while pq:
        current_distance, u = heapq.heappop(pq)

        if current_distance > distances[u]:
            continue

        for v, weight in enumerate(matrix[u]):
            if weight > 0:  # If there's an edge
                distance = current_distance + weight

                if distance < distances[v]:  # Found a shorter path
                    distances[v] = distance
                    heapq.heappush(pq, (distance, v))

    return distances

def is_eulerian(matrix):
    """Check if the graph is Eulerian."""
    odd_degree_count = sum(1 for row in matrix if sum(row) % 2 != 0)
    if odd_degree_count == 0:
        return "circuit"  # Euler circuit
    elif odd_degree_count == 2:
        return "path"  # Euler path
    else:
        return "none"  # Not Eulerian

def fleury(matrix, start):
    """Finds an Eulerian path or circuit using Fleury's algorithm."""
    path = []
    # Create a copy of the adjacency matrix to keep track of visited edges
    temp_matrix = [row[:] for row in matrix]
    current_vertex = start

    # While there are edges left in the graph
    while True:
        # Find the next vertex to visit
        for next_vertex in range(len(temp_matrix)):
            if temp_matrix[current_vertex][next_vertex] > 0:  # If there's an edge
                # Check if it's a bridge (if this edge is removed, does the graph remain connected?)
                temp_matrix[current_vertex][next_vertex] -= 1
                temp_matrix[next_vertex][current_vertex] -= 1
                
                if is_connected(temp_matrix, len(temp_matrix)):
                    path.append((current_vertex, next_vertex))
                    current_vertex = next_vertex
                else:
                    # Restore the edge if it's a bridge
                    temp_matrix[current_vertex][next_vertex] += 1
                    temp_matrix[next_vertex][current_vertex] += 1
        else:
            break  # No more edges to traverse
    
    return path

def is_connected(matrix, n):
    """Check if the graph is connected using DFS."""
    visited = [False] * n
    
    def dfs(v):
        visited[v] = True
        for i in range(n):
            if matrix[v][i] > 0 and not visited[i]:
                dfs(i)

    # Start DFS from the first vertex
    dfs(0)
    return all(visited)

def main():
    n = int(input("Enter the number of nodes: "))
    deg_seq = []
    print("Enter the degree sequence:")
    for i in range(n):
        deg = int(input(f"Degree of node {i}: "))
        if deg < 0:
            print("Invalid degree! Degree cannot be negative.")
            return
        deg_seq.append(deg)

    if havel_hakimi(deg_seq.copy()):
        print("\nThe sequence is graphical. Constructing the graph...\n")
        matrix = construct_graph(deg_seq)
        if matrix:
            print_matrix(matrix)

            # Input the starting vertex for Dijkstra's algorithm
            start = int(input("\nEnter the starting vertex for Dijkstra's algorithm: "))
            if start < 0 or start >= n:
                print("Invalid starting vertex!")
                return

            # Find shortest paths using Dijkstra's algorithm
            distances = dijkstra(matrix, start)
            print("\nShortest paths from vertex", start)
            for i, dist in enumerate(distances):
                print(f"Distance to vertex {i}: {dist}")

            # Check if the graph is Eulerian
            euler_type = is_eulerian(matrix)
            if euler_type != "none":
                print(f"\nThe graph has an Euler {euler_type}. Finding the Euler {euler_type}...\n")
                euler_path = fleury(matrix, start)
                print("Euler Path/Circuit:")
                for u, v in euler_path:
                    print(f"{u} -> {v}")
            else:
                print("\nThe graph is not Eulerian.")
    else:
        print("\nThe sequence is not graphical.")

if __name__ == "__main__":
    main()
