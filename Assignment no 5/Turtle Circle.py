import turtle
x= turtle.Turtle ()
def circle_from_rectangle(angle):
    x.forward (100 )
    x.right (angle )
    x.forward (10 )
    x.right (angle )
    x.forward (100 )
    x.right (angle )
    x.forward (10 )
    x.right (angle+5)
for i in range(200):
    circle_from_rectangle (90)