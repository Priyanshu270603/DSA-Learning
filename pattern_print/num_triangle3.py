n = int(input("enter the number: "))

i = 1


while i <= n:
    j = 1
    num = i
    while j <= i:
        print(num, end = " ")
        num += 1
        j += 1
    print()
    i += 1