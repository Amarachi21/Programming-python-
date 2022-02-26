def print_multiples_9(number):
    for index in range(0, number + 1):
        print(index, "*9 =",  index * 9)

n = int(input("please enter a number"))
print_multiples_9(n)
