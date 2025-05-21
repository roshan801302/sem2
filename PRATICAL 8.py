def compute_degrees(adj_list):
    in_degree = {v: 0 for v in adj_list}
    out_degree = {v: len(adj_list[v]) for v in adj_list}

    for src in adj_list:
        for dest in adj_list[src]:
            in_degree[dest] += 1

    return in_degree, out_degree

# User input
n = int(input("Enter number of vertices: "))
adj_list = {}

print("Enter neighbors for each vertex (space-separated):")
for i in range(n):
    adj_list[i] = list(map(int, input(f"Vertex {i}: ").split()))

# Compute degrees
in_d, out_d = compute_degrees(adj_list)

print("In-degree of each vertex:")
for v in in_d:
    print(f"Vertex {v}: {in_d[v]}")

print("Out-degree of each vertex:")
for v in out_d:
    print(f"Vertex {v}: {out_d[v]}")
