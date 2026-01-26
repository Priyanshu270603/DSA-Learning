n = int(input("Enter number of rows: "))

i = n
space = 0

while i >= 1:
    # print leading spaces
    s = 1
    while s <= space:
        print(" ", end="")
        s += 1

    # print stars
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1

    print()
    space += 2
    i -= 1
