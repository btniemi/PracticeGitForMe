# There is a broken calculator that has the integer startValue on its display initially. In one operation, you can:
#     multiply the number on display by 2, or
#     subtract 1 from the number on display.
# Given two integers startValue and target, return the minimum number of operations needed to display target on the calculator.

#input start=2 target=3
#output = 2

def brokenCalc(start, target):
    i = 0
    while start != target:
        i += 1
        if start % 2 == 1: #have to define if start is larer then target what to do as well
            start -= 1
        else:
            start = start * 2

    return i + start - target # why this here as well??? adding start and subtracting target, must be if it goes above??? ie 5, 8

def brokenCalc1(s, t):
    i = 0
    while s < t:
        i += 1
        if t % 2 == 1:
            t += 1
        else:
            t //= 2

    return i + s - t

#print(brokenCalc(2,3))
print(brokenCalc1(5,8))