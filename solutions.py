import sys
import math

from turtle import Turtle, Screen


def draw_segment(turtle, length):
    turtle.forward(length)

def draw_square(turtle, side_length):
    turtle.forward(side_length)
    turtle.left(90)
    turtle.forward(side_length)
    turtle.left(90)
    turtle.forward(side_length)
    turtle.left(90)
    turtle.forward(side_length)
    turtle.left(90)

def draw_polygon(turtle, n, side_length):
    for i in range(n):
        turtle.forward(side_length)
        turtle.left(360/n)

def draw_pentagon(turtle, side_length):
    draw_polygon(turtle, 5, side_length)

def draw_octagon(turtle, side_length):
    draw_polygon(turtle, 10, side_length)

def draw_circle(turtle, radius):
    n = 40
    draw_polygon(turtle, n, side_length=2 * radius * math.pi / n)

def draw_art(turtle):
    turtle.fillcolor('yellow')
    turtle.begin_fill()
    draw_circle(turtle, 100)
    turtle.end_fill()

    turtle.penup()
    turtle.left(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(40)
    turtle.pendown()
    turtle.backward(80)
    turtle.forward(40)
    turtle.left(90)
    turtle.penup()
    turtle.forward(90)
    turtle.right(90)
    turtle.forward(30)
    
    turtle.pendown()
    turtle.fillcolor('gray')
    turtle.width(2)
    turtle.begin_fill()
    draw_circle(turtle, 7)
    turtle.end_fill()

    turtle.penup()
    turtle.backward(60)

    turtle.pendown()
    turtle.fillcolor('gray')
    turtle.width(2)
    turtle.begin_fill()
    draw_circle(turtle, 7)
    turtle.end_fill()


def main():
    screen = Screen()
    turtle = Turtle()
    # screen.tracer(0)

    command = sys.argv[1]
    if command == 'line':
        draw_segment(turtle, 100)
    elif command == 'square':
        draw_square(turtle, 100)
    elif command == 'pentagon':
        draw_pentagon(turtle, 100)
    elif command == 'octagon':
        draw_octagon(turtle, 100)
    elif command == 'circle':
        draw_circle(turtle, 100)
    elif command == 'art':
        draw_art(turtle)
    else:
        raise Exception("use one of the 'line' 'square' 'pentagon' 'octagon' 'circle' 'art' commands")

    turtle.hideturtle()
    screen.update()

    screen.exitonclick()

if __name__ == "__main__":
    main()
