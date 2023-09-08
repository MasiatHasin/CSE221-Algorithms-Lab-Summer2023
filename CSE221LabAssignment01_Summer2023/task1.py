#Task 1
def task_a():
    f1 = open("input1a.txt", "r")
    f2 = open("output1a.txt", "w")
    f1 = f1.read().split("\n")
    T = int(f1[0])
    res = ''
    for i in range(1, T+1, 1):
        N= f1[i]
        if (int(N) % 2==0):
            res = 'Even'
        else:
            res = 'Odd'
        if i<T:
            string = "{} is an {} number.\n"
        else:
            string = "{} is an {} number."
        string2 = string.format(N,res)
        f2.write(string2)
    f2.close()

def task_b():
    f1 = open("input1b.txt", "r")
    f2 = open("output1b.txt", "w")
    f1 = f1.read().split("\n")
    T = int(f1[0])
    for i in range(1, T+1, 1):
        op = f1[i].split(" ")
        if op[2]=="+":
            result = int(op[1])+int(op[3])
        elif op[2]=="-":
            result = int(op[1])-int(op[3])
        elif op[2]=="/":
            result = int(op[1])/int(op[3])
        elif op[2]=="*":
            result = int(op[1])*int(op[3])
        if i<T:
            string = "The result of {} is {}\n"
        else:
            string = "The result of {} is {}"
        string2 = string.format(f1[i],result)
        f2.write(string2)
    f2.close()

task_a()
task_b()