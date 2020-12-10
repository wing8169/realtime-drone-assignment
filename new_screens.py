from new_setting import *
import pygame as pg


def show_start_screen(self):
    self.lose_snd.fadeout(2000)
    pg.mixer.music.play(-1)
    self.screen.blit(self.background_img, self.background_rect)
    self.screen.blit(self.main_icon, (WIDTH / 2 - 50, 15))
    self.waiting = True
    self.draw_text(GAME_TITLE, FONTNAME_TITLE, 40, GREY, WIDTH / 2, 150)
    text = self.draw_text("Start Game", FONTNAME, 30, GREY, WIDTH / 2, HEIGHT / 4 + 100)
    text2 = self.draw_text(self.mode, FONTNAME, 30, GREY, WIDTH / 2, HEIGHT / 4 + 175)
    text3 = self.draw_text("Setting", FONTNAME, 30, GREY, WIDTH / 2, HEIGHT / 4 + 250)
    text4 = self.draw_text("Exit Game", FONTNAME, 30, GREY, WIDTH / 2, HEIGHT / 4 + 325)
    text5 = self.draw_text("Current Game Mode Is " + self.mode, FONTNAME, 18, WHITE, WIDTH - 200, HEIGHT - 30)
    while self.waiting:
        self.clock.tick(FPS)
        self.mouse_click = False
        for event in pg.event.get():
            if event.type == pg.KEYUP:
                if event.key == pg.K_ESCAPE:
                    self.quit()
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.MOUSEBUTTONUP:
                self.mouse_click = True
        x, y = pg.mouse.get_pos()
        if text.collidepoint(x, y):
            self.screen.blit(self.background_img, self.background_rect)
            self.screen.blit(self.main_icon, (WIDTH / 2 - 50, 15))
            self.draw_text(GAME_TITLE, FONTNAME_TITLE, 40, GREY, WIDTH / 2, 150)
            text = self.draw_text("Start Game", FONTNAME, 30, DARK_GREY, WIDTH / 2, HEIGHT / 4 + 100)
            text2 = self.draw_text(self.mode, FONTNAME, 30, GREY, WIDTH / 2, HEIGHT / 4 + 175)
            text3 = self.draw_text("Setting", FONTNAME, 30, GREY, WIDTH / 2, HEIGHT / 4 + 250)
            text4 = self.draw_text("Exit Game", FONTNAME, 30, GREY, WIDTH / 2, HEIGHT / 4 + 325)
            text5 = self.draw_text("Current Game Mode Is " + self.mode, FONTNAME, 18, WHITE, WIDTH - 200, HEIGHT - 30)
            if self.mouse_click:
                self.waiting = False
        elif text2.collidepoint(x, y):
            self.screen.blit(self.background_img, self.background_rect)
            self.screen.blit(self.main_icon, (WIDTH / 2 - 50, 15))
            self.draw_text(GAME_TITLE, FONTNAME_TITLE, 40, GREY, WIDTH / 2, 150)
            text = self.draw_text("Start Game", FONTNAME, 30, GREY, WIDTH / 2, HEIGHT / 4 + 100)
            text2 = self.draw_text(self.mode, FONTNAME, 30, DARK_GREY, WIDTH / 2, HEIGHT / 4 + 175)
            text3 = self.draw_text("Setting", FONTNAME, 30, GREY, WIDTH / 2, HEIGHT / 4 + 250)
            text4 = self.draw_text("Exit Game", FONTNAME, 30, GREY, WIDTH / 2, HEIGHT / 4 + 325)
            text5 = self.draw_text("Current Game Mode Is " + self.mode, FONTNAME, 18, WHITE, WIDTH - 200, HEIGHT - 30)
            if self.mouse_click:
                if self.mode == "Single Player":
                    self.mode = "Multiplayer"
                else:
                    self.mode = "Single Player"
        elif text3.collidepoint(x, y):
            self.screen.blit(self.background_img, self.background_rect)
            self.screen.blit(self.main_icon, (WIDTH / 2 - 50, 15))
            self.draw_text(GAME_TITLE, FONTNAME_TITLE, 40, GREY, WIDTH / 2, 150)
            text = self.draw_text("Start Game", FONTNAME, 30, GREY, WIDTH / 2, HEIGHT / 4 + 100)
            text2 = self.draw_text(self.mode, FONTNAME, 30, GREY, WIDTH / 2, HEIGHT / 4 + 175)
            text3 = self.draw_text("Setting", FONTNAME, 30, DARK_GREY, WIDTH / 2, HEIGHT / 4 + 250)
            text4 = self.draw_text("Exit Game", FONTNAME, 30, GREY, WIDTH / 2, HEIGHT / 4 + 325)
            text5 = self.draw_text("Current Game Mode Is " + self.mode, FONTNAME, 18, WHITE, WIDTH - 200, HEIGHT - 30)
            if self.mouse_click:
                show_setting_screen(self)
        elif text4.collidepoint(x, y):
            self.screen.blit(self.background_img, self.background_rect)
            self.screen.blit(self.main_icon, (WIDTH / 2 - 50, 15))
            self.draw_text(GAME_TITLE, FONTNAME_TITLE, 40, GREY, WIDTH / 2, 150)
            text = self.draw_text("Start Game", FONTNAME, 30, GREY, WIDTH / 2, HEIGHT / 4 + 100)
            text2 = self.draw_text(self.mode, FONTNAME, 30, GREY, WIDTH / 2, HEIGHT / 4 + 175)
            text3 = self.draw_text("Setting", FONTNAME, 30, GREY, WIDTH / 2, HEIGHT / 4 + 250)
            text4 = self.draw_text("Exit Game", FONTNAME, 30, DARK_GREY, WIDTH / 2, HEIGHT / 4 + 325)
            text5 = self.draw_text("Current Game Mode Is " + self.mode, FONTNAME, 18, WHITE, WIDTH - 200, HEIGHT - 30)
            if self.mouse_click:
                self.quit()
        else:
            self.screen.blit(self.background_img, self.background_rect)
            self.screen.blit(self.main_icon, (WIDTH / 2 - 50, 15))
            self.draw_text(GAME_TITLE, FONTNAME_TITLE, 40, GREY, WIDTH / 2, 150)
            text = self.draw_text("Start Game", FONTNAME, 30, GREY, WIDTH / 2, HEIGHT / 4 + 100)
            text2 = self.draw_text(self.mode, FONTNAME, 30, GREY, WIDTH / 2, HEIGHT / 4 + 175)
            text3 = self.draw_text("Setting", FONTNAME, 30, GREY, WIDTH / 2, HEIGHT / 4 + 250)
            text4 = self.draw_text("Exit Game", FONTNAME, 30, GREY, WIDTH / 2, HEIGHT / 4 + 325)
            text5 = self.draw_text("Current Game Mode Is " + self.mode, FONTNAME, 18, WHITE, WIDTH - 200, HEIGHT - 30)
        pg.display.flip()
    self.new()
