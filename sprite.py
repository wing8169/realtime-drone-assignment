from enemy import *
from setting import *
import pygame as pg
import random
from os import path


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y, left, right, up, down, shoot, swish, stand_img, right_img, left_img, player, speedup=1):
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
        self.shoot_rate = 150
        self.last_shoot = pg.time.get_ticks()
        self.shield = 100
        self.swish_rate = 5000
        self.last_swish = pg.time.get_ticks()
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.shoot = shoot
        self.swish = swish
        self.speedup = speedup
        self.start_powerup_counter = False
        self.power = 1
        self.player = player

    def update(self):
        self.image = self.stand_img
        self.rect = self.rect
        self.radius = self.rect.width / 2 * .85
        self.speedx = 0
        self.speedy = 0
        keys = pg.key.get_pressed()
        if keys[self.left]:
            self.speedx -= PLAYERSPEED * self.speedup
            self.image = self.left_img
        if keys[self.right]:
            self.speedx += PLAYERSPEED * self.speedup
            self.image = self.right_img
        if keys[self.up]:
            self.speedy -= PLAYERSPEED * self.speedup
        if keys[self.down]:
            self.speedy += PLAYERSPEED * self.speedup
        if keys[self.shoot]:
            self.shooting()
        if keys[self.swish]:
            self.sword(self.player)
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

    def shooting(self):
        if pg.time.get_ticks() - self.last_shoot > self.shoot_rate:
            self.game.laser_snd.play()
            if self.power == 1:
                b = Bullet(self.game, -5, self.rect.centerx, self.rect.top)
                self.game.all_sprites.add(b)
                self.game.bullets.add(b)
            elif self.power == 2:
                b = Bullet(self.game, -5, self.rect.centerx - 10, self.rect.top)
                self.game.all_sprites.add(b)
                self.game.bullets.add(b)
                b = Bullet(self.game, -5, self.rect.centerx + 10, self.rect.top)
                self.game.all_sprites.add(b)
                self.game.bullets.add(b)
            self.last_shoot = pg.time.get_ticks()

    def sword(self, player):
        if pg.time.get_ticks() - self.last_swish > self.swish_rate:
            self.game.swish_snd.play()
            s = Sword(self.game, player)
            self.game.all_sprites.add(s)
            self.game.swords.add(s)
            self.last_swish = pg.time.get_ticks()


class Sword(pg.sprite.Sprite):
    def __init__(self, game, player):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rot = 0
        self.player = player
        self.orig_img = self.game.sword_img
        self.image = self.orig_img.copy()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        if self.player == "player1":
            self.rect.centerx = self.game.player1.rect.centerx
            self.rect.bottom = self.game.player1.rect.top
        else:
            self.rect.centerx = self.game.player2.rect.centerx
            self.rect.bottom = self.game.player2.rect.top
        self.speed = -6
        self.rot_speed = 40
        self.animate_timer = pg.time.get_ticks()

    def update(self):
        self.rect.y += self.speed
        if pg.time.get_ticks() - self.animate_timer > 1:
            self.animate_timer = pg.time.get_ticks()
            self.rot = (self.rot + self.speed) % 360
            self.new_image = pg.transform.rotate(self.orig_img, self.rot)
            self.new_image.set_colorkey(BLACK)
            self.old_center = self.rect.center
            self.image = self.new_image
            self.new_rect = self.image.get_rect()
            self.rect.center = self.old_center
        if self.rect.bottom < 0:
            self.kill()


class Bullet(pg.sprite.Sprite):
    def __init__(self, game, speed, centerx, bottom):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = self.game.laser_light
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()


class Powerup(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.powerup_type = random.choice(["cure", "double speed", "double attack speed", "full cure", "shooting power"])
        self.image = game.powerup_img[self.powerup_type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.left = random.randrange(0, WIDTH - self.rect.width)
        self.rect.bottom = -100
        self.speedy = random.randrange(1, 4)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.kill()

