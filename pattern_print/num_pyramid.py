n = int(input("enter the number: "))

i = 1

while i <= n:

    sp = n - i
    while sp:
        print(" ",end=" ")
        sp -= 1

    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1

    start = i - 1
    while start:
        print(start, end=" ")
        start -= 1

    print()
    i += 1

