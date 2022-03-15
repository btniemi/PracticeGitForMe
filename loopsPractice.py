# for x in range(5):
#     print(x)

# for row in range(0,5):
#     for col in range(row):
#         print(" ", end="")
#     print("*")
#
# for row in range(row, -1, -1):
#     for col in range(0, row):
#         print(" ", end="")
#     print("*")

#https://www.geeksforgeeks.org/print-the-alphabets-a-to-z-in-star-pattern/   go here to relearn loop patterns and stuff
for row in range(5):
    hight = 5 #need height and width of what you want to print
    width = 5
    for col in range(5):
        if row == col or col == (hight-1) or col == (width-5) or col == (width - (row+1)): #need to seperate these out if possible to help understand patter
            print("*", end="")
        else:
            print(end=" ")
    print()
