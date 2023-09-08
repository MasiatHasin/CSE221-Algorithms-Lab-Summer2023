#Task 4
def insertionSortSchedule(info):
    for i in range(1, len(info)):
        train, dest, time = info[i]
        hour = int(time.split(":")[0])
        j = i - 1
        prevTrain, prevDest, prevTime = info[j][0], info[j][1], info[j][2]
        prevHour = int(prevTime.split(":")[0])
        while j>=0 and (prevTrain > train or (prevTrain == train and prevHour < hour)):
            info[j+1] = info[j]
            j -= 1
            prevTrain, prevDest, prevTime = info[j][0], info[j][1], info[j][2]
            prevHour = int(prevTime.split(":")[0])
        info[j+1] = (train, dest, time)
    return info

f1 = open("input4.txt","r")
f2 = open("output4.txt","w")

f1 = f1.read().split("\n")
length = int(f1[0])

info = []

for i in range(1,length+1,1):
  line = f1[i].split(" ")
  train=line[0]
  dest=line[4]
  time=line[6]
  info.append([train,dest,time])
  
sortedInfo = insertionSortSchedule(info)

for i in range(length):
  info = sortedInfo[i]
  if i<length-1:
    string = "{} will departure for {} at {}\n"
  else:
    string = "{} will departure for {} at {}"
  string2 = string.format(info[0],info[1],info[2] )
  f2.write(string2)
f2.close()