f1 = open("input1a_2.txt", "r")
f2 = open("output1a_2.txt", "w")

inp = f1.read().split("\n")
f1.close()
line1 = inp[0].split(" ")
nodes = int(line1[0])
edges = int(line1[1])

mat = [[0 for i in range(nodes+1)] for i in range(nodes+1)]
for i in range(1, len(inp), 1):
  info = inp[i].split(" ")
  node1 = int(info[0])
  node2 = int(info[1])
  cost = int(info[2])
  mat[node1][node2] = cost

for i in range(len(mat)):
  line = map(str, mat[i])
  line = " ".join(list(map(str, line)))
  f2.write(line)
  if i<len(mat)-1:
    f2.write('\n')
f2.close()