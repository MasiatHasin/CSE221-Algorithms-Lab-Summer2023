def DFS(G,u,visited,stack):
    visited[u] = True
    stack[u] = True

    for v in G[u]:
        if not visited[v]:
            if DFS(G,v,visited,stack):
                return True
        elif stack[v]:
            return True

    stack[u] = False
    return False

def isCycle(G):
    for u in range(len(G)):
        if DFS(G,u,visited,stack):
            return True

    return False

f1 = open("input4_2.txt", "r")
f2 = open("output4_2.txt", "w")
lines = f1.read().split("\n")
N, M = map(int, lines[0].split())

G = {i:[] for i in range(N+1)}
for i in range(1, len(lines), 1):
  info = lines[i].split(" ")
  node1 = int(info[0])
  node2 = int(info[1])
  arr = G[node1]
  arr.append(node2)

visited = [False] * (N+1)
stack = [False] * (N+1)

if isCycle(G)==True:
  f2.write("YES")
else:
  f2.write("NO")
f2.close()