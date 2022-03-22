# You have n coins and you want to build a staircase with these coins.
# The staircase consists of k rows where the ith row has exactly i coins.
# The last row of the staircase may be incomplete.
# Given the integer n, return the number of complete rows of the staircase you will build.

# input = 5; output = 2 ; Explanation: Because the 3rd row is incomplete, we return 2.

def arrangeCoins(num):
    i = 0
    while num > i:
        i += 1  # keeps track of the number of coins to be used up and the rows because each row is equal to number of coins to use
        num -= i  # number of coins left to be used up
    return i  # number of completed rows


print(arrangeCoins(5))
