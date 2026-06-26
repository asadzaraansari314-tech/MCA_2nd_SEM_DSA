# Prim's Algorithm

INF = 999999

# Number of vertices
V = 5

# Graph (Adjacency Matrix)
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

selected = [False] * V
selected[0] = True

print("Edge : Weight")

for i in range(V - 1):
    minimum = INF
    x = 0
    y = 0

    for j in range(V):
        if selected[j]:
            for k in range(V):
                if (not selected[k]) and graph[j][k]:
                    if minimum > graph[j][k]:
                        minimum = graph[j][k]
                        x = j
                        y = k

    print(x, "-", y, ":", graph[x][y])
    selected[y] = True
