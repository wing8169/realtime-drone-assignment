from setting import *
import pygame as pg


def convert_str_to_k():
    pass


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
                if event.key == pg.K_s:
                    show_setting_screen(self)
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_KP_ENTER:
                    self.waiting = False
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


def show_go_screen(self):
    self.game_over_time = pg.time.get_ticks()
    self.complete_pct = round((self.game_over_time - self.game_timer) / END_TIME * 100, 3)
    self.screen.blit(self.background_img, self.background_rect)
    self.draw_progress_bar(self.game_over_time - self.game_timer, self.game_end_time)
    self.draw_text("You have completed " + str(self.complete_pct) + " %", FONTNAME, 24, GREY, WIDTH / 2,
                   HEIGHT / 2 - 200)
    self.draw_text("Ahh... You lose...", FONTNAME, 32, DARK_GREY, WIDTH / 2, HEIGHT / 2 - 150)
    self.draw_text("You Score is : " + str(self.score), FONTNAME, 32, GREY, WIDTH / 2, HEIGHT / 2 - 75)
    self.draw_text("Please Try Again !", FONTNAME, 32, DARK_GREY, WIDTH / 2, HEIGHT * 3 / 4 - 150)
    text1 = self.draw_text("Back To Main Menu", FONTNAME, 32, BLUE, WIDTH / 2, HEIGHT - 200)
    self.waiting = True
    while self.waiting:
        self.clock.tick(FPS)
        mouse_click = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.MOUSEBUTTONUP:
                mouse_click = True
        x, y = pg.mouse.get_pos()
        if text1.collidepoint(x, y):
            self.screen.blit(self.background_img, self.background_rect)
            self.draw_progress_bar(self.game_over_time - self.game_timer, self.game_end_time)
            self.draw_text("You have completed " + str(self.complete_pct) + " %", FONTNAME, 24, GREY, WIDTH / 2,
                           HEIGHT / 2 - 200)
            self.draw_text("Ahh... You lose...", FONTNAME, 32, DARK_GREY, WIDTH / 2, HEIGHT / 2 - 150)
            self.draw_text("You Score is : " + str(self.score), FONTNAME, 32, GREY, WIDTH / 2, HEIGHT / 2 - 75)
            self.draw_text("Please Try Again !", FONTNAME, 32, DARK_GREY, WIDTH / 2, HEIGHT * 3 / 4 - 150)
            text1 = self.draw_text("Back To Main Menu", FONTNAME, 32, WHITE, WIDTH / 2, HEIGHT - 200)
            if mouse_click:
                show_start_screen(self)
        else:
            self.screen.blit(self.background_img, self.background_rect)
            self.draw_progress_bar(self.game_over_time - self.game_timer, self.game_end_time)
            self.draw_text("You have completed " + str(self.complete_pct) + " %", FONTNAME, 24, GREY, WIDTH / 2, HEIGHT / 2 - 200)
            self.draw_text("Ahh... You lose...", FONTNAME, 32, DARK_GREY, WIDTH / 2, HEIGHT / 2 - 150)
            self.draw_text("You Score is : " + str(self.score), FONTNAME, 32, GREY, WIDTH / 2, HEIGHT / 2 - 75)
            self.draw_text("Please Try Again !", FONTNAME, 32, DARK_GREY, WIDTH / 2, HEIGHT * 3 / 4 - 150)
            text1 = self.draw_text("Back To Main Menu", FONTNAME, 32, BLUE, WIDTH / 2, HEIGHT - 200)
        pg.display.flip()
    show_start_screen(self)


def show_win_screen(self):
    self.screen.blit(self.background_img, self.background_rect)
    self.draw_text("CONGRATULATION !", FONTNAME, 35, GREY, WIDTH / 2, HEIGHT / 2 - 200)
    self.draw_text("YOU WON !", FONTNAME, 35, DARK_GREY, WIDTH / 2, HEIGHT / 2 - 150)
    text = self.draw_text("You Score Is : " + str(self.score), FONTNAME, 32, GREY, WIDTH / 2, HEIGHT * 3 / 4 - 200)
    text2 = self.draw_text("High Score : " + str(self.highscore), FONTNAME, 32, DARK_GREY, WIDTH / 2, HEIGHT * 3 / 4 - 150)
    text3 = self.draw_text("Back To Main Menu", FONTNAME, 32, BLUE, WIDTH / 2, HEIGHT * 3 / 4)
    if self.score > self.highscore:
        self.highscore = self.score
        with open(HS_FILE, "w") as f:
            f.write(str(self.highscore))
        self.draw_text("NEW HIGH SCORE!!", FONTNAME, 32, YELLOW, WIDTH / 2, HEIGHT * 3 / 4 - 100)

    self.waiting = True
    while self.waiting:
        self.clock.tick(FPS)
        mouse_click = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.MOUSEBUTTONUP:
                mouse_click = True
        x, y = pg.mouse.get_pos()
        if text3.collidepoint(x, y):
            self.screen.blit(self.background_img, self.background_rect)
            self.draw_text("CONGRATULATION !", FONTNAME, 35, YELLOW, WIDTH / 2, HEIGHT / 2 - 200)
            self.draw_text("YOU WON !", FONTNAME, 35, YELLOW, WIDTH / 2, HEIGHT / 2 - 150)
            text = self.draw_text("You Score Is : " + str(self.score), FONTNAME, 32, YELLOW, WIDTH / 2,
                                  HEIGHT * 3 / 4 - 200)
            text2 = self.draw_text("High Score : " + str(self.highscore), FONTNAME, 32, WHITE, WIDTH / 2, HEIGHT * 3 / 4 - 150)
            if self.score == self.highscore:
                self.draw_text("NEW HIGH SCORE!!", FONTNAME, 32, YELLOW, WIDTH / 2, HEIGHT * 3 / 4 - 100)
            text3 = self.draw_text("Back To Main Menu", FONTNAME, 32, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
            if mouse_click:
                show_start_screen(self)
        else:
            self.screen.blit(self.background_img, self.background_rect)
            self.draw_text("CONGRATULATION !", FONTNAME, 35, YELLOW, WIDTH / 2, HEIGHT / 2 - 200)
            self.draw_text("YOU WON !", FONTNAME, 35, YELLOW, WIDTH / 2, HEIGHT / 2 - 150)
            text = self.draw_text("You Score Is : " + str(self.score), FONTNAME, 32, YELLOW, WIDTH / 2,
                                  HEIGHT * 3 / 4 - 200)
            text2 = self.draw_text("High Score : " + str(self.highscore), FONTNAME, 32, WHITE, WIDTH / 2, HEIGHT * 3 / 4 - 150)
            if self.score == self.highscore:
                self.draw_text("NEW HIGH SCORE!!", FONTNAME, 32, YELLOW, WIDTH / 2, HEIGHT * 3 / 4 - 100)
            text3 = self.draw_text("Back To Main Menu", FONTNAME, 32, BLUE, WIDTH / 2, HEIGHT * 3 / 4)
        pg.display.flip()
    self.running = True


def show_setting_screen(self):
    self.waiting = True
    text1 = self.draw_text("SETTING", FONTNAME, 48, BLUE, WIDTH / 2, 50)
    text2 = self.draw_text("VOLUME", FONTNAME, 24, BLUE, WIDTH / 2, HEIGHT / 2 - 100)
    text3 = self.draw_text("BACK", FONTNAME, 48, BLUE, WIDTH * 3 / 4, HEIGHT - 100)
    text4 = self.draw_text("Change Player One Controller", FONTNAME, 24, BLUE, WIDTH / 2, HEIGHT / 2)
    text5 = self.draw_text("Change Player Two Controller", FONTNAME, 24, BLUE, WIDTH / 2, HEIGHT / 2 + 75)
    while self.waiting:
        self.clock.tick(FPS)
        self.screen.blit(self.background_img, self.background_rect)
        self.mouse_click = False
        self.draw_volume_bar(self.music_volume)
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT]:
            self.music_volume -= 0.05
            if self.music_volume <= 0:
                self.music_volume = 0
            pg.mixer.music.set_volume(self.music_volume)
            self.laser_snd.set_volume(self.music_volume)
            self.swish_snd.set_volume(self.music_volume)
            self.boss1_snd.set_volume(self.music_volume)
            self.lose_snd.set_volume(self.music_volume)
            self.boss1_die_snd.set_volume(self.music_volume)
            self.boss1_dmg_snd.set_volume(self.music_volume)
            self.mob1_die_snd.set_volume(self.music_volume)
            self.powerup_snd['cure'].set_volume(self.music_volume)
            self.powerup_snd['double speed'].set_volume(self.music_volume)
            self.powerup_snd['double attack speed'].set_volume(self.music_volume)
            self.powerup_snd['full cure'].set_volume(self.music_volume)
            self.powerup_snd['shooting power'].set_volume(self.music_volume)
        if keystate[pg.K_RIGHT]:
            self.music_volume += 0.05
            if self.music_volume >= 1:
                self.music_volume = 1
            pg.mixer.music.set_volume(self.music_volume)
            self.laser_snd.set_volume(self.music_volume)
            self.swish_snd.set_volume(self.music_volume)
            self.boss1_snd.set_volume(self.music_volume)
            self.lose_snd.set_volume(self.music_volume)
            self.boss1_die_snd.set_volume(self.music_volume)
            self.boss1_dmg_snd.set_volume(self.music_volume)
            self.mob1_die_snd.set_volume(self.music_volume)
            self.powerup_snd['cure'].set_volume(self.music_volume)
            self.powerup_snd['double speed'].set_volume(self.music_volume)
            self.powerup_snd['double attack speed'].set_volume(self.music_volume)
            self.powerup_snd['full cure'].set_volume(self.music_volume)
            self.powerup_snd['shooting power'].set_volume(self.music_volume)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.MOUSEBUTTONUP:
                self.mouse_click = True
            if event.type == pg.KEYUP:
                if event.key == pg.K_ESCAPE:
                    show_start_screen(self)
        x, y = pg.mouse.get_pos()
        if text1.collidepoint(x, y):
            self.screen.blit(self.background_img, self.background_rect)
            text1 = self.draw_text("SETTING", FONTNAME, 48, WHITE, WIDTH / 2, 50)
            text2 = self.draw_text("VOLUME", FONTNAME, 24, BLUE, WIDTH / 2, HEIGHT / 2 - 100)
            text3 = self.draw_text("BACK", FONTNAME, 48, BLUE, WIDTH * 3 / 4, HEIGHT - 100)
            text4 = self.draw_text("Change Player One Controller", FONTNAME, 24, BLUE, WIDTH / 2, HEIGHT / 2)
            text5 = self.draw_text("Change Player Two Controller", FONTNAME, 24, BLUE, WIDTH / 2, HEIGHT / 2 + 75)
            self.draw_volume_bar(self.music_volume)
        elif text2.collidepoint(x, y):
            self.screen.blit(self.background_img, self.background_rect)
            text1 = self.draw_text("SETTING", FONTNAME, 48, BLUE, WIDTH / 2, 50)
            text2 = self.draw_text("VOLUME", FONTNAME, 24, WHITE, WIDTH / 2, HEIGHT / 2 - 100)
            text3 = self.draw_text("BACK", FONTNAME, 48, BLUE, WIDTH * 3 / 4, HEIGHT - 100)
            text4 = self.draw_text("Change Player One Controller", FONTNAME, 24, BLUE, WIDTH / 2, HEIGHT / 2)
            text5 = self.draw_text("Change Player Two Controller", FONTNAME, 24, BLUE, WIDTH / 2, HEIGHT / 2 + 75)
            self.draw_volume_bar(self.music_volume)
        elif text3.collidepoint(x, y):
            self.screen.blit(self.background_img, self.background_rect)
            text1 = self.draw_text("SETTING", FONTNAME, 48, BLUE, WIDTH / 2, 50)
            text2 = self.draw_text("VOLUME", FONTNAME, 24, BLUE, WIDTH / 2, HEIGHT / 2 - 100)
            text3 = self.draw_text("BACK", FONTNAME, 48, WHITE, WIDTH * 3 / 4, HEIGHT - 100)
            text4 = self.draw_text("Change Player One Controller", FONTNAME, 24, BLUE, WIDTH / 2, HEIGHT / 2)
            text5 = self.draw_text("Change Player Two Controller", FONTNAME, 24, BLUE, WIDTH / 2, HEIGHT / 2 + 75)
            self.draw_volume_bar(self.music_volume)
            if self.mouse_click:
                show_start_screen(self)
        elif text4.collidepoint(x, y):
            self.screen.blit(self.background_img, self.background_rect)
            text1 = self.draw_text("SETTING", FONTNAME, 48, BLUE, WIDTH / 2, 50)
            text2 = self.draw_text("VOLUME", FONTNAME, 24, BLUE, WIDTH / 2, HEIGHT / 2 - 100)
            text3 = self.draw_text("BACK", FONTNAME, 48, BLUE, WIDTH * 3 / 4, HEIGHT - 100)
            text4 = self.draw_text("Change Player One Controller", FONTNAME, 24, WHITE, WIDTH / 2, HEIGHT / 2)
            text5 = self.draw_text("Change Player Two Controller", FONTNAME, 24, BLUE, WIDTH / 2, HEIGHT / 2 + 75)
            self.draw_volume_bar(self.music_volume)
            if self.mouse_click:
                player1_controller(self)
        elif text5.collidepoint(x, y):
            self.screen.blit(self.background_img, self.background_rect)
            text1 = self.draw_text("SETTING", FONTNAME, 48, BLUE, WIDTH / 2, 50)
            text2 = self.draw_text("VOLUME", FONTNAME, 24, BLUE, WIDTH / 2, HEIGHT / 2 - 100)
            text3 = self.draw_text("BACK", FONTNAME, 48, BLUE, WIDTH * 3 / 4, HEIGHT - 100)
            text4 = self.draw_text("Change Player One Controller", FONTNAME, 24, BLUE, WIDTH / 2, HEIGHT / 2)
            text5 = self.draw_text("Change Player Two Controller", FONTNAME, 24, WHITE, WIDTH / 2, HEIGHT / 2 + 75)
            self.draw_volume_bar(self.music_volume)
            if self.mouse_click:
                player2_controller(self)
        else:
            self.screen.blit(self.background_img, self.background_rect)
            text1 = self.draw_text("SETTING", FONTNAME, 48, BLUE, WIDTH / 2, 50)
            text2 = self.draw_text("VOLUME", FONTNAME, 24, BLUE, WIDTH / 2, HEIGHT / 2 - 100)
            text3 = self.draw_text("BACK", FONTNAME, 48, BLUE, WIDTH * 3 / 4, HEIGHT - 100)
            text4 = self.draw_text("Change Player One Controller", FONTNAME, 24, BLUE, WIDTH / 2, HEIGHT / 2)
            text5 = self.draw_text("Change Player Two Controller", FONTNAME, 24, BLUE, WIDTH / 2, HEIGHT / 2 + 75)
            self.draw_volume_bar(self.music_volume)
        pg.display.flip()


def player1_controller(self):
    self.waiting = True
    self.select = ""
    text1 = self.draw_text("SETTING", FONTNAME, 48, BLUE, WIDTH / 2, 50)
    text2 = self.draw_text("Move Up : " + pg.key.name(self.PLAYER_1_UP), FONTNAME, 24, BLUE, WIDTH / 2, 150)
    text3 = self.draw_text("BACK", FONTNAME, 48, BLUE, WIDTH * 3 / 4, HEIGHT - 100)
    text4 = self.draw_text("Move Down : " + pg.key.name(self.PLAYER_1_DOWN), FONTNAME, 24, YELLOW, WIDTH / 2, 200)
    text5 = self.draw_text("Move Left : " + pg.key.name(self.PLAYER_1_LEFT), FONTNAME, 24, BLUE, WIDTH / 2, 250)
    text6 = self.draw_text("Move right : " + pg.key.name(self.PLAYER_1_RIGHT), FONTNAME, 24, YELLOW, WIDTH / 2, 300)
    text7 = self.draw_text("Shoot : " + pg.key.name(self.PLAYER_1_SHOOT), FONTNAME, 24, BLUE, WIDTH / 2, 350)
    text8 = self.draw_text("Skills : " + pg.key.name(self.PLAYER_1_SWISH), FONTNAME, 24, YELLOW, WIDTH / 2, 400)
    while self.waiting:
        self.clock.tick(FPS)
        self.screen.blit(self.background_img, self.background_rect)
        self.mouse_click = False
        keystate = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.MOUSEBUTTONUP:
                self.mouse_click = True
            if event.type == pg.KEYUP:
                if event.key == pg.K_ESCAPE:
                    show_start_screen(self)
                if self.select == "up":
                    self.PLAYER_1_UP = event.key
                elif self.select == "down":
                    self.PLAYER_1_DOWN = event.key
                elif self.select == "left":
                    self.PLAYER_1_LEFT = event.key
                elif self.select == "right":
                    self.PLAYER_1_RIGHT = event.key
                elif self.select == "shoot":
                    self.PLAYER_1_SHOOT = event.key
                elif self.select == "swish":
                    self.PLAYER_1_SWISH = event.key
        x, y = pg.mouse.get_pos()
        if text3.collidepoint(x, y):
            self.screen.blit(self.background_img, self.background_rect)
            text1 = self.draw_text("SETTING", FONTNAME, 48, BLUE, WIDTH / 2, 50)
            text2 = self.draw_text("Move Up : " + pg.key.name(self.PLAYER_1_UP), FONTNAME, 24, BLUE, WIDTH / 2, 150)
            text3 = self.draw_text("BACK", FONTNAME, 48, WHITE, WIDTH * 3 / 4, HEIGHT - 100)
            text4 = self.draw_text("Move Down : " + pg.key.name(self.PLAYER_1_DOWN), FONTNAME, 24, YELLOW, WIDTH / 2,
                                   200)
            text5 = self.draw_text("Move Left : " + pg.key.name(self.PLAYER_1_LEFT), FONTNAME, 24, BLUE, WIDTH / 2, 250)
            text6 = self.draw_text("Move right : " + pg.key.name(self.PLAYER_1_RIGHT), FONTNAME, 24, YELLOW, WIDTH / 2,
                                   300)
            text7 = self.draw_text("Shoot : " + pg.key.name(self.PLAYER_1_SHOOT), FONTNAME, 24, BLUE, WIDTH / 2, 350)
            text8 = self.draw_text("Skills : " + pg.key.name(self.PLAYER_1_SWISH), FONTNAME, 24, YELLOW, WIDTH / 2, 400)
            if self.mouse_click:
                show_setting_screen(self)

        elif text2.collidepoint(x, y):
            self.screen.blit(self.background_img, self.background_rect)
            text1 = self.draw_text("SETTING", FONTNAME, 48, BLUE, WIDTH / 2, 50)
            text2 = self.draw_text("Move Up : " + pg.key.name(self.PLAYER_1_UP), FONTNAME, 24, WHITE, WIDTH / 2, 150)
            text3 = self.draw_text("BACK", FONTNAME, 48, BLUE, WIDTH * 3 / 4, HEIGHT - 100)
            text4 = self.draw_text("Move Down : " + pg.key.name(self.PLAYER_1_DOWN), FONTNAME, 24, YELLOW, WIDTH / 2,
                                   200)
            text5 = self.draw_text("Move Left : " + pg.key.name(self.PLAYER_1_LEFT), FONTNAME, 24, BLUE, WIDTH / 2, 250)
            text6 = self.draw_text("Move right : " + pg.key.name(self.PLAYER_1_RIGHT), FONTNAME, 24, YELLOW, WIDTH / 2,
                                   300)
            text7 = self.draw_text("Shoot : " + pg.key.name(self.PLAYER_1_SHOOT), FONTNAME, 24, BLUE, WIDTH / 2, 350)
            text8 = self.draw_text("Skills : " + pg.key.name(self.PLAYER_1_SWISH), FONTNAME, 24, YELLOW, WIDTH / 2, 400)
            if self.mouse_click:
                self.select = "up"

        elif text4.collidepoint(x, y):
            self.screen.blit(self.background_img, self.background_rect)
            text1 = self.draw_text("SETTING", FONTNAME, 48, BLUE, WIDTH / 2, 50)
            text2 = self.draw_text("Move Up : " + pg.key.name(self.PLAYER_1_UP), FONTNAME, 24, BLUE, WIDTH / 2, 150)
            text3 = self.draw_text("BACK", FONTNAME, 48, BLUE, WIDTH * 3 / 4, HEIGHT - 100)
            text4 = self.draw_text("Move Down : " + pg.key.name(self.PLAYER_1_DOWN), FONTNAME, 24, WHITE, WIDTH / 2,
                                   200)
            text5 = self.draw_text("Move Left : " + pg.key.name(self.PLAYER_1_LEFT), FONTNAME, 24, BLUE, WIDTH / 2, 250)
            text6 = self.draw_text("Move right : " + pg.key.name(self.PLAYER_1_RIGHT), FONTNAME, 24, YELLOW, WIDTH / 2,
                                   300)
            text7 = self.draw_text("Shoot : " + pg.key.name(self.PLAYER_1_SHOOT), FONTNAME, 24, BLUE, WIDTH / 2, 350)
            text8 = self.draw_text("Skills : " + pg.key.name(self.PLAYER_1_SWISH), FONTNAME, 24, YELLOW, WIDTH / 2, 400)
            if self.mouse_click:
                self.select = "down"

        elif text5.collidepoint(x, y):
            self.screen.blit(self.background_img, self.background_rect)
            text1 = self.draw_text("SETTING", FONTNAME, 48, BLUE, WIDTH / 2, 50)
            text2 = self.draw_text("Move Up : " + pg.key.name(self.PLAYER_1_UP), FONTNAME, 24, BLUE, WIDTH / 2, 150)
            text3 = self.draw_text("BACK", FONTNAME, 48, BLUE, WIDTH * 3 / 4, HEIGHT - 100)
            text4 = self.draw_text("Move Down : " + pg.key.name(self.PLAYER_1_DOWN), FONTNAME, 24, YELLOW, WIDTH / 2,
                                   200)
            text5 = self.draw_text("Move Left : " + pg.key.name(self.PLAYER_1_LEFT), FONTNAME, 24, WHITE, WIDTH / 2, 250)
            text6 = self.draw_text("Move right : " + pg.key.name(self.PLAYER_1_RIGHT), FONTNAME, 24, YELLOW, WIDTH / 2,
                                   300)
            text7 = self.draw_text("Shoot : " + pg.key.name(self.PLAYER_1_SHOOT), FONTNAME, 24, BLUE, WIDTH / 2, 350)
            text8 = self.draw_text("Skills : " + pg.key.name(self.PLAYER_1_SWISH), FONTNAME, 24, YELLOW, WIDTH / 2, 400)
            if self.mouse_click:
                self.select = "left"

        elif text6.collidepoint(x, y):
            self.screen.blit(self.background_img, self.background_rect)
            text1 = self.draw_text("SETTING", FONTNAME, 48, BLUE, WIDTH / 2, 50)
            text2 = self.draw_text("Move Up : " + pg.key.name(self.PLAYER_1_UP), FONTNAME, 24, BLUE, WIDTH / 2, 150)
            text3 = self.draw_text("BACK", FONTNAME, 48, BLUE, WIDTH * 3 / 4, HEIGHT - 100)
            text4 = self.draw_text("Move Down : " + pg.key.name(self.PLAYER_1_DOWN), FONTNAME, 24, YELLOW, WIDTH / 2,
                                   200)
            text5 = self.draw_text("Move Left : " + pg.key.name(self.PLAYER_1_LEFT), FONTNAME, 24, BLUE, WIDTH / 2, 250)
            text6 = self.draw_text("Move right : " + pg.key.name(self.PLAYER_1_RIGHT), FONTNAME, 24, WHITE, WIDTH / 2,
                                   300)
            text7 = self.draw_text("Shoot : " + pg.key.name(self.PLAYER_1_SHOOT), FONTNAME, 24, BLUE, WIDTH / 2, 350)
            text8 = self.draw_text("Skills : " + pg.key.name(self.PLAYER_1_SWISH), FONTNAME, 24, YELLOW, WIDTH / 2, 400)
            if self.mouse_click:
                self.select = "right"

        elif text7.collidepoint(x, y):
            self.screen.blit(self.background_img, self.background_rect)
            text1 = self.draw_text("SETTING", FONTNAME, 48, BLUE, WIDTH / 2, 50)
            text2 = self.draw_text("Move Up : " + pg.key.name(self.PLAYER_1_UP), FONTNAME, 24, BLUE, WIDTH / 2, 150)
            text3 = self.draw_text("BACK", FONTNAME, 48, BLUE, WIDTH * 3 / 4, HEIGHT - 100)
            text4 = self.draw_text("Move Down : " + pg.key.name(self.PLAYER_1_DOWN), FONTNAME, 24, YELLOW, WIDTH / 2,
                                   200)
            text5 = self.draw_text("Move Left : " + pg.key.name(self.PLAYER_1_LEFT), FONTNAME, 24, BLUE, WIDTH / 2, 250)
            text6 = self.draw_text("Move right : " + pg.key.name(self.PLAYER_1_RIGHT), FONTNAME, 24, YELLOW, WIDTH / 2,
                                   300)
            text7 = self.draw_text("Shoot : " + pg.key.name(self.PLAYER_1_SHOOT), FONTNAME, 24, WHITE, WIDTH / 2, 350)
            text8 = self.draw_text("Skills : " + pg.key.name(self.PLAYER_1_SWISH), FONTNAME, 24, YELLOW, WIDTH / 2, 400)
            if self.mouse_click:
                self.select = "shoot"

        elif text8.collidepoint(x, y):
            self.screen.blit(self.background_img, self.background_rect)
            text1 = self.draw_text("SETTING", FONTNAME, 48, BLUE, WIDTH / 2, 50)
            text2 = self.draw_text("Move Up : " + pg.key.name(self.PLAYER_1_UP), FONTNAME, 24, BLUE, WIDTH / 2, 150)
            text3 = self.draw_text("BACK", FONTNAME, 48, BLUE, WIDTH * 3 / 4, HEIGHT - 100)
            text4 = self.draw_text("Move Down : " + pg.key.name(self.PLAYER_1_DOWN), FONTNAME, 24, YELLOW, WIDTH / 2,
                                   200)
            text5 = self.draw_text("Move Left : " + pg.key.name(self.PLAYER_1_LEFT), FONTNAME, 24, BLUE, WIDTH / 2, 250)
            text6 = self.draw_text("Move right : " + pg.key.name(self.PLAYER_1_RIGHT), FONTNAME, 24, YELLOW, WIDTH / 2,
                                   300)
            text7 = self.draw_text("Shoot : " + pg.key.name(self.PLAYER_1_SHOOT), FONTNAME, 24, BLUE, WIDTH / 2, 350)
            text8 = self.draw_text("Skills : " + pg.key.name(self.PLAYER_1_SWISH), FONTNAME, 24, WHITE, WIDTH / 2, 400)
            if self.mouse_click:
                self.select = "swish"

        else:
            self.screen.blit(self.background_img, self.background_rect)
            text1 = self.draw_text("SETTING", FONTNAME, 48, BLUE, WIDTH / 2, 50)
            text2 = self.draw_text("Move Up : " + pg.key.name(self.PLAYER_1_UP), FONTNAME, 24, BLUE, WIDTH / 2, 150)
            text3 = self.draw_text("BACK", FONTNAME, 48, BLUE, WIDTH * 3 / 4, HEIGHT - 100)
            text4 = self.draw_text("Move Down : " + pg.key.name(self.PLAYER_1_DOWN), FONTNAME, 24, YELLOW, WIDTH / 2,
                                   200)
            text5 = self.draw_text("Move Left : " + pg.key.name(self.PLAYER_1_LEFT), FONTNAME, 24, BLUE, WIDTH / 2, 250)
            text6 = self.draw_text("Move right : " + pg.key.name(self.PLAYER_1_RIGHT), FONTNAME, 24, YELLOW, WIDTH / 2,
                                   300)
            text7 = self.draw_text("Shoot : " + pg.key.name(self.PLAYER_1_SHOOT), FONTNAME, 24, BLUE, WIDTH / 2, 350)
            text8 = self.draw_text("Skills : " + pg.key.name(self.PLAYER_1_SWISH), FONTNAME, 24, YELLOW, WIDTH / 2, 400)
        pg.display.flip()


def player2_controller(self):
    self.waiting = True
    self.select = ""
    text1 = self.draw_text("SETTING", FONTNAME, 48, BLUE, WIDTH / 2, 50)
    text2 = self.draw_text("Move Up : " + pg.key.name(self.PLAYER_2_UP), FONTNAME, 24, BLUE, WIDTH / 2, 150)
    text3 = self.draw_text("BACK", FONTNAME, 48, BLUE, WIDTH * 3 / 4, HEIGHT - 100)
    text4 = self.draw_text("Move Down : " + pg.key.name(self.PLAYER_2_DOWN), FONTNAME, 24, YELLOW, WIDTH / 2, 200)
    text5 = self.draw_text("Move Left : " + pg.key.name(self.PLAYER_2_LEFT), FONTNAME, 24, BLUE, WIDTH / 2, 250)
    text6 = self.draw_text("Move right : " + pg.key.name(self.PLAYER_2_RIGHT), FONTNAME, 24, YELLOW, WIDTH / 2, 300)
    text7 = self.draw_text("Shoot : " + pg.key.name(self.PLAYER_2_SHOOT), FONTNAME, 24, BLUE, WIDTH / 2, 350)
    text8 = self.draw_text("Skills : " + pg.key.name(self.PLAYER_2_SWISH), FONTNAME, 24, YELLOW, WIDTH / 2, 400)
    while self.waiting:
        self.clock.tick(FPS)
        self.screen.blit(self.background_img, self.background_rect)
        self.mouse_click = False
        keystate = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.MOUSEBUTTONUP:
                self.mouse_click = True
            if event.type == pg.KEYUP:
                if event.key == pg.K_ESCAPE:
                    show_start_screen(self)
                if self.select == "up":
                    self.PLAYER_2_UP = event.key
                elif self.select == "down":
                    self.PLAYER_2_DOWN = event.key
                elif self.select == "left":
                    self.PLAYER_2_LEFT = event.key
                elif self.select == "right":
                    self.PLAYER_2_RIGHT = event.key
                elif self.select == "shoot":
                    self.PLAYER_2_SHOOT = event.key
                elif self.select == "swish":
                    self.PLAYER_2_SWISH = event.key
        x, y = pg.mouse.get_pos()
        if text3.collidepoint(x, y):
            self.screen.blit(self.background_img, self.background_rect)
            text1 = self.draw_text("SETTING", FONTNAME, 48, BLUE, WIDTH / 2, 50)
            text2 = self.draw_text("Move Up : " + pg.key.name(self.PLAYER_2_UP), FONTNAME, 24, BLUE, WIDTH / 2, 150)
            text3 = self.draw_text("BACK", FONTNAME, 48, WHITE, WIDTH * 3 / 4, HEIGHT - 100)
            text4 = self.draw_text("Move Down : " + pg.key.name(self.PLAYER_2_DOWN), FONTNAME, 24, YELLOW, WIDTH / 2,
                                   200)
            text5 = self.draw_text("Move Left : " + pg.key.name(self.PLAYER_2_LEFT), FONTNAME, 24, BLUE, WIDTH / 2, 250)
            text6 = self.draw_text("Move right : " + pg.key.name(self.PLAYER_2_RIGHT), FONTNAME, 24, YELLOW, WIDTH / 2,
                                   300)
            text7 = self.draw_text("Shoot : " + pg.key.name(self.PLAYER_2_SHOOT), FONTNAME, 24, BLUE, WIDTH / 2, 350)
            text8 = self.draw_text("Skills : " + pg.key.name(self.PLAYER_2_SWISH), FONTNAME, 24, YELLOW, WIDTH / 2, 400)
            if self.mouse_click:
                show_setting_screen(self)

        elif text2.collidepoint(x, y):
            self.screen.blit(self.background_img, self.background_rect)
            text1 = self.draw_text("SETTING", FONTNAME, 48, BLUE, WIDTH / 2, 50)
            text2 = self.draw_text("Move Up : " + pg.key.name(self.PLAYER_2_UP), FONTNAME, 24, WHITE, WIDTH / 2, 150)
            text3 = self.draw_text("BACK", FONTNAME, 48, BLUE, WIDTH * 3 / 4, HEIGHT - 100)
            text4 = self.draw_text("Move Down : " + pg.key.name(self.PLAYER_2_DOWN), FONTNAME, 24, YELLOW, WIDTH / 2,
                                   200)
            text5 = self.draw_text("Move Left : " + pg.key.name(self.PLAYER_2_LEFT), FONTNAME, 24, BLUE, WIDTH / 2, 250)
            text6 = self.draw_text("Move right : " + pg.key.name(self.PLAYER_2_RIGHT), FONTNAME, 24, YELLOW, WIDTH / 2,
                                   300)
            text7 = self.draw_text("Shoot : " + pg.key.name(self.PLAYER_2_SHOOT), FONTNAME, 24, BLUE, WIDTH / 2, 350)
            text8 = self.draw_text("Skills : " + pg.key.name(self.PLAYER_2_SWISH), FONTNAME, 24, YELLOW, WIDTH / 2, 400)
            if self.mouse_click:
                self.select = "up"

        elif text4.collidepoint(x, y):
            self.screen.blit(self.background_img, self.background_rect)
            text1 = self.draw_text("SETTING", FONTNAME, 48, BLUE, WIDTH / 2, 50)
            text2 = self.draw_text("Move Up : " + pg.key.name(self.PLAYER_2_UP), FONTNAME, 24, BLUE, WIDTH / 2, 150)
            text3 = self.draw_text("BACK", FONTNAME, 48, BLUE, WIDTH * 3 / 4, HEIGHT - 100)
            text4 = self.draw_text("Move Down : " + pg.key.name(self.PLAYER_2_DOWN), FONTNAME, 24, WHITE, WIDTH / 2,
                                   200)
            text5 = self.draw_text("Move Left : " + pg.key.name(self.PLAYER_2_LEFT), FONTNAME, 24, BLUE, WIDTH / 2, 250)
            text6 = self.draw_text("Move right : " + pg.key.name(self.PLAYER_2_RIGHT), FONTNAME, 24, YELLOW, WIDTH / 2,
                                   300)
            text7 = self.draw_text("Shoot : " + pg.key.name(self.PLAYER_2_SHOOT), FONTNAME, 24, BLUE, WIDTH / 2, 350)
            text8 = self.draw_text("Skills : " + pg.key.name(self.PLAYER_2_SWISH), FONTNAME, 24, YELLOW, WIDTH / 2, 400)
            if self.mouse_click:
                self.select = "down"

        elif text5.collidepoint(x, y):
            self.screen.blit(self.background_img, self.background_rect)
            text1 = self.draw_text("SETTING", FONTNAME, 48, BLUE, WIDTH / 2, 50)
            text2 = self.draw_text("Move Up : " + pg.key.name(self.PLAYER_2_UP), FONTNAME, 24, BLUE, WIDTH / 2, 150)
            text3 = self.draw_text("BACK", FONTNAME, 48, BLUE, WIDTH * 3 / 4, HEIGHT - 100)
            text4 = self.draw_text("Move Down : " + pg.key.name(self.PLAYER_2_DOWN), FONTNAME, 24, YELLOW, WIDTH / 2,
                                   200)
            text5 = self.draw_text("Move Left : " + pg.key.name(self.PLAYER_2_LEFT), FONTNAME, 24, WHITE, WIDTH / 2,
                                   250)
            text6 = self.draw_text("Move right : " + pg.key.name(self.PLAYER_2_RIGHT), FONTNAME, 24, YELLOW, WIDTH / 2,
                                   300)
            text7 = self.draw_text("Shoot : " + pg.key.name(self.PLAYER_2_SHOOT), FONTNAME, 24, BLUE, WIDTH / 2, 350)
            text8 = self.draw_text("Skills : " + pg.key.name(self.PLAYER_2_SWISH), FONTNAME, 24, YELLOW, WIDTH / 2, 400)
            if self.mouse_click:
                self.select = "left"

        elif text6.collidepoint(x, y):
            self.screen.blit(self.background_img, self.background_rect)
            text1 = self.draw_text("SETTING", FONTNAME, 48, BLUE, WIDTH / 2, 50)
            text2 = self.draw_text("Move Up : " + pg.key.name(self.PLAYER_2_UP), FONTNAME, 24, BLUE, WIDTH / 2, 150)
            text3 = self.draw_text("BACK", FONTNAME, 48, BLUE, WIDTH * 3 / 4, HEIGHT - 100)
            text4 = self.draw_text("Move Down : " + pg.key.name(self.PLAYER_2_DOWN), FONTNAME, 24, YELLOW, WIDTH / 2,
                                   200)
            text5 = self.draw_text("Move Left : " + pg.key.name(self.PLAYER_2_LEFT), FONTNAME, 24, BLUE, WIDTH / 2, 250)
            text6 = self.draw_text("Move right : " + pg.key.name(self.PLAYER_2_RIGHT), FONTNAME, 24, WHITE, WIDTH / 2,
                                   300)
            text7 = self.draw_text("Shoot : " + pg.key.name(self.PLAYER_2_SHOOT), FONTNAME, 24, BLUE, WIDTH / 2, 350)
            text8 = self.draw_text("Skills : " + pg.key.name(self.PLAYER_2_SWISH), FONTNAME, 24, YELLOW, WIDTH / 2, 400)
            if self.mouse_click:
                self.select = "right"

        elif text7.collidepoint(x, y):
            self.screen.blit(self.background_img, self.background_rect)
            text1 = self.draw_text("SETTING", FONTNAME, 48, BLUE, WIDTH / 2, 50)
            text2 = self.draw_text("Move Up : " + pg.key.name(self.PLAYER_2_UP), FONTNAME, 24, BLUE, WIDTH / 2, 150)
            text3 = self.draw_text("BACK", FONTNAME, 48, BLUE, WIDTH * 3 / 4, HEIGHT - 100)
            text4 = self.draw_text("Move Down : " + pg.key.name(self.PLAYER_2_DOWN), FONTNAME, 24, YELLOW, WIDTH / 2,
                                   200)
            text5 = self.draw_text("Move Left : " + pg.key.name(self.PLAYER_2_LEFT), FONTNAME, 24, BLUE, WIDTH / 2, 250)
            text6 = self.draw_text("Move right : " + pg.key.name(self.PLAYER_2_RIGHT), FONTNAME, 24, YELLOW, WIDTH / 2,
                                   300)
            text7 = self.draw_text("Shoot : " + pg.key.name(self.PLAYER_2_SHOOT), FONTNAME, 24, WHITE, WIDTH / 2, 350)
            text8 = self.draw_text("Skills : " + pg.key.name(self.PLAYER_2_SWISH), FONTNAME, 24, YELLOW, WIDTH / 2, 400)
            if self.mouse_click:
                self.select = "shoot"

        elif text8.collidepoint(x, y):
            self.screen.blit(self.background_img, self.background_rect)
            text1 = self.draw_text("SETTING", FONTNAME, 48, BLUE, WIDTH / 2, 50)
            text2 = self.draw_text("Move Up : " + pg.key.name(self.PLAYER_2_UP), FONTNAME, 24, BLUE, WIDTH / 2, 150)
            text3 = self.draw_text("BACK", FONTNAME, 48, BLUE, WIDTH * 3 / 4, HEIGHT - 100)
            text4 = self.draw_text("Move Down : " + pg.key.name(self.PLAYER_2_DOWN), FONTNAME, 24, YELLOW, WIDTH / 2,
                                   200)
            text5 = self.draw_text("Move Left : " + pg.key.name(self.PLAYER_2_LEFT), FONTNAME, 24, BLUE, WIDTH / 2, 250)
            text6 = self.draw_text("Move right : " + pg.key.name(self.PLAYER_2_RIGHT), FONTNAME, 24, YELLOW, WIDTH / 2,
                                   300)
            text7 = self.draw_text("Shoot : " + pg.key.name(self.PLAYER_2_SHOOT), FONTNAME, 24, BLUE, WIDTH / 2, 350)
            text8 = self.draw_text("Skills : " + pg.key.name(self.PLAYER_2_SWISH), FONTNAME, 24, WHITE, WIDTH / 2, 400)
            if self.mouse_click:
                self.select = "swish"

        else:
            self.screen.blit(self.background_img, self.background_rect)
            text1 = self.draw_text("SETTING", FONTNAME, 48, BLUE, WIDTH / 2, 50)
            text2 = self.draw_text("Move Up : " + pg.key.name(self.PLAYER_2_UP), FONTNAME, 24, BLUE, WIDTH / 2, 150)
            text3 = self.draw_text("BACK", FONTNAME, 48, BLUE, WIDTH * 3 / 4, HEIGHT - 100)
            text4 = self.draw_text("Move Down : " + pg.key.name(self.PLAYER_2_DOWN), FONTNAME, 24, YELLOW, WIDTH / 2,
                                   200)
            text5 = self.draw_text("Move Left : " + pg.key.name(self.PLAYER_2_LEFT), FONTNAME, 24, BLUE, WIDTH / 2, 250)
            text6 = self.draw_text("Move right : " + pg.key.name(self.PLAYER_2_RIGHT), FONTNAME, 24, YELLOW, WIDTH / 2,
                                   300)
            text7 = self.draw_text("Shoot : " + pg.key.name(self.PLAYER_2_SHOOT), FONTNAME, 24, BLUE, WIDTH / 2, 350)
            text8 = self.draw_text("Skills : " + pg.key.name(self.PLAYER_2_SWISH), FONTNAME, 24, YELLOW, WIDTH / 2, 400)
        pg.display.flip()


def draw_button(self, key, x, y, text_x, text_y):
    frame_bar = pg.Rect(x, y, 50, 50)
    self.draw_text(str(key), FONTNAME, 24, WHITE, text_x, text_y)
    pg.draw.rect(self.screen, WHITE, frame_bar, 2)