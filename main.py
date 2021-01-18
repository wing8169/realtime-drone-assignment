from drone import *
from setting import *
import pygame as pg
import sys
import math

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

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()

    def quit(self):
        pg.quit()
        sys.exit()

    def draw_background(self):
        color = (245, 245, 245)
        pg.draw.rect(self.screen, color, pg.Rect(0, 0, 800, 600))
        self.screen.blit(self.background_img, (50, 50))

    def draw_instructions(self):
        # command instructions
        self.draw_text("Commands".format(complete=self.drone.completed),
                       None, 30, GREY, 420, 70)
        self.draw_text("Q - Take Off", None, 20, GREY, 420, 100)
        self.draw_text("E - Land", None, 20, GREY, 420, 120)
        self.draw_text("R - Toggle Manual / Automatic", None, 20, GREY, 420, 140)
        self.draw_text("1/2/3/4 - Set Next Distance To 20/50/70/100", None, 20, GREY, 420, 160)
        self.draw_text("5/6/7/8/9 - Set Next Angle To 15/30/60/90/180", None, 20, GREY, 420, 180)
        self.draw_text("W - Move Forward", None, 20, GREY, 420, 200)
        self.draw_text("S - Move Backward", None, 20, GREY, 420, 220)
        self.draw_text("A - Move Left", None, 20, GREY, 420, 240)
        self.draw_text("D - Move Right", None, 20, GREY, 420, 260)
        self.draw_text("Z - Move Up", None, 20, GREY, 420, 280)
        self.draw_text("X - Move Down", None, 20, GREY, 420, 300)
        self.draw_text("C - Rotate Clockwise", None, 20, GREY, 420, 320)
        self.draw_text("V - Rotate Anti-Clockwise", None, 20, GREY, 420, 340)
        # drone information
        self.draw_text("X Coordinate: {x}".format(x=self.drone.rect.x), None, 20, GREY, 50, 390)
        self.draw_text("Y Coordinate: {y}".format(y=self.drone.rect.y), None, 20, GREY, 50, 420)
        self.draw_text("Z Coordinate: {z}".format(z=self.drone.z), None, 20, GREY, 50, 450)
        self.draw_text("Current Angle: {a}".format(a=round(self.drone.current_angle)), None, 20, GREY, 50, 480)
        self.draw_text("Status: " + ("Taken Off" if self.drone.flying else "Landed"), None, 20, GREY, 50, 510)
        self.draw_text("Mode: {mode}".format(mode=self.drone.mode), None, 20, GREY, 50, 540)
        # other information
        self.draw_text("Distance to move: {d}".format(d=self.drone.next_distance),
                       None, 20, GREY, 420, 390)
        self.draw_text("Angle to move: {a}".format(a=self.drone.next_angle),
                       None, 20, GREY, 420, 420)
        self.draw_text("Latest command: {command}".format(command=self.drone.current_command),
                       None, 20, GREY, 420, 450)
        self.draw_text("Next checkpoint: {checkpoint}".format(checkpoint=self.drone.current_checkpoint + 1),
                       None, 20, GREY, 420, 480)
        self.draw_text("Number of completed routes: {complete}".format(complete=self.drone.completed),
                       None, 20, GREY, 420, 510)
        if self.drone.route is None:
            self.draw_text("-1m from next checkpoint", None, 20, GREY, 420, 540)
        else:
            self.draw_text(
                "{dist}m from next checkpoint".format(dist=round(calculate_dist(self.drone.rect.x, self.drone.rect.y,
                                                                                self.drone.route[0],
                                                                                self.drone.route[1]))),
                None, 20, GREY, 420, 540)

    def draw(self):
        self.draw_background()
        # draw drone
        self.all_sprites.draw(self.screen)
        # draw instruction text
        self.draw_instructions()
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

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            # toggle manual / auto for drone
            elif event.type == pg.KEYUP:
                if self.drone.flying:
                    if event.key == DRONE_TOGGLE:
                        self.drone.mode = "Manual" if self.drone.mode == "Automatic" else "Automatic"
                        if self.drone.mode == "Automatic":
                            # if just toggled automatic mode, trigger command printing
                            self.drone.current_command, self.drone.current_angle = calculate_command(
                                self.drone.current_angle,
                                self.drone.rect.x,
                                self.drone.rect.y,
                                DRONE_ROUTES[self.drone.current_checkpoint][0],
                                DRONE_ROUTES[self.drone.current_checkpoint][1])
                            self.drone.tello.send(self.drone.current_command)
                        else:
                            self.drone.tello.send("stop")
                            self.drone.current_command = "stop"
                            self.drone.target_next_route = None
                    if event.key == DRONE_UP:
                        self.drone.tello.send("up " + str(self.drone.next_distance))
                        self.drone.current_command = "up " + str(self.drone.next_distance)
                        self.drone.z += self.drone.next_distance
                    if event.key == DRONE_DOWN:
                        self.drone.tello.send("down " + str(self.drone.next_distance))
                        self.drone.current_command = "down " + str(self.drone.next_distance)
                        self.drone.z -= self.drone.next_distance
                        if self.drone.z < 0:
                            self.drone.z = 0
                    if event.key == DRONE_LEFT:
                        self.drone.tello.send("left " + str(self.drone.next_distance))
                        self.drone.current_command = "left " + str(self.drone.next_distance)
                        if self.drone.next_distance != 0:
                            target_angle = self.drone.current_angle - 90
                            target_x = self.drone.rect.x + self.drone.next_distance * math.cos(
                                math.radians(target_angle))
                            target_y = self.drone.rect.y + self.drone.next_distance * math.sin(
                                math.radians(target_angle))
                            self.drone.target_next_route = [target_x, target_y]
                    if event.key == DRONE_RIGHT:
                        self.drone.tello.send("right " + str(self.drone.next_distance))
                        self.drone.current_command = "right " + str(self.drone.next_distance)
                        if self.drone.next_distance != 0:
                            target_angle = self.drone.current_angle + 90
                            target_x = self.drone.rect.x + self.drone.next_distance * math.cos(
                                math.radians(target_angle))
                            target_y = self.drone.rect.y + self.drone.next_distance * math.sin(
                                math.radians(target_angle))
                            self.drone.target_next_route = [target_x, target_y]
                    if event.key == DRONE_FORWARD:
                        self.drone.tello.send("forward " + str(self.drone.next_distance))
                        self.drone.current_command = "forward " + str(self.drone.next_distance)
                        if self.drone.next_distance != 0:
                            target_angle = self.drone.current_angle
                            target_x = self.drone.rect.x + self.drone.next_distance * math.cos(
                                math.radians(target_angle))
                            target_y = self.drone.rect.y + self.drone.next_distance * math.sin(
                                math.radians(target_angle))
                            self.drone.target_next_route = [target_x, target_y]
                    if event.key == DRONE_BACKWARD:
                        self.drone.tello.send("backward " + str(self.drone.next_distance))
                        self.drone.current_command = "backward " + str(self.drone.next_distance)
                        self.drone.target_next_route = [self.drone.rect.x, self.drone.rect.y + self.drone.next_distance]
                        if self.drone.next_distance != 0:
                            target_angle = self.drone.current_angle - 180
                            target_x = self.drone.rect.x + self.drone.next_distance * math.cos(
                                math.radians(target_angle))
                            target_y = self.drone.rect.y + self.drone.next_distance * math.sin(
                                math.radians(target_angle))
                            self.drone.target_next_route = [target_x, target_y]
                    if event.key == DRONE_CW:
                        self.drone.tello.send("cw " + str(self.drone.next_angle))
                        self.drone.current_command = "cw " + str(self.drone.next_angle)
                        self.drone.current_angle += self.drone.next_angle
                        if self.drone.current_angle > 180:
                            self.drone.current_angle = -(360 - self.drone.current_angle)
                    if event.key == DRONE_CCW:
                        self.drone.tello.send("ccw " + str(self.drone.next_angle))
                        self.drone.current_command = "ccw " + str(self.drone.next_angle)
                        self.drone.current_angle -= self.drone.next_angle
                        if self.drone.current_angle <= -180:
                            self.drone.current_angle += 360
                if event.key == DRONE_DISTANCE_1:
                    self.drone.next_distance = DRONE_DISTANCES[0]
                elif event.key == DRONE_DISTANCE_2:
                    self.drone.next_distance = DRONE_DISTANCES[1]
                elif event.key == DRONE_DISTANCE_3:
                    self.drone.next_distance = DRONE_DISTANCES[2]
                elif event.key == DRONE_DISTANCE_4:
                    self.drone.next_distance = DRONE_DISTANCES[3]
                elif event.key == DRONE_ANGLE_1:
                    self.drone.next_angle = DRONE_ANGLES[0]
                elif event.key == DRONE_ANGLE_2:
                    self.drone.next_angle = DRONE_ANGLES[1]
                elif event.key == DRONE_ANGLE_3:
                    self.drone.next_angle = DRONE_ANGLES[2]
                elif event.key == DRONE_ANGLE_4:
                    self.drone.next_angle = DRONE_ANGLES[3]
                elif event.key == DRONE_ANGLE_5:
                    self.drone.next_angle = DRONE_ANGLES[4]
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
