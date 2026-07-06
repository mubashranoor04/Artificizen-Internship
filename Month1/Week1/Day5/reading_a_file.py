#3. Write a program that reads a text file and reports the number of lines, words, and characters
file_path = "notes.txt"

with open(file_path, "r") as file:
    data = file.read()

line_count = len(data.splitlines())
word_count = len(data.split())
character_count = len(data)

print("Lines:", line_count)
print("Words:", word_count)
print("Characters:", character_count)