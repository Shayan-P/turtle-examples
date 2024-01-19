import sys
import math

from turtle import Turtle, Screen


def draw_segment(turtle, length):
    ###########################
    #   YOUR CODE GOES HERE   #
    ###########################
    pass

def draw_square(turtle, side_length):
    ###########################
    #   YOUR CODE GOES HERE   #
    ###########################
    pass

def draw_polygon(turtle, n, side_length):
    ###########################
    #   YOUR CODE GOES HERE   #
    ###########################
    pass

def draw_pentagon(turtle, side_length):
    ###########################
    #   YOUR CODE GOES HERE   #
    ###########################
    pass

def draw_octagon(turtle, side_length):
    ###########################
    #   YOUR CODE GOES HERE   #
    ###########################
    pass

def draw_circle(turtle, radius):
    ###########################
    #   YOUR CODE GOES HERE   #
    ###########################
    pass

def draw_art(turtle):
    ###########################
    #   YOUR CODE GOES HERE   #
    ###########################
    pass


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
