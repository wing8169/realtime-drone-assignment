import pygame as pg
from os import path
import random
import sys

WIDTH = 480
HEIGHT = 600
TITLE = "SPACE TRAVELLER 20190524"
GAME_TITLE = "SPACE TRAVELLER"
FPS = 60
END_TIME = 60000 * 3

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
SND_DIR = path.join(DIR, "snd")
FILE_DIR = path.join(DIR, "score").replace("\\", "/")
HS_FILE = path.join(DIR, "highscore.txt").replace("\\", "/")

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
PLAYER_INIT_X = WIDTH / 2
PLAYER_INIT_Y = HEIGHT - 50
PLAYERSPEED = 7

# health bar settings
BAR_LENGTH = 150
BAR_HEIGHT = 15

# enemy health bar settings
ENEMY_BAR_LENGTH = 100
ENEMY_BAR_HEIGHT = 10

# define boss attributes
BOSS_1_SPEED_X = random.choice((-5, 5))
BOSS_1_SPEED_Y = random.choice((-5, 5))
BOSS_1_MOVE_RATE = 3000
BOSS_1_SPAWN_TIME = 60000

BOSS_2_SPAWN_TIME = 60000 * 2
BOSS_2_ATK_RATE = 5000
BOSS_2_MOVE_SPEED = 10

# power up configuration
POWERUP_PERIOD = 5000

# player control setting
PLAYER_1_UP = pg.K_w
PLAYER_1_DOWN = pg.K_s
PLAYER_1_LEFT = pg.K_a
PLAYER_1_RIGHT = pg.K_d
PLAYER_1_SHOOT = pg.K_j
PLAYER_1_SWISH = pg.K_k
PLAYER_2_UP = pg.K_UP
PLAYER_2_DOWN = pg.K_DOWN
PLAYER_2_LEFT = pg.K_LEFT
PLAYER_2_RIGHT = pg.K_RIGHT
PLAYER_2_SHOOT = pg.K_SEMICOLON
PLAYER_2_SWISH = pg.K_QUOTE
