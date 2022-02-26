def print_sum(number):
    sum = 0
    for index in range(0, number + 1):
        sum += index
        print("sum from 1 to ",index,"is ",sum)

n = int(input("please enter a number"))
print_sum(n)
