import pygame
class GameVariables:
    SCREEN_WIDTH = 1080
    SCREEN_HEIGHT = 720
    SQUARE_SIZE = 32
    FPS = 60
    MISSILE_SIZE = 16

    FONT_BIG: pygame.font.Font = None
    FONT_MIDDLE: pygame.font.Font= None
    FONT_SMALL: pygame.font.Font = None

    @staticmethod
    def init():
        pygame.init()
        GameVariables.FONT_BIG = pygame.sysfont.SysFont("arial", 48, bold=True)
        GameVariables.FONT_MIDDLE = pygame.sysfont.SysFont("arial", 30, bold=False)
        GameVariables.FONT_SMALL = pygame.sysfont.SysFont("arial", 14, bold=False)


class GameScreens:
    MAIN = "mainscreen"
    PLAY = "playscreen"
    Exit = "exit"
    GAMEOVER = "Gameover"
    actual= MAIN
