from turtle import Turtle, Screen


screen = Screen()
turtle = Turtle()

turtle.width(3) 
turtle.color('red')
turtle.fillcolor('yellow')
# screen.tracer(0)

for steps in range(100):
    for c in ('blue', 'red', 'green'):
        turtle.color(c)
        turtle.forward(steps)
        turtle.right(30)

screen.update()

screen.exitonclick()
