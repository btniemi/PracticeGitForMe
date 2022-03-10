# Write a function (or small set of functions) that, given an integer, prints an
# arrow of that height. Here are a few examples for differnt inputs:
# Input is 1:
# >
#
# Input is 2:
# \
# /
#
# Input is 3:
# \
#  >
# /
#
# Input is 4:
# \
#  \
#  /
# /
#
# Input is 5:
# \
#  \
#   >
#  /
# /
# Please provide working code, in a language of your choice, to solve the above
# problem.

def arrow(n):
    if n%2 == 0:
        for i in range(0, n//2):
            for j in range(0, i):
                print(" ", end='')
            print("\\")

        for i in range(n//2, 0, -1):
            for j in range(0, i-1):
                print(" ", end='')
            print("/")
    else:
        for i in range(0, n // 2):
            for j in range(0, i):
                print(" ", end='')
            print("\\")

        for x in range(n // 2, -1, -1):
            for y in range(0, x+1):
                if y == n//2:
                    print(">")
                elif y == x:
                    print('/')
                else:
                    print(" ", end='')

arrow(1)
print("separator for new arrow print")
arrow(2)
print("separator for new arrow print")
arrow(3)
print("separator for new arrow print")
arrow(4)
print("separator for new arrow print")
arrow(5)
print("separator for new arrow print")

