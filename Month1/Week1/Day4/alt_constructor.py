#5. Add a @classmethod to a Person class that works as an alternate constructor, e.g. Person.from_birth_year(name, year).
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    @classmethod
    def from_birth_year(cls, name, year):
        age=2026-year
        return cls(name, age)

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

person1=Person.from_birth_year("Mubashra", 2004)
person1.display()