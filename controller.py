import pygame as pg


class Controller(pg.sprite.Sprite):
    def __init__(self, game, x, y, left, right, up, down, stand_img, down_img, right_img, up_img, left_img):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.stand_img = stand_img
        self.right_img = right_img
        self.left_img = left_img
        self.up_img = up_img
        self.down_img = down_img
        self.game = game
        self.image = self.stand_img
        self.rect = self.image.get_rect()
        self.radius = self.rect.width / 2 * .85
        self.rect.center = (x, y)
        self.left = left
        self.right = right
        self.up = up
        self.down = down

    def update(self):
        # toggle controller
        keys = pg.key.get_pressed()
        if keys[self.left]:
            self.image = self.left_img
        elif keys[self.right]:
            self.image = self.right_img
        elif keys[self.up]:
            self.image = self.up_img
        elif keys[self.down]:
            self.image = self.down_img
        else:
            self.image = self.stand_img
