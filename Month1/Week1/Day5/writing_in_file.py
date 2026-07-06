# 4. Write a program that saves a list of dictionaries (student records) to a JSON file, then loads them back
import json
student_data = [
    {"name": "amna", "marks": 76},
    {"name": "sana", "marks": 99},
    {"name": "zainab", "marks": 86}
]
with open("records.json", "w") as file:
    json.dump(student_data, file, indent=4)

with open("records.json", "r") as file:
    loaded_data = json.load(file)

print(loaded_data)