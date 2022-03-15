#give an array of 0's and 1's find the transition point from one to another
# ie [0,0,0,1,1] Result = 3 because it the index of the first changed number


list1 = [0,0,0,0,1,1,1,1] #result should= 4
list2 = [0,0,1,1,1,1] #result should= 2
list3 = [0,0,0,0]
list4 = [1,1,1,1]

def transitionPoint(list):
    lenOfList = len(list)
    mid = lenOfList // 2
    result = 0
    for i in range(lenOfList):
        if list[mid] == 1 and list[mid-1] == 0:
            result = mid
            break
        elif list[mid] == 1 and list[mid - 1] == 1 and mid < i:
            mid = mid - 1
        elif list[mid] == 0 and list[mid - 1] == 0 and mid < i:
            mid = mid + 1
        else:
            result = "'no index found'"
    return result

print(str(transitionPoint(list1)) + ' is the index transition point of list1')
print(str(transitionPoint(list2)) + ' is the index transition point of list2')
print(str(transitionPoint(list3)) + ' is the index transition point of list3')
print(str(transitionPoint(list4)) + ' is the index transition point of list4')