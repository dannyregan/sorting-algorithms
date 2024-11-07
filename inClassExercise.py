def BFS(V, E):
    visited = {v: False for v in V}
    count = 0
    for vertex in V:
        if not visited[vertex]:
            Q = [vertex]
            visited[vertex] = True
            print(f'Vertex {vertex} visited. V =', visited)

            while (len(Q) != 0):
                current = Q.pop(0)
                print(f'Vertex {current} dequeued, Q =', Q)

                for e in E:
                    if (e[0] == current) and not (visited[e[1]]):
                        Q.append(e[1])
                        visited[e[1]] = True
                        print(f'Vertex {e[1]} enqueued, Q =', Q)
                        print(f'Vertex {e[1]} visited, V =', visited)

# def BFS(V, E):
#     for i in range(len(V)):
#         V[i] = -1
#     count = 0
#     for i in range(len(V)):
#         if (V[i] == -1):
#             Q = [i]
#             V[i], count = count , count + 1
#             while (len(Q) != 0):
#                 for e in E:
#                     if (e[0] == Q[0]) and (V[e[1]] == -1):
#                         Q.append(e[1])
#                         V[e[1]], count = count, count + 1
#                     elif (e[1] == Q[0]) and (V[e[0]] == -1):
#                         Q.append(e[0])
#                         V[e[0]], count = count, count + 1
#                 Q.pop(0)

V = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
E = [
    ['A', 'E', 1],
    ['A', 'H', 1],
    ['B', 'A', 1],
    ['C', 'F', 1],
    ['C', 'G', 1],
    ['D', 'A', 1],
    ['D', 'E', 1],
    ['E', 'C', 1],
    ['F', 'D', 1],
    ['F', 'E', 1],
    ['G', 'B', 1],
    ['G', 'E', 1],
    ['H', 'D', 1]
]

# ===================================================
BFS(V, E)

# E = [
#     [0, 4, 1],  # 'A' - 'E'
#     [0, 7, 1],  # 'A' - 'H'
#     [1, 0, 1],  # 'B' - 'A'
#     [2, 5, 1],  # 'C' - 'F'
#     [2, 6, 1],  # 'C' - 'G'
#     [3, 0, 1],  # 'D' - 'A'
#     [3, 4, 1],  # 'D' - 'E'
#     [4, 2, 1],  # 'E' - 'C'
#     [5, 3, 1],  # 'F' - 'D'
#     [5, 4, 1],  # 'F' - 'E'
#     [6, 1, 1],  # 'G' - 'B'
#     [6, 4, 1],  # 'G' - 'E'
#     [7, 3, 1]   # 'H' - 'D'
# ]

# V = [0]*6
# E = [[0,1,1], [0,2,1], [0,3,1], [1,4,1], [3,6,1], [4,5,1]]