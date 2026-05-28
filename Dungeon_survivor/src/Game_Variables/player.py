import pygame
import random
from .Player_sprite import Sprite

from .Variables import GameVariables as GV
from .schuss_elemente_player import Rocket

class Player:
    def __init__(self, screen, rockets):
        self.x_pos_player = GV.SCREEN_WIDTH/2-(GV.SQUARE_SIZE/2)
        self.y_pos_player = GV.SCREEN_HEIGHT/2-(GV.SQUARE_SIZE/2)
        self.screen = screen
        self.rockets = rockets
        self.actual_weapon = GV.actual_WAEPON
        self.speed = 2
        self.sprite = Sprite(
            filepath="assets/Ninja Adventure - Asset Pack/Actor/CharacterAnimated/NinjaGreen/SpriteSheet.png",
            animation_speed=10,
            image_rect=pygame.Rect(0, 32*9, 32, 32),
            image_count=15)

        self.sprite.load_spritesheet()
        self.frame_counter = 0
        self.sword = pygame.image.load("assets/Ninja Adventure - Asset Pack/Items/Weapons/Sword2/Sprite.png")
        self.x_pos = 0
        self.y_pos = 0
        self.dx = 0
        self.dy = 0


    def draw(self):
        self.sprite.draw(
            self.screen,
            self.x_pos_player,
            self.y_pos_player,
            self.frame_counter)


    def move(self):

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_a]:
            if self.x_pos_player <= 0:
                pass
            else:
                self.x_pos_player -= self.speed
                self.sprite = Sprite(
                    filepath="assets/Ninja Adventure - Asset Pack/Actor/CharacterAnimated/NinjaGreen/SpriteSheet.png",
                    animation_speed=10,
                    image_rect=pygame.Rect(32*2, 0, 32, 32),
                    image_count=15)
                self.sprite.load_spritesheet()
            if GV.actual_WAEPON == 0:
                self.x_pos = self.x_pos_player + 5
                self.y_pos = self.y_pos_player + 45
                sword = pygame.transform.scale(self.sword, (30, 30))
                self.screen.blit(sword, (self.x_pos, self.y_pos))

        if pressed_keys[pygame.K_d]:
            if self.x_pos_player >= GV.SCREEN_WIDTH - GV.SQUARE_SIZE:
                pass
            else:
                self.x_pos_player += self.speed
                self.sprite = Sprite(
                    filepath="assets/Ninja Adventure - Asset Pack/Actor/CharacterAnimated/NinjaGreen/SpriteSheet.png",
                    animation_speed=10,
                    image_rect=pygame.Rect(32 * 3, 0, 32, 32),
                    image_count=15)
                self.sprite.load_spritesheet()

            if GV.actual_WAEPON == 0:
                self.x_pos = self.x_pos_player + 60
                self.y_pos = self.y_pos_player + 50
                sword = pygame.transform.scale(self.sword, (30, 30))
                self.screen.blit(sword, (self.x_pos, self.y_pos))

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_w]:
            if self.y_pos_player <= 0:
                pass
            else:
                self.y_pos_player -= self.speed
                self.sprite = Sprite(
                    filepath="assets/Ninja Adventure - Asset Pack/Actor/CharacterAnimated/NinjaGreen/SpriteSheet.png",
                    animation_speed=10,
                    image_rect=pygame.Rect(32, 0, 32, 32),
                    image_count=15)
                self.sprite.load_spritesheet()
            if GV.actual_WAEPON == 0:
                self.x_pos = self.x_pos_player + 60
                self.y_pos = self.y_pos_player + 45
                sword = pygame.transform.scale(self.sword, (30, 30))
                self.screen.blit(sword, (self.x_pos, self.y_pos))

        if pressed_keys[pygame.K_s]:
            if self.y_pos_player >= GV.SCREEN_HEIGHT - GV.SQUARE_SIZE:
                pass
            else:
                self.y_pos_player += self.speed
                self.sprite = Sprite(
                    filepath="assets/Ninja Adventure - Asset Pack/Actor/CharacterAnimated/NinjaGreen/SpriteSheet.png",
                    animation_speed=10,
                    image_rect=pygame.Rect(0, 32*2, 32, 32),
                    image_count=15)
                self.sprite.load_spritesheet()
            if GV.actual_WAEPON == 0:
                self.x_pos = self.x_pos_player+5
                self.y_pos = self.y_pos_player+45
                sword = pygame.transform.scale(self.sword, (30, 30))
                self.screen.blit(sword, (self.x_pos, self.y_pos))

        if GV.actual_WAEPON == 0:
            sword = pygame.transform.scale(self.sword, (30, 30))
            self.screen.blit(sword, (self.x_pos, self.y_pos))







    def shoot(self, event):
        if self.actual_weapon == 0:

            #KI Anfang
            #KI: Chat gpt
            #prompt: Wie bekomme ich das event hier her mit einem mausklick
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    #KI Ende
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
                        dy=dy * 8,
                        player_x_pos=self.x_pos_player,
                        player_y_pos= self.y_pos_player
                    )
                    self.rockets.add_rocket(rocket)

        if self.actual_weapon == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    # KI Ende
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
                        dy=dy * 8,
                        player_x_pos = self.x_pos_player,
                        player_y_pos = self.y_pos_player
                    )
                    self.rockets.add_rocket(rocket)


        if self.actual_weapon == 2:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    # KI Ende
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
                        dy=dy * 8,
                        player_x_pos=self.x_pos_player,
                        player_y_pos=self.y_pos_player
                    )
                    self.rockets.add_rocket(rocket)

        if self.actual_weapon == 3:
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
                    dy=dy * 8,
                    player_x_pos=self.x_pos_player,
                    player_y_pos=self.y_pos_player
                )
                self.rockets.add_rocket(rocket)

    def get_pos(self):
        return self.x_pos_player, self.y_pos_player

    def update_and_draw(self):
        self.move()
        self.draw()
        self.frame_counter +=1


    def update_and_shoot(self, event):
        self.shoot(event)