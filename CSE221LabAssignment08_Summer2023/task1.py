def getParent(parent, n):
  par = parent[n]
  if par==n:
    return par
  else:
    return getParent(parent, par)

f1 = open("input1_2.txt", "r")
f2 = open("output1_2.txt", "w")

inp = f1.read().split("\n")
f1.close()
line1 = inp[0].split(" ")
nodes = int(line1[0])
edges = int(line1[1])

conn = []
graph = []
parent = [0]* (nodes+1)
totalCost = 0

parent = [i for i in range(nodes + 1)]

for i in range(1, len(inp)-1, 1):
  info = inp[i].split(" ")
  node1 = int(info[0])
  node2 = int(info[1])
  cost = int(info[2])
  lst = [node1, node2, cost]
  conn.append(lst)

conn = sorted(conn, key=lambda x: x[2])

for i in range(len(conn)):
  node1 = conn[i][0]
  node2 = conn[i][1]
  cost = conn[i][2]

  parent1 = getParent(parent, node1)
  parent2 = getParent(parent, node2)

  if (parent1!=parent2):
    parent[node2] = parent1
    parent[parent2] = parent1
    graph.append(conn[i])
    totalCost+=cost

f2.write(str(totalCost))
f2.close()