#Task 3
def insertionSortPairs(pairs):
    pairs = list(pairs.items())
    for i in range(1, len(pairs)):
        id, mark = pairs[i]
        j = i - 1
        prevMark, prevId = pairs[j][1], pairs[j][0]
        while j>=0 and (int(prevMark) < int(mark) or (int(prevMark) == int(mark) and int(prevId) > int(id))):
            pairs[j+1] = pairs[j]
            j -= 1
            prevMark, prevId = pairs[j][1], pairs[j][0]
        pairs[j+1] = (id, mark)
    return pairs

f1 = open("input3.txt","r")
f2 = open("output3.txt","w")

f1 = f1.read().split("\n")
length = int(f1[0])
id = f1[1].split(" ")
mark = f1[2].split(" ")

pairs = {}

for i in range(length):
  pairs[id[i]] = mark[i]

sortedPairs = insertionSortPairs(pairs)

for i in range(length):
  pair = sortedPairs[i]
  if i<length-1:
    string = "ID: {} Mark: {}\n"
  else:
    string = "ID: {} Mark: {}"
  string2 = string.format(pair[0],pair[1] )
  f2.write(string2)