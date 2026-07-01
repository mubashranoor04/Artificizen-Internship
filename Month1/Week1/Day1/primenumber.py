#Write a program to check whether a number is prime
n=int(input("Enter a number: "))
isPrime = True

for i in range(2,n):
    if n%i == 0:
        isPrime = False
        break

if isPrime:
    print("Prime Number")
else:
    print("Not a Prime Number")