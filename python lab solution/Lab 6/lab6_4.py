number1 = input("Please enter first number: ")
number2 = input("Please enter second number: ")
number3 = input("Please enter third number: ")

while True:
    try:
        number1 = float(number1)
        number2 = float(number2)
        number3 = float(number3)

        result = (number1 / number2) + number3
        print(result)
        break
    except ValueError:
        print("No correct values were passed.")
        number1 = input("Please enter first number: ")
        number2 = input("Please enter second number: ")
        number3 = input("Please enter third number: ")
    except ZeroDivisionError:
        print("Second number cannot be 0")
        number2 = input("Please enter second number: ")

