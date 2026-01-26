n = int(input("Enter the number of times you want the pattern to be printed: "))

i = 1
while i <= n:
    j = 1
    while j <= 4:
        print(i, end=" ")
        j += 1
    print()
    i += 1