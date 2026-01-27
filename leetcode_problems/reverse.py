x = int(input("Enter the number: "))

INT_MAX = 2**31 - 1
INT_MIN = -2**31

sign = -1 if x < 0 else 1
x = abs(x)

ans = 0
while x != 0:
    digit = x % 10
    x //= 10

    # overflow check BEFORE updating
    if ans > (INT_MAX - digit) // 10:
        print(0)

    ans = ans * 10 + digit

print (sign * ans)