def shortestPath(G, start, end):
    pathList = [[start]]
    visited = [start]
    if start == end:
        return [start]
        
    while len(pathList)>0:
        currentPath = pathList[0]
        lastNode = currentPath[-1]
        pathList.pop(0)
        nextNodes = G[lastNode]
        
        if end in nextNodes:
            currentPath.append(end)
            return currentPath
       
        for node in nextNodes:
            if not node in visited:
                newPath = list(currentPath)
                newPath.append(node)
                pathList.append(newPath)
                visited.append(node)
    return []

f1 = open("input5_2.txt", "r")
f2 = open("output5_2.txt", "w")
lines = f1.read().split("\n")
N, M, E = map(int, lines[0].split())

G = {i:[] for i in range(N+1)}
for i in range(1, len(lines), 1):
  info = lines[i].split(" ")
  node1 = int(info[0])
  node2 = int(info[1])
  arr = G[node1]
  arr.append(node2)
  arr = G[node2]
  arr.append(node1)

path = shortestPath(G, 1, E)

f2.write("TIME: "+str(len(path)-1)+"\n")
f2.write("Shortest Path: "+" ".join(list(map(str, path))))
f2.close()