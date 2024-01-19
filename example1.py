from turtle import Turtle, Screen


screen = Screen()
turtle = Turtle()

turtle.width(3) 
turtle.color('red')
turtle.fillcolor('yellow')
# screen.tracer(0)

turtle.begin_fill()
while True:
    turtle.forward(200)
    turtle.left(170)
    if abs(turtle.pos()) < 1:
        break
turtle.end_fill()

screen.update()

screen.exitonclick()
