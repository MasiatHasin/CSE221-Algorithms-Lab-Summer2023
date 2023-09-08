import heapq as hq
import math

def djikstra(G, s, N):
    dist = [math.inf] * len(G)
    dist[s] = 0
    Q = []
    hq.heappush(Q, (dist[s], s))
    prev = [None] * len(G)
    visited = [False] * len(G)

    while Q:
        num, u = hq.heappop(Q)
        if visited[u]:
            continue
        visited[u] = True
        for v, danger in G[u]:
            alt = max(dist[u], danger)
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                hq.heappush(Q, (dist[v], v))
    return dist[N]

f1 = open("input3_2.txt", "r")
f2 = open("output3_2.txt", "w")

inp = f1.read().split("\n")
f1.close()
line1 = inp[0].split(" ")
nodes = int(line1[0])
edges = int(line1[1])
source = 1
dest = nodes

dic = {i:[] for i in range(nodes+1)}
for i in range(1, len(inp), 1):
  info = inp[i].split(" ")
  node1 = int(info[0])
  node2 = int(info[1])
  cost = int(info[2])
  arr = dic[node1]
  arr.append((node2, cost))

minDanger = djikstra(dic, source, dest)
f2.write(str(minDanger))