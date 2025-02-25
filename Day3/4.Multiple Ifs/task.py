print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
ticket = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        ticket = 5
        print(f"Child ticket is {ticket}.")
    elif age > 12 and age <= 18:
        ticket = 7
        print(f"Youth ticket is {ticket}.")
    else:
        ticket = 12
        print(f"Adult ticket is {ticket}.")

    photos = input("Do you want photos? ")
    if photos == "Yes":
        ticket += 3
        print(f"The total bill is {ticket}.")
    else:
        print(f"The total bill is {ticket}")
else:
    print("Sorry you have to grow taller before you can ride.")
