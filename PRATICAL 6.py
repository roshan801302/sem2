def is_complete_graph(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if i != j and matrix[i][j] != 1:
                return False
    return True

# User input
n = int(input("Enter number of vertices: "))
print("Enter adjacency matrix row by row:")
matrix = [list(map(int, input().split())) for _ in range(n)]

# Check for completeness
if is_complete_graph(matrix):
    print("The graph is a Complete Graph.")
else:
    print("The graph is NOT a Complete Graph.")
