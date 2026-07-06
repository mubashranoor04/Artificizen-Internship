#1. Create a base class Animal with a speak() method, and Dog/Cat subclasses that override it
class Animal():
    def speak(self):
        print("Animal makes a sound")
class Dog(Animal):
    def speak(self):
        pass
        print("Woof Woof")
class Cat(Animal):
    def speak(self):
        pass
        print("Meow Meow")
dog = Dog()
cat = Cat()
dog.speak()
cat.speak()