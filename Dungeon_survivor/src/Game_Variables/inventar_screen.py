import pygame
import json

from .Variables import GameVariables as GV
from .Variables import GameScreens


class Inventar:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.inhalt = self.lade_spielstand()
        self.coin_score = self.lade_coins()

        self.background = pygame.image.load("assets/ChatGPT Image 14. Juni 2026, 10_12_35.png")

        self.waffen = [
            ["Schwert", 0, 200, "assets/Ninja Adventure - Asset Pack/Items/Weapons/Sword2/Sprite.png", GameScreens.SCHWERT],
            ["Axt", 1, 310, "assets/Ninja Adventure - Asset Pack/Items/Weapons/AxeTool/Sprite.png", GameScreens.AXT],
            ["Bogen", 2, 420, "assets/Ninja Adventure - Asset Pack/Items/Weapons/Bow2/Sprite.png", GameScreens.BOGEN],
            ["Armbrust", 3, 530, "assets/Ninja Adventure - Asset Pack/Items/Weapons/Crossbow/Sprite.png", GameScreens.ARMBRUST],
        ]

        self.waffen_bilder = []
        for waffe in self.waffen:
            bild = pygame.image.load(waffe[3])
            bild = pygame.transform.scale(bild, (bild.get_width() * 6, bild.get_height() * 6))
            self.waffen_bilder.append(bild)

        self.skins = [
            ["Ninja", 4, 200, "assets/Ninja Adventure - Asset Pack/Actor/Character/NinjaGreen/Faceset.png"],
            ["Monk", 5, 310, "assets/Ninja Adventure - Asset Pack/Actor/Character/Monk2/Faceset.png"],
            ["Lion", 6, 420, "assets/Ninja Adventure - Asset Pack/Actor/Character/Lion/Faceset.png"],
            ["Vampire", 7, 530, "assets/Ninja Adventure - Asset Pack/Actor/Character/Vampire/Faceset.png"]
        ]

        self.skin_bilder = []

        for skin in self.skins:
            bild = pygame.image.load(skin[3]).convert_alpha()
            bild = pygame.transform.scale(bild, (bild.get_width() * 2.5, bild.get_height() * 2.5))
            self.skin_bilder.append(bild)

    def lade_spielstand(self):
        with open("save/speichern_spielstand.json", "r") as fp:
            return json.load(fp)

    def speichere_spielstand(self):
        with open("save/speichern_spielstand.json", "w") as fp:
            json.dump(self.inhalt, fp, indent=4)

    def lade_coins(self):
        with open("save/Coin_speicher.txt", "r") as fp:
            inhalt_coin = fp.read()

        if len(inhalt_coin) > 0:

            return int(inhalt_coin)
        else:
            return 0

    def speichere_coins(self):
        with open("Coin_speicher.txt", "w") as fp:
            fp.write(f"{self.coin_score}")

    def auswahl_setzen_waffen(self, index):
        for waffe in self.waffen:
            name = waffe[0]
            i = waffe[1]
            self.inhalt[i][name]["ausgewaehlt"] = "Nein"

        name = self.waffen[index][0]
        self.inhalt[index][name]["ausgewaehlt"] = "Ja"
        GV.actual_WAEPON = index

    def auswahl_setzte_skins(self, index):
        for skin in self.skins:
            name = skin[0]
            i = skin[1]
            self.inhalt[i][name]["ausgewaehlt"] = "Nein"

        name = self.skins[index][0]
        echter_index = self.skins[index][1]
        self.inhalt[echter_index][name]["ausgewaehlt"] = "Ja"
        GV.actual_CHARACTER = index

    def run(self):
        pygame.display.set_caption("Dungeon Survivor - Inventar")
        pygame.mixer.music.load("assets/Ninja Adventure - Asset Pack/Audio/Musics/16 - Melancholia.ogg")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.6)

        while True:
            self.texte_und_rects()

            for event in pygame.event.get():
                rueckgabe = self.handle_event(event)
                if rueckgabe != None:
                    return rueckgabe

            self.draw()
            self.speichere_spielstand()

            pygame.display.flip()
            self.clock.tick(GV.FPS)

    def texte_und_rects(self):
        self.coin_text = GV.FONT_MIDDLE.render(f"Coin: {self.coin_score}", True, "gold1")
        self.coin_text_rect = self.coin_text.get_rect(center=(GV.SCREEN_WIDTH - 150, 30))

        self.waffen_text = GV.FONT_BIG.render("Waffe", False, "yellow")
        self.skins_text = GV.FONT_BIG.render("Skin ", False, "yellow")

        self.waffen_text_rect = self.waffen_text.get_rect(topleft=(GV.SCREEN_WIDTH - GV.SCREEN_WIDTH / 1.2, 50))
        self.skins_text_rect = self.skins_text.get_rect(topleft=(GV.SCREEN_WIDTH - GV.SCREEN_WIDTH / 4, 50))

        self.ausruesten_text_rects_waffen = []
        self.ausruesten_text_rects_skins = []
        self.information_text_circles = []
        self.upgrade_text_rects = []

        for waffe in self.waffen:
            y = waffe[2]
            self.ausruesten_text_rects_waffen.append(pygame.Rect(GV.SCREEN_WIDTH - GV.SCREEN_WIDTH / 3 + 50, y + 20, 220, 40))
            self.information_text_circles.append(pygame.Rect(GV.SCREEN_WIDTH - GV.SCREEN_WIDTH / 3 + 250, y - 5, 30, 30))
            self.upgrade_text_rects.append(pygame.Rect(GV.SCREEN_WIDTH - GV.SCREEN_WIDTH / 4 + 40, y + 60, 180, 30))

        for skin in self.skins:
            y = skin[2]
            self.ausruesten_text_rects_skins.append(pygame.Rect(200, y + 25, 220, 40))


    def handle_event(self, event):
        if event.type == pygame.QUIT:
            return GameScreens.Exit

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            return GameScreens.MAIN

        if event.type == pygame.MOUSEBUTTONDOWN:
            for waffe in self.waffen:
                name = waffe[0]
                index = waffe[1]

                if self.ausruesten_text_rects_waffen[index].collidepoint(event.pos):
                    if self.inhalt[index][name]["Verfuegbarkeit"] == "False":
                        self.auswahl_setzen_waffen(index)

                if self.information_text_circles[index].collidepoint(event.pos):
                    return waffe[4]

                if index == 2 or index == 3:
                    if self.upgrade_text_rects[index].collidepoint(event.pos):
                        self.upgrade_waffe(index, name)

            for counter, skin in enumerate(self.skins):
                name = skin[0]
                index = skin[1]

                if self.ausruesten_text_rects_skins[counter].collidepoint(event.pos):

                    if self.inhalt[index][name]["Verfuegbarkeit"] == "False":
                        self.auswahl_setzte_skins(counter)

        return None

    def upgrade_waffe(self, index, name):
        max_level = 3 if name == "Bogen" else 6

        if self.inhalt[index][name]["Verfuegbarkeit"] == "False":
            if self.inhalt[index][name]["upgrade"] < max_level:
                if self.coin_score >= self.inhalt[index][name]["upgrade_kosten"]:
                    self.inhalt[index][name]["upgrade"] += 1
                    self.coin_score -= self.inhalt[index][name]["upgrade_kosten"]
                    self.speichere_coins()

    def draw(self):
        self.screen.blit(self.background, (0, 0))

        pygame.draw.rect(self.screen, "black", self.waffen_text_rect)
        self.screen.blit(self.waffen_text, self.waffen_text_rect)

        pygame.draw.rect(self.screen, "black", self.skins_text_rect)
        self.screen.blit(self.skins_text, self.skins_text_rect)

        pygame.draw.rect(self.screen, "black", self.coin_text_rect)
        self.screen.blit(self.coin_text, self.coin_text_rect)

        pygame.draw.rect(self.screen, "white", (GV.SCREEN_WIDTH - GV.SCREEN_WIDTH / 2.3, 170, 400, 500))

        for waffe in self.waffen:
            name = waffe[0]
            index = waffe[1]
            y = waffe[2]

            besitzt = self.inhalt[index][name]["Verfuegbarkeit"] == "False"
            farbe = "green" if besitzt else "red"

            pygame.draw.rect(self.screen, farbe, (GV.SCREEN_WIDTH - GV.SCREEN_WIDTH / 2.5 - 10, y - 10, 110, 100))

            waffen_image_rect = pygame.Rect(GV.SCREEN_WIDTH - GV.SCREEN_WIDTH / 2.5, y, 80, 80)
            waffen_pos = self.waffen_bilder[index].get_rect(center=waffen_image_rect.center)
            self.screen.blit(self.waffen_bilder[index], waffen_pos)

            ausruesten_text = self.get_ausruesten_text(index, name)
            self.screen.blit(ausruesten_text, self.ausruesten_text_rects_waffen[index])

            self.draw_upgrade(index, name, y)
            self.draw_information(index)
            self.draw_skins()

    def get_ausruesten_text(self, index, name):
        if self.inhalt[index][name]["Verfuegbarkeit"] == "False":
            if self.inhalt[index][name]["ausgewaehlt"] == "Ja":
                GV.actual_WAEPON = index
                return GV.FONT_MIDDLE.render("Ausgerüstet", False, "green")
            return GV.FONT_MIDDLE.render("Ausrüsten", False, "black")

        return GV.FONT_SMALL.render("Nicht Verfügbar", False, "red")

    def draw_upgrade(self, index, name, y):
        if index != 2 and index != 3:
            return

        if self.inhalt[index][name]["Verfuegbarkeit"] != "False":
            return

        if name == "Bogen":
            max_level = 3
        else:
            max_level = 6

        lvl_text = GV.FONT_SMALL.render(f"Lvl: {self.inhalt[index][name]['upgrade']}", True, "black")
        lvl_text_rect = lvl_text.get_rect(topleft=(GV.SCREEN_WIDTH - GV.SCREEN_WIDTH / 3 + 40, y + 60))
        self.screen.blit(lvl_text, lvl_text_rect)

        if self.inhalt[index][name]["upgrade"] >= max_level:
            upgrade_text = GV.FONT_SMALL.render("Max. Level", True, "gold1")
        else:
            upgrade_text = GV.FONT_SMALL.render(f"Upgrade {self.inhalt[index][name]['upgrade_kosten']}", True, "blue")

        self.screen.blit(upgrade_text, self.upgrade_text_rects[index])

    def draw_information(self, index):
        information_text = GV.FONT_MIDDLE.render("i", True, "black")

        pygame.draw.circle(
            self.screen,
            "yellow",
            self.information_text_circles[index].center,
            15
        )

        information_rect = information_text.get_rect(
            center=self.information_text_circles[index].center
        )

        self.screen.blit(information_text, information_rect)

    def draw_skins(self):
        pygame.draw.rect(self.screen, "white", (60, 170, 400, 500))
        leben_text_0 = GV.FONT_SMALL.render("200 Leben", True, "black")
        leben_text_1 = GV.FONT_SMALL.render("250 Leben", True, "black")
        leben_text_2 = GV.FONT_SMALL.render("300 Leben", True, "black")
        leben_text_3 = GV.FONT_SMALL.render("500 Leben", True, "black")

        self.screen.blit(leben_text_0, (200, self.skins[0][2] + 70))
        self.screen.blit(leben_text_1, (200, self.skins[1][2] + 70))
        self.screen.blit(leben_text_2, (200, self.skins[2][2] + 70))
        self.screen.blit(leben_text_3, (200, self.skins[3][2] + 70))

        for skin in self.skins:
            name = skin[0]
            index = skin[1]
            y = skin[2]


            #bsp. besitzt = (angenommen die skin Verfügbarkeit ist True) "True" == "False" und das ist False
            besitzt = self.inhalt[index][name]["Verfuegbarkeit"] == "False"

            if besitzt:
                farbe = "green"
            else:
                farbe = "red"

            pygame.draw.rect(self.screen, farbe, (90, y - 10, 100, 100))

            skin_image_rect = pygame.Rect(100, y, 80, 80)
            skin_pos = self.skin_bilder[index - 4].get_rect(center=skin_image_rect.center)
            self.screen.blit(self.skin_bilder[index - 4], skin_pos)

            if besitzt:
                if self.inhalt[index][name]["ausgewaehlt"] == "Ja":
                    text = GV.FONT_MIDDLE.render("Ausgerüstet", False, "green")
                else:
                    text = GV.FONT_MIDDLE.render("Ausrüsten", False, "black")
            else:
                text = GV.FONT_SMALL.render("Nicht Verfügbar", False, "red")

            self.screen.blit(text, (200, y + 25))
