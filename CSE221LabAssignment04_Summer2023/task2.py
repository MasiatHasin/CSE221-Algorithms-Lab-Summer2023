def BFS(G, s):
    visited = []
    Q = []
    path = []
    visited.append(s)
    Q.append(s)

    while Q:
        u = Q.pop(0)
        path.append(u)

        for v in G[u]:
            if v not in visited:
                visited.append(v)
                Q.append(v)
    return path

f1 = open("input2_2.txt", "r")
f2 = open("output2_2.txt", "w")
lines = f1.read().split("\n")
N, M = map(int, lines[0].split())

G = {i:[] for i in range(N+1)}
for i in range(1, len(lines), 1):
  info = lines[i].split(" ")
  node1 = int(info[0])
  node2 = int(info[1])
  arr = G[node1]
  arr.append(node2)

path = BFS(G, 1)

f2.write(" ".join(list(map(str, path))))
f2.close()