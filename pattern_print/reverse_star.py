n = int(input("Enter the number rows: "))

i = 1

while i <= n:
    sp = n - i
    while sp:
        print(" ", end = " ")
        sp -= 1

    j = 1
    while j <= i:
        print("*", end = " ")
        j += 1

    print()
    i += 1