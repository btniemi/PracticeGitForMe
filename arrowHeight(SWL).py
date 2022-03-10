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
    # i chose to separate the 2 cases of even (n) given or odd (n) given and handle them separately
    if n%2 == 0:
        # for printing upper part of arrow if n == even
        for i in range(0, n//2): # I had the right process for splitting just not implemented quite right. The use of floor division helped
            for j in range(0, i):
                print(" ", end='') #prints spaces up to where need the \ to be places
            print("\\")
        # for printing the lower part
        for i in range(n//2, 0, -1): # this is like same loop above but just in reverse allows us to access peak at right point and go down from there ie other side of arrow
            for j in range(0, i-1):
                print(" ", end='')
            print("/")
    else:
        # printing top part if n == odd
        for i in range(0, n // 2):
            for j in range(0, i):
                print(" ", end='')
            print("\\")
        # printing botton part of arrow
        for x in range(n // 2, -1, -1): # <-- iterates from n//2 to -1 one extra the amount of times to get bottom half example if n=5 then top have loops 2times and this bottom half loops 3
            for y in range(0, x+1): # --> goes from 0 to how many times above loops for
                if y == n//2:
                    print(">")
                elif y == x:
                    print('/')
                else:
                    print(" ", end='')

#calls to function to print out arrows
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

