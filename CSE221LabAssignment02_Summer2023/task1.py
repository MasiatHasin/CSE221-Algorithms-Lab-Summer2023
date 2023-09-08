#task 1 (1)
def task1_1():
  f1 = open("input1.txt", "r")
  f2 = open("output1.txt", "w")

  inp = f1.read().split("\n")
  f1.close()
  line1 = inp[0].split(" ")
  length = int(line1[0])
  sum = int(line1[1])

  arr = inp[1].split(" ")
  found = False
  for i in range(length):
    if found==False:
      num1 = int(arr[i])
      for j in range(i+1,length,1):
        num2 = int(arr[j])
        if num1+num2 == sum:
          f2.write( str(i+1)+" "+ str(j+1))
          found = True
          break
    else:
      break
  if found==False:
    f2.write("IMPOSSIBLE")
  f2.close()

#task 1 (2)
def task1_2():
  f1 = open("input1.txt", "r")
  f2 = open("output1.txt", "w")

  inp = f1.read().split("\n")
  f1.close()
  line1 = inp[0].split(" ")
  length = int(line1[0])
  sum = int(line1[1])

  arr = inp[1].split(" ")

  needed = {}
  found = False
  for i in range(length):
    if int(arr[i]) in needed:
      first = needed[int(arr[i])]+1
      second = i+1
      f2.write(str(first)+" "+str(second))
      found= True
      break
    else:
      other = sum - int(arr[i])
      needed[other] = i
  if found==False:
    f2.write("IMPOSSIBLE")
  f2.close()

task1_1()
task1_2()