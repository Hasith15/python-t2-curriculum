import turtle
 
t = turtle.Turtle()
t.speed(6)

t.color("blue") # change turtle color
t.forward(100)

t.color("red")
t.pensize(4) # pen width
t.forward(100)

# filling shapes
t.penup()
t.goto(-150, 0)
t.pendown()

t.color("green")
## Call when you want whatever shape to be filled
t.begin_fill()
for i in range(4):
  t.forward(100)
  t.left(90)
## Call when you finish whatever shape you filled
t.end_fill()

turtle.done()
