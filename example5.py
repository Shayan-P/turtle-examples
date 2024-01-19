import turtle

def koch_snowflake(turtle, order, size):
    if order == 0:
        turtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(turtle, order - 1, size / 3)
            turtle.left(angle)

# Create a turtle object
my_turtle = turtle.Turtle()

# Turn off animation
turtle.tracer(0)

# Set the speed of the turtle (0 is the fastest, 1 is slow, 10 is normal)
my_turtle.speed(2)

# Move the turtle to a starting position
my_turtle.penup()
my_turtle.goto(-200, 100)
my_turtle.pendown()

# Draw the Koch snowflake
my_turtle.color('grey')
my_turtle.begin_fill()
for _ in range(3):
    koch_snowflake(my_turtle, 4, 400)
    my_turtle.left(-120)
my_turtle.end_fill()

# Hide the turtle
my_turtle.hideturtle()

# Update the screen to show the final result
turtle.update()

# Display the window
turtle.done()