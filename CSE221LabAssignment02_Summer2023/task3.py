def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)// 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    merged = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

f1 = open("input3.txt", "r")
f2 = open("output3.txt", "w")
inp = f1.read().split("\n")
f1.close()
arr = inp[1].split(" ")
arr = list(map(int, arr))
sorted = list(map(str, mergeSort(arr)))
f2.write(" ".join(sorted))
f2.close()