# Writing to a file
file = open("students.txt", "w")
file.write("Student Grade Report\n")
file.write("====================\n")
file.write("Alice  : A\n")
file.write("Bob    : B\n")
file.write("Charlie: C\n")
file.close()

print("File created and content written successfully!")

#Appending
file = open("students.txt", "a")
file.write("David  : A\n")
file.write("Eve    : B\n")
file.close()

print("New content appended successfully!")

# Reading the file
file = open("students.txt", "r")
content = file.read()
file.close()

print("\n File Contents")
print(content)