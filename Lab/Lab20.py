# Find parent of a node
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

# Union of two sets
def union(parent, x, y):
    parent[find(parent, x)] = find(parent, y)

# Kruskal's Algorithm
def kruskal(vertices, edges):
    edges.sort(key=lambda x: x[2])   # Sort edges by weight

    parent = []
    for i in range(vertices):
        parent.append(i)

    print("Edges in Minimum Spanning Tree:")

    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            print(u, "-", v, "Weight =", w)
            union(parent, u, v)

# Number of vertices
vertices = 4

# Edges: (Source, Destination, Weight)
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

# Run Kruskal's Algorithm
kruskal(vertices, edges)
