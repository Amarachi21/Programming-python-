def factorial(number):
    factorial = 1
    for index in range (1, number+ 1 ):
        factorial *= index
        print(index,"! = ", factorial)

n = int(input("please enter a number"))
factorial(n)
