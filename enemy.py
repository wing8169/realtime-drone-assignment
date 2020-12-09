
from sprite import *
from setting import *
import pygame as pg
import random


class Mob(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.mob_1
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = self.rect.width / 2 * .80
        self.rect.bottom = -200
        self.rect.right = random.randrange(WIDTH - 200, WIDTH + 200)
        self.speedy = random.randrange(2, 4)
        self.speedx = random.randrange(-3, 3)
        self.health = 50
        self.left_bar = self.rect.centerx - ENEMY_BAR_LENGTH / 2
        self.bottom_bar = self.rect.bottom + 3

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.left > HEIGHT or self.rect.right < 0 or self.rect.top > HEIGHT:
            self.rect.bottom = -200
            self.rect.right = random.randrange(WIDTH - 200, WIDTH + 200)
            self.speedy = random.randrange(3, 8)
            self.speedx = random.randrange(-3, 3)
            self.health = 50
        self.left_bar = self.rect.centerx - ENEMY_BAR_LENGTH / 2
        self.bottom_bar = self.rect.bottom + 3


def draw_enemy_health_bar(self, health_pct, x, y, color=DARK_RED):
    current_health_length = health_pct * ENEMY_BAR_LENGTH
    frame_bar = pg.Rect(x, y, ENEMY_BAR_LENGTH, ENEMY_BAR_HEIGHT)
    health_bar = pg.Rect(x, y, current_health_length, ENEMY_BAR_HEIGHT)
    pg.draw.rect(self.game.screen, color, health_bar)
    pg.draw.rect(self.game.screen, WHITE, frame_bar, 2)


class Boss1(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = self.game.enemy_img
        self.rect = self.image.get_rect()
        self.radius = self.rect.width / 2 * .85
        self.rect.center = (WIDTH / 2, HEIGHT / 4)
        self.speedx = 0
        self.speedy = 0
        self.shoot_rate = 400
        self.last_shoot = pg.time.get_ticks()
        self.shield = 2000
        self.movement_timer = pg.time.get_ticks()
        self.left_bar = self.rect.centerx - ENEMY_BAR_LENGTH / 2
        self.bottom_bar = self.rect.bottom + 3

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if pg.time.get_ticks() - self.last_shoot > self.shoot_rate:
            self.shoot()
            self.last_shoot = pg.time.get_ticks()
        if pg.time.get_ticks() - self.movement_timer > BOSS_1_MOVE_RATE:
            self.speedx = random.choice((-5, 5))
            self.speedy = random.choice((-5, 5))
            self.movement_timer = pg.time.get_ticks()
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT / 2:
            self.rect.bottom = HEIGHT / 2
        self.left_bar = self.rect.centerx - ENEMY_BAR_LENGTH / 2
        self.bottom_bar = self.rect.bottom + 3

    def shoot(self):
        self.game.boss1_snd.play()
        b = EnemyBullet(self.game, 5, self.rect.centerx, self.rect.bottom + 20)
        self.game.all_sprites.add(b)
        self.game.enemybullets.add(b)
        self.last_shoot = pg.time.get_ticks()


class EnemyBullet(pg.sprite.Sprite):
    def __init__(self, game, speed, centerx, bottom):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = self.game.boss1_attack
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speed = speed
        self.radius = self.rect.width / 5

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()


class Boss2(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = self.game.boss2_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH
        self.rect.top = 0
        self.shield = 4000
        self.movement_timer = pg.time.get_ticks()
        self.attack_timer = pg.time.get_ticks()
        self.speedx = 0
        self.speedy = 0
        self.radius = self.rect.width / 4
        self.left_bar = self.rect.centerx - ENEMY_BAR_LENGTH / 2
        self.bottom_bar = self.rect.bottom + 3
        self.key = ["left", "right", "up", "down"]
        self.movement = random.choice(self.key)
        self.speed = random.choice([5, 7, 10, 13, 15])
        self.boss_move_rate = random.randrange(300, 1000)

    def update(self):
        self.left_bar = self.rect.centerx - ENEMY_BAR_LENGTH / 2
        self.bottom_bar = self.rect.bottom + 3
        if pg.time.get_ticks() - self.movement_timer > self.boss_move_rate:
            self.speed = random.choice([5, 7, 10, 13, 15])
            self.movement = random.choice(self.key)
            self.movement_timer = pg.time.get_ticks()
            self.boss_move_rate = random.randrange(300, 1000)
        if self.movement == "left":
            self.speedx = -self.speed
            self.image = self.game.boss2_left_img
        if self.movement == "down":
            self.speedy = self.speed
            self.image = self.game.boss2_img
        if self.movement == "right":
            self.speedx = self.speed
            self.image = self.game.boss2_right_img
        if self.movement == "up":
            self.speedy = -self.speed
            self.image = self.game.boss2_img
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

