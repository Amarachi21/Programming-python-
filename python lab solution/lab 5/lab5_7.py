def remove_odd_chars(some_string):
    """ This program removes all the odd characters
        of a given string and returns a new one"""
    new_string = some_string[::2]
    return new_string


some_string = "ababababababab"
print(remove_odd_chars(some_string))
