from xml.etree.ElementTree import indent

import pygame
import json
from Game_Variables.Variables import GameVariables as GV
from Game_Variables.Variables import GameScreens
from Game_Variables.enemys import Enemy as en
from Game_Variables.player import Player as pl
from Game_Variables.schuss_elemente_player import Rockets

from Game_Variables.shop_screen import SkinShop, WaffenShop
from Game_Variables.Highscore_speichern import  Highscores
from Game_Variables.highscore_screen import HighscoreScreen

def main_screen(screen, clock):
    coin_score = 0
    font = pygame.font.SysFont(None, 45)
    rocket_list = Rockets(screen=screen)
    with open("Coin_speicher.txt", "r") as fp:
        inhalt = fp.read()
    if len(inhalt) == 0:
        pass
    else:
        coin_score = int(inhalt)
    enemy = en(screen, rocket_list, coin_score)
    leben, welle, score_coin, coin_gesammelt, player_death = enemy.get_informationen()

    pygame.display.set_caption("Dungeon Survivor - Main screen")
    background = pygame.image.load("assets/HR_Fantasy_Landscape.png")
    resized_background = pygame.transform.scale(background, (GV.SCREEN_WIDTH, GV.SCREEN_HEIGHT))
    titel_text = GV.FONT_BIG.render("Dungeon Survivor", False, "darkred")
    starten_text = GV.FONT_MIDDLE.render("Spiel Starten", False, "gold")
    inventar_text = GV.FONT_MIDDLE.render("Inventar", False, "gray")
    highscore_text = GV.FONT_MIDDLE.render("Highscores", False, "gray")
    beenden_text = GV.FONT_MIDDLE.render("Beenden", False, "red")
    coins_text = GV.FONT_MIDDLE.render(f"Coins: {score_coin}",True, "gold1")
    shop_text = GV.FONT_MIDDLE.render("Shop", False, "gray")

    titel_text_rect = titel_text.get_rect(center=(GV.SCREEN_WIDTH / 2, 100))
    starten_text_rect = starten_text.get_rect(center=(GV.SCREEN_WIDTH / 2, 100 + 80))
    inventar_text_rect = inventar_text.get_rect(center=(GV.SCREEN_WIDTH / 2, 100 + 2* 80))
    highscore_text_rect = highscore_text.get_rect(center=(GV.SCREEN_WIDTH / 2, 100 + 3*80))
    beenden_text_rect = beenden_text.get_rect(center=(GV.SCREEN_WIDTH / 2, 100 + 5*80))
    coins_text_rect = coins_text.get_rect(center=(GV.SCREEN_WIDTH-150, 35))
    coin_int_rect = coins_text.get_rect(center=(GV.SCREEN_WIDTH - 20, 47))
    shop_text_rect = shop_text.get_rect(center=(GV.SCREEN_WIDTH / 2, 100 + 4 * 80))

    image = pygame.image.load("assets/Ninja Adventure - Asset Pack/Ui/Theme/Wip/ThemeDark/nine_path_panel.png").convert_alpha()
    # KI-Anfang
    # KI: ChatGPT
    # prompt: Wie kann ich von diesem rechteck     starten_text_rect = starten_text.get_rect(center=(GV.SCREEN_WIDTH / 2, 100 + 80)) den länge und die breite bekommen
    res_image = pygame.transform.scale(image, (starten_text_rect.width, starten_text_rect.height))
    # KI-Ende


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


        screen.blit(resized_background, (0, 0))
        #screen.blit(res_image , starten_text_rect)

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
        #screen.blit(font.render(f"{score_coin}", True, (0, 0, 0)), coin_int_rect)
        leben, welle, score_coin, coin_gesammelt, player_death = enemy.get_informationen()
        pygame.display.flip()
        clock.tick(GV.FPS)

def play_screen(screen, clock):
    pygame.display.set_caption("Dungeon Survivor - Game")
    coin_score = 0
    rocket_list = Rockets(screen=screen)
    with open("Coin_speicher.txt", "r") as fp:
        inhalt = fp.read()
    if len(inhalt) == 0:
        pass
    else:
        coin_score = int(inhalt)
    enemy = en(screen, rocket_list, coin_score)
    leben, welle, score_coin, coin_gesammelt, player_death = enemy.get_informationen()
    coin_list = enemy.get_coin_list()
    player = pl(screen, rocket_list, enemy, coin_list)
    #KI-anfang
    #KI: ChatGPT
    #prompt: Wie bekomme ich den hintergrund in ein laufendes bild hinein
    background_play = pygame.image.load("assets/twosoulsnomark.png").convert()
    #KI-Ende
    background_play = pygame.transform.scale(background_play, (GV.SCREEN_WIDTH, GV.SCREEN_HEIGHT))

    font = pygame.font.SysFont(None, 45)

    Leben = GV.FONT_MIDDLE.render(f"Leben: {leben:.0f}", True, "red3")
    Welle = GV.FONT_MIDDLE.render(f"Welle: {welle:.0f}", True, "white")
    Coin = GV.FONT_MIDDLE.render(f"Coins: {coin_gesammelt}", True, "gold1")
    Leben_rect = Leben.get_rect(topleft=(10, 10))
    Welle_rect = Welle.get_rect(topright=(GV.SCREEN_WIDTH - 70, 10))
    Coin_rect = Coin.get_rect(topright=(GV.SCREEN_WIDTH - 70, 50))
    welle_int_rect = Leben.get_rect(center=(GV.SCREEN_WIDTH-20, 35))
    coin_int_rect = Leben.get_rect(center=(GV.SCREEN_WIDTH-20, 65))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameScreens.Exit

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    next = pause_screen(screen, clock)

                    if next == "beenden":
                        return GameScreens.MAIN
                elif player_death == 1:
                    with open("last_coins.txt", "w") as fp:
                        json.dump({
                            "Coins": coin_gesammelt,
                            "Welle": welle
                        }, fp, indent=4)
                    return GameScreens.GAMEOVER

            player.update_and_shoot(event)


        screen.blit(background_play,(0, 0))
        player.update_and_draw()
        x_pos, y_pos = player.get_pos()
        enemy.update_and_draw(x_pos, y_pos)


        rocket_list.update_and_draw()

        Leben = GV.FONT_MIDDLE.render(f"Leben: {leben:.0f}", True, "red3")
        Welle = GV.FONT_MIDDLE.render(f"Welle: {welle:.0f}", True, "white")
        Coin = GV.FONT_MIDDLE.render(f"Coins: {coin_gesammelt}", True, "gold1")

        screen.blit(source=Leben, dest=Leben_rect)
        screen.blit(source=Welle, dest=Welle_rect)
        screen.blit(source=Coin, dest=Coin_rect)

        #screen.blit(font.render(f"{leben:.0f}", True, (255, 255, 255)), Level_rect)
        #screen.blit(font.render(f"{welle:.0f}", True, (255, 255, 255)), welle_int_rect)
        #screen.blit(font.render(f"{coin_gesammelt}", True, (255, 255, 255)), coin_int_rect)

        leben, welle, score_coin, coin_gesammelt, player_death = enemy.get_informationen()
        pygame.display.flip()
        clock.tick(GV.FPS)

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

def pause_screen(screen, clock):
    pygame.display.set_caption("Dungeon Survivor - Pausiert")
    # 1. Fortsetzen
    # 2. Beenden
    fortsetzen_text = GV.FONT_MIDDLE.render("Fortsetzen", False, "green")
    beenden_text = GV.FONT_MIDDLE.render("Beenden", False, "darkred")
    fortsetzen_text_rect = fortsetzen_text.get_rect(center=(GV.SCREEN_WIDTH / 2, 100))
    beenden_text_rect = beenden_text.get_rect(center=(GV.SCREEN_WIDTH / 2, GV.SCREEN_HEIGHT - 100))
    leertaste_text = GV.FONT_SMALL.render("leertaste", False, "white")
    leertaste_text_rect = leertaste_text.get_rect(center=(GV.SCREEN_WIDTH / 2, 70))
    esc_text = GV.FONT_SMALL.render("ESC", False, "white")
    esc_text_rect = esc_text.get_rect(center=(GV.SCREEN_WIDTH / 2, GV.SCREEN_HEIGHT- 130))


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameScreens.Exit

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return GameScreens.PLAY
                elif event.key == pygame.K_ESCAPE:
                    return "beenden"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if fortsetzen_text_rect.collidepoint(event.pos):
                    return GameScreens.PLAY
                elif beenden_text_rect.collidepoint(event.pos):
                    return GameScreens.MAIN

        pygame.draw.rect(surface=screen, rect=fortsetzen_text_rect, color="black")
        pygame.draw.rect(surface=screen, rect=beenden_text_rect, color="black")
        pygame.draw.rect(surface=screen, rect=leertaste_text_rect, color="black")
        pygame.draw.rect(surface=screen, rect=esc_text_rect, color="black")


        screen.blit(source=fortsetzen_text, dest=fortsetzen_text_rect)
        screen.blit(source=beenden_text, dest=beenden_text_rect)
        screen.blit(source=leertaste_text, dest=leertaste_text_rect)
        screen.blit(source=esc_text, dest=esc_text_rect)

        pygame.display.flip()
        clock.tick(GV.FPS)


def shop_screen(screen, clock):
    pygame.display.set_caption("Dungeon Survivor - Shop")
    background = pygame.image.load("assets/StockCake-Gemütliche_Pixel-Taverne-3432555-medium.png")
    resized_background = pygame.transform.scale(background, (GV.SCREEN_WIDTH, GV.SCREEN_HEIGHT))

    spielstand = spielstand_auslesen("speichern_spielstand.json")
    with open("Coin_speicher.txt", "r") as fp:
        coins = int(fp.read())


    waffenshop = WaffenShop(60, 10, 4)
    skinshop = SkinShop(60, 10, 4)
    waffenshop.update(spielstand, coins)
    skinshop.update(spielstand, coins)

    tab = "waffen"

    while True:

        for event in pygame.event.get():
            if tab == "waffen":
                waffenshop.update(spielstand, coins)


            else:
                skinshop.update(spielstand, coins)
            if event.type == pygame.QUIT:
                return GameScreens.Exit

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return GameScreens.MAIN

            if event.type == pygame.MOUSEBUTTONDOWN and tab == "waffen":
                #KI-Anfang
                #KI: ChatGPT
                #promp: Warum funktioniert das und das bei waffenshop nicht: skinshop.handle_click(event, spielstand, coins)
                neuer_tab = waffenshop.handle_click(event, spielstand, coins)

                if neuer_tab:
                    tab = neuer_tab
            elif event.type == pygame.MOUSEBUTTONDOWN and tab == "skins":
                #KI-Anfang
                #KI: ChatGPT
                #promp: Warum funktioniert das und das bei waffenshop nicht: skinshop.handle_click(event, spielstand, coins)
                neuer_tab = skinshop.handle_click(event, spielstand, coins)

                if neuer_tab:
                    tab = neuer_tab
        screen.blit(resized_background, (0, 0))


        if tab == "waffen":
            waffenshop.draw(screen)

        else:
            skinshop.draw(screen)

        pygame.display.flip()
        clock.tick(GV.FPS)


def highscore_screen(screen, clock):
    highscore = HighscoreScreen(screen, clock)
    return highscore.run()

def inventar_screen(screen, clock):
    pygame.display.set_caption("Dungeon Survivor - Inventar")
    with open("speichern_spielstand.json", "r") as fp:
        inhalt = json.load(fp)

    background = pygame.image.load("assets/redcometnomark.png")
    Skin_text = GV.FONT_BIG.render("Waffe", False, "yellow")
    Waffe_text = GV.FONT_BIG.render("Skin ", False, "yellow")

    coin_score = 0
    rocket_list = Rockets(screen=screen)
    with open("Coin_speicher.txt", "r") as fp:
        inhalt_coin = fp.read()
    if len(inhalt_coin) == 0:
        pass
    else:
        coin_score = int(inhalt_coin)
    enemy = en(screen, rocket_list, coin_score)
    leben, welle, score_coin, coin_gesammelt, player_death = enemy.get_informationen()

    upgrade_text_Bogen = None
    upgrade_text_Bogen_blau = None
    Lvl_text_rect_Bogen = None
    upgrade_text_rect_Bogen = None

    upgrade_text_Armbrust = None
    upgrade_text_Armbrust_blau = None
    Lvl_text_rect_Armbrust = None
    upgrade_text_rect_Armbrust = None

    if inhalt[0]['Schwert']['Verfuegbarkeit'] == "False":
        #upgrade_text_Schwert = GV.FONT_SMALL.render(f"Lvl: {inhalt[0]['Schwert']['upgrade']}", True, "black")
        #upgrade_text_Schwert_blau = GV.FONT_SMALL.render(f"Upgrade {inhalt[0]['Schwert']['upgrade_kosten']}", True,
                           #"blue")
        #Lvl_text_rect_Schwert = upgrade_text_Schwert.get_rect(topleft=(GV.SCREEN_WIDTH - GV.SCREEN_WIDTH / 3 + 40, 260))
        #upgrade_text_rect_Schwert = upgrade_text_Schwert_blau.get_rect(
            #topleft=(GV.SCREEN_WIDTH - GV.SCREEN_WIDTH / 4 + 40, 260))

        if inhalt[0]['Schwert']['ausgewaehlt'] == "Ja":
            schwert_ausrüsten_text = GV.FONT_MIDDLE.render("Augesrüstet", False, "green")
        else:
            schwert_ausrüsten_text = GV.FONT_MIDDLE.render("Ausrüsten", False, "black")
    else:
        schwert_ausrüsten_text = GV.FONT_SMALL.render("Nicht Verfügbar", False, "red")
    if inhalt[1]['Axt']['Verfuegbarkeit'] == "False":
        #upgrade_text_Axt = GV.FONT_SMALL.render(f"Lvl: {inhalt[1]['Axt']['upgrade']}", True, "black")
        #upgrade_text_Axt_blau = GV.FONT_SMALL.render(f"Upgrade {inhalt[1]['Axt']['upgrade_kosten']}", True, "blue")
        #Lvl_text_rect_Axt = upgrade_text_Axt.get_rect(topleft=(GV.SCREEN_WIDTH - GV.SCREEN_WIDTH / 3 + 40, 370))
        #upgrade_text_rect_Axt = upgrade_text_Axt_blau.get_rect(
            #topleft=(GV.SCREEN_WIDTH - GV.SCREEN_WIDTH / 4 + 40, 370))

        if inhalt[1]['Axt']['ausgewaehlt'] == "Ja":
            axt_ausrüsten_text = GV.FONT_MIDDLE.render("Ausgerüstet", False, "green")
        else:
            axt_ausrüsten_text = GV.FONT_MIDDLE.render("Ausrüsten", False, "black")
    else:
        axt_ausrüsten_text = GV.FONT_SMALL.render("Nicht Verfügbar", False, "red")
    if inhalt[2]['Bogen']['Verfuegbarkeit'] == "False":
        upgrade_text_Bogen = GV.FONT_SMALL.render(f"Lvl: {inhalt[2]['Bogen']['upgrade']}", True, "black")
        upgrade_text_Bogen_blau = GV.FONT_SMALL.render(f"Upgrade {inhalt[2]['Bogen']['upgrade_kosten']}", True, "blue")
        Lvl_text_rect_Bogen = upgrade_text_Bogen.get_rect(topleft=(GV.SCREEN_WIDTH - GV.SCREEN_WIDTH / 3 + 40, 480))
        upgrade_text_rect_Bogen = upgrade_text_Bogen_blau.get_rect(
            topleft=(GV.SCREEN_WIDTH - GV.SCREEN_WIDTH / 4 + 40, 480))

        if inhalt[2]['Bogen']['ausgewaehlt'] == "Ja":
            Bogen_ausrüsten_text = GV.FONT_MIDDLE.render("Ausgerüstet", False, "green")
        else:
            Bogen_ausrüsten_text = GV.FONT_MIDDLE.render("Ausrüsten", False, "black")
    else:
        Bogen_ausrüsten_text = GV.FONT_SMALL.render("Nicht Verfügbar", False, "red")
    if inhalt[3]['Armbrust']['Verfuegbarkeit'] == "False":
        upgrade_text_Armbrust = GV.FONT_SMALL.render(f"Lvl: {inhalt[3]['Armbrust']['upgrade']}", True, "black")
        upgrade_text_Armbrust_blau = GV.FONT_SMALL.render(f"Upgrade {inhalt[3]['Armbrust']['upgrade_kosten']}", True,
                                                          "blue")
        Lvl_text_rect_Armbrust = upgrade_text_Armbrust.get_rect(
            topleft=(GV.SCREEN_WIDTH - GV.SCREEN_WIDTH / 3 + 40, 590))
        upgrade_text_rect_Armbrust = upgrade_text_Armbrust_blau.get_rect(
            topleft=(GV.SCREEN_WIDTH - GV.SCREEN_WIDTH / 4 + 40, 590))

        if inhalt[3]['Armbrust']['ausgewaehlt'] == "Ja":
            Armbrust_ausrüsten_text = GV.FONT_MIDDLE.render("Ausgerüstet", False, "green")
        else:
            Armbrust_ausrüsten_text = GV.FONT_MIDDLE.render("Ausrüsten", False, "black")
    else:
        Armbrust_ausrüsten_text = GV.FONT_SMALL.render("Nicht Verfügbar", False, "red")

    margin = 60
    abstand = 10
    anzahl = 4

    bogen_upgrade_text_rect = None
    armbrust_upgrade_text_rect = None

    coin_text = GV.FONT_MIDDLE.render(f"Coin: {coin_score}", True, "gold1")

    hoehe = (GV.SCREEN_HEIGHT - 2 * margin - (anzahl - 1) * abstand) / anzahl
    hoehe_bild = hoehe - 4 * abstand

    skins_text_rect = Skin_text.get_rect(topleft=(GV.SCREEN_WIDTH - GV.SCREEN_WIDTH / 4, 50))
    waffen_text_rect = Waffe_text.get_rect(topleft=(GV.SCREEN_WIDTH - GV.SCREEN_WIDTH / 1.2, 50))


    schwert_ausrüsten_text_rect = schwert_ausrüsten_text.get_rect(topleft=(GV.SCREEN_WIDTH-GV.SCREEN_WIDTH/3+50, 200))
    axt_ausrüsten_text_rect = axt_ausrüsten_text.get_rect(topleft=(GV.SCREEN_WIDTH-GV.SCREEN_WIDTH/3+50, 320))
    Bogen_ausrüsten_text_rect = Bogen_ausrüsten_text.get_rect(topleft=(GV.SCREEN_WIDTH-GV.SCREEN_WIDTH/3+50, 420))
    Armbrust_ausrüsten_text_rect = Armbrust_ausrüsten_text.get_rect(topleft=(GV.SCREEN_WIDTH-GV.SCREEN_WIDTH/3+50, 530))

    if inhalt[2]['Bogen']['Verfuegbarkeit'] == "False":
        bogen_upgrade_text_rect = upgrade_text_Bogen.get_rect(topleft=(GV.SCREEN_WIDTH - GV.SCREEN_WIDTH / 4 + 60, 480))
    if inhalt[3]['Armbrust']['Verfuegbarkeit'] == "False":
        armbrust_upgrade_text_rect = upgrade_text_Armbrust.get_rect(topleft=(GV.SCREEN_WIDTH - GV.SCREEN_WIDTH / 4 + 60, 590))
    coin_text_rect = coin_text.get_rect(center=(GV.SCREEN_WIDTH-150, 30))

    schwert_image = pygame.image.load("assets/Ninja Adventure - Asset Pack/Items/Weapons/Sword2/Sprite.png")
    axt_image = pygame.image.load("assets/Ninja Adventure - Asset Pack/Items/Weapons/AxeTool/Sprite.png")
    bogen_image = pygame.image.load("assets/Ninja Adventure - Asset Pack/Items/Weapons/Bow2/Sprite.png")
    armbrust_image = pygame.image.load("assets/Ninja Adventure - Asset Pack/Items/Weapons/Crossbow/Sprite.png")



    schwert_image_rect = pygame.Rect(GV.SCREEN_WIDTH-GV.SCREEN_WIDTH/2.5-10, 200-10, hoehe_bild, hoehe_bild)
    axt_image_rect = pygame.Rect(GV.SCREEN_WIDTH-GV.SCREEN_WIDTH/2.5, 305, hoehe_bild, hoehe_bild)
    bogen_image_rect = pygame.Rect(GV.SCREEN_WIDTH-GV.SCREEN_WIDTH/2.5, 425, hoehe_bild, hoehe_bild)
    armbrust_image_rect = pygame.Rect(GV.SCREEN_WIDTH-GV.SCREEN_WIDTH/2.5, 535, hoehe_bild, hoehe_bild)


    res_schwert_image = pygame.transform.scale(schwert_image,
                                               (6 * schwert_image.get_width(), 6 * schwert_image.get_height()))
    res_axt_image = pygame.transform.scale(axt_image, (6 * axt_image.get_width(), 6 * axt_image.get_height()))
    res_bogen_image = pygame.transform.scale(bogen_image, (6 * bogen_image.get_width(), 6 * bogen_image.get_height()))
    res_armbrust_image = pygame.transform.scale(armbrust_image,
                                                (6 * armbrust_image.get_width(), 6 * armbrust_image.get_height()))





    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return GameScreens.Exit

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return GameScreens.MAIN

            if event.type == pygame.MOUSEBUTTONDOWN:


                if schwert_ausrüsten_text_rect.collidepoint(event.pos):
                    if inhalt[0]['Schwert']['Verfuegbarkeit'] == "False":
                        inhalt[0]['Schwert']['ausgewaehlt'] = "Ja"
                        GV.actual_WAEPON = 0
                        inhalt[1]['Axt']['ausgewaehlt'] = "Nein"
                        inhalt[2]['Bogen']['ausgewaehlt'] = "Nein"
                        inhalt[3]['Armbrust']['ausgewaehlt'] = "Nein"

                if axt_ausrüsten_text_rect.collidepoint(event.pos):
                    if inhalt[1]['Axt']['Verfuegbarkeit'] == "False":
                        inhalt[1]['Axt']['ausgewaehlt'] = "Ja"
                        GV.actual_WAEPON = 1
                        inhalt[0]['Schwert']['ausgewaehlt'] = "Nein"
                        inhalt[2]['Bogen']['ausgewaehlt'] = "Nein"
                        inhalt[3]['Armbrust']['ausgewaehlt'] = "Nein"

                if Bogen_ausrüsten_text_rect.collidepoint(event.pos):
                    if inhalt[2]['Bogen']['Verfuegbarkeit'] == "False":
                        inhalt[2]['Bogen']['ausgewaehlt'] = "Ja"
                        GV.actual_WAEPON = 2
                        inhalt[0]['Schwert']['ausgewaehlt'] = "Nein"
                        inhalt[1]['Axt']['ausgewaehlt'] = "Nein"
                        inhalt[3]['Armbrust']['ausgewaehlt'] = "Nein"

                if Armbrust_ausrüsten_text_rect.collidepoint(event.pos):
                    if inhalt[3]['Armbrust']['Verfuegbarkeit'] == "False":
                        inhalt[3]['Armbrust']['ausgewaehlt'] = "Ja"
                        GV.actual_WAEPON = 3
                        inhalt[0]['Schwert']['ausgewaehlt'] = "Nein"
                        inhalt[1]['Axt']['ausgewaehlt'] = "Nein"
                        inhalt[2]['Bogen']['ausgewaehlt'] = "Nein"
                if inhalt[2]['Bogen']['Verfuegbarkeit'] == "False":
                    if bogen_upgrade_text_rect.collidepoint(event.pos):
                        if inhalt[2]['Bogen']['upgrade'] >= 3:
                            pass
                        else:
                            inhalt[2]['Bogen']['upgrade'] += 1
                            coin_score -= inhalt[2]['Bogen']['upgrade_kosten']

                    with open("Coin_speicher.txt", "w") as fp:
                        fp.write(f"{coin_score}")
                if inhalt[3]['Armbrust']['Verfuegbarkeit'] == "False":
                    if armbrust_upgrade_text_rect.collidepoint(event.pos):
                        if inhalt[3]['Armbrust']['upgrade'] >= 6:
                            pass
                        else:
                            inhalt[3]['Armbrust']['upgrade'] += 1
                            coin_score -= inhalt[3]['Armbrust']['upgrade_kosten']

                    with open("Coin_speicher.txt", "w") as fp:
                        fp.write(f"{coin_score}")






        screen.blit(background, (0, 0))


        pygame.draw.rect(surface=screen, rect=waffen_text_rect, color="black")
        screen.blit(source=Waffe_text, dest=waffen_text_rect)
        pygame.draw.rect(surface=screen, rect=skins_text_rect, color="black")
        screen.blit(source=Skin_text, dest=skins_text_rect)
        pygame.draw.rect(surface=screen, rect=coin_text_rect, color="black")
        screen.blit(source=coin_text, dest=coin_text_rect)





        pygame.draw.rect(surface=screen, rect=(GV.SCREEN_WIDTH-GV.SCREEN_WIDTH/2.3, 170, 400, 500), color="white")


        if inhalt[0]['Schwert']['Verfuegbarkeit'] == "False":
            pygame.draw.rect(surface=screen, rect=(GV.SCREEN_WIDTH-GV.SCREEN_WIDTH/2.5-10, 200-10, 110, 100), color="green")
        else:
            pygame.draw.rect(surface=screen, rect=(GV.SCREEN_WIDTH-GV.SCREEN_WIDTH/2.5-10, 200-10, 110, 100), color="red")

        if inhalt[1]['Axt']['Verfuegbarkeit'] == "False":
            pygame.draw.rect(surface=screen, rect=(GV.SCREEN_WIDTH-GV.SCREEN_WIDTH/2.5 -10 , 310, 110, 100), color="green")
        else:
            pygame.draw.rect(surface=screen, rect=(GV.SCREEN_WIDTH-GV.SCREEN_WIDTH/2.5 -10 , 310, 110, 100), color="red")

        if inhalt[2]['Bogen']['Verfuegbarkeit'] == "False":
            pygame.draw.rect(surface=screen, rect=(GV.SCREEN_WIDTH-GV.SCREEN_WIDTH/2.5 -10, 420, 110, 100 ), color="green")
        else:
            pygame.draw.rect(surface=screen, rect=(GV.SCREEN_WIDTH-GV.SCREEN_WIDTH/2.5 -10, 420, 110, 100 ), color="red")

        if inhalt[3]['Armbrust']['Verfuegbarkeit'] == "False":
            pygame.draw.rect(surface=screen, rect=(GV.SCREEN_WIDTH-GV.SCREEN_WIDTH/2.5 - 10 , 530, 110, 100 ), color="green")
        else:
            pygame.draw.rect(surface=screen, rect=(GV.SCREEN_WIDTH-GV.SCREEN_WIDTH/2.5 - 10 , 530, 110, 100 ), color="red")

        if inhalt[0]['Schwert']['Verfuegbarkeit'] == "False":

            if inhalt[0]['Schwert']['ausgewaehlt'] == "Ja":
                schwert_ausrüsten_text = GV.FONT_MIDDLE.render("Augesrüstet", False, "green")
                GV.actual_WAEPON = 0
            else:
                schwert_ausrüsten_text = GV.FONT_MIDDLE.render("Ausrüsten", False, "black")
        else:
            schwert_ausrüsten_text = GV.FONT_SMALL.render("Nicht Verfügbar", False, "red")
        if inhalt[1]['Axt']['Verfuegbarkeit'] == "False":
            if inhalt[1]['Axt']['ausgewaehlt'] == "Ja":
                axt_ausrüsten_text = GV.FONT_MIDDLE.render("Ausgerüstet", False, "green")
                GV.actual_WAEPON = 1
            else:
                axt_ausrüsten_text = GV.FONT_MIDDLE.render("Ausrüsten", False, "black")

        else:
            axt_ausrüsten_text = GV.FONT_SMALL.render("Nicht Verfügbar", False, "red")
        if inhalt[2]['Bogen']['Verfuegbarkeit'] == "False":
            if inhalt[2]['Bogen']['ausgewaehlt'] == "Ja":
                Bogen_ausrüsten_text = GV.FONT_MIDDLE.render("Ausgerüstet", False, "green")
                GV.actual_WAEPON = 2
            else:
                Bogen_ausrüsten_text = GV.FONT_MIDDLE.render("Ausrüsten", False, "black")
        else:
            Bogen_ausrüsten_text = GV.FONT_SMALL.render("Nicht Verfügbar", False, "red")
        if inhalt[3]['Armbrust']['Verfuegbarkeit'] == "False":
            if inhalt[3]['Armbrust']['ausgewaehlt'] == "Ja":
                Armbrust_ausrüsten_text = GV.FONT_MIDDLE.render("Ausgerüstet", False, "green")
                GV.actual_WAEPON = 3
            else:
                Armbrust_ausrüsten_text = GV.FONT_MIDDLE.render("Ausrüsten", False, "black")
        else:
            Armbrust_ausrüsten_text = GV.FONT_SMALL.render("Nicht Verfügbar", False, "red")

        schwert_pos = res_schwert_image.get_rect(center=schwert_image_rect.center)
        # KI-Ende
        axt_pos = res_axt_image.get_rect(center=axt_image_rect.center)
        bogen_pos = res_bogen_image.get_rect(center=bogen_image_rect.center)
        armbrust_pos = res_armbrust_image.get_rect(center=armbrust_image_rect.center)

        screen.blit(res_schwert_image, schwert_pos)
        screen.blit(res_axt_image, axt_pos)
        screen.blit(res_bogen_image, bogen_pos)
        screen.blit(res_armbrust_image, armbrust_pos)

        screen.blit(source=schwert_ausrüsten_text, dest=schwert_ausrüsten_text_rect)
        screen.blit(source=axt_ausrüsten_text, dest=axt_ausrüsten_text_rect)
        screen.blit(source=Bogen_ausrüsten_text, dest=Bogen_ausrüsten_text_rect)
        screen.blit(source=Armbrust_ausrüsten_text, dest=Armbrust_ausrüsten_text_rect)

        #if inhalt[0]['Schwert']['Verfuegbarkeit'] == "False":
            #screen.blit(source=upgrade_text_Schwert_blau, dest=upgrade_text_rect_Schwert)
            #screen.blit(source=upgrade_text_Schwert, dest=Lvl_text_rect_Schwert)

        #if inhalt[1]['Axt']['Verfuegbarkeit'] == "False":
            #screen.blit(source=upgrade_text_Axt_blau, dest=upgrade_text_rect_Axt)
            #screen.blit(source=upgrade_text_Axt, dest=Lvl_text_rect_Axt)



        if inhalt[2]['Bogen']['Verfuegbarkeit'] == "False":
            if inhalt[2]['Bogen']['upgrade'] == 3:
                upgrade_text_Bogen = GV.FONT_SMALL.render(f"Lvl: {inhalt[2]['Bogen']['upgrade']}", True, "black")
                Lvl_text_rect_Bogen = upgrade_text_Bogen.get_rect(
                    topleft=(GV.SCREEN_WIDTH - GV.SCREEN_WIDTH / 3 + 40, 480))
                max_out_text = GV.FONT_SMALL.render("Max. Level", True,
                                                               "gold1")
                max_out_text_rect = max_out_text.get_rect(
                    topleft=(GV.SCREEN_WIDTH - GV.SCREEN_WIDTH / 4+20, 480))
                screen.blit(source=max_out_text, dest=max_out_text_rect)
                screen.blit(source=upgrade_text_Bogen, dest=Lvl_text_rect_Bogen)
            else:
                upgrade_text_Bogen = GV.FONT_SMALL.render(f"Lvl: {inhalt[2]['Bogen']['upgrade']}", True, "black")
                upgrade_text_Bogen_blau = GV.FONT_SMALL.render(f"Upgrade {inhalt[2]['Bogen']['upgrade_kosten']}", True,
                                                               "blue")
                Lvl_text_rect_Bogen = upgrade_text_Bogen.get_rect(topleft=(GV.SCREEN_WIDTH - GV.SCREEN_WIDTH / 3 + 40, 480))
                upgrade_text_rect_Bogen = upgrade_text_Bogen_blau.get_rect(
                    topleft=(GV.SCREEN_WIDTH - GV.SCREEN_WIDTH / 4 + 40, 480))

                screen.blit(source=upgrade_text_Bogen_blau, dest=upgrade_text_rect_Bogen)
                screen.blit(source=upgrade_text_Bogen, dest=Lvl_text_rect_Bogen)



        if inhalt[3]['Armbrust']['Verfuegbarkeit'] == "False":
            if inhalt[3]['Armbrust']['upgrade'] == 6:
                upgrade_text_Armbrust = GV.FONT_SMALL.render(f"Lvl: {inhalt[3]['Armbrust']['upgrade']}", True, "black")
                Lvl_text_rect_Armbrust = upgrade_text_Armbrust.get_rect(
                    topleft=(GV.SCREEN_WIDTH - GV.SCREEN_WIDTH / 3 + 40, 590))
                max_out_text = GV.FONT_SMALL.render("Max. Level", True,
                                                    "gold1")
                max_out_text_rect = max_out_text.get_rect(
                    topleft=(GV.SCREEN_WIDTH - GV.SCREEN_WIDTH / 4 + 20, 590))
                screen.blit(source=max_out_text, dest=max_out_text_rect)
                screen.blit(source=upgrade_text_Armbrust, dest=Lvl_text_rect_Armbrust)
            else:
                upgrade_text_Armbrust = GV.FONT_SMALL.render(f"Lvl: {inhalt[3]['Armbrust']['upgrade']}", True, "black")
                upgrade_text_Armbrust_blau = GV.FONT_SMALL.render(f"Upgrade {inhalt[3]['Armbrust']['upgrade_kosten']}",
                                                                  True,
                                                                  "blue")
                Lvl_text_rect_Armbrust = upgrade_text_Armbrust.get_rect(
                    topleft=(GV.SCREEN_WIDTH - GV.SCREEN_WIDTH / 3 + 40, 590))
                upgrade_text_rect_Armbrust = upgrade_text_Armbrust_blau.get_rect(
                    topleft=(GV.SCREEN_WIDTH - GV.SCREEN_WIDTH / 4 + 40, 590))

                screen.blit(source=upgrade_text_Armbrust_blau, dest=upgrade_text_rect_Armbrust)
                screen.blit(source=upgrade_text_Armbrust, dest=Lvl_text_rect_Armbrust)



        with open("speichern_spielstand.json", "w") as fp:
            json.dump(inhalt, fp, indent=4)


        pygame.display.flip()
        clock.tick(GV.FPS)


def name_eingeben(screen, clock):

    name = ""

    while True:

        pygame.display.set_caption("Dungeon Survivor - RIP")
        background = pygame.image.load("assets/Background 300x128.png")
        resized_background = pygame.transform.scale(background, (GV.SCREEN_WIDTH, GV.SCREEN_HEIGHT))

        titel = GV.FONT_BIG.render("GAME OVER", False, "red")
        eingabe = GV.FONT_MIDDLE.render("Name eingeben:", False, "white")
        name_text = GV.FONT_BIG.render(name, False, "yellow")


        screen.blit(resized_background, (0, 0))
        screen.blit(titel, (350, 150))
        screen.blit(eingabe, (350, 280))
        screen.blit(name_text, (350, 350))

        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
            # KI-Anfang
            # KI: ChatGPT
            #prompt: Wie kann ich jetzt die Eingabe im screen machen
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN and name != "":
                    return name

                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]

                else:
                    if len(name) < 12:
                        name += event.unicode
            # KI-Ende

        clock.tick(GV.FPS)

def Gameover(screen, clock):
    name = name_eingeben(screen, clock)
    with open("last_coins.txt", "r") as fp:
        stats = json.load(fp)
    coins = stats["Coins"]
    welle = stats["Welle"]
    highscore = Highscores()
    highscore.speichern(name, coins, welle)

    return GameScreens.MAIN


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