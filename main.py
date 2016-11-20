from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from PIL.Image import open

vertices1= [
    (0, 0),
    (100, 0),
    (100, 100),
    (0, 100)
    ]

color1 = (0,0,1)
    
vertices2= [
    (150, 0),
    (250, 0),
    (250, 100),
    (150, 100)
    ]

color2 = (0, 1, 0)

vertices3= [
    (300, 0),
    (400, 0),
    (400, 100),
    (300, 100)
    ]

color3 = (1, 0, 0)

texture = [
    (1,0),
    (1,1),
    (0,1),
    (0, 0)
    ]

window = 0                                             # glut window number
width, height = 500, 400

vertex = 1

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    refresh2d(glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT))
    
##    draw_square_color(vertices1, color1)
##    draw_square_color(vertices2, color2)
##    draw_square_color(vertices3, color3)

    draw_square_image(vertices1, "nicolini.jpg")
    draw_square_image(vertices2, "colocolo.jpeg")
    draw_square_image(vertices3, "mario.jpeg")

    glutSwapBuffers()


def init_glut():
    glutInit()                                             # initialize glut
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, height)                      # set window size
    glutInitWindowPosition(0, 0)                           # set window position
    window = glutCreateWindow("cp-project")              # create window with title
    glutDisplayFunc(draw)                               # set draw function callback
    glutKeyboardFunc(keyboard)
    glutMouseFunc(mouse)
    glutIdleFunc(draw)                                     # draw all the time
    glutMainLoop()

def draw_square_color(vertices, color):
    glColor3fv(color)

    glBegin(GL_QUADS)
    for vertex in vertices:
        glVertex2fv(vertex) 
    glEnd()

def draw_square_image(vertices, image):
    LoadTextures(image)
    glEnable(GL_TEXTURE_2D)

    glBegin(GL_QUADS)
    i = 0
    for vertex in vertices:
        glVertex2fv(vertex); glTexCoord2fv(texture[i])
        i+=1  
    glEnd() 

def mouse(button, state, x, y):
    h = glutGet(GLUT_WINDOW_HEIGHT)
    print("mouse handler: ", button, state, x, h - y)
    print vertex
    if button == GLUT_LEFT_BUTTON:
        if vertex == 1:
            vertices1[0] = (x, h - y)
        elif vertex == 2:
            vertices1[1] = (x, h - y)
        elif vertex == 3:
            vertices1[2] = (x, h - y)
        elif vertex == 4:
            vertices1[3] = (x, h - y)
        elif vertex == 5:
            vertices2[0] = (x, h - y)
        elif vertex == 6:
            vertices2[1] = (x, h - y)
        elif vertex == 7:
            vertices2[2] = (x, h - y)
        elif vertex == 8:
            vertices2[3] = (x, h - y)
        elif vertex == 9:
            vertices3[0] = (x, h - y)
        elif vertex == 10:
            vertices3[1] = (x, h - y)
        elif vertex == 11:
            vertices3[2] = (x, h - y)
        elif vertex == 12:
            vertices3[3] = (x, h - y)

def keyboard(key, x, y):
    print key
    global vertex
    if key == '1':
        vertex = 1
    elif key == '2':
        vertex = 2
    elif key == '3':
        vertex = 3
    elif key == '4':
        vertex = 4
    elif key == 'q':
        vertex = 5
    elif key == 'w':
        vertex = 6
    elif key == 'e':
        vertex = 7
    elif key == 'r':
        vertex = 8
    elif key == 'a':
        vertex = 9
    elif key == 's':
        vertex = 10
    elif key == 'd':
        vertex = 11
    elif key == 'f':
        vertex = 12

def LoadTextures(image):
    #global texture
    image = open(image)
    
    ix = image.size[0]
    iy = image.size[1]
    image = image.tobytes("raw", "RGBX", 0, -1)
    
    # Create Texture    
    glBindTexture(GL_TEXTURE_2D, glGenTextures(1))   # 2d texture (x and y size)
    
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)


def main():
    init_glut()


main()                 


