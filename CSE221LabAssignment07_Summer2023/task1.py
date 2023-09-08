f1 = open("input1_2.txt", "r")
f2 = open("output1_2.txt", "w")

input = f1.read().split("\n")
f1.close()

config = input[0].split(" ")
n = int(config[0])
tasks = []
p = []

for i in range(1, len(input), 1):
  data = input[i].split(" ")
  start = int(data[0])
  end = int(data[1])
  tasks.append((start, end))

tasks = sorted(tasks, key=lambda x: x[1])

for i in range(len(tasks)):
  curr = tasks[i]
  if len(p)==0:
    p.append(curr)
  else:
    last = p[-1]
    diff = curr[0] -  last[1]
    if diff>=0:
        p.append(curr)

for i in range(len(p)):
  elem = p[i]
  f2.write(str(elem[0])+" "+str(elem[1]))
  if i<len(p)-1:
    f2.write("\n")

f2.close()