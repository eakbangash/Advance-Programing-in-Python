# len String Operation
word = str(input("Enter a word"))
print(len(word))
print("*len string Operation Executed \n")

# Substring String Operation
sentence = str(input("Enter a sentence"))
word = str(input("Enter a word you want to search"))
f=0
if sentence.find(word) == -1:
   print("not found")
else:
   print("found" )
print("*Substring string Operation Executed \n")

# Concatenate String Operation
first_message = str(input("Enter first Message"))
second_message = str(input("Enter second Message"))
combining = first_message + "\t" + second_message
print(combining)
print("*Concatenate string Operation Executed \n")
