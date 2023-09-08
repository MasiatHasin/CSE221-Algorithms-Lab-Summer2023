from collections import defaultdict

def DFS(G, v, visited, stack):
    visited[v] = True
    for i in G[v]:
        if not visited[i]:
            DFS(G, i, visited, stack)
    stack.append(v)

def transpose(G):
    transposed_G = {i:[] for i in range(len(G))}
    for i in G:
        for j in G[i]:
            transposed_G[j].append(i)
    return transposed_G

def SCC_DFS(G, v, visited, scc):
    visited[v] = True
    scc.append(v)
    for i in G[v]:
        if not visited[i]:
            SCC_DFS(G, i, visited, scc)

def SCC(G):
    stack = []
    visited = [False] * len(G)
    for i in range(len(G)):
        if not visited[i]:
            DFS(G, i, visited, stack)

    transposed = transpose(G)
    visited = [False] * len(G)
    scc_components = []

    while stack:
        v = stack.pop()
        if v!= 0:
            if not visited[v]:
                scc = []
                SCC_DFS(transposed, v, visited, scc)
                scc_components.append(scc)

    return scc_components
f1 = open("input3_1.txt", "r")
f2 = open("output3_1.txt", "w")
inp = f1.read().split("\n")
f1.close()
line1 = inp[0].split(" ")
nodes = int(line1[0])
edges = int(line1[1])

dic = {i:[] for i in range(nodes+1)}
for i in range(1, len(inp), 1):
  info = inp[i].split(" ")
  node1 = int(info[0])
  node2 = int(info[1])
  arr = dic[node1]
  arr.append(node2)
  
scc = SCC(dic)
for i in range(len(scc)):
    f2.write(" ".join(list(map(str, scc[i]))))
    if i<len(scc)-1:
        f2.write("\n")
f2.close()