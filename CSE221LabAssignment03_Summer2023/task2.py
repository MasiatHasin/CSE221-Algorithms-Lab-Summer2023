def findMax(arr):
    if len(arr) <= 1:
        return arr, int(arr[0])

    mid = len(arr) // 2
    left, max_value = findMax(arr[:mid])
    right, max_value = findMax(arr[mid:])

    findMaxMaind, max_value = findMaxMain(left, right, max_value)
    return findMaxMaind, max_value


def findMaxMain(left, right, max_value):
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        exp = left[i] + right[j]*right[j]
        max_value = max(max_value, exp)
        if left[i] <= right[j]:
            i += 1
        else:
            j += 1

    return left+right, max_value

f1 = open("input2.txt", "r")
f2 = open("output2.txt", "w")
inp = f1.read().split("\n")
f1.close()
arr = inp[1].split(" ")
arr = list(map(int, arr))
sorted, max = findMax(arr)
f2.write(str(max))
f2.close()