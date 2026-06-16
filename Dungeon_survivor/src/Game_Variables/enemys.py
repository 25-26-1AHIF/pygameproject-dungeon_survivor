import pygame
import random
import json

from .Variables import GameVariables as GV, GameScreens
from .Variables import GameScreens as GM
from .schuss_elemente_player import Rocket
from .schuss_elemente_player import Rockets
from .Coin_spawner import Coin
from .enemy_sprite import Sprite
from .player import Player as pl


class Enemy:
    def __init__(self, screen, rocket_list, coin_score):
        self.screen = screen
        self.x_pos_enemy = 0
        self.y_pos_enemy = 0
        self.welle_timer = pygame.time.get_ticks()
        self.welle_interval = 15000  # 15 Sekunden
        self.dx_enemy = 0
        self.dy_enemy = 0
        self.speed = 0.5
        self.welle = 1
        self.max_enemy = 100
        self.enemy_list = []
        self.Leben = 200
        self.rocket_list = rocket_list
        self.coin_list = []
        self.radius = 5
        self.score_coin = coin_score
        self.image = None
        self.coin_gesammelt = 0
        self.player_death = 0


        #self.raccon_image = pygame.image.load(
            #"assets/Ninja Adventure - Asset Pack/Actor/Monster/Racoon/Faceset.png"
        #).convert()

        #self.bear_image = pygame.image.load(
            #"assets/Ninja Adventure - Asset Pack/Actor/Monster/Bear/Faceset.png"
        #).convert()

        self.Coin_sprite = Coin(
            filepath="assets/New Piskel (2).png",
            animation_speed=5,
            image_rect=pygame.Rect(0, 0, 20, 20),
            image_count=8)


        self.sprite = Sprite(
            filepath="assets/Ninja Adventure - Asset Pack/Actor/Monster/Racoon/SpriteSheet.png",
            animation_speed=10,
            image_rect=pygame.Rect(0, 0, 16, 16),
            image_count=4)

        self.Reptile = Sprite(
            filepath="assets/Ninja Adventure - Asset Pack/Actor/Monster/Reptile/Reptile.png",
            animation_speed=10,
            image_rect=pygame.Rect(0, 0, 16, 16),
            image_count=4
        )
        self.Bat = Sprite(
            filepath="assets/Ninja Adventure - Asset Pack/Actor/Monster/YellowsBat/SpriteSheet.png",
            animation_speed=10,
            image_rect=pygame.Rect(0, 0, 16, 16),
            image_count=4
        )
        self.Beast = Sprite(
            filepath="assets/Ninja Adventure - Asset Pack/Actor/Monster/Beast2/Beast2.png",
            animation_speed=10,
            image_rect=pygame.Rect(0, 0, 16, 16),
            image_count=4
        )
        self.Axolot = Sprite(
            filepath="assets/Ninja Adventure - Asset Pack/Actor/Monster/Axolot/SpriteSheet.png",
            animation_speed=10,
            image_rect=pygame.Rect(0, 0, 16, 16),
            image_count=4
        )
        self.cyclope = Sprite(
            filepath="assets/Ninja Adventure - Asset Pack/Actor/Monster/Cyclope/SpriteSheet.png",
            animation_speed=10,
            image_rect=pygame.Rect(0, 0, 16, 16),
            image_count=4
        )

        self.sprite.load_spritesheet()
        self.Reptile.load_spritesheet()
        self.cyclope.load_spritesheet()
        self.Axolot.load_spritesheet()
        self.Beast.load_spritesheet()
        self.Bat.load_spritesheet()
        self.Coin_sprite.load_spritesheet()

        self.frame_counter = 0

    def get_sprite_for_wave(self):
        if self.welle >= 11:
            return self.cyclope
        elif self.welle >= 9:
            return self.Axolot
        elif self.welle >= 7:
            return self.Beast
        elif self.welle >= 5:
            return self.Bat
        elif self.welle >= 3:
            return self.Reptile
        else:
            return self.sprite

    def move_and_spawn(self, player_x_pos, player_y_pos):

        if len(self.enemy_list) < self.max_enemy + (self.max_enemy * self.welle/10):

            side = random.choice(["left", "right", "top", "bottom"])

            if side == "left":
                x = 0
                y = random.randint(0, GV.SCREEN_HEIGHT)

            elif side == "right":
                x = GV.SCREEN_WIDTH
                y = random.randint(0, GV.SCREEN_HEIGHT)

            elif side == "top":
                x = random.randint(0, GV.SCREEN_WIDTH)
                y = 0

            else:
                x = random.randint(0, GV.SCREEN_WIDTH)
                y = GV.SCREEN_HEIGHT

            sprite = self.get_sprite_for_wave()
            self.enemy_list.append([x, y, 0, 0, sprite])


        player_center_x = player_x_pos + GV.SQUARE_SIZE / 2
        player_center_y = player_y_pos + GV.SQUARE_SIZE / 2

        Player_rect = pygame.Rect(
            player_x_pos,
            player_y_pos,
            GV.SQUARE_SIZE,
            GV.SQUARE_SIZE
        )

        #KI-Anfang
        #KI Chat GPT
        #Antwort: mache[:] für einen sicheren Durchlauf.[:] erstellt eine kopie der liste
        for missile in self.enemy_list[:]:
        #KI-Ende

            dx = player_center_x - missile[0]
            dy = player_center_y - missile[1]

            length = (dx * dx + dy * dy) ** 0.5

            if length == 0:
                length = 0.0001

            dx /= length
            dy /= length

            missile[2] = dx * self.speed
            missile[3] = dy * self.speed

            missile[0] += missile[2]
            missile[1] += missile[3]

            missile[4].draw(
                self.screen,
                missile[0],
                missile[1],
                self.frame_counter
            )

            #enemy_rect = self.image.get_rect(center=(missile[0], missile[1]))
            #self.screen.blit(self.image, enemy_rect)

            missile_rect = pygame.Rect(
                missile[0],
                missile[1],
                64,
                64
            )

            if missile_rect.colliderect(Player_rect):
                self.enemy_list.remove(missile)
                self.Leben -= int(10 * self.welle / 15)


            if self.Leben <= 0:
                GameScreens.actual = GameScreens.GAMEOVER
                self.player_death = 1

    def death(self, player_x_pos, player_y_pos):
        with open("speichern_spielstand.json", "r") as fp:
            inhalt = json.load(fp)
        rockets_list = self.rocket_list.get_rockets()

        for enemy in self.enemy_list[:]:

            enemy_rect = pygame.Rect(
                enemy[0],
                enemy[1],
                64,
                64
            )

            for missile in rockets_list[:]:

                missile_rect = pygame.Rect(
                    missile.x_pos,
                    missile.y_pos,
                    GV.MISSILE_SIZE,
                    GV.MISSILE_SIZE
                )

                if missile_rect.colliderect(enemy_rect):

                    self.coin_list.append([enemy[0], enemy[1], pygame.time.get_ticks()])

                    remove_missile = True

                    if GV.actual_WAEPON == 2:
                        if inhalt[2]['Bogen']['upgrade'] == 3:
                            remove_missile = False

                    elif GV.actual_WAEPON == 3:
                        if inhalt[3]['Armbrust']['upgrade'] == 6:
                            remove_missile = False

                    if remove_missile:
                        if missile in rockets_list:
                            rockets_list.remove(missile)

                    if enemy in self.enemy_list:
                        self.enemy_list.remove(enemy)




    def coin_spawn(self, player_x_pos, player_y_pos):
        zeit = pygame.time.get_ticks()

        for coins in self.coin_list[:]:

            if zeit - coins[2] > 15000:
                self.coin_list.remove(coins)


            self.Coin_sprite.draw(
                self.screen,
                coins[0],
                coins[1],
                self.frame_counter
            )

            Spieler_rect = pygame.Rect(
                player_x_pos,
                player_y_pos,
                GV.SQUARE_SIZE,
                GV.SQUARE_SIZE
            )

            coin_rect = self.Coin_sprite.images[0].get_rect(
                topleft=(coins[0], coins[1])
            )

            if coin_rect.colliderect(Spieler_rect):

                self.coin_gesammelt += 1
                self.coin_list.remove(coins)
                self.score_coin += 1

        with open("Coin_speicher.txt", "w") as fp:
            fp.write(f"{self.score_coin}")

    def update_and_draw(self, player_x_pos, player_y_pos):

        self.move_and_spawn(player_x_pos, player_y_pos)

        self.death(player_x_pos, player_y_pos)

        self.coin_spawn(player_x_pos, player_y_pos)

        self.update_welle_timer()
        self.frame_counter += 1

    def get_informationen(self):
        return (
            self.Leben,
            self.welle,
            self.score_coin,
            self.coin_gesammelt,
            self.player_death

        )

    def update_welle_timer(self):
        current_time = pygame.time.get_ticks()

        if current_time - self.welle_timer >= self.welle_interval:
            self.welle += 1
            self.welle_timer = current_time

    def get_coins(self):
        return self.coin_gesammelt

    def get_enemy_list(self):
        return self.enemy_list

    def get_coin_list(self):
        return self.coin_list

    def get_welle(self):
        return self.welle
