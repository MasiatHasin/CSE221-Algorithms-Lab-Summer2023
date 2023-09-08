def DFS(G, u):
    visited[u] = 1
    path.append(u)

    for v in G[u]:
        if visited[v] != 1:
            DFS(G, v)
    return path

f1 = open("input3_3.txt", "r")
f2 = open("output3_3.txt", "w")
lines = f1.read().split("\n")
N, M = map(int, lines[0].split())

G = {i:[] for i in range(N+1)}
for i in range(1, len(lines), 1):
  info = lines[i].split(" ")
  node1 = int(info[0])
  node2 = int(info[1])
  arr = G[node1]
  arr.append(node2)


visited = [0] * (N+1)
path = []
DFS(G, 1)

f2.write(" ".join(list(map(str, path))))
f2.close()