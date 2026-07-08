# Day 03 – Functions and Python Modules

## Overview

This directory contains the programs and practice exercises completed on **Day 03** of my internship. The objective of this session was to master the creation of reusable code through functions, understand Python's module import system, write custom modules, and learn how to avoid common pitfalls like mutable default arguments.

## Topics Covered

### Functions Basics

* Defining functions (`def`)
* Parameters vs. Arguments
* Positional and Keyword Arguments
* Return values (`return`)

### Default Arguments & Best Practices

* Setting default parameters
* The risk of **Mutable Default Arguments** (e.g., `list=[]` vs `list=None`)
* Object reference and memory behavior during function definitions

### Python Modules

* Global imports (`import module`)
* Specific imports (`from module import function`)
* Understanding naming conflicts and namespace encapsulation
* Writing, structure, and executing your own custom `.py` modules
* Using `if __name__ == "__main__":` for local testing

---

## Practice Exercises

### 1. Safe Playlist Generator

* **Objective:** Create a function that appends songs to a user playlist using safe default arguments to avoid data leaking between different users.
* **Concepts Used:** Functions, Default Arguments, `None` Type Evaluation, Mutable vs Immutable Behavior.
* **File:** `playlist_manager.py`

### 2. Custom Calculator Module

* **Objective:** Write a standalone module containing core arithmetic functions and import it into a separate execution script using different import styles.
* **Concepts Used:** Custom Modules, `import`, `from ... import`, Namespace management.
* **File:** `calculator.py` and `main_app.py`

### 3. Temperature Converter with Defaults

* **Objective:** Build a function that converts temperatures between Celsius and Fahrenheit, utilizing default arguments to assume Celsius unless explicitly changed by the user.
* **Concepts Used:** Keyword Arguments, Mathematical operations, Default parameters.
* **File:** `temp_converter.py`

---

## Additional Practice

### Modules and Scope Practice

The `module_practice.py` file contains comprehensive revision exercises and experiments regarding variable scope, local vs global variables within functions, and importing standard Python libraries (like `math` and `random`) to reinforce modular coding practices.

* **Concepts Covered:** Global vs Local scope, standard library imports, aliasing modules (`import math as m`).
* **File:** `module_practice.py`

---

## Learning Outcomes

By the end of Day 03, I was able to:

* Design clean, modular, and reusable blocks of code using Python functions.
* Identify and avoid the "mutable default argument trap" by using `None` placeholders safely.
* Break large scripts down into separate, organized custom modules.
* Effectively navigate and use Python's `import` and `from ... import` syntax without breaking namespaces.
* Understand function execution context and memory allocation for default states.

---

## Status

**Completed**
