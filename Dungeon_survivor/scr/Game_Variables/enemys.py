import pygame
import random

from .Variables import GameVariables as GV
from .Variables import GameScreens as GM
from .schuss_elemente_player import Rocket
from .schuss_elemente_player import Rockets
from .Coin_spawner import Coin


class Enemy:
    def __init__(self, screen, rocket_list):
        self.screen = screen
        self.x_pos_enemy = 0
        self.y_pos_enemy = 0
        self.dx_enemy = 0
        self.dy_enemy = 0
        self.speed = 0.5
        self.welle = 1
        self.max_enemy = 100
        self.enemy_list = []
        self.Leben = 500
        self.rocket_list = rocket_list
        self.coin_list = []
        self.radius = 5
        self.score_coin = 0
        self.image = None
        self.raccon_image = pygame.image.load(
            "assets/Ninja Adventure - Asset Pack/Actor/Monster/Racoon/Faceset.png"
        ).convert()
        self.bear_image = pygame.image.load(
            "assets/Ninja Adventure - Asset Pack/Actor/Monster/Bear/Faceset.png"
        ).convert()
        self.Coin_sprite = Coin(filepath="assets/New Piskel (1).png", animation_speed=35,
                             image_rect=pygame.Rect(0, 0, 22, 22), image_count=6)

        self.Coin_sprite.load_spritesheet()
        self.frame_counter = 0



    def move_and_spawn(self, player_x_pos, player_y_pos):

        if len(self.enemy_list) < self.max_enemy * self.welle / 5:

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


            self.enemy_list.append([x, y, 0, 0])

        if self.welle >= 2:
            self.speed = 2

        player_center_x = player_x_pos + GV.SQUARE_SIZE / 2
        player_center_y = player_y_pos + GV.SQUARE_SIZE / 2
        Player_rect = pygame.Rect(player_x_pos, player_y_pos, GV.SQUARE_SIZE, GV.SQUARE_SIZE)

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


            if self.welle <= 2:
                self.image = self.raccon_image
            else:
                self.image = self.bear_image


            enemy_rect = self.image.get_rect(center=(missile[0], missile[1]))
            self.screen.blit(self.image, enemy_rect)



            missile_rect = pygame.Rect(missile[0], missile[1], 5, 5)

            if self.welle >= 2:
                self.speed = 2

            if missile_rect.colliderect(Player_rect):
                self.enemy_list.remove(missile)
                self.Leben -= 10 * self.welle / 8

                if self.Leben <= 0:
                    GM.actual = GM.GAMEOVER

    def death(self):
        rockets_list = self.rocket_list.get_rockets()

        for enemy in self.enemy_list[:]:

            enemy_rect = pygame.Rect(enemy[0], enemy[1], 20, 20)

            for missile in rockets_list[:]:

                missile_rect = pygame.Rect(missile.x_pos, missile.y_pos, GV.MISSILE_SIZE, GV.MISSILE_SIZE)

                if missile_rect.colliderect(enemy_rect):
                    self.coin_list.append([enemy[0], enemy[1]])

                    if missile in rockets_list:
                        rockets_list.remove(missile)

                    if enemy in self.enemy_list:
                        self.enemy_list.remove((enemy))


                    self.welle += 0.005
                    break

    def coin_spawn(self, player_x_pos, player_y_pos):
        for coins in self.coin_list[:]:
            self.Coin_sprite.draw(self.screen, coins[0], coins[1], self.frame_counter)


            Spieler_rect = pygame.Rect(player_x_pos, player_y_pos, GV.SQUARE_SIZE, GV.SQUARE_SIZE)
            coin_rect = self.Coin_sprite.images[0].get_rect(
                topleft=(coins[0], coins[1])
            )

            if coin_rect.colliderect(Spieler_rect):
                self.score_coin += 1
                self.coin_list.remove(coins)

        self.frame_counter += 1

        with open("Coin_speicher.txt", "w") as fp:
            fp.write(f"{self.score_coin}")



    def update_and_draw(self, player_x_pos, player_y_pos):
        self.move_and_spawn(player_x_pos, player_y_pos)
        self.death()
        self.coin_spawn(player_x_pos, player_y_pos)


    def get(self):
        return self.Leben, self.welle, self.score_coin
