# to draw we need to do this:
import turtle
# make a turtle object (basically turtle is someone else's class)
t = turtle.Turtle() # initialize turtle
# methods from turtle
t.speed(3) # set turtle speed (0-10 range for speed, 0 is instant)
t.forward(100) # move pen forward
t.left(90) # move pen 90 degrees left
t.forward(100)
t.right(90) # move pen 90 degrees right
t.forward(50)

# pen control
t.penup() # lifts your pen UP ; no drawing when moving
t.forward(50)
t.left(90)
t.forward(50)
t.pendown() # lowers your pen DOWN; back to drawing
t.forward(50)


turtle.done()