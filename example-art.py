import math

from turtle import Turtle, Screen

FULL_ROTATION_DEGREE = 360
HALF_ROTATION_DEGREE = FULL_ROTATION_DEGREE / 2
QUARTER_ROTATION_DEGREE = HALF_ROTATION_DEGREE / 2

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class PenColor:
    Green = "green"
    Magenta = "magenta"
    Orange = "orange"
    Gray = "gray"

def radian_to_degree(radian):
    return (radian / math.pi * HALF_ROTATION_DEGREE) % FULL_ROTATION_DEGREE

def draw_polygon(turtle, side_length, num_sides):
    rotate_degree = FULL_ROTATION_DEGREE / num_sides
    for _ in range(num_sides):
        turtle.forward(side_length)
        turtle.left(-rotate_degree)

def draw_square(turtle, side_length):
    square_sides = 4
    draw_polygon(turtle, side_length, square_sides)

def chord_length(radius, angle):
    return radius * 2 * math.sin(angle/2)

def draw_approximate_circle(turtle, radius, num_sides):
    c_angle = 2 * math.pi / num_sides
    c_length = chord_length(radius, c_angle)
    draw_polygon(turtle, c_length, num_sides)

def distance(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    return math.sqrt(dx*dx + dy*dy)

def draw_fractal(turtle, length, level=0):
    stem_level = 2
    stem_flower_level = 3
    flower_level = 4

    if level <= stem_level:
        color = PenColor.Green
    elif level == stem_flower_level:
        color = PenColor.Magenta
    elif level == flower_level:
        color = PenColor.Orange
    else:
        return

    rotate_angle = 10
    extra_rotate_angle = 13
    side_number = 5
    length_decay = 0.4

    for _ in range(side_number):
        turtle.forward(length)
        turtle.color(color)
        turtle.left(rotate_angle)
        turtle.left(extra_rotate_angle)
        draw_fractal(turtle, length * length_decay, level + 1)
        turtle.left(-extra_rotate_angle)

    for _ in range(side_number):
        turtle.left(-rotate_angle)
        turtle.color(color)
        turtle.left(HALF_ROTATION_DEGREE)
        turtle.forward(length)
        turtle.left(HALF_ROTATION_DEGREE)

def draw_ground(turtle, side_length, margin, iterations):
    turtle.color(PenColor.Gray)
    turtle.left(HALF_ROTATION_DEGREE)

    rotation_frw = 60
    rotation_rev = HALF_ROTATION_DEGREE - rotation_frw

    for _ in range(iterations):
        turtle.forward(side_length)
        turtle.left(rotation_frw)
        turtle.forward(margin)
        turtle.left(rotation_rev)

        turtle.forward(2 * side_length)

        turtle.left(-rotation_frw)
        turtle.forward(margin)
        turtle.left(-rotation_rev)
        turtle.forward(side_length)

    turtle.left(-QUARTER_ROTATION_DEGREE)

def draw_art(turtle):
    draw_ground(turtle, side_length=100, margin=3, iterations=2)
    fractal_side_length = 120
    draw_fractal(turtle, fractal_side_length)

def main():
    screen = Screen()
    turtle = Turtle()
    turtle.penup()
    turtle.goto(100, -300)
    turtle.pendown()
    turtle.width(3) 
    screen.tracer(0)

    draw_art(turtle)
    
    screen.update()

    screen.exitonclick()

if __name__ == "__main__":
    main()