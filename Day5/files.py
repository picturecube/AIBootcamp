import os
from pathlib import Path
print(os.getcwd())

file_path = Path(__file__).parent / "notes.txt"
print("file_path:",file_path)
# 'with' auto-closes the file
with open(file_path, "r") as file:
    contents = file.read()
print(contents)

#this code reads line by line
with open(file_path, "r") as file:
    for line in file:
        print("Line:", line.strip())

with open("output.txt", "w") as file:
    file.write("This file was created\n")
    file.write("by my program!\n")
with open("output.txt", "r") as file:
    contents = file.read()
    print(contents)


import csv
students = [
    ["Name", "Grade", "Score"],
    ["Priya", 9, 97],
    ["Marcus", 9, 84],
]
with open("new_students.csv", "w",
          newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)