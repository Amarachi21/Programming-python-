print ("How many three-digit numbers are divisible by 17?")
input("Press Enter to find out...")
list_of_ints = []
for number in range(100,1000):
    if number % 17 == 0:
         list_of_ints += number #line 7 error
print(list_of_ints)       
print(len(list_of_ints))
