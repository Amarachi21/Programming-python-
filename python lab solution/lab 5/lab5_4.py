def sum_of_numbers():
    number = int(input("Please enter a number: "))
    sum = 0
    for i in range(1, number + 1):
        sum += i
    return sum


# Main code
print(sum_of_numbers())

# def sum_num():
#     number = int(input("Enter a number:"))
#     sum_of_num = int(number * (number + 1) / 2)
#     print("The sum of 1 to", number, "is", sum_of_num)
#
#
# sum_num()
