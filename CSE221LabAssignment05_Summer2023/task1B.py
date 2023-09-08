def DFS(G, u, time, visited, s_time, e_time,stack):
    s_time[u] = time
    time += 1
    visited[u] = True
    stack[u] = True
    cycle_detected = False

    for v in G[u]:
        if not visited[v]:
            time, e_time, cycle_detected = DFS(G, v, time, visited, s_time, e_time, stack)
            if cycle_detected:
                break
        elif stack[v]:
            cycle_detected = True
            break

    e_time[u] = time
    time += 1
    stack[u] = False
    return time, e_time, cycle_detected

def isCycle(G):
    num_vertices = len(G)
    visited = [False] * num_vertices
    s_time = [False] * num_vertices
    e_time = {i:[] for i in range(num_vertices)}
    stack = [False] * num_vertices
    time = 1
    cycle_detected = False
    for u in G:
        if not visited[u]:
            time, e_time, cycle_detected = DFS(G, u, time, visited, s_time, e_time, stack)
            if cycle_detected:
                break

    return e_time, cycle_detected

f1 = open("input1_1.txt", "r")
f2 = open("output1_1.txt", "w")

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

end_times, cycle = isCycle(dic)
if not cycle:
    result = [key for key, value in sorted(end_times.items(), key=lambda item: item[1], reverse=True)]
    result.remove(0)
    f2.write(" ".join(list(map(str, result))))
else:
    f2.write("IMPOSSIBLE")
f2.close()