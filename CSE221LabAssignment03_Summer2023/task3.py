def quicksort(a,p,r):
    if p<r:
        q = partition(a,p,r)
        quicksort(a,p,q-1)
        quicksort(a,q+1,r)

def partition(a,p,r):
    x = a[r]
    i = p-1
    for j in range(p, r, 1):
        if a[j]<x:
            i +=1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i+1

f1 = open("input3.txt", "r")
f2 = open("output3.txt", "w")
inp = f1.read().split("\n")
f1.close()
n = int(inp[0])
arr = inp[1].split(" ")
arr = list(map(int, arr))
quicksort(arr,0,n-1)
arr = list(map(str, arr))
f2.write(" ".join(arr))
f2.close()