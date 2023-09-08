def countPair(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, count_left = countPair(arr[:mid])
    right, count_right = countPair(arr[mid:])
    sorted_arr, count = countPairMain(left, right)

    total_count = count_left + count_right + count
    return sorted_arr, total_count

def countPairMain(left, right):
    merged = []
    count = 0
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            merged.append(left[i])
            count += len(right) - j
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, count

f1 = open("input1.txt", "r")
f2 = open("output1.txt", "w")
inp = f1.read().split("\n")
f1.close()
arr = inp[1].split(" ")
arr = list(map(int, arr))
sorted_array, count = countPair(arr)
f2.write(str(count))
f2.close()