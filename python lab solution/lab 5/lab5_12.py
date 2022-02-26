def largest_list(list):
    largest = list[0]
    for el in list:
        if el > largest:
            largest = el
    return largest


print(largest_list([6, 5, 4, 3, 20, 1]))
