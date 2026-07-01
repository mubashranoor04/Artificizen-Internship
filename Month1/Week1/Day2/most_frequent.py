#6. Write a function that returns the most frequent element in a list.
num = [1,2,3,2,4,54,23,22,2,1,3,3,2]
def most_frequent(num):
    frequency= {}

    for n in num:
        frequency[n]= frequency.get(n, 0)+1
        print(frequency)
    most_frequent = num[0]

    for key in frequency:
        if frequency[key] > frequency[most_frequent]:
            most_frequent = key

    return most_frequent
print("Most frequent element" ,most_frequent(num))