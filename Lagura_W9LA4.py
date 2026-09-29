Lagura_flavor = input("Please enter pizza flavor (Hawaiian/Ham and Cheese/Four Cheese): ").lower()

if Lagura_flavor == "hawaiian":
    print("You Selected hawaiian!")
    Lagura_size = input("Please enter size (Small/Medium/Large): ").lower()
    if Lagura_size == "small":
        Lagura_price = 250
    elif Lagura_size == "medium":
        Lagura_price = 350
    elif Lagura_size == "large":
        Lagura_price = 450
    else:
        Lagura_price = 0
        print("Invalid pizza size")

elif Lagura_flavor == "ham and cheese":
    print("You Selected Ham and Cheese!")
    Lagura_size = input("Please enter size (Small/Medium/Large): ").lower()
    if Lagura_size == "small":
        Lagura_price = 300
    elif Lagura_size == "medium":
        Lagura_price = 350
    elif Lagura_size == "large":
        Lagura_price = 400
    else:
        Lagura_price = 0
        print("Invalid Pizza Size")

elif Lagura_flavor == "four cheese":
    print("You Selected Four Cheese!")
    Lagura_size = input("Please enter size (Small/Medium/Large): ").lower()
    if Lagura_size == "small":
        Lagura_price = 400
    elif Lagura_size == "medium":
        Lagura_price = 450
    elif Lagura_size == "large":
        Lagura_price = 500
    else:
        Lagura_price = 0
        print("Invalid Pizza Size")

else:
    Lagura_price = 0
    print("Invalid Pizza Flavor")

if Lagura_price > 0:
    print("This is your Price:", Lagura_price)