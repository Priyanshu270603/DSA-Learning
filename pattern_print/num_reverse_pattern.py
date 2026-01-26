n = int(input("Enter the number of times you want to print: "))

i = 1

while i <= n:
    j = n
    while j >= 1:
        print(j, end = " ")
        j -= 1
    print()
    i += 1