def multiples_of_9(number):
    for i in range(number + 1):
        print(i, "* 9 =", i * 9)


# Main code
n = int(input("Please enter a number: "))
multiples_of_9(n)
