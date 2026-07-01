#Reverse a string without using slicing or a built-in reverse function
string= input("Enter a string: ")
reversed_string=""
for i in range(len(string)-1, -1, -1):
    reversed_string += string[i]
print(reversed_string)