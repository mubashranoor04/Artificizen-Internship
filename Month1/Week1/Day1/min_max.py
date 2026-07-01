#Given a list of numbers, find the largest and smallest without using min()/max()
numbers=[22,23,26.24,3,2,1,0,87,56,40,9]
largest=numbers[0]
smallest=numbers[0]

for num in numbers:
    if num>largest:
        largest=num
    if num<smallest:
        smallest=num

print("Numbers:", numbers)
print("Largest Number:", largest)
print("Smallest Number:", smallest)