#3. Find duplicate elements in a list using a set.
numbers= [0,8,9,0,7,8,9,6,7,9,9,0,8]

unique_num= set()
duplicate_num= set()
for n in numbers:
    if n in unique_num:
        duplicate_num.add(n)
    else:
        unique_num.add(n)
print(duplicate_num)