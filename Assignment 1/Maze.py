
print("forward\n"
      "left\n"
      "right\n"
      "turn\n")

a = input("sensing ")
while a == "forward":
    print("going straight!")
    a = input("sensing")
while a=="right":
    print("moving towards right")
    a = input("sensing")
while a == "left":
    print ("moving towards left")
    a = input("sensing")
while a == "turn":
    print("turn 180 degree")
while a == "left":
    print("moving towards left")
    a = input("sensing")
    break