def fibo(n):
    if storage[n]:
        return storage[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fibo(n - 1) + fibo(n - 2)
        storage[n] = result
        return result

f1 = open("input2_4.txt", "r")
f2 = open("output2_4.txt", "w")

inp = int(f1.read())
f1.close()

storage = {i:[] for i in range(inp+2)}

f2.write(str(fibo(inp+1)))
f2.close()