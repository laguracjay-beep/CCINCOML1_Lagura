Lagura_grade = int(input("Please input your grade: "))

match Lagura_grade:
    case Lagura_grade if 90 <= Lagura_grade <= 100:
        print("Excellent")
    case Lagura_grade if 80 <= Lagura_grade <= 89:
        print("Very Good")
    case Lagura_grade if 75 <= Lagura_grade <= 79:
        print("Passed")
    case Lagura_grade if 0 <= Lagura_grade <= 74:
        print("Failed")
    case _:
        print("Invalid Grade")