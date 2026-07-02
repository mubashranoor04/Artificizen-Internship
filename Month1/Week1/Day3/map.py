#2. Use map() and a lambda to square every number in a list.
number=[2,4,7,8]
result= map(lambda x: x*x, number)
print(list(result))