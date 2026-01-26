n = int(input("Enter the number of rows: "))

i = 0
while i < n:
    j = 0
    while j <= i:
        print(chr(65 + i + j), end = " ")
        j += 1
    print()
    i += 1