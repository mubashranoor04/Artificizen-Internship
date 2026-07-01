#1. Use a list comprehension to extract all even numbers from a list in one line.
numbers= [12,13,65,453,27,65,99,0,28,2,6,54,3]
even_numbers = {i for i in numbers if i%2==0}
print(even_numbers)