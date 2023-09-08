def partition(a,p,r):
    x = a[r]
    i = p-1
    for j in range(p, r, 1):
        if a[j]<x:
            i +=1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i+1

def findKSmallest(a,k):
    p = 0
    r = len(a)-1

    while p<=r:
            pivotIdx = partition(a,p,r)
            if pivotIdx==k-1:
                return a[pivotIdx]
            elif pivotIdx>k-1:
                r = pivotIdx-1
            else:
                p = pivotIdx+1
    return None

f1 = open("input4.txt", "r")
f2 = open("output4.txt", "w")
inp = f1.read().split("\n")
f1.close()
na = (inp[0].split(" "))[0]
nq = (inp[0].split(" "))[2]
arr = inp[1].split(" ")
arr = list(map(int, arr))

for i in range(3, len(inp), 1):
  result = findKSmallest(arr, int(inp[i]))
  if i<len(inp)-1:
    f2.write(str(result)+"\n")
  else:
    f2.write(str(result))
f2.close()
