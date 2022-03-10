expllist = [3, 4, 2, 6, 7, 4]

for element in expllist:
    x = expllist.index(element)
    print(x)

if 3 in expllist:
    print("yes 3 in the list")

print(expllist.index(6))
print(expllist.count(4))

y = set(expllist)
print(y)

numDict = {}
for x in range(len(expllist)):
    numDict[x] = expllist[x]

for elm in numDict:
    if numDict[elm] == 4:
        print('index of value 4: ' + str(elm))

def fiboRecursively(num):
    if num < 0: print("not valid")
    elif num == 0: return 0
    elif num == 1 or num == 2: return 1
    else: return fiboRecursively(num - 1) + fiboRecursively(num - 2)

def fiboSpace(num):
    a = 0
    b = 1
    if num < 0: print('not valid')
    elif num == 0: return 0
    elif num == 1: return b
    else:
        for i in range(1, num):
            c = a + b
            a = b
            b = c
        return c

fibList = [0,1] #depends on where you start this list to get your answer back
def fiboDynamic(num):
    if num <= 0: print('not valid')
    elif num <= len(fibList): return fibList[num - 1]
    else:
        temp_fib = fiboDynamic(num - 1) + fiboDynamic(num - 2)
        fibList.append(temp_fib)
        return temp_fib
# go through and walk through this to see how it really work with the debugger not really sure how it works
print(fibList)

print("fiboSpace:" + str(fiboSpace(9)))
print("fiboRecursively:" + str(fiboRecursively(9)))
print("fiboDynamic:" + str(fiboDynamic(9)))

print(fibList)
