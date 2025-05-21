def is_complete_graph(adj_list):
    n = len(adj_list)
    for vertex, neighbors in adj_list.items():
        if len(neighbors) != n - 1:
            return False
    return True

# User input
n = int(input("Enter number of vertices: "))
adj_list = {}

print("Enter neighbors for each vertex (space-separated):")
for i in range(n):
    adj_list[i] = list(map(int, input(f"Vertex {i}: ").split()))

# Check for completeness
if is_complete_graph(adj_list):
    print("The graph is a Complete Graph.")
else:
    print("The graph is NOT a Complete Graph.")
