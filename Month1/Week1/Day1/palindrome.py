#Check if a given string is a palindrome
string= input("Enter a string")
reversed_string=""
for i in range(len(string)-1, -1, -1):
    reversed_string+= string[i]
print(reversed_string)

if(string==reversed_string):
    print("It is a palindrome")
else:
    print("It is not a palindrome")