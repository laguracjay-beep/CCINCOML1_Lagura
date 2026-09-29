students = {
    "Chiu": 90,
    "Tajolosa": 95,
    "Jhanvi": 95,
    "Quismundo": 93,
    "Lagura": 85,
    "Pascual": 83
}
print("STUDENT GRADES")
print("---------------")
print("Chiu: ", students["Chiu"])
print("Tajolosa: ", students["Tajolosa"])
print("Jhanvi: ", students["Jhanvi"])
print("Quismundo: ", students["Quismundo"])
print("Lagura: ", students["Lagura"])
print("Pascual: ", students["Pascual"])

students["Osas"] = 87

students["Lagura"] = 89
students["Chiu"] = 94

name1 = input("Enter Student Name: ")
grade1 = int(input("Enter Grade: "))

students[name1] = grade1
print(students)
print("\nUpdated Student Grades")
print("-------------------------")
for name, grade in students.items():
    print(name, ":", grade)

search = input("\nEnter student name to search: ")

if search in students:
    print(search, "has grade of", students[search])
else:
    print("Student not found")