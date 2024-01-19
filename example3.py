from turtle import Turtle, Screen


screen = Screen()
turtle = Turtle()

turtle.width(3) 
turtle.color('red')
turtle.fillcolor('yellow')
# screen.tracer(0)

turtle.begin_fill()
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.end_fill()

screen.update()

screen.exitonclick()
