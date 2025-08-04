from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import numpy as np


# global functions
move_count = 0
reached_end_point = False
movement_allowed = True

# Maze (Sami)
maze_walls = [
    #lines of border
    (70, 70, 820, 70),  
    (850, 70, 850, 70),
    (70, 70, 70, 700),
    (70, 700, 80, 700),
    (100, 700, 850, 700),
    (850, 70, 850, 700),
    (100, 700, 100, 700),
    (80, 700, 80, 700),
    (80, 700, 100, 700),

(70, 140, 120, 140),
(160, 70, 160, 140),
(160, 180, 210, 180),
(210, 70, 210, 180),
(110, 180, 110, 340),
(70, 370, 110, 370),
(240, 70, 240, 210),
(240, 210, 160, 210),
(370, 210, 370, 180),
(370, 180, 530, 180),
(530, 180, 530, 70),
(560, 110, 800, 110),
(590, 110, 590, 140),
(560, 140, 590, 140),
(770, 140, 630, 140),
(630, 210, 810, 210),
(810, 140, 850, 140),
(110, 700, 110, 700),
(70, 700, 110, 700),
(140, 700, 140, 610),
(140, 400, 140, 370),
(110, 450, 110, 700),
(110, 560, 180, 560),
(140, 450, 140, 530),
(140, 530, 370, 530),
(560, 530, 560, 560),
(820, 660, 820, 590),
(770, 590, 690, 590),
(560, 500, 850, 500),
(690, 470, 790, 470),
(180, 700, 180, 700),
(210, 700, 370, 700),
(210, 700, 210, 530),
(240, 650, 240, 560),
(270, 700, 270, 560),
(340, 530, 340, 630),
(370, 630, 530, 630),
(370, 630, 370, 630),
(340,590, 310, 590),
(790, 470,790, 430),
(660, 470, 660, 400),
(660, 400, 660, 370),
(660, 370, 590, 370),
(590, 370, 590, 430),
(720, 370, 720, 400),
(560, 560, 400, 560),
(270, 270, 530, 270),
(480, 240, 480, 270),
(480, 240, 430, 240),
(400, 210, 590, 210),
(590, 210, 590, 340),
(590, 340, 690, 340),
(560, 240, 560, 340),
(620, 240, 620, 340),
(620, 240, 750, 240),
(690, 270, 690, 370),
(690, 270, 850, 270),
(370, 340, 370, 310),
(690, 370, 790, 370),
(180, 400, 180, 530),
(750, 400, 850, 400),
(180, 480, 300, 480),
(210, 430, 210, 480),
(690, 70,  690, 110),
(240, 700, 240, 700),
(180, 700, 280, 700),
(210, 700, 340, 700),
(310, 700, 560, 700),
(270, 700, 370, 700),
(370, 700, 370, 700),
(450, 700, 450, 700),
(610, 700, 610, 700),
(610, 700, 450, 700),
(400, 700, 400, 650),
(160, 210, 160, 290),
(270, 407, 270, 439),
(210, 370, 370, 370),
(270, 370, 270, 340),
(240, 270, 240, 340),
(240, 340, 310, 340),
(210, 240, 370, 240),
(320, 240, 320, 110),
(320, 110, 400, 110),
(400, 140, 400, 70),
(450, 700, 450, 700),
(370, 400, 370, 470),
(370, 430, 310, 430),
(400, 700, 400, 700),
(720, 700, 720, 700),
(800, 700, 850,700),
(770, 700, 770, 700),
(770, 700, 660, 700),
(640, 700, 850, 700),
(750, 700, 750, 700),
(690, 700, 720, 700),
(720, 700, 720, 630),
(750, 700, 850, 700),
(490, 700, 490, 630),
(590, 700, 590, 630),
(590, 630, 660, 630),
(660, 630, 660, 600),
(660,600, 490, 600),
(620, 600, 620, 530),
(400, 500, 400, 430),
(400, 500, 530, 500),
(530, 500, 530, 370),
(430, 470, 490, 470),
(430, 470, 430, 430),
(470, 430, 470, 330),
(400, 370, 470, 370),
(400, 370, 400, 400),
(690, 530, 850, 530),
(770, 530, 770, 660),

]


# circle er initial position 
circle_x = 175
circle_y = 675
circle_radius = 6

# circle reset if collision detected to this point
original_circle_x = circle_x
original_circle_y = circle_y

# all pixel size
def draw_points(x, y):
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


# circle with algo (Wasifur)
def midpoint_circle_algo(x_centre, y_centre, r):
    pixels = []
    x = 0
    y = r
    pixels = store(x_centre, y_centre, x, y)
    D = 1 - r

    while x <= y:
        # storing the pixels for circle
        pixels += store(x_centre, y_centre, x, y)

        if D < 0:
            x += 1
            D = D + 2 * x + 3
        else:
            x += 1
            y -= 1
            D = D + 2 * (x - y) + 3

    return pixels

def store(x_centre, y_centre, x, y):
    pixels = []
    pixels.append([x_centre + x, y_centre + y])
    pixels.append([x_centre - x, y_centre + y])
    pixels.append([x_centre + x, y_centre - y])
    pixels.append([x_centre - x, y_centre - y])
    pixels.append([x_centre + y, y_centre + x])
    pixels.append([x_centre - y, y_centre + x])
    pixels.append([x_centre + y, y_centre - x])
    pixels.append([x_centre - y, y_centre - x])
    return pixels



# line with algo (Sami)
def midpoint_line_algo(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    zone = find_zone(dx, dy)

    x1, y1, x2, y2 = convert_to_zone_0(x1, y1, x2, y2, zone)
    X0 = []
    Y0 = []
    d = []

    dx = x2 - x1
    dy = y2 - y1
    D = 2 * dy - dx

    d = d + [D]
    dNE = 2 * (dy - dx)
    dE = 2 * dy

    x = x1
    y = y1
    while x <= x2:
        a = x
        b = y
        X0 += [x]
        Y0 += [y]

        a, b = convert_to_previous_zone(a, b, zone)
        draw_points(a, b)
        x = x + 1
        if D > 0:
            y = y + 1
            D = D + dNE
        else:
            D = D + dE
            d += [D]


def find_zone(dx, dy):
    if (dx > -1 and dy > -1):
        if (abs(dx) >= abs(dy)):
            return 0
        else:
            return 1
    elif (dx < 0 and dy > -1):
        if (abs(dx) < abs(dy)):
            return 2
        else:
            return 3
    elif (dx < 0 and dy < 0):
        if (abs(dx) >= abs(dy)):
            return 4
        else:
            return 5
    else:
        if abs(dx) < abs(dy):
            return 6
        else:
            return 7


def convert_to_zone_0(x1, y1, x2, y2, zone):
    a = 0
    b = 0
    c = 0
    d = 0

    if zone == 0:
        a = x1
        b = y1
        c = x2
        d = y2

    elif zone == 1:
        a = y1
        b = x1
        c = y2
        d = x2

    elif zone == 2:
        a = y1
        b = -x1
        c = y2
        d = -x2

    elif zone == 3:
        a = -x1
        b = y1
        c = -x2
        d = y2

    elif zone == 4:
        a = -x1
        b = -y1
        c = -x2
        d = -y2

    elif zone == 5:
        a = -y1
        b = -x1
        c = -y2
        d = -x2

    elif zone == 6:
        a = -y1
        b = x1
        c = -y2
        d = x2

    elif zone == 7:
        a = x1
        b = -y1
        c = x2
        d = -y2

    return a, b, c, d


def convert_to_previous_zone(x, y, zone):
    if zone == 0:
        return x, y

    if zone == 1:
        return y, x

    if zone == 2:
        return -y, x

    if zone == 3:
        return -x, y

    if zone == 4:
        return -x, -y

    if zone == 5:
        return -y, -x

    if zone == 6:
        return y, -x

    if zone == 7:
        return x, -y


# checking when circle collides with walls (Washifur)
def check_collision(circle_x, circle_y, circle_radius, wall):
    wall_x1, wall_y1, wall_x2, wall_y2 = wall
    distance = circle_wall_distance(circle_x, circle_y, wall_x1, wall_y1, wall_x2, wall_y2)
    return distance < circle_radius


# this is to get distance between circle and walls (Washifur)
def circle_wall_distance(px, py, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    length_sqrt = dx * dx + dy * dy
    if length_sqrt == 0:
        return math.sqrt((px - x1) ** 2 + (py - y1) ** 2)
    t = max(0, min(1, ((px - x1) *(x2 - x1) + (py - y1) * (y2 - y1)) / length_sqrt))
    nearest_x = x1 + t * dx
    nearest_y = y1 + t * dy
    distance = math.sqrt((px - nearest_x)** 2 + (py - nearest_y) ** 2)
    return distance


def iterate():
    glViewport(0, 0, 900, 900)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 900, 0.0, 900, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


# translate to move our circle (Washifur)
def translate(s, a, b, c, d, e, f):
    translated_s = []
    t = np.array([[a, b, c],
                  [d, e, f],
                  [0, 0, 1]])

    for point in s:
        p = np.array([[point[0]],
                      [point[1]],
                      [1]])

        p_prime = np.matmul(t, p)
        translated_s.append([p_prime[0][0], p_prime[1][0]])

    return translated_s


# using mouse click and keyboard clicks (Sami)
def toggle_movement(button, state, _x, _y):
    global movement_allowed
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        movement_allowed = not movement_allowed

def movement_arrows(key, x, y):
    global circle_x, circle_y, move_count, movement_allowed

    if movement_allowed:
        if key == GLUT_KEY_RIGHT:
            translating_points = translate([[circle_x, circle_y, 1]],1, 0, 10, 0, 1, 0)
            circle_x, circle_y = translating_points[0][:2]
            move_count += 1

        elif key == GLUT_KEY_LEFT:
            translating_points = translate([[circle_x, circle_y, 1]],1, 0, -10, 0, 1, 0)
            circle_x, circle_y = translating_points[0][:2]
            move_count += 1

        elif key == GLUT_KEY_UP:
            translating_points = translate([[circle_x, circle_y, 1]],1, 0, 0, 0, 1, 10)
            circle_x, circle_y = translating_points[0][:2]
            move_count += 1

        elif key == GLUT_KEY_DOWN:
            translating_points = translate([[circle_x, circle_y, 1]],1, 0, 0, 0, 1, -10)
            circle_x, circle_y = translating_points[0][:2]
            move_count += 1

    glutPostRedisplay()


# used for writing 
def write_text(x, y, text_others):
    glRasterPos2f(x, y)
    for character in text_others:
        glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ord(character))


def showScreen():
    global circle_x, circle_y, original_circle_x, original_circle_y, reached_end_point
    glClearColor(0.0, 0.0,0.0, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    # game er end point (Sami)
    if not reached_end_point:
        if abs(circle_x- 840) <= 50 and abs(circle_y -70) <= 50:
            reached_end_point = True
            glutPostRedisplay()



    # calling collision (Washifur)
    for maze_wall in maze_walls:
        if check_collision(circle_x,circle_y, circle_radius,maze_wall):
            circle_x = original_circle_x
            circle_y = original_circle_y
            break

    # maze wall color
    glColor3f(1.0, 1.0, 1.0)
    for wall in maze_walls:
        midpoint_line_algo(wall[0],wall[1], wall[2], wall[3])

    # calling circle and color
    circle_pixels = midpoint_circle_algo(circle_x,circle_y, circle_radius)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POINTS)
    for pixel in circle_pixels:
        glVertex2f(pixel[0], pixel[1])
    glEnd()


    # main and end screen writings (sami)
    if reached_end_point:
        glClearColor(0.0, 0.0, 0.0,0.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glColor3f(0.0, 0.0, 1.0)
        write_text(450, 600, "Hooray!")
        write_text(300, 570, "You have successfully completed the maze")
        write_text(390, 550, f"Your move count: {move_count}")
        glutSwapBuffers()
        return    

    glColor3f(1.0, 1.0, 1.0)
    write_text(70, 705, "Start Point")
    write_text(810, 60, "End Point")
    write_text(680,725, "left-Click to un/pause")
    write_text(680, 735, "Arrows to move")
    write_text(350,710, "Speed-run Maze Game")
    write_text(680, 710, f"Move count: {move_count}")

    glutSwapBuffers()
    glutPostRedisplay()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(900, 900)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Speed-run Maze Game")
    glutDisplayFunc(showScreen)
    glutSpecialFunc(movement_arrows)
    glutMouseFunc(toggle_movement)
    glutMainLoop()


if __name__ == "__main__":
    main()