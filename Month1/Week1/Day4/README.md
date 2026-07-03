# Day 4 – Object-Oriented Programming (OOP) Part 1

## Topics Covered

Today I learned the fundamentals of Object-Oriented Programming (OOP) in Python and how it differs from OOP in C++.

### Concepts Studied
- Classes and Objects
- Creating Instances
- The `__init__()` Constructor
- Understanding `self`
- Instance Variables
- Class Variables
- Instance Methods
- `@classmethod`
- `@staticmethod`
- Encapsulation
- Public, Protected, and Private Attributes
- `@property` (Getters and Setters)
- Alternate Constructors using `@classmethod`

---

## Practice Questions

### 1. Car Class
- Created a `Car` class with:
  - `brand`
  - `model`
  - `year`
- Added a method to display the car's information.

### 2. BankAccount Class
- Implemented:
  - `deposit()`
  - `withdraw()`
- Prevented withdrawals when the requested amount exceeded the available balance.

### 3. Instance vs Class Variables
- Learned the difference between instance and class variables.
- Tracked the total number of objects created using a class variable.

### 4. Private Attributes with `@property`
- Created a private attribute using `__`.
- Used `@property` and `@setter` to safely access and modify the value.

### 5. Alternate Constructor
- Used `@classmethod` to create objects from a birth year instead of directly passing age.

---

## Key Learnings

- Every object has its own instance variables.
- Class variables are shared among all objects.
- `self` refers to the current object.
- `__init__()` acts as the constructor in Python.
- Instance methods work with object-specific data.
- `@classmethod` works with the class itself and can be used as an alternate constructor.
- `@staticmethod` is used for utility functions that don't depend on the object or class.
- Private attributes help protect important data.
- `@property` provides controlled access to private attributes.

---

## Progress

- **Month:** 1
- **Week:** 1
- **Day:** 4

Continuing my Python Fundamentals & OOP learning journey as part of the **Artificizen Internship Preparation**.