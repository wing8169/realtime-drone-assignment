import pygame as pg


class Obstacle(pg.sprite.Sprite):
    def __init__(self, game, x, y, img):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = img
        self.game = game
        self.rect = self.image.get_rect()
        self.radius = self.rect.width / 2 * .85
        self.rect.center = (x, y)

    def update(self):
        pass
