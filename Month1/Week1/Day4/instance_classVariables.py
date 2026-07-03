#3. Demonstrate the difference between instance and class variables: track how many objects of a class have been created.
#I write a small program that demonsrates this
class Student:
    count=0     # Class variable (shared by all objects)

    def __init__(self, name):
        self.name=name       # Instance variable (different for each object)
        Student.count+=1     # Increase count whenever a new object is created

# Creating objects
student1=Student("Amna")
student2=Student("Sana")
student3=Student("Mubashra")
student4=Student("Zainab")

# Instance variables
print(student1.name)
print(student2.name)
print(student3.name)

# Class variable
print("Total objects created:", Student.count)