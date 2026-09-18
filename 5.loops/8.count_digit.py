# 8. Count digits
n = int(input("Enter a number: "))
count = 0

if n == 0:
    count = 1
else:
    n = abs(n)
    while n > 0:
        count += 1
        n //= 10

print("Number of digits:", count)
