# 9. Check whether a number is prime
n = int(input("Enter a number: "))
prime = True

if n < 2:
    prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

if prime:
    print("Prime number")
else:
    print("Not a prime number")
