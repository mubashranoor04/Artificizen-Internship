#5. Sort a list of dictionaries (e.g., students with name and marks) by marks using sorted() and a key function
students = [
    {"name": "Ali", "age": 20},
    {"name": "Sara", "age": 18},
    {"name": "Ahmed", "age": 22}
]
sorted_students= sorted(students, key= lambda x:x["age"])
print(sorted_students)