Lagura_Patients = {
    "CJ": [80,90,85,120,40,68,70],
    "Charles": [80,130,91,70,56,100,130],
    "Clark": [90,90,120,130,140,80,99]
}

highestreading = 0
for name, reading in Lagura_Patients.items():
    tally = 0
    print("Blood sugar summary -")
    print(name)
    for item in reading:
        avg = sum(reading) / len(reading)
        diff = max(reading) - min(reading)
        if item >= 120:
            print(f"{item}: High")
            tally = tally + 1
            highestreading = item
        else:
            print(f"{item}: Normal")
    print(f"{tally} is the number of high readings")
    print(f"Highest reading: {highestreading}")
    print(f"The max reading is: {max(reading)}")
    print(f"The min reading is: {min(reading)}")
    print(f"The Average is: {avg:.2f}")
    print(f"The Difference is: {diff}")

    print("--------------------------------------------")




