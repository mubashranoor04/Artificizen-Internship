#1. Write a function that accepts any number of arguments and returns their sum(use *args).
def sum(*numbers):
    total=0
    for i in numbers:
        total+=i
    return total

print(sum(5,10))
print(sum(1,7,6))
print(sum(8,67,43,9,2))