import pygame
class GameVariables:
    SCREEN_WIDTH = 1080
    SCREEN_HEIGHT = 720
    SQUARE_SIZE = 32
    FPS = 144
    MISSILE_SIZE = 16
    BUTTON_WIDTH = 300
    BUTTON_HEIGHT = 60

    FONT_BIG: pygame.font.Font = None
    FONT_MIDDLE: pygame.font.Font= None
    FONT_SMALL: pygame.font.Font = None

    @staticmethod
    def init():
        pygame.init()
        # KI-Anfang
        # KI: ChatGPT
        # prompt: Was soll ich in Python für eine Schriftart für ein Pixelspiel nehmen für große mittle und kleine Schrift
        GameVariables.FONT_BIG = (pygame.font.Font("assets/Ninja Adventure - Asset Pack/Ui/Font/NormalFont.ttf", 48))
        GameVariables.FONT_MIDDLE = pygame.font.Font("assets/Ninja Adventure - Asset Pack/Ui/Font/NormalFont.ttf", 32)
        GameVariables.FONT_SMALL = pygame.font.Font("assets/Ninja Adventure - Asset Pack/Ui/Font/NormalFont.ttf", 16)
        # KI-Ende


class GameScreens:
    MAIN = "mainscreen"
    PLAY = "playscreen"
    INVENTAR = "inventarscreen"
    HIGHSCORE = "highscorescreen"
    SHOP = "shop"

    Exit = "exit"
    GAMEOVER = "Gameover"
    actual = MAIN
