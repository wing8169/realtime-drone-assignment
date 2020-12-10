import pygame as pg
from os import path
import sys

WIDTH = 800
HEIGHT = 600
TITLE = "DRONE SIMULATOR T2G4"
GAME_TITLE = "DRONE SIMULATOR T2G4"
FPS = 60

if getattr(sys, 'frozen', False):
    # frozen
    DIR = path.dirname(sys.executable).replace("\\", "/")
else:
    # unfrozen
    DIR = path.dirname(path.realpath(__file__)).replace("\\", "/")

FONTNAME_TITLE = path.join(
    DIR, "font/BungeeInline-Regular.ttf").replace("\\", "/")
FONTNAME = path.join(DIR, "font/BungeeInline-Regular.ttf").replace("\\", "/")
IMG_DIR = path.join(DIR, "img")

# define color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 150, 255)
GREY = (161, 171, 186)
DARK_GREEN = (0, 100, 0)
DARK_GREY = (106, 110, 114)
DARK_RED = (100, 0, 0)
YELLOW = (212, 202, 62)

# player attributes
DRONE_INIT_X = WIDTH / 2
DRONE_INIT_Y = HEIGHT - 50
DRONE_SPEED = 7

# player control setting
DRONE_UP = pg.K_w
DRONE_DOWN = pg.K_s
DRONE_LEFT = pg.K_a
DRONE_RIGHT = pg.K_d
DRONE_FLY = pg.K_e
DRONE_LAND = pg.K_q
