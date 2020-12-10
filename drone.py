from setting import *
import pygame as pg
import random
from os import path


class Drone(pg.sprite.Sprite):
    def __init__(self, game, x, y, left, right, up, down, fly, land, stand_img, right_img, left_img,
                 speedup=1):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.stand_img = stand_img
        self.right_img = right_img
        self.left_img = left_img
        self.game = game
        self.image = self.stand_img
        self.rect = self.image.get_rect()
        self.radius = self.rect.width / 2 * .85
        self.rect.center = (x, y)
        self.speedx = 0
        self.speedy = 0
        self.mode = "automatic"
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.fly = fly
        self.land = land
        self.speedup = speedup

    def update(self):
        if self.mode == "automatic":
            self.update_automatic()
        else:
            self.update_manual()

    def update_manual(self):
        self.image = self.stand_img
        self.rect = self.rect
        self.radius = self.rect.width / 2 * .85
        self.speedx = 0
        self.speedy = 0
        keys = pg.key.get_pressed()
        if keys[self.left]:
            self.speedx -= DRONE_SPEED * self.speedup
            self.image = self.left_img
        if keys[self.right]:
            self.speedx += DRONE_SPEED * self.speedup
            self.image = self.right_img
        if keys[self.up]:
            self.speedy -= DRONE_SPEED * self.speedup
        if keys[self.down]:
            self.speedy += DRONE_SPEED * self.speedup
        if keys[self.fly]:
            # TODO: Implement fly
            pass
        if keys[self.land]:
            # TODO: Implement land
            pass
        if self.speedx != 0 and self.speedy != 0:
            self.speedx *= 0.7071
            self.speedy *= 0.7071
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def update_automatic(self):
        self.image = self.stand_img
        self.rect = self.rect
        self.radius = self.rect.width / 2 * .85
        self.speedx = 0
        self.speedy = 0
        keys = pg.key.get_pressed()
        if keys[self.left]:
            self.speedx -= DRONE_SPEED * self.speedup
            self.image = self.left_img
        if keys[self.right]:
            self.speedx += DRONE_SPEED * self.speedup
            self.image = self.right_img
        if keys[self.up]:
            self.speedy -= DRONE_SPEED * self.speedup
        if keys[self.down]:
            self.speedy += DRONE_SPEED * self.speedup
        if keys[self.fly]:
            # TODO: Implement fly
            pass
        if keys[self.land]:
            # TODO: Implement land
            pass
        if self.speedx != 0 and self.speedy != 0:
            self.speedx *= 0.7071
            self.speedy *= 0.7071
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
