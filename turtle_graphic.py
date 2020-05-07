import turtle
wn=turtle.Screen()
alex=turtle.Turtle()
wn.bgcolor("black")
alex.shape("turtle")
bunny=turtle.Turtle()
bunny.shape("turtle")


d=50
a=90
alex.speed(1)
#,"magenta","red"

alex.shape("turtle")
d=3
a=30
alex.speed(100)
alex.right(75)
for _ in range(1000):
    PEN_COLOR=["orange","red","magenta","CRIMSON","aqua","MAROON"]
    for color in PEN_COLOR:
        alex.pencolor(color)
        alex.pensize(.5)
        #alex.stamp()
        alex.forward(d)
        alex.left(a)
        d=d+1
        s = 360/a
        l = 400
        bunny.speed(100)
        bunny.pensize(.5)
        bunny.pencolor(color)
        bunny.forward(l)
        bunny.penup()
        bunny.backward(l)
        bunny.left(a)
        bunny.pendown()
      
      #for _ in range(12):
           # PEN_COLOR = ["orange", "red", "magenta", "CRIMSON", "aqua", "MAROON"]
           # for color in PEN_COLOR:
      
                
            
        

