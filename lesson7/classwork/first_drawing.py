import turtle
t = turtle.Turtle()
t.speed(5)

# draw a square
for i in range(4): # repeat once per side
	t.forward(100)
	t.left(90)

t.penup()
t.goto(-150, 0)  # goto (x, y) on our screen
t.pendown()

# Draw a triangle:
for i in range(3):
  t.forward(100)
  t.left(120) # for degrees of triangle

t.penup()
t.goto(-100, 150)
t.pendown()
# make a circle
t.circle(50) # draw circle with radius
t.penup()
t.goto(10, 130)
t.pendown()
# draw a house
for i in range(4):
	t.forward(80)
	t.left(90)

t.left(90)
t.forward(80)
t.right(90)

for i in range(3):
  t.forward(80)
  t.left(120)
  

turtle.done()




# yay homework is optional