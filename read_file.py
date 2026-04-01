file = open("students.txt", "w")
file.write("Student Grade Report\n")
file.write("====================\n")
file.write("Alice  : A\n")
file.write("Bob    : B\n")
file.write("Charlie: C\n")
file.close()

print("File written successfully!\n")

# Opening in read mode
file = open("students.txt", "r")
content = file.read()
file.close()

print("File Contents")
print(content)