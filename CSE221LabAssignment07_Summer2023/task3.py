def getParent(parent, n):
  par = parent[n]
  if par==n:
    return par
  else:
    return getParent(parent, par)

f1 = open("input3_1.txt", "r")
f2 = open("output3_1.txt", "w")

inp = f1.read().split("\n")
f1.close()

config = inp[0].split(" ")
n = int(config[0])
k = int(config[1])

parent = [i for i in range(n + 1)]
friends = [1]*(n+1)

for i in range(1, len(inp),1):
    data = inp[i].split(" ")
    node1 = int(data[0])
    node2 = int(data[1])

    parent1 = getParent(parent, node1)
    parent2 = getParent(parent, node2)

    if (parent1!=parent2):
        parent[node2] = parent1
        parent[parent2] = parent1
        friends[parent1]= friends[parent1]+friends[parent2]
    f2.write(str(friends[parent1]))
    if i<len(inp)-1:
       f2.write("\n")
f2.close()

