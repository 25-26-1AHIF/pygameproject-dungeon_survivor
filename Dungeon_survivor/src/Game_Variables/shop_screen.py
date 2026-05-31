import pygame
import json
from .Variables import GameVariables as GV


def spielstand_auslesen(filepath: int) -> dict:
    with open(filepath, "r") as fp:
        spielstand = json.load(fp)
    return spielstand


def spielstand_speichern(filepath: str, source: dict) -> None:
    with open(filepath, "w") as fp:
        json.dump(source, fp, indent=4)


def muenzen_speichern(filepath: str, source: int) -> None:
    with open(filepath, "w") as fp:
        fp.write(f"{source}")


class WaffenShop:

    def __init__(self, margin, abstand, anzahl):
        self.margin = margin
        self.abstand = abstand
        self.anzahl = anzahl

    def update(self, spielstand, coins):
        self.waffen_text = GV.FONT_BIG.render("Waffen", False, "yellow")
        self.skins_text = GV.FONT_BIG.render("Skins ", False, "gray")

        self.waffen_text_rect = self.waffen_text.get_rect(topleft=(20, 100))
        self.skins_text_rect = self.skins_text.get_rect(topleft=(20, 100 + 80))

        self.hoehe = (GV.SCREEN_HEIGHT - 2 * self.margin - (self.anzahl - 1) * self.abstand) / self.anzahl
        self.hoehe_bild = self.hoehe - 4 * self.abstand

        self.x = 40 + self.waffen_text_rect.width
        self.y_start = self.margin

        self.schwert_headline = GV.FONT_MIDDLE.render("Schwert", False, "darkred")
        self.axt_headline = GV.FONT_MIDDLE.render("Axt", False, "darkred")
        self.bogen_headline = GV.FONT_MIDDLE.render("Bogen", False, "darkred")
        self.armbrust_headline = GV.FONT_MIDDLE.render("Armbrust", False, "darkred")

        self.schwert_text = GV.FONT_SMALL.render("Der Klassiker", False, "black")
        self.axt_text = GV.FONT_SMALL.render("Zwar langsam, zerhäckselt aber Gegner", False, "black")
        self.bogen_text = GV.FONT_SMALL.render("Ausgewogene Fernkampfwaffe", False, "black")
        self.armbrust_text = GV.FONT_SMALL.render("Töte Mehrere mit einem Schuss", False, "black")

        self.schwert_preis = GV.FONT_SMALL.render(f"Preis: {spielstand[0]['Schwert']['Coins']}", False, "gold3")
        self.axt_preis = GV.FONT_SMALL.render(f"Preis: {spielstand[1]['Axt']['Coins']}", False, "gold3")
        self.bogen_preis = GV.FONT_SMALL.render(f"Preis: {spielstand[2]['Bogen']['Coins']}", False, "gold3")
        self.armbrust_preis = GV.FONT_SMALL.render(f"Preis: {spielstand[3]['Armbrust']['Coins']}", False, "gold3")

        if spielstand[0]['Schwert']['Verfuegbarkeit'] == "True":
            self.schwert_kaufen = GV.FONT_MIDDLE.render("Kaufen", False, "green2")
            self.schwert_kaufen_rect = self.schwert_kaufen.get_rect(topleft=(self.x + 260 + self.hoehe_bild, self.y_start + 90))
        else:
            self.schwert_kaufen = GV.FONT_MIDDLE.render("Im Besitz", False, "red2")
            self.schwert_kaufen_rect = self.schwert_kaufen.get_rect(topleft=(self.x + 260 + self.hoehe_bild, self.y_start + 90))

        if spielstand[1]['Axt']['Verfuegbarkeit'] == "True":
            self.axt_kaufen = GV.FONT_MIDDLE.render("Kaufen", False, "green2")
            self.axt_kaufen_rect = self.axt_kaufen.get_rect(topleft=(self.x + 260 + self.hoehe_bild, self.y_start + 90 + 1 * (self.hoehe + self.abstand)))
        else:
            self.axt_kaufen = GV.FONT_MIDDLE.render("Im Besitz", False, "red2")
            self.axt_kaufen_rect = self.axt_kaufen.get_rect(topleft=(self.x + 260 + self.hoehe_bild, self.y_start + 90 + 1 * (self.hoehe + self.abstand)))

        if spielstand[2]['Bogen']['Verfuegbarkeit'] == "True":
            self.bogen_kaufen = GV.FONT_MIDDLE.render("Kaufen", False, "green2")
            self.bogen_kaufen_rect = self.bogen_kaufen.get_rect(topleft=(self.x + 260 + self.hoehe_bild, self.y_start + 90 + 2 * (self.hoehe + self.abstand)))
        else:
            self.bogen_kaufen = GV.FONT_MIDDLE.render("Im Besitz", False, "red2")
            self.bogen_kaufen_rect = self.bogen_kaufen.get_rect(topleft=(self.x + 260 + self.hoehe_bild, self.y_start + 90 + 2 * (self.hoehe + self.abstand)))

        if spielstand[3]['Armbrust']['Verfuegbarkeit'] == "True":
            self.armbrust_kaufen = GV.FONT_MIDDLE.render("Kaufen", False, "green2")
            self.armbrust_kaufen_rect = self.armbrust_kaufen.get_rect(topleft=(self.x + 260 + self.hoehe_bild, self.y_start + 90 + 3 * (self.hoehe + self.abstand)))
        else:
            self.armbrust_kaufen = GV.FONT_MIDDLE.render("Im Besitz", False, "red2")
            self.armbrust_kaufen_rect = self.armbrust_kaufen.get_rect(topleft=(self.x + 260 + self.hoehe_bild, self.y_start + 90 + 3 * (self.hoehe + self.abstand)))


        self.coins_text = GV.FONT_MIDDLE.render(f"Coins: {coins}", False, "yellow")
        self.coin_int_rect = self.coins_text.get_rect(center=(GV.SCREEN_WIDTH - 100, 47))

        # KI-Anfang
        # KI: ChatGPT
        # prompt: warum ist das letzte rechteck nicht ganz zu sehen: schwert_rect = pygame.Rect(40 + waffen_text_rect.width, 60, GV.SCREEN_WIDTH / 2, (GV.SCREEN_HEIGHT - 3 * 10) / 4) axt_rect = pygame.Rect(40 + waffen_text_rect.width, 60 + schwert_rect.height +10, GV.SCREEN_WIDTH / 2, (GV.SCREEN_HEIGHT - 2 * 10) / 4) bogen_rect = pygame.Rect(40 + waffen_text_rect.width, 60 + 2*(schwert_rect.height + 10), GV.SCREEN_WIDTH / 2, (GV.SCREEN_HEIGHT - 2 * 10) / 4) armbrust_rect = pygame.Rect(40 + waffen_text_rect.width, 60 + 3*(schwert_rect.height + 10), GV.SCREEN_WIDTH / 2, (GV.SCREEN_HEIGHT - 2 * 10) / 4)

        self.schwert_rect = pygame.Rect(self.x, self.y_start, GV.SCREEN_WIDTH / 2, self.hoehe)
        self.axt_rect = pygame.Rect(self.x, self.y_start + 1 * (self.hoehe + self.abstand), GV.SCREEN_WIDTH / 2, self.hoehe)
        self.bogen_rect = pygame.Rect(self.x, self.y_start + 2 * (self.hoehe + self.abstand), GV.SCREEN_WIDTH / 2, self.hoehe)
        self.armbrust_rect = pygame.Rect(self.x, self.y_start + 3 * (self.hoehe + self.abstand), GV.SCREEN_WIDTH / 2, self.hoehe)

        # KI-Ende

        self.schwert_image_rect = pygame.Rect(self.x + 10, self.y_start + 10, self.hoehe_bild, self.hoehe_bild)
        self.axt_image_rect = pygame.Rect(self.x + 10, self.y_start + 10 + 1 * (self.hoehe + self.abstand), self.hoehe_bild, self.hoehe_bild)
        self.bogen_image_rect = pygame.Rect(self.x + 10, self.y_start + 10 + 2 * (self.hoehe + self.abstand), self.hoehe_bild, self.hoehe_bild)
        self.armbrust_image_rect = pygame.Rect(self.x + 10, self.y_start + 10 + 3 * (self.hoehe + self.abstand), self.hoehe_bild, self.hoehe_bild)

        self.schwert_image = pygame.image.load("assets/Ninja Adventure - Asset Pack/Items/Weapons/Sword2/Sprite.png")
        self.axt_image = pygame.image.load("assets/Ninja Adventure - Asset Pack/Items/Weapons/AxeTool/Sprite.png")
        self.bogen_image = pygame.image.load("assets/Ninja Adventure - Asset Pack/Items/Weapons/Bow2/Sprite.png")
        self.armbrust_image = pygame.image.load("assets/Ninja Adventure - Asset Pack/Items/Weapons/Crossbow/Sprite.png")

        self.res_schwert_image = pygame.transform.scale(self.schwert_image,
                                                   (6 * self.schwert_image.get_width(), 6 * self.schwert_image.get_height()))
        self.res_axt_image = pygame.transform.scale(self.axt_image, (6 * self.axt_image.get_width(), 6 * self.axt_image.get_height()))
        self.res_bogen_image = pygame.transform.scale(self.bogen_image,
                                                 (6 * self.bogen_image.get_width(), 6 * self.bogen_image.get_height()))
        self.res_armbrust_image = pygame.transform.scale(self.armbrust_image,
                                                    (6 * self.armbrust_image.get_width(), 6 * self.armbrust_image.get_height()))



    def draw(self, screen):
        pygame.draw.rect(surface=screen, rect=self.schwert_rect, color="lightgray")
        pygame.draw.rect(surface=screen, rect=self.axt_rect, color="lightgray")
        pygame.draw.rect(surface=screen, rect=self.bogen_rect, color="lightgray")
        pygame.draw.rect(surface=screen, rect=self.armbrust_rect, color="lightgray")

        pygame.draw.rect(surface=screen, rect=self.schwert_image_rect, color="black")
        pygame.draw.rect(surface=screen, rect=self.axt_image_rect, color="black")
        pygame.draw.rect(surface=screen, rect=self.bogen_image_rect, color="black")
        pygame.draw.rect(surface=screen, rect=self.armbrust_image_rect, color="black")

        screen.blit(source=self.waffen_text, dest=self.waffen_text_rect)
        screen.blit(source=self.skins_text, dest=self.skins_text_rect)

        screen.blit(source=self.schwert_headline, dest=(self.x + 20 + self.hoehe_bild, self.y_start + 10))
        screen.blit(source=self.axt_headline, dest=(self.x + 20 + self.hoehe_bild, self.y_start + 10 + 1 * (self.hoehe + self.abstand)))
        screen.blit(source=self.bogen_headline, dest=(self.x + 20 + self.hoehe_bild, self.y_start + 10 + 2 * (self.hoehe + self.abstand)))
        screen.blit(source=self.armbrust_headline, dest=(self.x + 20 + self.hoehe_bild, self.y_start + 10 + 3 * (self.hoehe + self.abstand)))

        screen.blit(source=self.schwert_text, dest=(self.x + 20 + self.hoehe_bild, self.y_start + 50))
        screen.blit(source=self.axt_text, dest=(self.x + 20 + self.hoehe_bild, self.y_start + 50 + 1 * (self.hoehe + self.abstand)))
        screen.blit(source=self.bogen_text, dest=(self.x + 20 + self.hoehe_bild, self.y_start + 50 + 2 * (self.hoehe + self.abstand)))
        screen.blit(source=self.armbrust_text, dest=(self.x + 20 + self.hoehe_bild, self.y_start + 50 + 3 * (self.hoehe + self.abstand)))

        screen.blit(source=self.coins_text, dest=self.coin_int_rect)

        screen.blit(source=self.schwert_preis, dest=(self.x + 20 + self.hoehe_bild, self.y_start + 90))
        screen.blit(source=self.axt_preis, dest=(self.x + 20 + self.hoehe_bild, self.y_start + 90 + 1 * (self.hoehe + self.abstand)))
        screen.blit(source=self.bogen_preis, dest=(self.x + 20 + self.hoehe_bild, self.y_start + 90 + 2 * (self.hoehe + self.abstand)))
        screen.blit(source=self.armbrust_preis, dest=(self.x + 20 + self.hoehe_bild, self.y_start + 90 + 3 * (self.hoehe + self.abstand)))

        screen.blit(source=self.schwert_kaufen, dest=(self.x + 260 + self.hoehe_bild, self.y_start + 90))
        screen.blit(source=self.axt_kaufen, dest=(self.x + 260 + self.hoehe_bild, self.y_start + 90 + 1 * (self.hoehe + self.abstand)))
        screen.blit(source=self.bogen_kaufen, dest=(self.x + 260 + self.hoehe_bild, self.y_start + 90 + 2 * (self.hoehe + self.abstand)))
        screen.blit(source=self.armbrust_kaufen, dest=(self.x + 260 + self.hoehe_bild, self.y_start + 90 + 3 * (self.hoehe + self.abstand)))

        # KI-Anfang
        # KI: ChatGPT
        # prompt: wie du auf dem bild siehst ist das noch nicht genau zentriert wie kann man das machen
        schwert_pos = self.res_schwert_image.get_rect(center=self.schwert_image_rect.center)
        # KI-Ende
        axt_pos = self.res_axt_image.get_rect(center=self.axt_image_rect.center)
        bogen_pos = self.res_bogen_image.get_rect(center=self.bogen_image_rect.center)
        armbrust_pos = self.res_armbrust_image.get_rect(center=self.armbrust_image_rect.center)

        screen.blit(self.res_schwert_image, schwert_pos)
        screen.blit(self.res_axt_image, axt_pos)
        screen.blit(self.res_bogen_image, bogen_pos)
        screen.blit(self.res_armbrust_image, armbrust_pos)

    def handle_click(self, event, spielstand, coins):
        if self.waffen_text_rect.collidepoint(event.pos):
            return "waffen"

        elif self.skins_text_rect.collidepoint(event.pos):
            return "skins"

        elif self.schwert_kaufen_rect.collidepoint(event.pos) and spielstand[0]['Schwert'][
            'Verfuegbarkeit'] == "True":
            if coins >= spielstand[0]['Schwert']['Coins']:
                coins -= spielstand[0]['Schwert']['Coins']
                spielstand[0]['Schwert']['Verfuegbarkeit'] = "False"
                muenzen_speichern("Coin_speicher.txt", coins)
                spielstand_speichern("speichern_spielstand.json", spielstand)
                self.schwert_kaufen = GV.FONT_MIDDLE.render("Im Besitz", False, "red2")
                self.schwert_kaufen_rect = self.schwert_kaufen.get_rect(topleft=(self.x + 260 + self.hoehe_bild, self.y_start + 90))

        elif self.axt_kaufen_rect.collidepoint(event.pos) and spielstand[1]['Axt']['Verfuegbarkeit'] == "True":
            if coins >= spielstand[1]['Axt']['Coins']:
                coins -= spielstand[1]['Axt']['Coins']
                spielstand[1]['Axt']['Verfuegbarkeit'] = "False"
                muenzen_speichern("Coin_speicher.txt", coins)
                spielstand_speichern("speichern_spielstand.json", spielstand)
                self.axt_kaufen = GV.FONT_MIDDLE.render("Im Besitz", False, "red2")
                self.axt_kaufen_rect = self.axt_kaufen.get_rect(
                    topleft=(self.x + 260 + self.hoehe_bild, self.y_start + 90 + 1 * (self.hoehe + self.abstand)))

        elif self.bogen_kaufen_rect.collidepoint(event.pos) and spielstand[2]['Bogen']['Verfuegbarkeit'] == "True":
            if coins >= spielstand[2]['Bogen']['Coins']:
                coins -= spielstand[2]['Bogen']['Coins']
                spielstand[2]['Bogen']['Verfuegbarkeit'] = "False"
                muenzen_speichern("Coin_speicher.txt", coins)
                spielstand_speichern("speichern_spielstand.json", spielstand)
                self.bogen_kaufen = GV.FONT_MIDDLE.render("Im Besitz", False, "red2")
                self.bogen_kaufen_rect = self.bogen_kaufen.get_rect(
                    topleft=(self.x + 260 + self.hoehe_bild, self.y_start + 90 + 2 * (self.hoehe + self.abstand)))

        elif self.armbrust_kaufen_rect.collidepoint(event.pos) and spielstand[3]['Armbrust'][
            'Verfuegbarkeit'] == "True":
            if coins >= spielstand[3]['Armbrust']['Coins']:
                coins -= spielstand[3]['Armbrust']['Coins']
                spielstand[3]['Armbrust']['Verfuegbarkeit'] = "False"
                muenzen_speichern("Coin_speicher.txt", coins)
                spielstand_speichern("speichern_spielstand.json", spielstand)
                self.armbrust_kaufen = GV.FONT_MIDDLE.render("Im Besitz", False, "red2")
                self.armbrust_kaufen_rect = self.armbrust_kaufen.get_rect(
                    topleft=(self.x + 260 + self.hoehe_bild, self.y_start + 90 + 3 * (self.hoehe + self.abstand)))

class SkinShop:

    def __init__(self, margin, abstand, anzahl):
        self.margin = margin
        self.abstand = abstand
        self.anzahl = anzahl



    def update(self, spielstand, coins):
        self.waffen_text = GV.FONT_BIG.render("Waffen", False, "gray")
        self.skins_text = GV.FONT_BIG.render("Skins ", False, "yellow")

        self.waffen_text_rect = self.waffen_text.get_rect(topleft=(20, 100))
        self.skins_text_rect = self.skins_text.get_rect(topleft=(20, 100 + 80))

        self.hoehe = (GV.SCREEN_HEIGHT - 2 * self.margin - (self.anzahl - 1) * self.abstand) / self.anzahl
        self.hoehe_bild = self.hoehe - 4 * self.abstand

        self.x = 40 + self.waffen_text_rect.width
        self.y_start = self.margin
        self.ninja_headline = GV.FONT_MIDDLE.render("Ninja", False, "darkred")
        self.monk_headline = GV.FONT_MIDDLE.render("Monk", False, "darkred")
        self.lion_headline = GV.FONT_MIDDLE.render("Lion", False, "darkred")
        self.vampire_headline = GV.FONT_MIDDLE.render("Vampir", False, "darkred")

        self.ninja_text = GV.FONT_SMALL.render("Der Mainy", False, "black")
        self.monk_text = GV.FONT_SMALL.render("Der Opa", False, "black")
        self.lion_text = GV.FONT_SMALL.render("2-3 Jahre Dagestan", False, "black")
        self.vampire_text = GV.FONT_SMALL.render("Ostblock MVP", False, "black")

        self.ninja_preis = GV.FONT_SMALL.render(f"Preis: {spielstand[4]['Ninja']['Coins']}", False, "gold3")
        self.monk_preis = GV.FONT_SMALL.render(f"Preis: {spielstand[5]['Monk']['Coins']}", False, "gold3")
        self.lion_preis = GV.FONT_SMALL.render(f"Preis: {spielstand[6]['Lion']['Coins']}", False, "gold3")
        self.vampire_preis = GV.FONT_SMALL.render(f"Preis: {spielstand[7]['Vampire']['Coins']}", False, "gold3")

        self.ninja_rect = pygame.Rect(self.x, self.y_start, GV.SCREEN_WIDTH / 2, self.hoehe)
        self.monk_rect = pygame.Rect(self.x, self.y_start + 1 * (self.hoehe + self.abstand), GV.SCREEN_WIDTH / 2, self.hoehe)
        self.lion_rect = pygame.Rect(self.x, self.y_start + 2 * (self.hoehe + self.abstand), GV.SCREEN_WIDTH / 2, self.hoehe)
        self.vampire_rect = pygame.Rect(self.x, self.y_start + 3 * (self.hoehe + self.abstand), GV.SCREEN_WIDTH / 2, self.hoehe)

        self.ninja_image_rect = pygame.Rect(self.x + 10, self.y_start + 10, self.hoehe_bild, self.hoehe_bild)
        self.monk_image_rect = pygame.Rect(self.x + 10, self.y_start + 10 + 1 * (self.hoehe + self.abstand), self.hoehe_bild, self.hoehe_bild)
        self.lion_image_rect = pygame.Rect(self.x + 10, self.y_start + 10 + 2 * (self.hoehe + self.abstand), self.hoehe_bild, self.hoehe_bild)
        self.vampire_image_rect = pygame.Rect(self.x + 10, self.y_start + 10 + 3 * (self.hoehe + self.abstand), self.hoehe_bild, self.hoehe_bild)

        if spielstand[4]['Ninja']['Verfuegbarkeit'] == "True":
            self.ninja_kaufen = GV.FONT_MIDDLE.render("Kaufen", False, "green2")
            self.ninja_kaufen_rect = self.ninja_kaufen.get_rect(topleft=(self.x + 260 + self.hoehe_bild, self.y_start + 90))
        else:
            self.ninja_kaufen = GV.FONT_MIDDLE.render("Im Besitz", False, "red2")
            self.ninja_kaufen_rect = self.ninja_kaufen.get_rect(topleft=(self.x + 260 + self.hoehe_bild, self.y_start + 90))
        if spielstand[5]['Monk']['Verfuegbarkeit'] == "True":
            self.monk_kaufen = GV.FONT_MIDDLE.render("Kaufen", False, "green2")
            self.monk_kaufen_rect = self.monk_kaufen.get_rect(topleft=(self.x + 260 + self.hoehe_bild, self.y_start + 90 + 1 * (self.hoehe + self.abstand)))
        else:
            self.monk_kaufen = GV.FONT_MIDDLE.render("Im Besitz", False, "red2")
            self.monk_kaufen_rect = self.monk_kaufen.get_rect(topleft=(self.x + 260 + self.hoehe_bild, self.y_start + 90 + 1 * (self.hoehe + self.abstand)))

        if spielstand[6]['Lion']['Verfuegbarkeit'] == "True":
            self.lion_kaufen = GV.FONT_MIDDLE.render("Kaufen", False, "green2")
            self.lion_kaufen_rect = self.lion_kaufen.get_rect(topleft=(self.x + 260 + self.hoehe_bild, self.y_start + 90 + 2 * (self.hoehe + self.abstand)))
        else:
            self.lion_kaufen = GV.FONT_MIDDLE.render("Im Besitz", False, "red2")
            self.lion_kaufen_rect = self.lion_kaufen.get_rect(topleft=(self.x + 260 + self.hoehe_bild, self.y_start + 90 + 2 * (self.hoehe + self.abstand)))

        if spielstand[7]['Vampire']['Verfuegbarkeit'] == "True":
            self.vampire_kaufen = GV.FONT_MIDDLE.render("Kaufen", False, "green2")
            self.vampire_kaufen_rect = self.vampire_kaufen.get_rect(topleft=(self.x + 260 + self.hoehe_bild, self.y_start + 90 + 3 * (self.hoehe + self.abstand)))
        else:
            self.vampire_kaufen = GV.FONT_MIDDLE.render("Im Besitz", False, "red2")
            self.vampire_kaufen_rect = self.vampire_kaufen.get_rect(topleft=(self.x + 260 + self.hoehe_bild, self.y_start + 90 + 3 * (self.hoehe + self.abstand)))

        self.coins_text = GV.FONT_MIDDLE.render(f"Coins: {coins}", False, "yellow")
        self.coin_int_rect = self.coins_text.get_rect(center=(GV.SCREEN_WIDTH - 100, 47))

        self.ninja_image = pygame.image.load("assets/Ninja Adventure - Asset Pack/Actor/Character/NinjaGreen/Faceset.png")
        self.monk_image = pygame.image.load("assets/Ninja Adventure - Asset Pack/Actor/Character/Monk2/Faceset.png")
        self.lion_image = pygame.image.load("assets/Ninja Adventure - Asset Pack/Actor/Character/Lion/Faceset.png")
        self.vampire_image = pygame.image.load("assets/Ninja Adventure - Asset Pack/Actor/Character/Vampire/Faceset.png")

        self.res_ninja_image = pygame.transform.scale(self.ninja_image, (3 * self.ninja_image.get_width(), 3 * self.ninja_image.get_height()))
        self.res_monk_image = pygame.transform.scale(self.monk_image, (3 * self.monk_image.get_width(), 3 * self.monk_image.get_height()))
        self.res_lion_image = pygame.transform.scale(self.lion_image, (3 * self.lion_image.get_width(), 3 * self.lion_image.get_height()))
        self.res_vampire_image = pygame.transform.scale(self.vampire_image, (3 * self.vampire_image.get_width(), 3 * self.vampire_image.get_height()))


    def draw(self, screen):
        pygame.draw.rect(surface=screen, rect=self.ninja_rect, color="lightgray")
        pygame.draw.rect(surface=screen, rect=self.monk_rect, color="lightgray")
        pygame.draw.rect(surface=screen, rect=self.lion_rect, color="lightgray")
        pygame.draw.rect(surface=screen, rect=self.vampire_rect, color="lightgray")

        pygame.draw.rect(surface=screen, rect=self.ninja_image_rect, color="black")
        pygame.draw.rect(surface=screen, rect=self.monk_image_rect, color="black")
        pygame.draw.rect(surface=screen, rect=self.lion_image_rect, color="black")
        pygame.draw.rect(surface=screen, rect=self.vampire_image_rect, color="black")

        screen.blit(source=self.waffen_text, dest=self.waffen_text_rect)
        screen.blit(source=self.skins_text, dest=self.skins_text_rect)

        screen.blit(source=self.ninja_headline, dest=(self.x + 20 + self.hoehe_bild, self.y_start + 10))
        screen.blit(source=self.monk_headline, dest=(self.x + 20 + self.hoehe_bild, self.y_start + 10 + 1 * (self.hoehe + self.abstand)))
        screen.blit(source=self.lion_headline, dest=(self.x + 20 + self.hoehe_bild, self.y_start + 10 + 2 * (self.hoehe + self.abstand)))
        screen.blit(source=self.vampire_headline, dest=(self.x + 20 + self.hoehe_bild, self.y_start + 10 + 3 * (self.hoehe + self.abstand)))

        screen.blit(source=self.ninja_text, dest=(self.x + 20 + self.hoehe_bild, self.y_start + 50))
        screen.blit(source=self.monk_text, dest=(self.x + 20 + self.hoehe_bild, self.y_start + 50 + 1 * (self.hoehe + self.abstand)))
        screen.blit(source=self.lion_text, dest=(self.x + 20 + self.hoehe_bild, self.y_start + 50 + 2 * (self.hoehe + self.abstand)))
        screen.blit(source=self.vampire_text, dest=(self.x + 20 + self.hoehe_bild, self.y_start + 50 + 3 * (self.hoehe + self.abstand)))

        screen.blit(source=self.coins_text, dest=self.coin_int_rect)

        screen.blit(source=self.ninja_preis, dest=(self.x + 20 + self.hoehe_bild, self.y_start + 90))
        screen.blit(source=self.monk_preis, dest=(self.x + 20 + self.hoehe_bild, self.y_start + 90 + 1 * (self.hoehe + self.abstand)))
        screen.blit(source=self.lion_preis, dest=(self.x + 20 + self.hoehe_bild, self.y_start + 90 + 2 * (self.hoehe + self.abstand)))
        screen.blit(source=self.vampire_preis, dest=(self.x + 20 + self.hoehe_bild, self.y_start + 90 + 3 * (self.hoehe + self.abstand)))

        screen.blit(source=self.ninja_kaufen, dest=(self.x + 260 + self.hoehe_bild, self.y_start + 90))
        screen.blit(source=self.monk_kaufen, dest=(self.x + 260 + self.hoehe_bild, self.y_start + 90 + 1 * (self.hoehe + self.abstand)))
        screen.blit(source=self.lion_kaufen, dest=(self.x + 260 + self.hoehe_bild, self.y_start + 90 + 2 * (self.hoehe + self.abstand)))
        screen.blit(source=self.vampire_kaufen, dest=(self.x + 260 + self.hoehe_bild, self.y_start + 90 + 3 * (self.hoehe + self.abstand)))

        ninja_pos = self.res_ninja_image.get_rect(center=self.ninja_image_rect.center)
        monk_pos = self.res_monk_image.get_rect(center=self.monk_image_rect.center)
        lion_pos = self.res_lion_image.get_rect(center=self.lion_image_rect.center)
        vampire_pos = self.res_vampire_image.get_rect(center=self.vampire_image_rect.center)

        screen.blit(self.res_ninja_image, ninja_pos)
        screen.blit(self.res_monk_image, monk_pos)
        screen.blit(self.res_lion_image, lion_pos)
        screen.blit(self.res_vampire_image, vampire_pos)

    def handle_click(self, event, spielstand, coins):
        if self.waffen_text_rect.collidepoint(event.pos):
            return "waffen"

        elif self.skins_text_rect.collidepoint(event.pos):
            return "skins"

        elif self.ninja_kaufen_rect.collidepoint(event.pos) and spielstand[4]['Ninja']['Verfuegbarkeit'] == "True":
            if coins >= spielstand[4]['Ninja']['Coins']:
                coins -= spielstand[4]['Ninja']['Coins']
                spielstand[4]['Ninja']['Verfuegbarkeit'] = "False"
                muenzen_speichern("Coin_speicher.txt", coins)
                spielstand_speichern("speichern_spielstand.json", spielstand)
                self.ninja_kaufen = GV.FONT_MIDDLE.render("Im Besitz", False, "red2")
                self.ninja_kaufen_rect = self.ninja_kaufen.get_rect(topleft=(self.x + 260 + self.hoehe_bild, self.y_start + 90))

        elif self.monk_kaufen_rect.collidepoint(event.pos) and spielstand[5]['Monk']['Verfuegbarkeit'] == "True":
            if coins >= spielstand[5]['Monk']['Coins']:
                coins -= spielstand[5]['Monk']['Coins']
                spielstand[5]['Monk']['Verfuegbarkeit'] = "False"
                muenzen_speichern("Coin_speicher.txt", coins)
                spielstand_speichern("speichern_spielstand.json", spielstand)
                self.monk_kaufen = GV.FONT_MIDDLE.render("Im Besitz", False, "red2")
                self.monk_kaufen_rect = self.monk_kaufen.get_rect(topleft=(self.x + 260 + self.hoehe_bild, self.y_start + 90 + 1 * (self.hoehe + self.abstand)))

        elif self.lion_kaufen_rect.collidepoint(event.pos) and spielstand[6]['Lion']['Verfuegbarkeit'] == "True":
            if coins >= spielstand[6]['Lion']['Coins']:
                coins -= spielstand[6]['Lion']['Coins']
                spielstand[6]['Lion']['Verfuegbarkeit'] = "False"
                muenzen_speichern("Coin_speicher.txt", coins)
                spielstand_speichern("speichern_spielstand.json", spielstand)
                self.lion_kaufen = GV.FONT_MIDDLE.render("Im Besitz", False, "red2")
                self.lion_kaufen_rect = self.lion_kaufen.get_rect(topleft=(self.x + 260 + self.hoehe_bild, self.y_start + 90 + 2 * (self.hoehe + self.abstand)))

        elif self.vampire_kaufen_rect.collidepoint(event.pos) and spielstand[7]['Vampire'][
            'Verfuegbarkeit'] == "True":
            if coins >= spielstand[7]['Vampire']['Coins']:
                coins -= spielstand[7]['Vampire']['Coins']
                spielstand[7]['Vampire']['Verfuegbarkeit'] = "False"
                muenzen_speichern("Coin_speicher.txt", coins)
                spielstand_speichern("speichern_spielstand.json", spielstand)
                self.vampire_kaufen = GV.FONT_MIDDLE.render("Im Besitz", False, "red2")
                self.vampire_kaufen_rect = self.vampire_kaufen.get_rect(
                    topleft=(self.x + 260 + self.hoehe_bild, self.y_start + 90 + 3 * (self.hoehe + self.abstand))
                )

