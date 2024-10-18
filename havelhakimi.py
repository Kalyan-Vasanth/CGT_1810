def print_matrix(matrix):
    """Prints the adjacency matrix."""
    print("\nAdjacency Matrix:\n")
    n = len(matrix)
    
    # Print the header
    print("    ", end="")
    for i in range(n):
        print(f"({i}) ", end="")
    print()
    
    # Print the matrix with row labels
    for i, row in enumerate(matrix):
        print(f"({i}) ", end="")
        for val in row:
            print(f"  {val} ", end="")
        print()

def havel_hakimi(deg_seq):
    """Checks if the given degree sequence is graphical using the Havel-Hakimi algorithm."""
    while True:
        # Sort the degree sequence in descending order
        deg_seq.sort(reverse=True)

        # If all degrees are 0, the sequence is graphical
        if deg_seq[0] == 0:
            return True

        # Take the largest degree and remove it from the sequence
        d = deg_seq.pop(0)

        # Check if there are enough nodes to connect
        if d > len(deg_seq):
            return False

        # Reduce the degree of the next 'd' nodes
        for i in range(d):
            deg_seq[i] -= 1
            if deg_seq[i] < 0:
                return False  # Negative degree means the sequence is not graphical

def construct_graph(deg_seq):
    """Constructs the adjacency matrix for a graphical degree sequence."""
    n = len(deg_seq)
    matrix = [[0] * n for _ in range(n)]  # Initialize an n x n matrix with 0s

    # Create a list of (degree, node) pairs
    nodes = [(deg_seq[i], i) for i in range(n)]

    while nodes:
        # Sort nodes by degree in descending order
        nodes.sort(reverse=True, key=lambda x: x[0])

        # If the largest degree is 0, we are done
        if nodes[0][0] == 0:
            break

        # Get the node with the largest degree
        d, u = nodes.pop(0)

        if d > len(nodes):
            print("Error: Degree sequence is not handled correctly.")
            return None

        # Connect the node with the next 'd' nodes
        for i in range(d):
            v = nodes[i][1]

            # Set the edges in the adjacency matrix
            matrix[u][v] = 1
            matrix[v][u] = 1

            # Decrease the degree of the connected node
            nodes[i] = (nodes[i][0] - 1, nodes[i][1])

    return matrix

def main():
    # Input the number of nodes
    n = int(input("Enter the number of nodes: "))

    # Input the degree sequence
    deg_seq = []
    print("Enter the degree sequence:")
    for i in range(n):
        deg = int(input(f"Degree of node {i}: "))
        if deg < 0:
            print("Invalid degree! Degree cannot be negative.")
            return
        deg_seq.append(deg)

    # Check if the sequence is graphical
    if havel_hakimi(deg_seq.copy()):
        print("\nThe sequence is graphical. Constructing the graph...\n")
        matrix = construct_graph(deg_seq)
        if matrix:
            print_matrix(matrix)  # Print the adjacency matrix
    else:
        print("\nThe sequence is not graphical.")

if __name__ == "__main__":
    main()
