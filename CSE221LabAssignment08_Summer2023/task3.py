import math

f1 = open("input3_2.txt", "r")
f2 = open("output3_2.txt", "w")

inp = f1.read().split("\n")
f1.close()
line1 = inp[0].split(" ")
x = int(line1[0])
n = int(line1[1])
line2 = inp[1].split(" ")

table = [[0] * (n + 1) for i in range(x)]

for i in range(len(table)):
    row = table[i]
    coin = int(line2[i])
    for j in range(len(row)):
        if i<1:
            if coin==1:
                row[j] = j
            else:
                if j%coin!=0:
                    row[j] = math.inf
                else:
                    row[j] = j//coin
        else:
            if j<coin:
                row[j] = table[i-1][j]
            else:
                row[j] = min(table[i-1][j], 1+row[j-coin])
f2.write(str(table[-1][-1]))
f2.close()