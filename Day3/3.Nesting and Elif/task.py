print("Welcome to the rollercoaster!")
while True:
    try:
        height = int(input("What is your height in cm? "))
        if height < 0:
            raise ArithmeticError("Thu num should be positive")
        elif height >= 120:
            print("You can ride the rollercoaster")
            age = int(input("How old are you? "))
            if age < 0:
                raise ArithmeticError("Thu num should be positive")
            elif age <= 12 :
                print("Your ticket will cost $5")
            elif age > 12 and age <= 18:
                print("Your ticket will cost $7")
            else:
                print("Your ticket will cost $12")
        else:
            print("Sorry you have to grow taller before you can ride.")
        break
    except ValueError:
        print("ERROR!!! You have to add numbers")
    except ArithmeticError as error:
        print(error)
    except Exception:
        print("Error!!!")


