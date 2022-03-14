from random import randint

unsortedList = [2, 5, 7, 1, 9]
# sorted = [1,2,5,7,9]

# def bubbleSort(list):
#     n = len(list)
#     for i in range(n):
#         z = n - i - 1 #when sorting you want to run a bubble sort minus one loop from the number of elements in your list
#         for j in range(z):
#             if list[j] > list[j + 1]:
#                 q = list[j]
#                 p = list[j+1]
#                 list[j+1] = q
#                 list[j] = p
#     return list
#
# print(bubbleSort(unsortedList))

# def insertion_sort(array):
#     for i in range(1, len(array)):
#         key_item = array[i] #keep a value you want to insert
#         j = i - 1
#         while j >= 0 and array[j] > key_item: #iterate till find that spot where you want to insert it but keep replacing all down the line keeps list integrity
#             array[j + 1] = array[j]
#             j -= 1
#         array[j + 1] = key_item #insert that key where you want it/belongs
#     return array
#
# print(insertion_sort(unsortedList))

# def quickSort(list):
#     if len(list) < 2:
#         return list
#     low, same, high = [], [], []
#     pivot = list[randint(0, len(list)-1)]  # the value of a random element from the list given
#     for item in list:
#         if item < pivot:
#             low.append(item)
#         elif item == pivot:
#             same.append(item)
#         elif item > pivot:
#             high.append(item)
#     x = low
#     y = same
#     z = high
#     res = quickSort(low) + same + quickSort(high) # concatinates the lists generated from origninal list once the sort is done on each other list low and high if needed
#     return res
#
# print(quickSort(unsortedList))

# def merge_sort(array):
#     if len(array) < 2:
#         return array
#     midpoint = len(array) // 2
#     left = merge_sort(array[:midpoint])
#     right = merge_sort(array[midpoint:])
#     if len(left) == 0:
#         return right
#     if len(right) == 0:
#         return left
#     result = []
#     index_left = index_right = 0
#     while len(result) < len(left) + len(right):
#         if left[index_left] <= right[index_right]:
#             result.append(left[index_left])
#             index_left += 1
#         else:
#             result.append(right[index_right])
#             index_right += 1
#         if index_right == len(right):
#             result += left[index_left:]
#             break
#         if index_left == len(left):
#             result += right[index_right:]
#             break
#     return result
#
# print(merge_sort(unsortedList))