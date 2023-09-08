def mergeSort(arr):
    if len(arr) <= 1:
        return arr, int(arr[0])

    mid = len(arr) // 2
    left, maxValue = mergeSort(arr[:mid])
    right, maxValue = mergeSort(arr[mid:])

    merged, max_value = merge(left, right, maxValue)
    return merged, max_value


def merge(left, right, maxValue):
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            maxValue = max(maxValue, right[j])
            i += 1
        else:
            maxValue = max(maxValue, left[i])
            j += 1

    return left+right, maxValue

f1 = open("input4.txt", "r")
f2 = open("output4.txt", "w")
inp = f1.read().split("\n")
f1.close()
arr = inp[1].split(" ")
arr = list(map(int, arr))
sorted, max = mergeSort(arr)
f2.write(str(max))
f2.close()