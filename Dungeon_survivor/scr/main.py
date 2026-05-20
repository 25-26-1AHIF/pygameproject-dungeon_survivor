import pygame
from Game_Variables.Variables import GameVariables as GV
from Game_Variables.Variables import GameScreens
from Game_Variables.enemys import Enemy as en
from Game_Variables.player import Player as pl
from Game_Variables.schuss_elemente_player import Rockets

def main_screen(screen, clock):
    with open("Coin_speicher.txt", "r") as fp:
        inhalt = fp.read()
    Coin_inhalt = int(inhalt)

    font = pygame.font.SysFont(None, 45)
    rocket_list = Rockets(screen=screen)
    enemy = en(screen, rocket_list, Coin_inhalt)
    leben, welle, score_coin = enemy.get()

    pygame.display.set_caption("Dungeon Survivor - Main screen")
    background = pygame.image.load("assets/awesomeCavePixelArt.png")
    titel_text = GV.FONT_BIG.render("Dungeon Survivor", False, "darkred")
    starten_text = GV.FONT_MIDDLE.render("Spiel Starten", False, "yellow")
    inventar_text = GV.FONT_MIDDLE.render("Inventar", False, "gray")
    highscore_text = GV.FONT_MIDDLE.render("Highscores", False, "gray")
    beenden_text = GV.FONT_MIDDLE.render("Beenden", False, "red")
    coins_text = GV.FONT_MIDDLE.render("Coins:",True, "gray")
    shop_text = GV.FONT_MIDDLE.render("Shop", False, "gray")

    titel_text_rect = titel_text.get_rect(center=(GV.SCREEN_WIDTH / 2, 100))
    starten_text_rect = starten_text.get_rect(center=(GV.SCREEN_WIDTH / 2, 100 + 80))
    inventar_text_rect = inventar_text.get_rect(center=(GV.SCREEN_WIDTH / 2, 100 + 2* 80))
    highscore_text_rect = highscore_text.get_rect(center=(GV.SCREEN_WIDTH / 2, 100 + 3*80))
    beenden_text_rect = beenden_text.get_rect(center=(GV.SCREEN_WIDTH / 2, 100 + 5*80))
    coins_text_rect = coins_text.get_rect(center=(GV.SCREEN_WIDTH-150, 35))
    coin_int_rect = coins_text.get_rect(center=(GV.SCREEN_WIDTH - 20, 47))
    shop_text_rect = shop_text.get_rect(center=(GV.SCREEN_WIDTH / 2, 100 + 4 * 80))



    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameScreens.Exit

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return GameScreens.Exit
            if event.type == pygame.MOUSEBUTTONDOWN:
                if starten_text_rect.collidepoint(event.pos):
                    return GameScreens.PLAY
                if inventar_text_rect.collidepoint(event.pos):
                    return GameScreens.INVENTAR
                if highscore_text_rect.collidepoint(event.pos):
                    return GameScreens.HIGHSCORE
                if beenden_text_rect.collidepoint(event.pos):
                    return GameScreens.Exit
                if shop_text_rect.collidepoint(event.pos):
                    return GameScreens.SHOP


        screen.blit(background, (0, 0))

        pygame.draw.rect(surface=screen, rect=starten_text_rect, color="black")
        pygame.draw.rect(surface=screen, rect=inventar_text_rect, color="black")
        pygame.draw.rect(surface=screen, rect=highscore_text_rect, color="black")
        pygame.draw.rect(surface=screen, rect=beenden_text_rect, color="black")
        pygame.draw.rect(surface=screen, rect=coins_text_rect, color="black")
        pygame.draw.rect(surface=screen, rect=shop_text_rect, color="black")
        screen.blit(source=titel_text, dest=titel_text_rect)
        screen.blit(source=starten_text, dest=starten_text_rect)
        screen.blit(source=inventar_text, dest=inventar_text_rect)
        screen.blit(source=highscore_text, dest=highscore_text_rect)
        screen.blit(source=beenden_text, dest=beenden_text_rect)
        screen.blit(source=coins_text, dest=coins_text_rect)
        screen.blit(source=shop_text, dest=shop_text_rect)
        screen.blit(font.render(f"{score_coin}", True, (255, 255, 255)), coin_int_rect)
        leben, welle, score_coin = enemy.get()

        pygame.display.flip()
        clock.tick(GV.FPS)

def play_screen(screen, clock):

    with open("Coin_speicher.txt", "r") as fp:
        inhalt = fp.read()
    Coin_inhalt = int(inhalt)

    rocket_list = Rockets(screen=screen)
    enemy = en(screen, rocket_list, Coin_inhalt)
    player = pl(screen, rocket_list)
    leben, welle, score_coin = enemy.get()
    #KI-anfang
    #KI: ChatGPT
    #prompt: Wie bekomme ich den hintergrund in ein laufendes bild hinein
    background_play = pygame.image.load("assets/twosoulsnomark.png").convert()
    #KI-Ende
    background_play = pygame.transform.scale(background_play, (GV.SCREEN_WIDTH, GV.SCREEN_HEIGHT))

    font = pygame.font.SysFont(None, 45)

    Leben = GV.FONT_MIDDLE.render("Leben: ", True, "white")
    Welle = GV.FONT_MIDDLE.render("Welle: ", True, "white")
    Coin = GV.FONT_MIDDLE.render("Coins: ", True, "white")
    Leben_rect = Leben.get_rect(center=(GV.SCREEN_WIDTH/18, GV.SCREEN_HEIGHT/36))
    Welle_rect = Leben.get_rect(center=(GV.SCREEN_WIDTH-150, 20))
    Level_rect = Leben.get_rect(center=(GV.SCREEN_WIDTH/6, GV.SCREEN_HEIGHT/21))
    welle_int_rect = Leben.get_rect(center=(GV.SCREEN_WIDTH-20, 35))
    coin_int_rect = Leben.get_rect(center=(GV.SCREEN_WIDTH-20, 65))
    Coin_rect = Coin.get_rect(center=(GV.SCREEN_WIDTH-150, 50))




    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                leben_speichern, welle_speichern, score_coin_speichern = enemy.get()
                with open("Highscores.txx", "a") as fp:
                    fp.write(f"{leben_speichern, welle_speichern, score_coin_speichern}")
                return GameScreens.Exit

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    leben_speichern, welle_speichern, score_coin_speichern = enemy.get()
                    with open("Highscores.txx", "a") as fp:
                        fp.write(f"{leben_speichern, welle_speichern, score_coin_speichern}")
                    return GameScreens.PAUSE


        screen.blit(background_play,(0, 0))

        x_pos, y_pos = player.get_pos()
        enemy.update_and_draw(x_pos, y_pos)

        player.update_and_draw()
        rocket_list.update_and_draw()

        screen.blit(source=Leben, dest=Leben_rect)
        screen.blit(source=Welle, dest=Welle_rect)
        screen.blit(source=Coin, dest=Coin_rect)

        screen.blit(font.render(f"{leben:.0f}", True, (255, 255, 255)), Level_rect)
        screen.blit(font.render(f"{welle:.0f}", True, (255, 255, 255)), welle_int_rect)
        screen.blit(font.render(f"{score_coin}", True, (255, 255, 255)), coin_int_rect)


        leben, welle, score_coin = enemy.get()
        pygame.display.flip()
        clock.tick(GV.FPS)

def pause_screen(screen, clock):

    # 1. Fortsetzen
    # 2. Beenden
    fortsetzen_text = GV.FONT_MIDDLE.render("Fortsetzen", False, "green")
    beenden_text = GV.FONT_MIDDLE.render("Beenden", False, "darkred")
    fortsetzen_text_rect = fortsetzen_text.get_rect(center=(GV.SCREEN_WIDTH / 2, 100))
    beenden_text_rect = beenden_text.get_rect(center=(GV.SCREEN_WIDTH / 2, GV.SCREEN_HEIGHT - 100))

    pygame.draw.rect(surface=screen, rect=fortsetzen_text_rect, color="black")
    pygame.draw.rect(surface=screen, rect=beenden_text_rect, color="black")

    pygame.display.flip()
    clock.tick(GV.FPS)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameScreens.Exit

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return GameScreens.PLAY

            if event.type == pygame.MOUSEBUTTONDOWN:
                if fortsetzen_text_rect.collidepoint(event.pos):
                    return GameScreens.PLAY
                elif beenden_text_rect.collidepoint(event.pos):
                    return GameScreens.MAIN

        screen.blit(source=fortsetzen_text, dest=fortsetzen_text_rect)
        screen.blit(source=beenden_text, dest=beenden_text_rect)


        pygame.display.flip()
        clock.tick(GV.FPS)


def inventar_screen(screen, clock):
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

def highscore_screen(screen, clock):
    background = pygame.image.load("assets/Image.png")
    background = pygame.transform.scale(background, (GV.SCREEN_WIDTH, GV.SCREEN_HEIGHT))

    Highscore_text = GV.FONT_BIG.render("Highscores:", False, "gray")
    Highscore_text_rect = Highscore_text.get_rect(center=(GV.SCREEN_WIDTH / 4, 50 ))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameScreens.Exit

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return GameScreens.MAIN

        screen.blit(background, (0, 0))

        pygame.draw.rect(surface=screen, rect=Highscore_text_rect, color="black")
        screen.blit(source=Highscore_text, dest=Highscore_text_rect)

        pygame.display.flip()
        clock.tick(GV.FPS)

def shop_screen(screen, clock):
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


    while True:

        if GameScreens.actual == GameScreens.MAIN:
            GameScreens.actual = main_screen(screen, clock)

        elif GameScreens.actual == GameScreens.PLAY:
            GameScreens.actual = play_screen(screen, clock)

        elif GameScreens.actual == GameScreens.GAMEOVER:
            GameScreens.actual = Gameover(screen, clock)

        elif GameScreens.actual == GameScreens.Exit:
            break

        elif GameScreens.actual == GameScreens.INVENTAR:
            GameScreens.actual = inventar_screen(screen, clock)

        elif GameScreens.actual == GameScreens.HIGHSCORE:
            GameScreens.actual = highscore_screen(screen, clock)

        elif GameScreens.actual == GameScreens.SHOP:
            GameScreens.actual = shop_screen(screen, clock)

        elif GameScreens.actual == GameScreens.PAUSE:
            GameScreens.actual = pause_screen(screen, clock)

    pygame.quit()

if __name__ == "__main__":
    main()