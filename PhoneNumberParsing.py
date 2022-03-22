#given a set of rules determine who gets what for department

def prime(num):
    y = (num/2+1)
    if num > 1:
        for i in range(2, int(y)):
            if(num % i) == 0:
                return False
                break
            else:
                return True
    else:
        return False


def removeDash(string):
    list1 = [char for char in string]
    i = 2
    while i > 0:
        list1.remove('-')
        i -= 1
    return (list1)


def stringListToNums(listOfStrings):
    numList = [int(char) for char in listOfStrings]
    return numList


def parseDistrict(phonenum):
    z = removeDash(phonenum)
    q = stringListToNums(z)
    result = ''

    if str(q[0]) + str(q[1]) + str(q[2]) == '101':
        result = 'Mystic'
    elif q[0] + q[1] + q[2] == 5:
        result = 'Valor'
    elif result == '':
        for i in q:
            if prime(i) == False:
                result = 'Instinct'
                break
            else:
                result = 'Forbidden'

    print(result)

#234-452-2343
parseDistrict('234-452-2343')
parseDistrict('222-222-2222')