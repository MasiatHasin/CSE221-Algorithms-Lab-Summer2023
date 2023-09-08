def TopoSortBFS(G, indeg):
    count = 0
    q = []
    f = []
    for u in G:
        if indeg[u] == 0:
            q.append(u)
    while q:
        v = q.pop()
        count+=1
        f.append(v)
        for u in G[v]:
            indeg[u] = indeg[u]-1
            if indeg[u] == 0:
                q.append(u)
    if count!= len(G):
        return ["IMPOSSIBLE"]
    else:
        return f

f1 = open("input1_1.txt", "r")
f2 = open("output1_1.txt", "w")

inp = f1.read().split("\n")
f1.close()
line1 = inp[0].split(" ")
nodes = int(line1[0])
edges = int(line1[1])

indeg = [0]*(nodes+1)
dic = {i:[] for i in range(1,nodes+1)}
for i in range(1, len(inp), 1):
  info = inp[i].split(" ")
  node1 = int(info[0])
  node2 = int(info[1])
  arr = dic[node1]
  arr.append(node2)
  indeg[node2] = indeg[node2]+1

result = TopoSortBFS(dic,indeg)
f2.write(" ".join(list(map(str, result))))
f2.close()