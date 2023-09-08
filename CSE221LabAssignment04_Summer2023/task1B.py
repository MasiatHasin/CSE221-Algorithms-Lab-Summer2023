f1 = open("input1b_2.txt", "r")
f2 = open("output1b_2.txt", "w")

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
  cost = int(info[2])
  arr = dic[node1]
  arr.append((node2, cost))

vals = list(dic.values())
for i in range(len(vals)):
  f2.write(str(i)+' : '+" ".join(list(map(str, vals[i]))))
  if i<len(vals)-1:
    f2.write('\n')
f2.close()