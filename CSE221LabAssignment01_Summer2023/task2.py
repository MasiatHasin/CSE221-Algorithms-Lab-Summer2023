#Task 2
def bubbleSort(arr):
  sortHappened = False
  # We create a variable sortHappened to check if the array is sorted or not.
  # Initial value is False.
  for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        sortHappened = True
        # If a swap happens, it means that the array was not sorted.
        # So we set sortHappened to True.
    if sortHappened==False:
      break
      # sortHappened is False if no values needed swapping. This is only possible
      # if the loop has been completely sorted. So, We break out of the loop.
  return arr

f1 = open("input2.txt","r")
f2 = open("output2.txt","w")
array = f1.read().split("\n")[1]
array = array.split(" ")
array = list(map(int, array))
sortedArray = bubbleSort(array)
sortedArray = ' '.join(map(str, sortedArray))
f2.write(sortedArray)
f2.close()