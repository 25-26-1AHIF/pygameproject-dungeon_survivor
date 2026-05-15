import pygame
from Game_Variables.Variables import GameVariables as GV
from Game_Variables.Variables import GameScreens
from Game_Variables.enemys import Enemy as en
from Game_Variables.player import Player as pl
from Game_Variables.schuss_elemente_player import Rockets

def main_screen(screen, clock):



    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameScreens.Exit

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return GameScreens.MAIN

        screen.fill("black")
        pygame.display.flip()
        clock.tick(GV.FPS)

def play_screen(screen, clock):

    rocket_list = Rockets(screen=screen)
    enemy = en(screen, rocket_list)
    player = pl(screen, rocket_list)
    leben, welle = enemy.get()

    font = pygame.font.SysFont(None, 40)

    Leben = GV.FONT_MIDDLE.render("Leben: ", True, "white")
    Welle = GV.FONT_MIDDLE.render("Welle: ", True, "white")
    Leben_rect = Leben.get_rect(center=(50, 20))
    Welle_rect = Leben.get_rect(center=(GV.SCREEN_WIDTH-70, 20))
    Level_rect = Leben.get_rect(center=(140, 27))
    welle_int_rect = Leben.get_rect(center=(GV.SCREEN_WIDTH, 27))


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameScreens.Exit

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return GameScreens.MAIN

        screen.fill("black")

        x_pos, y_pos = player.get_pos()
        enemy.update_and_draw(x_pos, y_pos)
        player.update_and_draw()
        rocket_list.update_and_draw()

        screen.blit(source=Leben, dest=Leben_rect)
        screen.blit(source=Welle, dest=Welle_rect)

        screen.blit(font.render(f"{leben:.0f}", True, (255, 255, 255)), Level_rect)
        screen.blit(font.render(f"{welle:.0f}", True, (255, 255, 255)), welle_int_rect)


        leben, welle = enemy.get()
        pygame.display.flip()
        clock.tick(GV.FPS)


def Gameover(screen, clock):

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameScreens.Exit

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return GameScreens.MAIN

        screen.fill("black")
        pygame.display.flip()
        clock.tick(GV.FPS)


def main():
    GV.init()
    screen = pygame.display.set_mode((GV.SCREEN_WIDTH, GV.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    play_screen(screen, clock)    #hier muss dann am schluss main hin

    while True:

        if GameScreens.actual == GameScreens.MAIN:
            GameScreens.actual = main_screen(screen, clock)

        elif GameScreens.actual == GameScreens.PLAY:
            GameScreens.actual = play_screen(screen, clock)

        elif GameScreens.actual == GameScreens.GAMEOVER:
            GameScreens.actual = Gameover(screen, clock)

        elif GameScreens.actual == GameScreens.Exit:
            break

    pygame.quit()

if __name__ == "__main__":
    main()