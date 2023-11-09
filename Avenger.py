import turtle
import pygame
from pygame import mixer

pygame.init()
mixer.music.load('ShangChi.mp3')
mixer.music.play(-1)

screen = turtle.Screen
pencil = turtle.Turtle
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
ANIMATION_SPEED = 0

def create_screen():
    """Creates a non resizable screen with a white background color"""
    global screen
    global SCREEN_WIDTH
    global SCREEN_HEIGHT

    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.cv._rootwindow.resizable(False, False)
    # turtle.screensize(SCREEN_WIDTH, SCREEN_HEIGHT, "white")
    # https://trinket.io/docs/colors - find colors for turtle or just use r,g,b values
    screen.bgcolor("white")
    screen.onscreenclick(print_mouse_click_coordinates)

def print_mouse_click_coordinates(x, y):
    print("(",(x),",",(y),")")
    draw_circle(x, y, 2, should_fill=True)


def create_pencil():
    """Sets properties that allows our pencil to draw on the screen"""
    global pencil
    global ANIMATION_SPEED

    pencil = turtle.Turtle()
    # https://trinket.io/docs/colors - find colors for turtle or just use r,g,b values
    pencil.color("black")
    # ['arrow', 'blank', 'circle', 'classic', 'square', 'triangle', 'turtle']
    pencil.shape("arrow")
    pencil.pensize(1)
    pencil.speed(ANIMATION_SPEED)

def draw_circle(center_x, center_y, radius, should_fill=False, pen_color="black", fill_color="black"):
    global pencil

    pencil.penup()
    pencil.goto(center_x, center_y - radius)
    pencil.down()
    pencil.pencolor(pen_color)
    pencil.fillcolor(fill_color)

    if should_fill:
        pencil.begin_fill()

    pencil.circle(radius)

    if should_fill:
        pencil.end_fill()

def draw_polygon(coordinates, should_fill=False, pen_color="black", fill_color="black"):
    pencil.penup()
    pencil.pencolor(pen_color)
    pencil.fillcolor(fill_color)
    

    if len(coordinates) > 0:
        coordinates.append(coordinates[0])

    if should_fill:
        pencil.begin_fill()

    for points in coordinates:
        x, y = points
        pencil.goto(x,y)
        pencil.pendown()
        
    if should_fill:
        pencil.end_fill()

def draw_avengers_logo():
    """Will draw an avengers logo on the screen"""
    global pencil

    draw_circle(0, 0, 300, should_fill = True, fill_color = "black")
    draw_circle(0, 0, 255, should_fill=True, fill_color = "white")

    #Parallelogram - Shape 1
    draw_polygon([(-265.0, -298.0),
                  (60.0, 351.0),
                  (149.0, 364.0),
                  (-183.0, -310.0)], should_fill=True)

    #Trapezium - Shape 2
    draw_polygon([(108.0, 96.0),
                  (89.0, 253.0),
                  (148.0, 365.0),
                  (165.0, 56.0)], should_fill=True)

    #Square 1 (Fills white space)
    draw_polygon([(-18.0, 18.0),
                  (94.0, 15.0),
                  (96.0, -38.0),
                  (-43.0, -26.0)], should_fill=True)

    #Square 2 (Fills white space)       
    draw_polygon([(-16.0, 33.0),
                  (94.0, 38.0),
                  (96.0, -26.0),
                  (-43.0, -20.0)], should_fill=True)

    #Arrow - Shape 3
    draw_polygon([( 111.0 , 75.0 ),
                  ( 167.0 , 30.0 ),
                  ( 119.0 , -47.0 )], should_fill=True)

    #Triangle 1 - Shape 4
    draw_polygon([( 170.0 , 19.0 ),
                  ( 119.0 , -61.0 ),
                  ( 176.0 , -95.0 )], should_fill=True)

    #White space 1
    draw_polygon([(-230.0, -232.0),
                  (-245.0, -215.0),
                  (-205.0, -140.0),
                  (-190.0, -149.0)], should_fill=True, pen_color = "white", fill_color="white")

    #White space 2
    draw_polygon([(-165.0, -272.0),
                  (-130.0, -202.0),
                  (-117.0, -207.0),
                  (-147.0, -273.0)], should_fill=True, pen_color="white", fill_color="white")

    #Triangle 2 - Shape 5
    draw_polygon([( 120.0 , -69.0 ),
                  ( 175.0 , -102.0 ),
                  ( 122.0 , -158.0 )], should_fill=True)

    #Triangle 3.1 - Shape 6
    draw_polygon([( 177.0 , -108.0 ),
                  ( 123.0 , -166.0 ),
                  ( 183.0 , -170.0 )], should_fill=True)

    #Triangle 3.2 - Shape 6
    draw_polygon([( 123.0 , -167.0 ),
                   ( 184.0 , -171.0 ),
                   ( 125.0 , -181.0 )], should_fill=True)

    #White Spaces - Rectangle (2 right-angled triangles)
    draw_polygon([( 95.0 , 28.0 ),
                  ( 95.0 , -36.0 ),
                  ( 113.0 , 40.0 )], should_fill=True)

    #White Spaces - Rectangle (2 right-angled triangles)
    draw_polygon([( 97.0 , -38.0 ),
                  ( 114.0 , 40.0 ),
                  ( 118.0 , -33.0 )], should_fill=True)

    #Filling in white spaces
    draw_polygon([( 97.0 , -32.0 ),
                  ( 99.0 , -24.0 ),
                  ( 103.0 , -13.0 ),
                  ( 107.0 , 8.0 ),
                  ( 111.0 , 27.0 ),
                  ( 96.0 , -36.0 ),
                  ( 99.0 , -29.0 ),
                  ( 101.0 , -16.0 ),
                  ( 102.0 , -12.0 ),
                  ( 100.0 , -28.0 ),
                  ( 99.0 , -33.0 ),
                  ( 106.0 , 4.0 ),
                  ( 110.0 , 20.0 ),
                  ( 111.0 , 25.0 ),
                  ( 111.0 , 27.0 ),
                  ( 94.0 , 36.0 ),
                  ( 112.0 , 39.0 ),
                  ( 95.0 , 28.0 ),
                  ( 96.0 , 28.0 ),
                  ( 99.0 , 30.0 ),
                  ( 96.0 , 32.0 ),
                  ( 95.0 , 36.0 ),
                  ( 112.0 , 40.0 ),
                  ( 96.0 , 28.0 ),
                  ( 95.0 , 39.0 ),
                  ( 112.0 , 42.0 ),
                  ( 95.0 , 27.0 ),
                  ( 82.0 , 28.0 ),
                  ( 106.0 , 30.0 ),
                  ( 92.0 , 31.0 ),
                  ( 98.0 , 31.0 ),
                  ( 96.0 , 31.0 ),
                  ( 111.0 , 28.0 ),
                  ( 98.0 , -36.0 ),
                  ( 112.0 , 40.0 ),
                  ( 96.0 , 30.0 ),
                  ( 96.0 , 33.0 ),
                  ( 111.0 , 28.0 ),
                  ( 108.0 , 20.0 ),
                  ( 96.0 , -36.0 )], should_fill=True)
                 

def main():
    global pencil

    create_screen()
    create_pencil()

    draw_avengers_logo()

    pencil.hideturtle()

    # Needed to make sure the turtle window doesn't close after the drawing is finished
    turtle.done()


if __name__ == '__main__':
    main()
