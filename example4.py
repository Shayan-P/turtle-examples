import math
from turtle import Turtle, Screen


def radian_to_degree(radian):
    return (radian / math.pi * 180) % 360

def draw_polygon(turtle, side_length, num_sides):
    rotate_degree = 360 / num_sides
    for _ in range(num_sides):
        turtle.forward(side_length)
        turtle.left(-rotate_degree)

def chord_length(radius, angle):
    return radius * 2 * math.sin(angle/2)

def draw_approximate_circle(turtle, radius, num_sides):
    c_angle = 2 * math.pi / num_sides
    c_length = chord_length(radius, c_angle)
    draw_polygon(turtle, c_length, num_sides)


def main():
    screen = Screen()
    turtle = Turtle()

    turtle.width(3) 
    turtle.color('red')
    turtle.fillcolor('yellow')
    # screen.tracer(0)

    turtle.begin_fill()

    n = 5
    for _ in range(n):
        draw_approximate_circle(turtle, radius=100, num_sides=40)
        turtle.left(360/n)
        
    turtle.end_fill()

    screen.update()

    screen.exitonclick()

if __name__ == "__main__":
    main()