file_str = input("Open what file:")
while True:
    try:
        input_file = open(file_str)  # potential user error
    except IOError:
        print("The file", file_str, "doesn't exist.")
        file_str = input("Please enter another file name: ")
    else:
        break

find_line_str = input("Which line (integer):")
while True:
    try:
        find_line_int = int(find_line_str)
    except ValueError:
        print("Line", find_line_str, "isn't a legal line number.")
        find_line_str = input("Please enter another line (integer): ")
    else:
        break

line_count_int = 1
for line_str in input_file:
    if line_count_int == find_line_int:
        print("Line {} of file {} is {}".format(find_line_int, file_str,line_str))
        break
    line_count_int += 1
else:
    # get here if line sought doesn't exist
    print("Line {} of file {} not found".format(find_line_int, file_str))

input_file.close()
print("End of the program")
