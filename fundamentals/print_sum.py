n = int(input("Enter the number: "))

sum = 0

for num in range(1, n + 1):
    if num <= n:
        sum += num

print(sum)