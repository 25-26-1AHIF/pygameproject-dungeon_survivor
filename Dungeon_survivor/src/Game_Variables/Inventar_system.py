import pygame


class Inventar:

    def __init__(self, screen, inventar_list):
        self.screen = screen
        self.inventar_list = inventar_list
        self.axt = pygame.image.load("assets/Ninja Adventure - Asset Pack/Items/Weapons/Axe/Sprite.png")
        self.bogen = pygame.image.load("assets/Ninja Adventure - Asset Pack/Items/Weapons/Bow/Sprite.png")

    def check_system(self):
        pass





    def update_and_draw(self):
        self.check_system()