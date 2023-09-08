import heapq as hq
import math

def djikstra(G, s):
    dist = [math.inf]*len(G)
    dist[s] = 0
    Q = []
    hq.heappush(Q, (dist[s], s))
    prev = [None]*len(G)
    visited = [False]*len(G)
    cost = 0

    while Q:
        num, u = hq.heappop(Q)
        if visited[u] == True:
           continue
        visited[u] = True
        for v,cost in G[u]:
            alt = dist[u] + cost
            if alt<dist[v]:
                dist[v] = alt
                prev[v] = u
                hq.heappush(Q, (dist[v], v))

    dist.pop(0)
    while math.inf in dist:
        idx = dist.index(math.inf)
        dist[idx] = -1
    return dist

f1 = open("input1_2.txt", "r")
f2 = open("output1_2.txt", "w")

inp = f1.read().split("\n")
f1.close()
line1 = inp[0].split(" ")
nodes = int(line1[0])
edges = int(line1[1])
source = int(inp[-1])

dic = {i:[] for i in range(nodes+1)}
for i in range(1, len(inp)-1, 1):
  info = inp[i].split(" ")
  node1 = int(info[0])
  node2 = int(info[1])
  cost = int(info[2])
  arr = dic[node1]
  arr.append((node2, cost))

costs = djikstra(dic, source)
f2.write(" ".join(list(map(str, costs))))