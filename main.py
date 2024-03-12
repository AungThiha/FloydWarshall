INF = float('inf')

def floyd_warshall(graph, number_of_vertices):

    distances = [
        [0 for col in range(number_of_vertices)] \
            for row in range(number_of_vertices)
    ]

    for row in range(number_of_vertices):
        for col in range(number_of_vertices):
            distances[row][col] = graph[row][col]

    for k in range(number_of_vertices):
        for i in range(number_of_vertices):
            for j in range(number_of_vertices):
                potential_shortest = distances[i][k] + distances[k][j]
                if potential_shortest < distances[i][j]:
                    distances[i][j] = potential_shortest
    return distances

# visual of this graph can be found in `graph.jpg` in this repository
graph = [[0, INF, -2, INF],
            [4, 0, 3, INF],
            [INF, INF, 0, 2],
            [INF, -1, INF, 0]]

g_distances = floyd_warshall(graph, 4)

print("original: ", graph)
print("after floyd_warshall: ", g_distances)

print()

# visual of this graph with negative cycle can be found in `negative_cycle.jpg` in this repository
negative_cycle = [[0, INF, -1],
                    [-1, 0, INF],
                    [INF, -1, 0]]
negative_cycle_distances = floyd_warshall(negative_cycle, 3)
print("originl: ", negative_cycle)
print("after floyd_warshall: ", negative_cycle_distances)
