#4. Write a class with a private attribute, exposing it safely through @property
class Person:
    def __init__(self, name):
        self.__name=name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value!="":
            self.__name=value
        else:
            print("Name cannot be empty")

person1=Person("Mubashra")

print(person1.name)

person1.name="Zainab"
print(person1.name)

person1.name=""