number = int(input("How much Fibonacci Numbers do you want"))

first_number_def = 0
second_number_def = 1
temp = 0

for n in range (0,number):

    print (temp, end="   ")
    first_number_def = second_number_def
    second_number_def = temp
    temp = first_number_def + second_number_def
