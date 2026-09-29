students = {}
number = int(input("Enter Number of students: "))


for i in range(number):
    print(f"\nStudent {i + 1}")
    name = input("Input Student Name: ")
    grade1 = float(input("Enter Grade 1: "))
    grade2 = float(input("Enter Grade 2: "))
    grade3 = float(input("Enter Grade 3: "))


    students[name] = [grade1, grade2, grade3]

print("\n======== STUDENT RECORDS ===========")


highest = 0.0
namehighest = ""
tally = 0
lowest = 100
namelowest = ""



for name, grades in students.items():
    average = sum(grades) / len(grades)


    print(f"{name} - Grades: {grades[0]}, {grades[1]}, {grades[2]} | Average: {round(average, 2)}")


    if average > highest:
        highest = average
        namehighest = name
    if average < lowest:
        lowest = average
        namelowest = name

    for g in grades:
        if g < 75:
            tally = tally + 1

print("\n====================================")
print(f"Student {namehighest} got the highest average of {highest:.2f}")
print(f"Student {namelowest} got the lowest average of {lowest:.2f}")
print(f"There are {tally} grades which are below 75")
