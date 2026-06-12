import pygame
from .Variables import GameVariables as gv
import json

class Rocket:
    dx: float    # x_geschwindigkeit
    dy: float     # y_geschwindigkeit
    x_pos: float  # x_position vom rocket
    y_pos: float # y_position vom rocket


    def __init__(self, screen, x_pos, y_pos, dx, dy, player_x_pos, player_y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.dx = dx
        self.dy = dy
        self.player_x_pos = player_x_pos
        self.player_y_pos = player_y_pos
        self.screen = screen
        self.width = gv.MISSILE_SIZE
        self.height = gv.MISSILE_SIZE
        self.projektil = pygame.image.load("assets/Ninja Adventure - Asset Pack/Items/Projectile/Bomb.png")





    def update_and_draw(self):
        if gv.actual_WAEPON == 2:
            with open("speichern_spielstand.json", "r") as fp:
                inhalt = json.load(fp)
            if inhalt[2]['Bogen']['upgrade'] >= 2:
                self.projektil = pygame.transform.scale(self.projektil, (30, 30))
            else:
                self.projektil = pygame.transform.scale(self.projektil, (25, 25))

            self.x_pos += self.dx
            self.y_pos += self.dy
            self.screen.blit(self.projektil, (self.x_pos, self.y_pos))
        elif gv.actual_WAEPON == 3:
            with open("speichern_spielstand.json", "r") as fp:
                inhalt = json.load(fp)
            if inhalt[3]['Armbrust']['upgrade'] == 6:
                self.projektil = pygame.transform.scale(self.projektil, (40, 40))
            elif inhalt[3]['Armbrust']['upgrade'] >= 3:
                self.projektil = pygame.transform.scale(self.projektil, (30, 30))
            elif inhalt[3]['Armbrust']['upgrade'] <=2:
                self.projektil = pygame.transform.scale(self.projektil, (25, 25))

            self.x_pos += self.dx
            self.y_pos += self.dy
            self.screen.blit(self.projektil, (self.x_pos, self.y_pos))




class Rockets:
    def __init__(self, screen):
        self.screen = screen
        self.rockets = []

    def add_rocket(self, rocket: Rocket):
        self.rockets.append(rocket)

    def update_and_draw(self):
        #KI-Anfang
        #KI: ChatGPT
        #prompt: Fehler behebung wenn list index out of range
        for missile in self.rockets.copy()[::-1]:
            missile.update_and_draw()
        #KI-Ende

            if missile.y_pos <= 0 - missile.height or missile.y_pos >= gv.SCREEN_HEIGHT or missile.x_pos <= 0 - missile.height or missile.x_pos >= gv.SCREEN_WIDTH:
                self.rockets.remove(missile)

    def get_rockets(self):
        return self.rockets


