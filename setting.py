import pygame as pg
from os import path

WIDTH = 800
HEIGHT = 600
TITLE = "DRONE SIMULATOR T2G4"
GAME_TITLE = "DRONE SIMULATOR T2G4"
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
DRONE_INIT_X = 600
DRONE_INIT_Y = 80
DRONE_SPEED = 2

CONTROLLER_X = 200
CONTROLLER_Y = 450

# player control setting
DRONE_UP = pg.K_w
DRONE_DOWN = pg.K_s
DRONE_LEFT = pg.K_a
DRONE_RIGHT = pg.K_d
DRONE_FLY = pg.K_q
DRONE_LAND = pg.K_e
DRONE_TOGGLE = pg.K_r
BUILDING_TOGGLE = pg.K_b

# predefined route setting
DRONE_ROUTES = [[615, 50], [609, 119], [627, 159], [607, 241], [581, 300], [447, 248], [562, 50]]
