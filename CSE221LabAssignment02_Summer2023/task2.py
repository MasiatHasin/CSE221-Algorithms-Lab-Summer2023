#task 2 (1)
def task2_1():
    f1 = open("input2.txt", "r")
    f2 = open("output2.txt", "w")

    inp = f1.read().split("\n")
    f1.close()
    length1 = int(inp[0])
    arr1 = inp[1].split(" ")
    length2 = int(inp[2])
    arr2 = inp[3].split(" ")

    arr1.extend(arr2)
    arr1.sort()

    f2.write(" ".join(arr1))
    f2.close()

#task 2 (2)
def task2_2():
    f1 = open("input2.txt", "r")
    f2 = open("output2.txt", "w")

    inp = f1.read().split("\n")
    f1.close()
    length1 = int(inp[0])
    arr1 = inp[1].split(" ")
    length2 = int(inp[2])
    arr2 = inp[3].split(" ")
    totlength = length1+length2
    arr3 = []

    p1 = 0
    p2 = 0
    for i in range(totlength):
        if p1<length1 and p2<length2:
            if int(arr1[p1])<int(arr2[p2]):
                arr3.append(arr1[p1])
                p1+=1
            else:
                arr3.append(arr2[p2])
                p2+=1
    if p2<length2:
        arr3.extend(arr2[p2:])
    elif p1<length1:
        arr3.extend(arr2[p1:])

    f2.write(" ".join(arr3))
    f2.close()

task2_1()
task2_2()