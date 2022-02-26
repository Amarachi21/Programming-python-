def first_half(my_string):
    if len(my_string) % 2 == 1:
        print("Odd length")
        return my_string
    else:
        half = len(my_string)//2
        return my_string[:half]


print(first_half("Python"))
