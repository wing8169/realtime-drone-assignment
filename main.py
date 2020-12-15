# credits to :
# Transparent drone image: https://www.pngkey.com/download/u2w7u2q8y3t4a9r5_online-taxifahrer-dr-drone-animation/

from controller import Controller
from drone import *
from obstacle import Obstacle
from setting import *
import pygame as pg
import sys

from utils import calculate_command, calculate_dist


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
        self.alpha = 0  # hit obstacle pop up

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
            if pos.distance_to(pg.math.Vector2(obstacle.rect.x, obstacle.rect.y)) <= 60:
                if self.drone.mode != "Manual":
                    self.drone.mode = "Manual"
                    # pop up
                    self.alpha = 255
        if self.alpha > 0:
            # Reduce alpha each frame, but make sure it doesn't get below 0.
            self.alpha = max(self.alpha - 4, 0)
            self.txt_surf = self.orig_surf.copy()  # Don't modify the original text surf.
            # Fill alpha_surf with this color to set its alpha value.
            self.alpha_surf.fill((255, 255, 255, self.alpha))
            # To make the text surface transparent, blit the transparent
            # alpha_surf onto it with the BLEND_RGBA_MULT flag.
            self.txt_surf.blit(self.alpha_surf, (0, 0), special_flags=pg.BLEND_RGBA_MULT)

    def quit(self):
        pg.quit()
        sys.exit()

    def draw_background(self):
        color = (245, 245, 245)
        pg.draw.rect(self.screen, color, pg.Rect(0, 0, 800, 600))
        self.screen.blit(self.background_img, (420, 50))

    def draw_mini_map(self):
        rect = pg.Rect(self.drone.rect.left - 50, self.drone.rect.top - 50, 150, 150)
        sub = self.screen.subsurface(rect)
        screenshot = pg.Surface((150, 150))
        screenshot.blit(sub, (0, 0))
        self.screen.blit(pg.transform.scale(screenshot, (350, 300)), (30, 50))

    def draw_instructions(self):
        self.draw_text("Fly (Q), Land (E), Toggle Manual (R), Toggle Building (B)", None, 20, GREY, 30, 580)
        self.draw_text("Coordinates: ({x}, {y})".format(x=self.drone.rect.x, y=self.drone.rect.y),
                       None, 20, GREY, 420, 390)
        self.draw_text("Status: " + ("Flying" if self.drone.flying else "Landed"), None, 20, GREY, 420, 420)
        self.draw_text("Mode: {mode}".format(mode=self.drone.mode), None, 20, GREY, 420, 450)
        self.draw_text("Current command: {command}".format(command=self.drone.current_command),
                       None, 20, GREY, 420, 480)
        self.draw_text("Speed x: {x} m/s".format(x=self.drone.speedx),
                       None, 20, GREY, 420, 510)
        self.draw_text("Speed y: {y} m/s".format(y=self.drone.speedy),
                       None, 20, GREY, 420, 540)
        self.draw_text("Next checkpoint: {checkpoint}".format(checkpoint=self.drone.current_checkpoint + 1),
                       None, 20, GREY, 580, 390)
        self.draw_text("Completed: {complete}".format(complete=self.drone.completed),
                       None, 20, GREY, 580, 420)
        self.draw_text(
            "{dist}m from next checkpoint".format(dist=round(calculate_dist(self.drone.rect.x, self.drone.rect.y,
                                                                            self.drone.route[0],
                                                                            self.drone.route[1]))),
            None, 20, GREY, 580, 450)
        self.draw_text("Movement Control (WASD)".format(complete=self.drone.completed),
                       None, 20, GREY, 135, 550)

    def draw(self):
        self.draw_background()
        # draw drone
        self.all_sprites.draw(self.screen)
        # draw mini map
        self.draw_mini_map()
        # draw instruction text
        self.draw_instructions()
        self.screen.blit(self.txt_surf, (100, 250))
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
        # initialize movement controller
        self.controller = Controller(self, CONTROLLER_X, CONTROLLER_Y, DRONE_LEFT, DRONE_RIGHT,
                                     DRONE_UP, DRONE_DOWN, self.controller_img, self.controller_click_img,
                                     pg.transform.rotate(self.controller_click_img, 90),
                                     pg.transform.rotate(self.controller_click_img, 180),
                                     pg.transform.rotate(self.controller_click_img, 270))
        self.all_sprites.add(self.controller)
        # initialize obstacle
        self.obstacles = pg.sprite.Group()
        self.obstacle = Obstacle(self, 550, 150, self.building_img)
        self.obstacles.add(self.obstacle)
        self.all_sprites.add(self.obstacle)
        # initialize pop up
        self.orig_surf = self.draw_text("Detected Obstacle, Switching to Manual Mode", None, 40, DARK_RED, 350, 250,
                                        False)
        self.txt_surf = self.orig_surf.copy()
        self.alpha_surf = pg.Surface(self.txt_surf.get_size(), pg.SRCALPHA)
        self.alpha_surf.fill((255, 255, 255, self.alpha))
        self.txt_surf.blit(self.alpha_surf, (0, 0), special_flags=pg.BLEND_RGBA_MULT)
        self.run()

    def load_data(self):
        self.dir = path.dirname(path.realpath(__file__)).replace("\\", "/")
        self.img_dir = path.join(self.dir, "img")
        self.background_img = pg.image.load(
            path.join(self.img_dir, "fsktm.jpg").replace("\\", "/")).convert()
        self.background_img = pg.transform.scale(self.background_img, (350, 300))
        self.background_rect = self.background_img.get_rect()
        self.drone_img = pg.image.load(path.join(self.img_dir,
                                                 "drone.png").replace("\\", "/")).convert()
        self.drone_img = pg.transform.smoothscale(self.drone_img, (50, 50))
        self.drone_img.set_colorkey(BLACK)
        self.drone_left = pg.image.load(path.join(self.img_dir,
                                                  "drone_left.png").replace("\\", "/")).convert()
        self.drone_left = pg.transform.smoothscale(self.drone_left, (50, 50))
        self.drone_left.set_colorkey(BLACK)
        self.drone_right = pg.image.load(path.join(self.img_dir,
                                                   "drone_right.png").replace("\\", "/")).convert()
        self.drone_right = pg.transform.smoothscale(self.drone_right, (50, 50))
        self.drone_right.set_colorkey(BLACK)
        self.building_img = pg.image.load(path.join(self.img_dir,
                                                    "building.png").replace("\\", "/")).convert()
        self.building_img = pg.transform.scale(self.building_img, (50, 50))
        self.building_img.set_colorkey(BLACK)
        self.controller_img = pg.image.load(path.join(self.img_dir,
                                                      "controller_noclick.png").replace("\\", "/")).convert()
        self.controller_img = pg.transform.scale(self.controller_img, (150, 150))
        self.controller_img.set_colorkey(BLACK)
        self.controller_click_img = pg.image.load(path.join(self.img_dir,
                                                            "controller.png").replace("\\", "/")).convert()
        self.controller_click_img = pg.transform.scale(self.controller_click_img, (150, 150))
        self.controller_click_img.set_colorkey(BLACK)

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
                    else:
                        self.drone.current_command = "Manual Mode"
                if event.key == BUILDING_TOGGLE:
                    if self.obstacle.alive():
                        self.obstacle.kill()
                        self.obstacles.remove(self.obstacle)
                        self.all_sprites.remove(self.obstacle)
                    else:
                        self.obstacle = Obstacle(self, 550, 150, self.building_img)
                        self.all_sprites.add(self.obstacle)
                        self.obstacles.add(self.obstacle)
        keystate = pg.key.get_pressed()
        if keystate[pg.K_ESCAPE]:
            pg.quit()
            sys.exit()

    def draw_text(self, text, font_type, size, color, x, y, can_blit=True):
        font = pg.font.Font(font_type, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (int(x), int(y))
        if can_blit:
            self.screen.blit(text_surface, text_rect)
        return text_surface


g = Game()
while g.running:
    g.new()
