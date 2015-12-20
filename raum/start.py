__author__ = 'Faiku Fitim, Janusz Gradonski'

import sys
from raum import *
import tkinter
from raum.Galaxie import *

def main(sc):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)   # Select type of Display mode
        glutInitWindowSize(900, 600)                               # get a 640 x 480 window
        glutInitWindowPosition(500, 300)                              # the window starts at the upper left corner of the screen
        glutCreateWindow(b'Fitim Gradonski Solarsystem')   # Titel
        glutDisplayFunc(sc.DrawGLScene)                           # Register the drawing function with glut
        glutIdleFunc(sc.DrawGLScene)                              # scene nochmal zeichnen
     #   glutReshapeFunc(sc.ReSizeGLScene)
        # Das Fenster wird initialisiert
        sc.init(640, 480)
        glutMainLoop()


s = Galaxie(900, 600)
main(s)