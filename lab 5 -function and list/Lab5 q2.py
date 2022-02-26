def print_even_odd(number):
    for index in range(0, number + 1):
        if index % 2 == 0:
            print(index, "is even")
        else:
            print(index, "is odd")



n = int(input("please enter a number: "))
print_even_odd(n)
