import pygame
import json
from .Variables import GameVariables as GV
from .Variables import GameScreens


class HighscoreScreen:

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.highscores = self.load_highscores()

        self.box_rect = pygame.Rect(300, 130, 520, 430)

        self.platz_x = 350
        self.name_x = 460
        self.welle_x = 650
        self.coins_x = 760

        self.kopf_y = 170
        self.start_y = 215
        self.zeilen_abstand = 38

        self.background = pygame.image.load("assets/HR_CastleOnTheMountains-Valrok.png")

    def load_highscores(self):
        try:
            with open("highscores.json", "r") as fp:
                highscores = json.load(fp)
        #KI-Anfang
        #KI: ChatGPT
        #prompt: warum funktioniert mein laden vom highscore nicht:
        except:
            highscores = []
        # KI-Ende

        #KI-Anfang
        #KI: ChatGPT
        #prompt: ich kann nur bubble sort und das ist nicht so gut zum sortieren kannst du es mir sinnvoll machen
        highscores.sort(key=lambda eintrag: int(eintrag["Coins"]), reverse=True)
        return highscores[:10]
        #KI-Ende

    def handle_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return GameScreens.Exit

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return GameScreens.MAIN
        #KI-Anfang
        #KI:ChatGPT
        #prompt: Warum stürzt dieser Code ab:
        return None
        #KI-Ende

    def draw_background(self):
        self.background = pygame.transform.scale(self.background, (GV.SCREEN_WIDTH, GV.SCREEN_HEIGHT))
        self.screen.blit(self.background, (0,0))

        titel = GV.FONT_BIG.render("Highscores", False, "gold")
        titel_rect = titel.get_rect(center=(GV.SCREEN_WIDTH / 2, 50))
        self.screen.blit(titel, titel_rect)

    def draw_highscores(self):
        platz_text = GV.FONT_SMALL.render("Platz", False, "white")
        name_text = GV.FONT_SMALL.render("Name", False, "white")
        welle_text = GV.FONT_SMALL.render("Welle", False, "white")
        coins_text = GV.FONT_SMALL.render("Coins", False, "gold2")

        self.screen.blit(platz_text, (self.platz_x, self.kopf_y))
        self.screen.blit(name_text, (self.name_x, self.kopf_y))
        self.screen.blit(welle_text, (self.welle_x, self.kopf_y))
        self.screen.blit(coins_text, (self.coins_x, self.kopf_y))

        for index, eintrag in enumerate(self.highscores):
            y = self.start_y + index * self.zeilen_abstand

            if index == 0:
                #KI-Anfang
                #KI: ChatGPT
                #prompt: was für pygame farben soll ich für platz 1 2 3 machen
                platz = GV.FONT_SMALL.render(f"{index + 1}.", False, "gold1")
                #KI-Ende
                name = GV.FONT_SMALL.render(eintrag["Name"], False, "white")
                welle = GV.FONT_SMALL.render(str(eintrag["Welle"]), False, "white")
                coins = GV.FONT_SMALL.render(str(eintrag["Coins"]), False, "gold")

            elif index == 1:
                #KI-Anfang
                #KI: ChatGPT
                #prompt: was für pygame farben soll ich für platz 1 2 3 machen
                platz = GV.FONT_SMALL.render(f"{index + 1}.", False, "gray80")
                #KI-Ende
                name = GV.FONT_SMALL.render(eintrag["Name"], False, "white")
                welle = GV.FONT_SMALL.render(str(eintrag["Welle"]), False, "white")
                coins = GV.FONT_SMALL.render(str(eintrag["Coins"]), False, "gold")

            elif index == 2:
                #KI-Anfang
                #KI: ChatGPT
                #prompt: was für pygame farben soll ich für platz 1 2 3 machen
                platz = GV.FONT_SMALL.render(f"{index + 1}.", False, "chocolate2")
                #KI-Ende
                name = GV.FONT_SMALL.render(eintrag["Name"], False, "white")
                welle = GV.FONT_SMALL.render(str(eintrag["Welle"]), False, "white")
                coins = GV.FONT_SMALL.render(str(eintrag["Coins"]), False, "gold")

            else:
                platz = GV.FONT_SMALL.render(f"{index + 1}.", False, "white")
                name = GV.FONT_SMALL.render(eintrag["Name"], False, "white")
                welle = GV.FONT_SMALL.render(str(eintrag["Welle"]), False, "white")
                coins = GV.FONT_SMALL.render(str(eintrag["Coins"]), False, "gold")

            self.screen.blit(platz, (self.platz_x, y))
            self.screen.blit(name, (self.name_x, y))
            self.screen.blit(welle, (self.welle_x, y))
            self.screen.blit(coins, (self.coins_x, y))

    def draw(self):
        self.draw_background()
        pygame.draw.rect(self.screen,"gray20",(250, 120, 650, 420))
        self.draw_highscores()

        pygame.display.flip()

    def run(self):
        self.highscores = self.load_highscores()

        while True:
            neuer_screen = self.handle_events()

            if neuer_screen is not None:
                return neuer_screen

            self.draw()
            self.clock.tick(GV.FPS)