# credits to :
# Bonsaiheldin | http://bonsaiheld.org
# Battle in the winter.mp3 from Johan Brodd
# "PlanetCute" art by Daniel Cook (Lostgarden.com)
# -----------------------------------------------------------------------------------
# about laserfire01 and laserfire02:
# ------
# | Info |
#  ------
#
# This SFX was created for the game prototype: Space Pioneer
#
# Triki Minut Interactive
# www.trikiminut.com
#
# Credit:
#
# K.L.Jonasson, Winnipeg, Canada.
# Triki Minut Interactive
# www.trikiminut.com
# ------------------------------------------------------------------------------------
# player image by OpenPixelProject.com

# laser beam image by rubberduck

# swish sound effect by artistic dude

# slime monster by http://bevouliin.com

# Death is just another path by Otto Halmén

# monster sound by Ogrebane

# mutant sound by Gobusto

# Biomech Dragon Splice.png by MetaShinryu, Stephen "Redshrike" Challener and Daniel Cook

from sprite import *
from enemy import *
from setting import *
from screens import *
import pygame as pg

from threading import Thread
import serial
from pykeyboard import PyKeyboard
import time


class Game:
    def __init__(self):
        # init controls for player 1
        self.PLAYER_1_UP = PLAYER_1_UP
        self.PLAYER_1_DOWN = PLAYER_1_DOWN
        self.PLAYER_1_LEFT = PLAYER_1_LEFT
        self.PLAYER_1_RIGHT = PLAYER_1_RIGHT
        self.PLAYER_1_SHOOT = PLAYER_1_SHOOT
        self.PLAYER_1_SWISH = PLAYER_1_SWISH
        # init controls for player 2
        self.PLAYER_2_UP = PLAYER_2_UP
        self.PLAYER_2_DOWN = PLAYER_2_DOWN
        self.PLAYER_2_LEFT = PLAYER_2_LEFT
        self.PLAYER_2_RIGHT = PLAYER_2_RIGHT
        self.PLAYER_2_SHOOT = PLAYER_2_SHOOT
        self.PLAYER_2_SWISH = PLAYER_2_SWISH
        pg.mixer.pre_init(22050, -16, 2, 1024)
        pg.mixer.init()
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.load_data()
        self.music_volume = 1
        self.mode = "Single Player"
        self.game_end_time = END_TIME  # each game 3 minutes
        pg.mixer.music.play(-1)

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        show_go_screen(self)

    def check_bullet_hit_mob1(self, mob_1_id):
        if mob_1_id.alive():
            hits = pg.sprite.spritecollide(
                mob_1_id, self.bullets, True, pg.sprite.collide_circle)
            for hit in hits:
                print(self.score)
                print(len(self.mobs))
                mob_1_id.health -= 10
                if mob_1_id.health <= 0:
                    self.score += 100
                    mob_1_id.health = 0
                    self.mob1_die_snd.play()
                    mob_1_id.kill()
                    mob_1_id = Mob(self)
                    self.all_sprites.add(mob_1_id)
                    self.mobs.add(mob_1_id)

    def check_sword_hit_mob1(self, mob_1_id):
        if mob_1_id.alive():
            hits = pg.sprite.spritecollide(
                mob_1_id, self.swords, False, pg.sprite.collide_circle)
            for hit in hits:
                mob_1_id.speedy = random.randrange(5, 8)
                mob_1_id.speedx = random.randrange(-6, 6)
                mob_1_id.health -= 1
                if mob_1_id.health <= 0:
                    self.score += 100
                    mob_1_id.health = 0
                    self.mob1_die_snd.play()
                    mob_1_id.kill()
                    mob_1_id = Mob(self)
                    self.all_sprites.add(mob_1_id)
                    self.mobs.add(mob_1_id)

    def check_player_hit_mob1(self, player, mob_1_id):
        if mob_1_id.alive():
            if pg.sprite.collide_circle(player, mob_1_id):
                player.shield -= 10
                mob_1_id.kill()
                self.mob1_die_snd.play()
                if not mob_1_id.alive():
                    mob_1_id = Mob(self)
                    self.all_sprites.add(mob_1_id)
                    self.mobs.add(mob_1_id)
                if player.shield <= 0:
                    player.shield = 0
                    player.kill()

    def check_player1_hit_mob1(self):
        for mobby in self.mobs:
            self.check_player_hit_mob1(self.player1, mobby)

    def check_player2_hit_mob1(self):
        for mobby in self.mobs:
            self.check_player_hit_mob1(self.player2, mobby)

    def check_player_hit_powerup(self, player):
        hits = pg.sprite.spritecollide(player, self.powerups, True)
        for hit in hits:
            self.powerup_snd[hit.powerup_type].play()
            if hit.powerup_type == "cure":
                player.shield += 30
                if player.shield > 100:
                    player.shield = 100
            if hit.powerup_type == "double speed":
                player.start_powerup_counter = True
                self.powerup_lasting_time = pg.time.get_ticks()
                player.speedup = 3.5
            if hit.powerup_type == "double attack speed":
                player.start_powerup_counter = True
                self.powerup_lasting_time = pg.time.get_ticks()
                player.shoot_rate = 75
            if hit.powerup_type == "full cure":
                player.shield = 100
            if hit.powerup_type == "shooting power":
                player.start_powerup_counter = True
                self.powerup_lasting_time = pg.time.get_ticks()
                player.power += 1
                if player.power >= 2:
                    player.power = 2

    def update(self):
        self.all_sprites.update()

        # spawn power-ups
        if pg.time.get_ticks() - self.powerup_time > random.randrange(2500, 10000):
            self.power_up = Powerup(self)
            self.all_sprites.add(self.power_up)
            self.powerups.add(self.power_up)
            self.powerup_time = pg.time.get_ticks()

        # check if the player wins
        if pg.time.get_ticks() - self.game_timer > self.game_end_time and (
                self.player1.alive() or self.player2.alive()):
            show_win_screen(self)

        # check if the boss is out
        if pg.time.get_ticks() - self.boss_timer > BOSS_1_SPAWN_TIME and self.boss1_live:
            if not self.bosses:
                self.boss1 = Boss1(self)
                self.all_sprites.add(self.boss1)
                self.bosses.add(self.boss1)
            # check if the player bullet hits the boss 1
            if self.boss1.alive():
                hits = pg.sprite.spritecollide(
                    self.boss1, self.bullets, True, pg.sprite.collide_circle)
                for hit in hits:
                    if self.boss1.shield > 0:
                        self.boss1_dmg_snd.play()
                        self.boss1.shield -= 50
                        if self.boss1.shield <= 0:
                            self.boss1.shield = 0
                            self.boss1.kill()
                            self.boss1_die_snd.play()
                            self.score += 1000
                            self.boss1_live = False
                            self.boss2_live = True
                hits = pg.sprite.spritecollide(
                    self.boss1, self.swords, False, pg.sprite.collide_circle)
                for hit in hits:
                    if self.boss1.shield > 0:
                        self.boss1_dmg_snd.play()
                        self.boss1.shield -= 5
                        if self.boss1.shield <= 0:
                            self.boss1.shield = 0
                            self.boss1.kill()
                            self.boss1_die_snd.play()
                            self.score += 1000
                            self.boss1_live = False
                            self.boss2_live = True

        elif pg.time.get_ticks() - self.boss_timer > BOSS_2_SPAWN_TIME and self.boss2_live:
            if not self.bosses:
                self.boss2 = Boss2(self)
                self.all_sprites.add(self.boss2)
                self.bosses.add(self.boss2)
            if self.boss2.alive():
                hits = pg.sprite.spritecollide(
                    self.boss2, self.bullets, True, pg.sprite.collide_circle)
                for hit in hits:
                    if self.boss2.shield > 0:
                        self.boss1_dmg_snd.play()
                        self.boss2.shield -= 100
                        if self.boss2.shield <= 0:
                            self.boss2.shield = 0
                            self.boss2.kill()
                            self.boss1_die_snd.play()
                            self.score += 10000
                            self.boss2_live = False
                hits = pg.sprite.spritecollide(
                    self.boss2, self.swords, False, pg.sprite.collide_circle)
                for hit in hits:
                    if self.boss2.shield > 0:
                        self.boss1_dmg_snd.play()
                        self.boss2.shield -= 5
                        if self.boss2.shield <= 0:
                            self.boss2.shield = 0
                            self.boss2.kill()
                            self.boss1_die_snd.play()
                            self.score += 10000
                            self.boss2_live = False

        # check if a bullet hits a mob
        for mobbies in self.mobs:
            self.check_bullet_hit_mob1(mobbies)
            self.check_sword_hit_mob1(mobbies)

        if self.player1.alive():
            # check if player hits boss 2
            hits = pg.sprite.spritecollide(self.player1, self.bosses, False)
            for hit in hits:
                self.player1.shield -= 1
                if self.player1.shield <= 0:
                    self.player1.shield = 0
                    self.player1.kill()
            # check if powerup time ends
            if pg.time.get_ticks() - self.powerup_lasting_time > POWERUP_PERIOD and self.player1.start_powerup_counter:
                self.player1.speedup = 1
                self.player1.shoot_rate = 150
                self.player1.power -= 1
                if self.player1.power <= 1:
                    self.player1.power = 1
            self.check_player_hit_powerup(self.player1)
            # check if the player hits a mob
            self.check_player1_hit_mob1()
            # check if the enemy bullet hits the player
            hits = pg.sprite.spritecollide(
                self.player1, self.enemybullets, True, pg.sprite.collide_circle)
            for hit in hits:
                self.player1.shield -= 20
                if self.player1.shield <= 0:
                    self.player1.shield = 0
                    self.player1.kill()
        if self.mode == "Multiplayer":
            if self.player2.alive():
                hits = pg.sprite.spritecollide(
                    self.player2, self.bosses, False)
                for hit in hits:
                    self.player2.shield -= 1
                    if self.player2.shield <= 0:
                        self.player2.shield = 0
                        self.player2.kill()
                if pg.time.get_ticks() - self.powerup_lasting_time > POWERUP_PERIOD and self.player2.start_powerup_counter:
                    self.player2.speedup = 1
                    self.player2.shoot_rate = 150
                    self.player2.power -= 1
                    if self.player2.power <= 1:
                        self.player2.power = 1
                self.check_player_hit_powerup(self.player2)
                self.check_player2_hit_mob1()
                hits = pg.sprite.spritecollide(
                    self.player2, self.enemybullets, True, pg.sprite.collide_circle)
                for hit in hits:
                    self.player2.shield -= 20
                    if self.player2.shield <= 0:
                        self.player2.shield = 0
                        self.player2.kill()

        # check if both players died
        if self.mode == "Single Player":
            if not self.player1.alive():
                self.lose_snd.play(-1, fade_ms=4000)
                pg.mixer.music.fadeout(1000)
                self.playing = False
        else:
            if not self.player1.alive() and not self.player2.alive():
                self.lose_snd.play(-1, fade_ms=4000)
                pg.mixer.music.fadeout(1000)
                self.playing = False

    def quit(self):
        pg.quit()
        sys.exit()

    def draw_background(self):
        self.screen.blit(self.background_img, (0, 0))
        self.screen.blit(self.background_star, (0, self.y2))
        self.screen.blit(self.background_star, (0, self.y1))
        self.y1 += self.scroll_speed
        self.y2 += self.scroll_speed
        if self.y1 >= HEIGHT:
            self.y1 = -HEIGHT
        if self.y2 >= HEIGHT:
            self.y2 = -HEIGHT

    def draw(self):
        self.draw_background()
        if self.mode == "Single Player":
            self.draw_health_bar(self.player1.shield * 0.01, y=38)
            self.draw_ulti_bar(pg.time.get_ticks() - self.player1.last_swish)
        elif self.mode == "Multiplayer":
            self.draw_health_bar(self.player1.shield * 0.01)
            self.draw_health_bar(self.player2.shield * 0.01, 20, 50)
            self.draw_ulti_bar(pg.time.get_ticks() -
                               self.player1.last_swish, -30)
            self.draw_ulti_bar(pg.time.get_ticks() -
                               self.player2.last_swish, 10)
        self.all_sprites.draw(self.screen)
        self.draw_text("score : " + str(self.score),
                       FONTNAME, 24, WHITE, WIDTH * 3 / 4, 30)
        for mobby in self.mobs:
            draw_enemy_health_bar(mobby, mobby.health /
                                  50, mobby.left_bar, mobby.bottom_bar)
        if self.bosses:
            if pg.time.get_ticks() - self.boss_timer > BOSS_1_SPAWN_TIME and self.boss1_live:
                draw_enemy_health_bar(self.boss1, self.boss1.shield /
                                      2000, self.boss1.left_bar, self.boss1.bottom_bar, BLUE)
            if pg.time.get_ticks() - self.boss_timer > BOSS_2_SPAWN_TIME and self.boss2_live:
                draw_enemy_health_bar(self.boss2, self.boss2.shield / 4000, self.boss2.left_bar, self.boss2.bottom_bar,
                                      BLUE)
        self.draw_progress_bar(pg.time.get_ticks() -
                               self.game_timer, self.game_end_time)
        pg.display.flip()

    def new(self):
        # initialize everything here
        self.game_timer = pg.time.get_ticks()
        self.all_sprites = pg.sprite.Group()
        self.players = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.powerups = pg.sprite.Group()
        self.swords = pg.sprite.Group()
        self.bosses = pg.sprite.Group()
        self.enemybullets = pg.sprite.Group()
        self.boss1_live = True
        self.boss2_live = False
        self.no_boss = True
        self.mob1_1 = Mob(self)
        self.all_sprites.add(self.mob1_1)
        self.mobs.add(self.mob1_1)
        self.mob1_2 = Mob(self)
        self.all_sprites.add(self.mob1_2)
        self.mobs.add(self.mob1_2)
        self.mob1_3 = Mob(self)
        self.all_sprites.add(self.mob1_3)
        self.mobs.add(self.mob1_3)
        self.mob1_4 = Mob(self)
        self.all_sprites.add(self.mob1_4)
        self.mobs.add(self.mob1_4)
        self.mob1_5 = Mob(self)
        self.all_sprites.add(self.mob1_5)
        self.mobs.add(self.mob1_5)
        self.mob1_6 = Mob(self)
        self.all_sprites.add(self.mob1_6)
        self.mobs.add(self.mob1_6)
        self.mob1_7 = Mob(self)
        self.all_sprites.add(self.mob1_7)
        self.mobs.add(self.mob1_7)
        self.mob1_8 = Mob(self)
        self.all_sprites.add(self.mob1_8)
        self.mobs.add(self.mob1_8)
        self.score = 0
        self.powerup_type = []
        self.powerup_lasting_time = 0
        if self.mode == "Single Player":
            self.player1 = Player(self, PLAYER_INIT_X, PLAYER_INIT_Y, PLAYER_1_LEFT, PLAYER_1_RIGHT,
                                  PLAYER_1_UP, PLAYER_1_DOWN, PLAYER_1_SHOOT, PLAYER_1_SWISH, self.player1_stand,
                                  self.player1_right, self.player1_left, "player1")
            self.all_sprites.add(self.player1)
            self.players.add(self.player1)
        elif self.mode == "Multiplayer":
            self.player1 = Player(self, PLAYER_INIT_X - 100, PLAYER_INIT_Y, PLAYER_1_LEFT, PLAYER_1_RIGHT,
                                  PLAYER_1_UP, PLAYER_1_DOWN, PLAYER_1_SHOOT, PLAYER_1_SWISH, self.player1_stand,
                                  self.player1_right, self.player1_left, "player1")
            self.all_sprites.add(self.player1)
            self.players.add(self.player1)
            self.player2 = Player(self, PLAYER_INIT_X + 100, PLAYER_INIT_Y, PLAYER_2_LEFT, PLAYER_2_RIGHT,
                                  PLAYER_2_UP, PLAYER_2_DOWN, PLAYER_2_SHOOT, PLAYER_2_SWISH, self.player2_stand,
                                  self.player2_right, self.player2_left, "player2")
            self.all_sprites.add(self.player2)
            self.players.add(self.player2)
        self.y1 = 0
        self.y2 = -HEIGHT
        self.scroll_speed = 3
        self.boss_timer = pg.time.get_ticks()
        self.powerup_time = pg.time.get_ticks()
        self.run()

    def load_data(self):
        if getattr(sys, 'frozen', False):
            # frozen
            self.dir = path.dirname(sys.executable).replace("\\", "/")
        else:
            # unfrozen
            self.dir = path.dirname(path.realpath(__file__)).replace("\\", "/")
        self.img_dir = path.join(self.dir, "img")
        self.snd_dir = path.join(self.dir, "snd")
        self.background_img = pg.image.load(
            path.join(self.img_dir, "n1-top@3x.png").replace("\\", "/")).convert()
        self.background_rect = self.background_img.get_rect()
        self.background_star = pg.image.load(
            path.join(self.img_dir, "spr_stars01.png").replace("\\", "/")).convert()
        self.background_star.set_colorkey(BLACK)
        self.mob_1 = pg.image.load(
            path.join(self.img_dir, "character boy.png").replace("\\", "/")).convert()
        self.player1_stand = pg.image.load(path.join(self.img_dir,
                                                     "spr_m_traveler_duck_anim.gif").replace("\\", "/")).convert()
        self.player1_stand = pg.transform.scale(self.player1_stand, (70, 70))
        self.player1_stand.set_colorkey(BLACK)
        self.player1_right = pg.image.load(path.join(self.img_dir,
                                                     "spr_m_traveler_run_anim_1.png").replace("\\",
                                                                                              "/")).convert_alpha()
        self.player1_right = pg.transform.scale(self.player1_right, (70, 70))
        self.player1_right.set_colorkey(BLACK)
        self.player1_left = pg.transform.flip(self.player1_right, True, False)
        self.player1_left.set_colorkey(BLACK)

        self.player2_stand = pg.image.load(path.join(self.img_dir,
                                                     "spr_frog_g_jump_2up.gif").replace("\\", "/")).convert_alpha()
        self.player2_stand = pg.transform.scale(self.player2_stand, (40, 40))
        self.player2_stand.set_colorkey(BLACK)
        self.player2_right = pg.image.load(path.join(self.img_dir,
                                                     "spr_frog_g_jump_3down.gif").replace("\\",
                                                                                          "/")).convert_alpha()
        self.player2_right = pg.transform.scale(self.player2_right, (40, 40))
        self.player2_right.set_colorkey(BLACK)
        self.player2_left = pg.transform.flip(self.player2_right, True, False)
        self.player2_left.set_colorkey(BLACK)

        self.laser_light = pg.image.load(path.join(self.img_dir,
                                                   "green_effect_08.png").replace("\\", "/")).convert_alpha()
        self.laser_light.set_colorkey(BLACK)

        self.boss1_attack = pg.image.load(path.join(self.img_dir,
                                                    "magic_effect_2_05.png").replace("\\", "/")).convert_alpha()
        self.boss1_attack.set_colorkey(BLACK)

        self.sword_img = pg.image.load(path.join(self.img_dir,
                                                 "Weapons_0010_Capa-8 (2).png").replace("\\", "/")).convert()
        self.sword_img = pg.transform.scale(self.sword_img, (40, 70))
        self.sword_img.set_colorkey(BLACK)
        self.enemy_img = pg.image.load(path.join(self.img_dir,
                                                 "slime-monster.png").replace("\\", "/")).convert_alpha()
        self.enemy_img = pg.transform.scale(self.enemy_img, (100, 100))
        self.enemy_img.set_colorkey(BLACK)
        self.boss2_img = pg.image.load(path.join(self.img_dir,
                                                 "Biomech Dragon Splice.png").replace("\\", "/")).convert_alpha()
        self.boss2_right_img = pg.transform.rotate(self.boss2_img, -30)
        self.boss2_left_img = pg.transform.rotate(self.boss2_img, 30)
        self.powerup_img = {}
        self.powerup_img["cure"] = pg.image.load(path.join(self.img_dir,
                                                           "pill_red.png").replace("\\", "/")).convert_alpha()
        self.powerup_img["full cure"] = pg.transform.scale(
            self.powerup_img["cure"], (40, 40))
        self.powerup_img["double speed"] = pg.image.load(path.join(self.img_dir,
                                                                   "bolt_gold.png").replace("\\", "/")).convert_alpha()
        self.powerup_img["double attack speed"] = pg.transform.rotate(pg.image.load(path.join(self.img_dir,
                                                                                              "Weapons_0010_Capa-8 (3).png").replace(
            "\\", "/")).convert_alpha(), 180)
        self.powerup_img["shooting power"] = pg.image.load(path.join(self.img_dir,
                                                                     "powerupGreen_bolt.png").replace("\\",
                                                                                                      "/")).convert_alpha()

        self.main_icon = pg.image.load(path.join(
            self.img_dir, "opp_promo_traveler.png").replace("\\", "/")).convert_alpha()
        self.main_icon = pg.transform.scale(self.main_icon, (100, 130))
        self.main_icon.set_colorkey(BLACK)

        self.progress_icon = pg.image.load(path.join(
            self.img_dir, "spr_toucan_fly_anim.gif").replace("\\", "/")).convert_alpha()
        self.progress_icon.set_colorkey(BLACK)

        self.ulti_icon = pg.image.load(path.join(
            self.img_dir, "powerupYellow_bolt.png").replace("\\", "/")).convert_alpha()
        self.ulti_icon_transparent = pg.image.load(path.join(
            self.img_dir, "powerupBlue_bolt.png").replace("\\", "/")).convert_alpha()

        self.boss1_icon = pg.transform.scale(self.enemy_img, (32, 32))
        self.boss1_icon.set_colorkey(BLACK)
        self.boss2_icon = pg.transform.scale(self.boss2_img, (32, 44))
        self.boss2_icon.set_colorkey(BLACK)

        # load background music and sound effects
        pg.mixer.music.load(
            path.join(self.snd_dir, "Battle in the winter.mp3").replace("\\", "/"))
        self.laser_snd = pg.mixer.Sound(
            path.join(self.snd_dir, "laserfire01.ogg").replace("\\", "/"))
        self.swish_snd = pg.mixer.Sound(
            path.join(self.snd_dir, "swish_2.wav").replace("\\", "/"))
        self.boss1_snd = pg.mixer.Sound(
            path.join(self.snd_dir, "foom_0.wav").replace("\\", "/"))
        self.lose_snd = pg.mixer.Sound(
            path.join(self.snd_dir, "Death Is Just Another Path.ogg").replace("\\", "/"))
        self.boss1_die_snd = pg.mixer.Sound(
            path.join(self.snd_dir, "bossdie.wav").replace("\\", "/"))
        self.boss1_dmg_snd = pg.mixer.Sound(
            path.join(self.snd_dir, "bosshurt.wav").replace("\\", "/"))
        self.mob1_die_snd = pg.mixer.Sound(
            path.join(self.snd_dir, "mutantdie.wav").replace("\\", "/"))
        self.powerup_snd = {}
        self.powerup_snd['cure'] = pg.mixer.Sound(
            path.join(self.snd_dir, "pow1.wav").replace("\\", "/"))
        self.powerup_snd['double speed'] = pg.mixer.Sound(
            path.join(self.snd_dir, "pow2.wav").replace("\\", "/"))
        self.powerup_snd['double attack speed'] = pg.mixer.Sound(
            path.join(self.snd_dir, "pow3.wav").replace("\\", "/"))
        self.powerup_snd['full cure'] = pg.mixer.Sound(
            path.join(self.snd_dir, "pow1.wav").replace("\\", "/"))
        self.powerup_snd['shooting power'] = pg.mixer.Sound(
            path.join(self.snd_dir, "pow2.wav").replace("\\", "/"))

        # load files
        try:
            with open(HS_FILE, "r") as f:
                self.highscore = int(f.read())
        except:
            self.highscore = 0

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        keystate = pg.key.get_pressed()
        if keystate[pg.K_ESCAPE]:
            pg.quit()
            sys.exit()

    def draw_text(self, text, font_type, size, color, x, y):
        font = pg.font.Font(font_type, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (int(x), int(y))
        self.screen.blit(text_surface, text_rect)
        return text_rect

    def draw_health_bar(self, health_pct, x=20, y=30):
        current_health_length = health_pct * BAR_LENGTH
        frame_bar = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
        health_bar = pg.Rect(int(x), int(y), current_health_length, BAR_HEIGHT)
        pg.draw.rect(self.screen, GREEN, health_bar)
        pg.draw.rect(self.screen, WHITE, frame_bar, 2)

    def draw_volume_bar(self, volume):
        current_volume_position = volume * 200
        frame_bar = pg.Rect(WIDTH / 2, HEIGHT / 2 - 50, 200, 20)
        frame_bar.center = (WIDTH / 2, HEIGHT / 2 - 50)
        volume_position = pg.Rect(
            WIDTH / 2 + current_volume_position, HEIGHT / 2 - 50, 15, BAR_HEIGHT + 15)
        volume_position.center = (
            frame_bar.left + current_volume_position, HEIGHT / 2 - 50)
        pg.draw.rect(self.screen, WHITE, frame_bar, 2)
        pg.draw.rect(self.screen, RED, volume_position)

    def draw_progress_bar(self, game_time, stage_time):
        frame_bar = pg.Rect(WIDTH / 2, 20, 400, 15)
        frame_bar.center = (WIDTH / 2, 20)
        current_progress = game_time / stage_time * 400 + frame_bar.left
        progress_icon = self.progress_icon
        boss1_icon = self.boss1_icon
        boss1_rect = boss1_icon.get_rect()
        boss1_rect.center = (BOSS_1_SPAWN_TIME /
                             stage_time * 400 + frame_bar.left, 15)
        boss2_icon = self.boss2_icon
        boss2_rect = boss2_icon.get_rect()
        boss2_rect.center = (BOSS_2_SPAWN_TIME /
                             stage_time * 400 + frame_bar.left, 15)
        icon_rect = progress_icon.get_rect()
        icon_rect.center = (current_progress, 25)
        done_bar = pg.Rect(
            WIDTH / 2, 12, icon_rect.centerx - frame_bar.left, 15)
        done_bar.left = frame_bar.left
        pg.draw.rect(self.screen, GREEN, done_bar)
        pg.draw.rect(self.screen, WHITE, frame_bar, 2)
        self.screen.blit(boss1_icon, boss1_rect)
        self.screen.blit(boss2_icon, boss2_rect)
        self.screen.blit(progress_icon, icon_rect)

    # cd time = pg.time.get_ticks - self.last_swish; cd time / 5000 = current progress 5000 = 100px
    def draw_ulti_bar(self, cd_time, height=0):
        frame_bar = pg.Rect(WIDTH - 75, HEIGHT - 30 + height, 100, 10)
        frame_bar.center = (WIDTH - 75, HEIGHT - 30 + height)
        current_cd = cd_time / 5000 * 100
        if current_cd > 100:
            current_cd = 100
        done_bar = pg.Rect(WIDTH - 75, HEIGHT - 30 + height, current_cd, 10)
        done_bar.left = frame_bar.left
        done_bar.centery = HEIGHT - 30 + height
        ulti_icon = self.ulti_icon
        ulti_icon_rect = ulti_icon.get_rect()
        ulti_icon_rect.center = (WIDTH - 125, HEIGHT - 30 + height)
        ulti_icon_transparent = self.ulti_icon_transparent
        ulti_icon_transparent_rect = ulti_icon_transparent.get_rect()
        ulti_icon_transparent_rect.center = (WIDTH - 125, HEIGHT - 30 + height)
        pg.draw.rect(self.screen, BLUE, done_bar)
        pg.draw.rect(self.screen, WHITE, frame_bar, 2)
        if cd_time < 5000:
            self.screen.blit(ulti_icon_transparent, ulti_icon_transparent_rect)
        else:
            self.screen.blit(ulti_icon, ulti_icon_rect)

    # copied from website
    def blit_alpha(self, target, source, center, opacity):
        x = center[0]
        y = center[1]
        temp = pg.Surface((source.get_width(), source.get_height()))
        temp.blit(target, (-x, -y))
        temp.blit(source, (0, 0))
        temp.set_alpha(opacity)
        temp_rect = temp.get_rect()
        temp_rect.center = center
        target.blit(temp, temp_rect)


g = Game()
while g.running:
    show_start_screen(g)
    g.new()
    show_go_screen(g)
