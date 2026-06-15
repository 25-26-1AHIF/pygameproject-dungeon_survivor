import pygame
import random
from .Player_sprite import Sprite
import math
import json

from .Variables import GameVariables as GV
from .schuss_elemente_player import Rocket
from .enemys import Enemy as en
from .attack_sprite import Sprite as sp

class Player:
    def __init__(self, screen, rockets, enemies, coin_list):
        self.x_pos_player = GV.SCREEN_WIDTH/2-(GV.SQUARE_SIZE/2)
        self.y_pos_player = GV.SCREEN_HEIGHT/2-(GV.SQUARE_SIZE/2)
        self.screen = screen
        self.rockets = rockets
        self.actual_weapon = GV.actual_WAEPON
        self.speed = 2
        self.sprite = Sprite(
            filepath="assets/Ninja Adventure - Asset Pack/Actor/CharacterAnimated/NinjaGreen/SpriteSheet.png",
            animation_speed=10,
            image_rect=pygame.Rect(0, 32*4, 32, 32),
            image_count=4)

        self.sprite.load_spritesheet()
        self.last_shot = 0
        self.shoot_cooldown = 100
        self.frame_counter = 0
        self.Sprite_attack_axt = sp(filepath="assets/Ninja Adventure - Asset Pack/FX/Attack/CircularSlash/SpriteSheet.png",
            animation_speed=5,
            image_rect=pygame.Rect(0, 0, 32, 32),
            image_count=4)
        self.Sprite_attack_sword = sp(filepath="assets/Ninja Adventure - Asset Pack/FX/Attack/Claw/SpriteSheet.png",
                                      animation_speed=5,
                                      image_rect=pygame.Rect(0, 0, 32, 32),
                                      image_count=4)
        self.sword = pygame.image.load("assets/Ninja Adventure - Asset Pack/Items/Weapons/Sword2/Sprite.png")
        self.axt = pygame.image.load("assets/Ninja Adventure - Asset Pack/Items/Weapons/AxeTool/Sprite.png")
        self.bogen = pygame.image.load("assets/Ninja Adventure - Asset Pack/Items/Weapons/Bow/Sprite.png")
        self.armbrust = pygame.image.load("assets/Ninja Adventure - Asset Pack/Items/Weapons/Crossbow/Sprite.png")
        self.x_pos = 0
        self.y_pos = 0
        self.dx = 0
        self.dy = 0
        self.attack_angle = 0
        self.enemies = enemies
        self.enemys_list = None
        self.facing = "down"
        self.coin_list = coin_list
        self.attacking = False
        self.attack_frame = 0
        self.sprite_left = Sprite(
            filepath="assets/Ninja Adventure - Asset Pack/Actor/CharacterAnimated/NinjaGreen/SpriteSheet.png",
            animation_speed=10,
            image_rect=pygame.Rect(32 * 2, 32 * 4, 32, 32),
            image_count=4)
        self.sprite_right = Sprite(
            filepath="assets/Ninja Adventure - Asset Pack/Actor/CharacterAnimated/NinjaGreen/SpriteSheet.png",
            animation_speed=10,
            image_rect=pygame.Rect(32 * 3, 32 * 4, 32, 32),
            image_count=4)
        self.sprite_up = Sprite(
            filepath="assets/Ninja Adventure - Asset Pack/Actor/CharacterAnimated/NinjaGreen/SpriteSheet.png",
            animation_speed=10,
            image_rect=pygame.Rect(32, 32 * 4, 32, 32),
            image_count=4)
        self.sprite_down = Sprite(
            filepath="assets/Ninja Adventure - Asset Pack/Actor/CharacterAnimated/NinjaGreen/SpriteSheet.png",
            animation_speed=10,
            image_rect=pygame.Rect(0, 32 * 4, 32, 32),
            image_count=4)


        self.sprite_left_stand = Sprite(
            filepath="assets/Ninja Adventure - Asset Pack/Actor/CharacterAnimated/NinjaGreen/SpriteSheet.png",
            animation_speed=10,
            image_rect=pygame.Rect(32 * 2, 0, 32, 32),
            image_count=4)

        self.sprite_right_stand = Sprite(
            filepath="assets/Ninja Adventure - Asset Pack/Actor/CharacterAnimated/NinjaGreen/SpriteSheet.png",
            animation_speed=10,
            image_rect=pygame.Rect(32 * 3, 0, 32, 32),
            image_count=4)

        self.sprite_up_stand = Sprite(
            filepath="assets/Ninja Adventure - Asset Pack/Actor/CharacterAnimated/NinjaGreen/SpriteSheet.png",
            animation_speed=10,
            image_rect=pygame.Rect(32, 0, 32, 32),
            image_count=4)
        self.sprite_down_stand = Sprite(
            filepath="assets/Ninja Adventure - Asset Pack/Actor/CharacterAnimated/NinjaGreen/SpriteSheet.png",
            animation_speed=10,
            image_rect=pygame.Rect(0, 0, 32, 32),
            image_count=4)

        self.sprite_left.load_spritesheet()
        self.sprite_right.load_spritesheet()
        self.sprite_up.load_spritesheet()
        self.sprite_down.load_spritesheet()

        self.sprite_left_stand.load_spritesheet()
        self.sprite_right_stand.load_spritesheet()
        self.sprite_up_stand.load_spritesheet()
        self.sprite_down_stand.load_spritesheet()

        self.Sprite_attack_axt.load_spritesheet()
        self.Sprite_attack_sword.load_spritesheet()



    def draw_character(self):
        self.sprite.draw(
            self.screen,
            self.x_pos_player,
            self.y_pos_player,
            self.frame_counter)

    def draw_attack(self):
        if GV.actual_WAEPON == 1:
            self.Sprite_attack_axt.draw(
                self.screen,
                self.x_pos_player,
                self.y_pos_player,
                self.frame_counter)
        elif GV.actual_WAEPON == 0:
            self.Sprite_attack_sword.draw(
                self.screen,
                self.x_pos_player,
                self.y_pos_player,
                self.frame_counter)
    def move(self):

        pressed_keys = pygame.key.get_pressed()

        moving = False

        if pressed_keys[pygame.K_a]:
            if self.x_pos_player > 0:
                self.x_pos_player -= self.speed
                moving = True
                self.facing = "left"
                self.sprite = self.sprite_left

        if pressed_keys[pygame.K_d]:
            if self.x_pos_player < GV.SCREEN_WIDTH - GV.SQUARE_SIZE:
                self.x_pos_player += self.speed
                moving = True
                self.facing = "right"
                self.sprite = self.sprite_right

        if pressed_keys[pygame.K_w]:
            if self.y_pos_player > 0:
                self.y_pos_player -= self.speed
                moving = True
                self.facing = "up"
                self.sprite = self.sprite_up

        if pressed_keys[pygame.K_s]:
            if self.y_pos_player < GV.SCREEN_HEIGHT - GV.SQUARE_SIZE:
                self.y_pos_player += self.speed
                moving = True
                self.facing = "down"
                self.sprite = self.sprite_down



        self.sprite.draw(self.screen, self.x_pos_player, self.y_pos_player, self.frame_counter)

        if self.facing == "right":
            self.x_pos = self.x_pos_player + 60
            self.y_pos = self.y_pos_player + 48
        elif self.facing == "left":
            self.x_pos = self.x_pos_player + 20
            self.y_pos = self.y_pos_player + 48
        elif self.facing == "up":
            self.x_pos = self.x_pos_player + 60
            self.y_pos = self.y_pos_player + 48
        elif self.facing == "down":
            self.x_pos = self.x_pos_player + 20
            self.y_pos = self.y_pos_player + 48

        if not moving:

            if self.facing == "right":
                self.sprite = self.sprite_right_stand

            elif self.facing == "left":
                self.sprite = self.sprite_left_stand

            elif self.facing == "up":
                self.sprite = self.sprite_up_stand

            elif self.facing == "down":
                self.sprite = self.sprite_down_stand

    def draw_weapon(self):
        weapon = None

        if GV.actual_WAEPON == 0:
            weapon = pygame.transform.scale(self.sword, (22, 34))

            if self.facing == "right":
                weapon = pygame.transform.rotate(weapon, -90)
                x = self.x_pos_player + 40
                y = self.y_pos_player + 57

            elif self.facing == "left":
                weapon = pygame.transform.rotate(weapon, -90)
                weapon = pygame.transform.flip(weapon, True, False)
                x = self.x_pos_player + 20
                y = self.y_pos_player + 57

            elif self.facing == "up":
                x = self.x_pos_player + 20
                y = self.y_pos_player + 45

            else:
                weapon = pygame.transform.rotate(weapon, 180)
                x = self.x_pos_player + 25
                y = self.y_pos_player + 60

        elif GV.actual_WAEPON == 1:
            weapon = pygame.transform.scale(self.axt, (25, 34))

            if self.facing == "right":
                weapon = pygame.transform.rotate(weapon, -90)
                weapon = pygame.transform.flip(weapon, False, True)
                x = self.x_pos_player + 40
                y = self.y_pos_player + 65

            elif self.facing == "left":
                weapon = pygame.transform.rotate(weapon, 90)
                #weapon = pygame.transform.flip(weapon, False, True)
                x = self.x_pos_player + 25
                y = self.y_pos_player + 65

            elif self.facing == "up":
                x = self.x_pos_player + 16
                y = self.y_pos_player + 40

            else:
                weapon = pygame.transform.flip(weapon, False, True)
                x = self.x_pos_player + 16
                y = self.y_pos_player + 65

        elif GV.actual_WAEPON == 2:
            weapon = pygame.transform.scale(self.bogen, (28, 28))
            weapon = pygame.transform.rotate(weapon, 90)

            if self.facing == "right":
                x = self.x_pos_player + 32
                y = self.y_pos_player + 55

            elif self.facing == "left":
                weapon = pygame.transform.flip(weapon, True, False)
                x = self.x_pos_player + 40
                y = self.y_pos_player + 55

            elif self.facing == "up":
                weapon = pygame.transform.rotate(weapon, 90)
                x = self.x_pos_player + 24
                y = self.y_pos_player + 55

            else:
                weapon = pygame.transform.rotate(weapon, -90)
                x = self.x_pos_player + 24
                y = self.y_pos_player + 55

        elif GV.actual_WAEPON == 3:
            weapon = pygame.transform.scale(self.armbrust, (30, 30))

            if self.facing == "right":
                x = self.x_pos_player + 45
                y = self.y_pos_player + 50

            elif self.facing == "left":
                weapon = pygame.transform.flip(weapon, True, False)
                x = self.x_pos_player + 28
                y = self.y_pos_player + 50

            elif self.facing == "up":
                weapon = pygame.transform.rotate(weapon, 90)
                x = self.x_pos_player + 16
                y = self.y_pos_player + 44

            else:
                weapon = pygame.transform.rotate(weapon, -90)
                x = self.x_pos_player + 28
                y = self.y_pos_player + 64

        else:
            return

        self.screen.blit(weapon, (x, y))






    def shoot(self, event):
        with open("speichern_spielstand.json", "r") as fp:
            inhalt = json.load(fp)
        if self.actual_weapon == 0:
            self.enemys_list = self.enemies.get_enemy_list()
            #KI Anfang
            #KI: Chat gpt
            #prompt: Wie bekomme ich das event hier her mit einem mausklick
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    #KI Ende
                    self.attacking = True
                    self.attack_frame = 0
                    self.sword_attack()

        if self.actual_weapon == 1:
            self.enemys_list = self.enemies.get_enemy_list()
            # KI Anfang
            # KI: Chat gpt
            # prompt: Wie bekomme ich das event hier her mit einem mausklick
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # KI Ende

                    self.attacking = True
                    self.attack_frame = 0
                    self.axt_attack()



        if self.actual_weapon == 2:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    attack_sound = pygame.mixer.Sound("assets/Ninja Adventure - Asset Pack/Audio/Sounds/Whoosh & Slash/Launch.wav")
                    attack_sound.set_volume(0.7)
                    attack_sound.play()

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
            self.shoot_cooldown = self.shoot_cooldown - inhalt[3]['Armbrust']['upgrade'] *10
            pressed_key = pygame.mouse.get_pressed()
            current_time = pygame.time.get_ticks()

            if pressed_key[0] and current_time - self.last_shot >= self.shoot_cooldown:

                attack_sound = pygame.mixer.Sound("assets/Ninja Adventure - Asset Pack/Audio/Sounds/Whoosh & Slash/Launch.wav")
                attack_sound.set_volume(0.7)
                attack_sound.play()
                self.last_shot = current_time
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

            self.shoot_cooldown = 100

    def sword_attack(self):
        attack_sound = pygame.mixer.Sound("assets/Ninja Adventure - Asset Pack/Audio/Sounds/Whoosh & Slash/Sword2.wav")
        attack_sound.set_volume(0.7)
        attack_sound.play()
        mouse_x, mouse_y = pygame.mouse.get_pos()

        px = self.x_pos_player + GV.SQUARE_SIZE / 2
        py = self.y_pos_player + GV.SQUARE_SIZE / 2

        # Winkel zwischen Spieler und Maus berechnen
        # atan2 liefert den Winkel in Radiant.
        # KI: Anfang
        # KI: Chat gpt
        # prompt: Helfe mir die Attacke von einem schwert in einem bestimmten radius
        # und winkel in richtung zur maus zu berechnen
        attack_angle = math.atan2(mouse_y - py, mouse_x - px)
        # KI: ende

        radius = 150

        # Angriffswinkel (180 Grad)
        # KI: Anfang
        # KI: Chat gpt
        # prompt: Helfe mir die Attacke von einem schwert in einem bestimmten radius
        # und winkel in richtung zur maus zu berechnen
        arc = math.pi
        # KI: ende


        for enemy in self.enemys_list[:]:  # FIX: statt self.enemys_list

            dx = enemy[0] - px

            dy = enemy[1] - py

            # Entfernung zwischen Spieler und Gegner berechnen
            # nach dem Satz des Pythagoras
            # KI: Anfang
            # KI: Chat gpt
            # prompt: Helfe mir die Attacke von einem schwert in einem bestimmten radius
            # und winkel in richtung zur maus zu berechnen
            distance = math.sqrt(dx * dx + dy * dy)

            # Wenn Gegner außerhalb der Reichweite ist,
            # nächsten Gegner prüfen
            if distance > radius:
                continue
            # KI: ende

            # Winkel vom Spieler zum Gegner berechnen
            # KI: Anfang
            # KI: Chat gpt
            # prompt: Helfe mir die Attacke von einem schwert in einem bestimmten radius
            # und winkel in richtung zur maus zu berechnen
            enemy_angle = math.atan2(dy, dx)

            # Winkelunterschied zwischen Angriffsrichtung
            # und Gegnerposition berechnen
            diff = abs(enemy_angle - attack_angle)
            # KI: ende

            # Korrigiert den Spezialfall
            # wenn ein Winkel z.B. bei 350°
            # und der andere bei 10° liegt
            # KI: Anfang
            # KI: Chat gpt
            # prompt: Helfe mir die Attacke von einem schwert in einem bestimmten radius
            # und winkel in richtung zur maus zu berechnen
            if diff > math.pi:
                diff = 2 * math.pi - diff

            # Prüfen ob Gegner innerhalb
            # des Angriffswinkels liegt
            if diff < arc / 2:
                # Gegner wird aus der Liste entfernt
                # (= Gegner stirbt)
                self.enemys_list.remove(enemy)
                self.coin_list.append([enemy[0], enemy[1]])
            # KI: ende

    def axt_attack(self):
        attack_sound = pygame.mixer.Sound("assets/Ninja Adventure - Asset Pack/Audio/Sounds/Whoosh & Slash/Slash.wav")
        attack_sound.set_volume(0.7)
        attack_sound.play()
        mouse_x, mouse_y = pygame.mouse.get_pos()

        px = self.x_pos_player + GV.SQUARE_SIZE / 2
        py = self.y_pos_player + GV.SQUARE_SIZE / 2

        # Winkel zwischen Spieler und Maus berechnen
        # atan2 liefert den Winkel in Radiant.
        # KI: Anfang
        # KI: Chat gpt
        # prompt: Helfe mir die Attacke von einem schwert in einem bestimmten radius
        # und winkel in richtung zur maus zu berechnen
        attack_angle = math.atan2(mouse_y - py, mouse_x - px)
        # KI: ende

        radius = 170

        # Angriffswinkel (180 Grad)
        # KI: Anfang
        # KI: Chat gpt
        # prompt: Helfe mir die Attacke von einem schwert in einem bestimmten radius
        # und winkel in richtung zur maus zu berechnen
        arc = math.pi*2
        # KI: ende


        for enemy in self.enemys_list[:]:  # FIX: statt self.enemys_list

            dx = enemy[0] - px

            dy = enemy[1] - py

            # Entfernung zwischen Spieler und Gegner berechnen
            # nach dem Satz des Pythagoras
            # KI: Anfang
            # KI: Chat gpt
            # prompt: Helfe mir die Attacke von einem schwert in einem bestimmten radius
            # und winkel in richtung zur maus zu berechnen
            distance = math.sqrt(dx * dx + dy * dy)

            # Wenn Gegner außerhalb der Reichweite ist,
            # nächsten Gegner prüfen
            if distance > radius:
                continue
            # KI: ende

            # Winkel vom Spieler zum Gegner berechnen
            # KI: Anfang
            # KI: Chat gpt
            # prompt: Helfe mir die Attacke von einem schwert in einem bestimmten radius
            # und winkel in richtung zur maus zu berechnen
            enemy_angle = math.atan2(dy, dx)

            # Winkelunterschied zwischen Angriffsrichtung
            # und Gegnerposition berechnen
            diff = abs(enemy_angle - attack_angle)
            # KI: ende

            # Korrigiert den Spezialfall
            # wenn ein Winkel z.B. bei 350°
            # und der andere bei 10° liegt
            # KI: Anfang
            # KI: Chat gpt
            # prompt: Helfe mir die Attacke von einem schwert in einem bestimmten radius
            # und winkel in richtung zur maus zu berechnen
            if diff > math.pi:
                diff = 2 * math.pi - diff

            # Prüfen ob Gegner innerhalb
            # des Angriffswinkels liegt
            if diff < arc / 2:
                # Gegner wird aus der Liste entfernt
                # (= Gegner stirbt)
                self.enemys_list.remove(enemy)
                self.coin_list.append([enemy[0], enemy[1]])
            # KI: ende


    def get_pos(self):
        return self.x_pos_player, self.y_pos_player

    def update_and_draw(self):
        self.move()
        self.draw_character()
        self.draw_weapon()
        self.frame_counter +=1
        if self.attacking:
            if GV.actual_WAEPON == 1:
                self.Sprite_attack_axt.draw(
                    self.screen,
                    self.x_pos_player,
                    self.y_pos_player,
                    self.attack_frame
                )
            elif GV.actual_WAEPON == 0:
                self.Sprite_attack_sword.draw(
                    self.screen,
                    self.x_pos_player,
                    self.y_pos_player,
                    self.attack_frame
                )

            self.attack_frame += 1

        if self.attack_frame >= self.Sprite_attack_axt.image_count * self.Sprite_attack_axt.animation_speed:
            self.attacking = False
            self.attack_frame = 0
        if self.attack_frame >= self.Sprite_attack_sword.image_count * self.Sprite_attack_sword.animation_speed:
            self.attacking = False
            self.attack_frame = 0



    def update_and_shoot(self, event):
        self.shoot(event)