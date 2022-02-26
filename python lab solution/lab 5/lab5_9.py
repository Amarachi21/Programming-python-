def insert_string_middle(string1, string2):

    if len(string1) % 2 == 1:
        print("Function only accepts even length")
        exit()

    result = string1[:len(string1) // 2] + string2 + string1[len(string1) // 2:]
    return result


print(insert_string_middle("{{}", "PHP"))
