import pygame
import random

from .Variables import GameVariables as GV
from .schuss_elemente_player import Rocket

class Player:
    def __init__(self, screen, rockets):
        self.x_pos_player = GV.SCREEN_WIDTH/2-(GV.SQUARE_SIZE/2)
        self.y_pos_player = GV.SCREEN_HEIGHT/2-(GV.SQUARE_SIZE/2)
        self.screen = screen
        self.rockets = rockets

    def draw(self):


        pygame.draw.rect(surface=self.screen, rect = (self.x_pos_player, self.y_pos_player, GV.SQUARE_SIZE, GV.SQUARE_SIZE), color="red", width=0)


    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_a]:
            if self.x_pos_player <= 0:
                pass
            else:
                self.x_pos_player -= 5

        if pressed_keys[pygame.K_d]:
            if self.x_pos_player >= GV.SCREEN_WIDTH - GV.SQUARE_SIZE:
                pass
            else:
                self.x_pos_player += 5

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_w]:
            if self.y_pos_player <= 0:
                pass
            else:
                self.y_pos_player -= 5

        if pressed_keys[pygame.K_s]:
            if self.y_pos_player >= GV.SCREEN_HEIGHT - GV.SQUARE_SIZE:
                pass
            else:
                self.y_pos_player += 5

        pygame.draw.rect(surface=self.screen,
                         rect=(self.x_pos_player, self.y_pos_player, GV.SQUARE_SIZE, GV.SQUARE_SIZE), color="red",
                         width=0)

    def shoot(self):
        pressed_key = pygame.mouse.get_pressed()
        if pressed_key[0]:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                player_center_x = self.x_pos_player + GV.SQUARE_SIZE / 2
                player_center_y = self.y_pos_player + GV.SQUARE_SIZE / 2

                dx = mouse_x - player_center_x
                dy = mouse_y - player_center_y

                length = (dx * dx + dy * dy) ** 0.5
                if length == 0:
                    length = 0.0001

                dx /= length
                dy /= length

                rocket = Rocket(
                    x_pos=player_center_x,
                    y_pos=player_center_y,
                    screen=self.screen,
                    dx=dx * 8,  # Geschwindigkeit
                    dy=dy * 8
                )
                self.rockets.add_rocket(rocket)

    def get_pos(self):
        return self.x_pos_player, self.y_pos_player

    def update_and_draw(self):
        self.draw()
        self.move()
        self.shoot()