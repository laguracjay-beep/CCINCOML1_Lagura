Lagura_JanitorSalary = 18000
Lagura_ClerkSalary = 22000
Lagura_CashierSalary = 24000
Lagura_ManagerSalary = 40000

while True:

    Lagura_Name = input("\nPlease Input Your name: ").title()
    Lagura_Position = input("Please input your position (Please choose between: Janitor, Clerk, Cashier, and Manager): ").title()
    Lagura_Hours = int(input("Please input your hours worked: "))

    print("\nEmployee Name: ", Lagura_Name)
    print("Employee Job Position: ", Lagura_Position)

    match Lagura_Position:
        case "Janitor":
            Lagura_HalfMonthPay = Lagura_JanitorSalary / 2
            Lagura_HourlyRate = Lagura_HalfMonthPay / 88
            print("This is the Half Month Salary: ", Lagura_HalfMonthPay)
            print(f"This is the Job Rate: {Lagura_HourlyRate:.2f}")
            if Lagura_Hours < 88:
                Lagura_Absent = 88 - Lagura_Hours
                Lagura_Deduction = Lagura_Absent * Lagura_HourlyRate
                Lagura_Net = Lagura_HalfMonthPay - Lagura_Deduction
                print("This is the Absent Hours: ", Lagura_Absent)
                print(f"This is the deduction: {Lagura_Deduction:.2f}")
                print(f"This is the net: {Lagura_Net:.2f}")
            else:
                Lagura_Overtime = Lagura_Hours - 88
                Lagura_OvertimeRate = Lagura_HourlyRate * 1.25
                Lagura_OvertimePay = Lagura_Overtime * Lagura_OvertimeRate
                Lagura_Net = Lagura_HalfMonthPay + Lagura_OvertimePay
                print("This is the Overtime Hours: ", Lagura_Overtime)
                print(f"This is the Overtime Rate: {Lagura_OvertimeRate:.2f}")
                print(f"This is the Overtime Pay: {Lagura_OvertimePay:.2f}")
                print(f"This is the net pay {Lagura_Net:.2f}")
        case "Clerk":
            Lagura_HalfMonthPay = Lagura_ClerkSalary / 2
            Lagura_HourlyRate = Lagura_HalfMonthPay / 88
            print("This is the Half Month Salary", Lagura_HalfMonthPay)
            print(f"This is the Job Rate: {Lagura_HourlyRate:.2f}")
            if Lagura_Hours < 88:
                Lagura_Absent = 88 - Lagura_Hours
                Lagura_Deduction = Lagura_Absent * Lagura_HourlyRate
                Lagura_Net = Lagura_HalfMonthPay - Lagura_Deduction
                print("This is the Absent Hours: ", Lagura_Absent)
                print(f"This is the deduction: {Lagura_Deduction:.2f}")
                print(f"This is the net: {Lagura_Net:.2f}")
            else:
                Lagura_Overtime = Lagura_Hours - 88
                Lagura_OvertimeRate = Lagura_HourlyRate * 1.25
                Lagura_OvertimePay = Lagura_Overtime * Lagura_OvertimeRate
                Lagura_Net = Lagura_HalfMonthPay + Lagura_OvertimePay
                print("This is the Overtime Hours: ", Lagura_Overtime)
                print(f"This is the Overtime Rate: {Lagura_OvertimeRate:.2f}")
                print(f"This is the Overtime Pay: {Lagura_OvertimePay:.2f}")
                print(f"This is the net pay {Lagura_Net:.2f}")
        case "Cashier":
            Lagura_HalfMonthPay = Lagura_CashierSalary / 2
            Lagura_HourlyRate = Lagura_HalfMonthPay / 88
            print("This is the Half Month Salary", Lagura_HalfMonthPay)
            print(f"This is the Job Rate: {Lagura_HourlyRate:.2f}")
            if Lagura_Hours < 88:
                Lagura_Absent = 88 - Lagura_Hours
                Lagura_Deduction = Lagura_Absent * Lagura_HourlyRate
                Lagura_Net = Lagura_HalfMonthPay - Lagura_Deduction
                print("This is the Absent Hours: ", Lagura_Absent)
                print(f"This is the deduction: {Lagura_Deduction:.2f}")
                print(f"This is the net: {Lagura_Net:.2f}")
            else:
                Lagura_Overtime = Lagura_Hours - 88
                Lagura_OvertimeRate = Lagura_HourlyRate * 1.25
                Lagura_OvertimePay = Lagura_Overtime * Lagura_OvertimeRate
                Lagura_Net = Lagura_HalfMonthPay + Lagura_OvertimePay
                print("This is the Overtime Hours: ", Lagura_Overtime)
                print(f"This is the Overtime Rate: {Lagura_OvertimeRate:.2f}")
                print(f"This is the Overtime Pay: {Lagura_OvertimePay:.2f}")
                print(f"This is the net pay {Lagura_Net:.2f}")
        case "Manager":
            Lagura_HalfMonthPay = Lagura_ManagerSalary / 2
            Lagura_HourlyRate = Lagura_HalfMonthPay / 88
            print("This is the Half Month Salary", Lagura_HalfMonthPay)
            print(f"This is the Job Rate: {Lagura_HourlyRate:.2f}")
            if Lagura_Hours < 88:
                Lagura_Absent = 88 - Lagura_Hours
                Lagura_Deduction = Lagura_Absent * Lagura_HourlyRate
                Lagura_Net = Lagura_HalfMonthPay - Lagura_Deduction
                print("This is the Absent Hours: ", Lagura_Absent)
                print(f"This is the deduction: {Lagura_Deduction:.2f}")
                print(f"This is the net: {Lagura_Net:.2f}")
            else:
                Lagura_Overtime = Lagura_Hours - 88
                Lagura_OvertimeRate = Lagura_HourlyRate * 1.25
                Lagura_OvertimePay = Lagura_Overtime * Lagura_OvertimeRate
                Lagura_Net = Lagura_HalfMonthPay + Lagura_OvertimePay
                print("This is the Overtime Hours: ", Lagura_Overtime)
                print(f"This is the Overtime Rate: {Lagura_OvertimeRate:.2f}")
                print(f"This is the Overtime Pay: {Lagura_OvertimePay:.2f}")
                print(f"This is the net pay {Lagura_Net:.2f}")
        case _:
            print("Invalid Option")


    Lagura_Repeat = input("\nDo you want to calculate another employee?(Y/N): ").upper()

    if Lagura_Repeat != "Y":
        print("Thank you for using the payroll system. Goodbye!")
        break
