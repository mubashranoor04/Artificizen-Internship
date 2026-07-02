#4. Write a recursive function to calculate the factorial of a number
def factorial(n):
    if (n==1 or n==0):
        return 1
    return n*factorial(n-1)

number= int(input("enter a number:"))
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {number} is {factorial(number)}")