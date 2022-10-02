number = int(input("Enter a number"))

for n in range(1,number)[::-1]:
    number = number*n
    n = n-1
print(number)
