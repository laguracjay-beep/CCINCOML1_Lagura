students = {
    "Ana" : [90, 82, 93],
    "Ben" : [89, 94, 93],
    "LeBron" : [99, 99, 99],
    "Bronny" : [70,69,74]
}
highest = 0
namehighest = ""
tally = 0
lowest = 100
namelowest = ""

for name, grade in students.items():
    average = sum(grade) / len(grade)
    print(name, *grade, "Average: ", average)
    if average > highest:
        highest = average
        namehighest = name
    if average < lowest:
        lowest = average
        namelowest = name
    for g in grade:
        if g < 75:
            tally = tally + 1



print(f"Student {namehighest} got the highest average: {round(highest, 2)}")
print(f"Student {namelowest} got the lowest average: {round(lowest, 2)}")
print(f"There are {tally} grades which are below 75. ")