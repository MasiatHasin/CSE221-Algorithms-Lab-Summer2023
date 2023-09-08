f1 = open("input2_1.txt", "r")
f2 = open("output2_1.txt", "w")

input = f1.read().split("\n")
f1.close()

config = input[0].split(" ")
n = int(config[0])
p = int(config[1])
tasks = []
total = [[]]*p
pos = []
count = 0

for i in range(1, len(input), 1):
  data = input[i].split(" ")
  start = int(data[0])
  end = int(data[1])
  tasks.append((start, end))

tasks = sorted(tasks, key=lambda x: x[1])

for i in range(len(tasks)):
  curr = tasks[i]
  if i==0:
    total[0]=[curr]
    count+=1
  else:
    for j in range(len(total)):
      if len(total[j])>0:
        d = int(curr[0]) - int(total[j][-1][1])
      else:
        d = -9999
      if d>=0:
        pos.append([j,d])
    if len(pos)>0:
      pos = sorted(pos, key=lambda x: x[1])
      idx = pos[0][0]
      total[idx].append(curr)
      count+=1
    else:
      if [] in total:
          idx = total.index([])
          total[idx]=[curr]
          count+=1
  pos = [] 
f2.write(str(count))