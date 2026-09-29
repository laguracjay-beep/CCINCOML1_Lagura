students = {
    "Ana" : [90, 82, 93],
    "Ben" : [89, 94, 93]
}

for name, grade in students.items():
    print(name, ":", *grade)

student = {
    "Ana" : (87, 85, 76),
    "Ben" : (90,97,95)
}

for name, adjective in student.items():
    print(name, ":", adjective)

