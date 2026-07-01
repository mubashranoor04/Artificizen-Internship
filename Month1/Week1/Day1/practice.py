name= "Ayna"
age= 18
cgpa= 3.5
is_CompsciStud= True
fav_progLang= None
print("Name: ", name)
print("Age: ", age)
print("cgpa: ", cgpa)
print("Are you a computer science student? ", is_CompsciStud)
print("what's your favourite programming language: ", fav_progLang)

print(type(name))
print(type(age))
print(type(cgpa))
print(type(is_CompsciStud))
print(type(fav_progLang))

age="21"
age=int(age)+5
print(age)

if age>=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

marks=73

if (marks>=90 and marks<=100):
    print ("Grade: A")
elif (marks>=80 and marks<90):
    print ("Grade: B")
elif (marks>=70 and marks<80):
    print ("Grade: C")
else:
    print ("Fail")

#Student Information System
name= input("Enter your name: ")
age= int(input("Enter age: "))
marks= int(input("Enter marks: "))

print(f"\nHello {name}!")
if(age>=18):
    print("You can vote")
else:
    print("You can not vote")

if (marks>=90 and marks<=100):
    print ("Grade: A")
elif (marks>=80 and marks<90):
    print ("Grade: B")
elif (marks>=70 and marks<80):
    print ("Grade: C")
else:
    print ("Fail")

if (marks%2==0):
    print("marks are even")
else:
    print("marks are odd")
status="Pass" if marks>=50 else "Fail"
print(f"Status:{status}")
print (name, age, marks, sep=" | ")
print("Thank you for using the system", end=" ")
print(":)")

for i in  range(1,6):
    print (i)
#Write a program that prints all even numbers from 2 to 20 using range()
for i in range(2,22,2):
    print (i)
for i in range(5):
    print("*")

#Print numbers 1 to 10 using while

i=1
while i<11:
    print(i)
    i+=1
i=2
while i<22:
    print(i)
    i+=2
i=10
while i>0:
    print(i)
    i-=1

#Print numbers 1–10 but stop when number = 7

for i in range (1,11):
    if i==7:
        break
    print(i)

#Print 1–10 but skip number 5
for i in range(1,11):
    if i==5:
        continue
    print(i)

#Print only odd numbers from 1–20 using continue
for i in range(1,21):
    if i%2==0:
        continue
    print(i)