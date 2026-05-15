import pygame
from .Variables import GameVariables as gv

class Rocket:
    dx: float    # x_geschwindigkeit
    dy: float     # y_geschwindigkeit
    x_pos: float  # x_position vom rocket
    y_pos: float # y_position vom rocket


    def __init__(self, screen, x_pos, y_pos, dx, dy):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.dx = dx
        self.dy = dy
        self.screen = screen
        self.width = gv.MISSILE_SIZE
        self.height = gv.MISSILE_SIZE


    def update_and_draw(self):
        self.x_pos += self.dx
        self.y_pos += self.dy
        pygame.draw.circle(surface=self.screen,
                         center=(self.x_pos, self.y_pos),
                         color="yellow",
                         width=0, radius=8)




class Rockets:
    def __init__(self, screen):
        self.screen = screen
        self.rockets = []

    def add_rocket(self, rocket: Rocket):
        self.rockets.append(rocket)

    def update_and_draw(self):
        for idx, missile in enumerate(reversed(self.rockets)):
            missile.update_and_draw()

            if missile.y_pos <= 0 - missile.height or missile.y_pos >= gv.SCREEN_HEIGHT or missile.x_pos <= 0 - missile.height or missile.x_pos >= gv.SCREEN_WIDTH:
                self.rockets.pop(len(self.rockets) - idx - 1)

    def get_rockets(self):
        return self.rockets


