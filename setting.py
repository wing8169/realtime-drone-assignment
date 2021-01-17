import pygame as pg
from os import path

WIDTH = 800
HEIGHT = 600
TITLE = "DRONE CONTROL PANEL T2G4"
GAME_TITLE = "DRONE CONTROL PANEL T2G4"
FPS = 60

DIR = path.dirname(path.realpath(__file__)).replace("\\", "/")
IMG_DIR = path.join(DIR, "img")

# define color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 150, 255)
GREY = (80, 92, 106)
DARK_GREEN = (0, 100, 0)
DARK_GREY = (106, 110, 114)
DARK_RED = (100, 0, 0)
YELLOW = (212, 202, 62)

# player attributes
DRONE_INIT_X = 230
DRONE_INIT_Y = 80
DRONE_SPEED = 2

# player control setting
DRONE_UP = pg.K_z
DRONE_DOWN = pg.K_x
DRONE_LEFT = pg.K_a
DRONE_RIGHT = pg.K_d
DRONE_FORWARD = pg.K_w
DRONE_BACKWARD = pg.K_s
DRONE_DISTANCE_1 = pg.K_1
DRONE_DISTANCE_2 = pg.K_2
DRONE_DISTANCE_3 = pg.K_3
DRONE_DISTANCE_4 = pg.K_4
DRONE_ANGLE_1 = pg.K_5
DRONE_ANGLE_2 = pg.K_6
DRONE_ANGLE_3 = pg.K_7
DRONE_ANGLE_4 = pg.K_8
DRONE_ANGLE_5 = pg.K_9
DRONE_FLY = pg.K_q
DRONE_LAND = pg.K_e
DRONE_TOGGLE = pg.K_r
DRONE_CW = pg.K_c
DRONE_CCW = pg.K_v

# predefined route setting
DRONE_ROUTES = [[245, 50], [239, 119], [257, 159], [237, 241], [211, 300], [77, 248], [192, 50]]
DRONE_DISTANCES = [20, 50, 70, 100]
DRONE_ANGLES = [15, 30, 60, 90, 180]
