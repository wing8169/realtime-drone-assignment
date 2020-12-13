# credits to :
# Transparent drone image: https://www.pngkey.com/download/u2w7u2q8y3t4a9r5_online-taxifahrer-dr-drone-animation/

from drone import *
from obstacle import Obstacle
from setting import *
import pygame as pg
import sys

from utils import calculate_command


class Game:
    def __init__(self):
        # init controls for drone
        self.DRONE_UP = DRONE_UP
        self.DRONE_DOWN = DRONE_DOWN
        self.DRONE_LEFT = DRONE_LEFT
        self.DRONE_RIGHT = DRONE_RIGHT
        self.DRONE_FLY = DRONE_FLY
        self.DRONE_LAND = DRONE_LAND
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.load_data()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()
        # check if the drone is near the obstacles
        for obstacle in self.obstacles:
            pos = pg.math.Vector2(self.drone.rect.x, self.drone.rect.y)
            if pos.distance_to(pg.math.Vector2(obstacle.rect.x, obstacle.rect.y)) <= 90:
                self.drone.mode = "Manual"

    def quit(self):
        pg.quit()
        sys.exit()

    def draw_background(self):
        self.screen.blit(self.background_img, (0, 0))

    def draw(self):
        self.draw_background()
        # draw drone
        self.all_sprites.draw(self.screen)
        # draw mini map
        rect = pg.Rect(self.drone.rect.left - 50, self.drone.rect.top - 50, 200, 150)
        sub = self.screen.subsurface(rect)
        screenshot = pg.Surface((200, 150))
        screenshot.blit(sub, (0, 0))
        self.screen.blit(pg.transform.scale(screenshot, (200, 200)), (0, 0))
        # draw instruction text
        self.draw_text("Controls", None, 30, BLACK, 580, 50)
        self.draw_text("Fly: Q", None, 24, BLACK, 580, 80)
        self.draw_text("Building: B", None, 24, BLACK, 650, 80)
        self.draw_text("Land: E", None, 24, BLACK, 580, 110)
        self.draw_text("Manual Control: WASD", None, 24, BLACK, 580, 140)
        self.draw_text("Toggle Manual/Auto: R", None, 24, BLACK, 580, 170)
        self.draw_text("Drone Status", None, 30, BLACK, 580, 200)
        self.draw_text("Current Mode: " + self.drone.mode, None, 24, BLACK, 580, 230)
        self.draw_text("Current Position: " + ("Flying" if self.drone.flying else "Landed"), None, 24, BLACK, 580, 260)
        self.draw_text("Current Command: " + self.drone.current_command, None, 24, BLACK, 50, 290)
        pg.display.flip()

    def new(self):
        # initialize everything here
        self.game_timer = pg.time.get_ticks()
        self.all_sprites = pg.sprite.Group()
        # initialize drone
        self.drones = pg.sprite.Group()
        self.drone = Drone(self, DRONE_INIT_X, DRONE_INIT_Y, DRONE_LEFT, DRONE_RIGHT,
                           DRONE_UP, DRONE_DOWN, DRONE_FLY, DRONE_LAND, self.drone_img,
                           self.drone_right, self.drone_left)
        self.all_sprites.add(self.drone)
        self.drones.add(self.drone)
        # initialize obstacle
        self.obstacles = pg.sprite.Group()
        self.obstacle = Obstacle(self, 300, 300, self.building_img)
        self.all_sprites.add(self.obstacle)
        self.obstacles.add(self.obstacle)
        self.run()

    def load_data(self):
        self.dir = path.dirname(path.realpath(__file__)).replace("\\", "/")
        self.img_dir = path.join(self.dir, "img")
        self.background_img = pg.image.load(
            path.join(self.img_dir, "bg.jpg").replace("\\", "/")).convert()
        self.background_img = pg.transform.scale(self.background_img, (800, 600))
        self.background_rect = self.background_img.get_rect()
        self.drone_img = pg.image.load(path.join(self.img_dir,
                                                 "drone.png").replace("\\", "/")).convert()
        self.drone_img = pg.transform.scale(self.drone_img, (100, 50))
        self.drone_img.set_colorkey(BLACK)
        self.drone_left = pg.image.load(path.join(self.img_dir,
                                                  "drone_left.png").replace("\\", "/")).convert()
        self.drone_left = pg.transform.scale(self.drone_left, (100, 50))
        self.drone_left.set_colorkey(BLACK)
        self.drone_right = pg.image.load(path.join(self.img_dir,
                                                   "drone_right.png").replace("\\", "/")).convert()
        self.drone_right = pg.transform.scale(self.drone_right, (100, 50))
        self.drone_right.set_colorkey(BLACK)
        self.building_img = pg.image.load(path.join(self.img_dir,
                                                    "building.png").replace("\\", "/")).convert()
        self.building_img = pg.transform.scale(self.building_img, (100, 100))
        self.building_img.set_colorkey(BLACK)

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            # toggle manual / auto for drone
            elif event.type == pg.KEYUP:
                if event.key == DRONE_TOGGLE and self.drone.flying:
                    self.drone.mode = "Manual" if self.drone.mode == "Automatic" else "Automatic"
                    if self.drone.mode == "Automatic":
                        # if just toggled automatic mode, trigger command printing
                        self.drone.current_command, self.drone.current_angle = calculate_command(
                            self.drone.current_angle,
                            self.drone.rect.x,
                            self.drone.rect.y,
                            self.drone.route[0],
                            self.drone.route[1])
                        self.drone.tello.send(self.drone.current_command)
                if event.key == BUILDING_TOGGLE:
                    if self.obstacle.alive():
                        self.obstacle.kill()
                    else:
                        self.obstacle = Obstacle(self, 300, 300, self.building_img)
                        self.all_sprites.add(self.obstacle)
                        self.obstacles.add(self.obstacle)
        keystate = pg.key.get_pressed()
        if keystate[pg.K_ESCAPE]:
            pg.quit()
            sys.exit()

    def draw_text(self, text, font_type, size, color, x, y):
        font = pg.font.Font(font_type, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (int(x), int(y))
        self.screen.blit(text_surface, text_rect)
        return text_rect


g = Game()
while g.running:
    g.new()
