from xml.etree.ElementTree import indent

import pygame
import json
from Game_Variables.Variables import GameVariables as GV
from Game_Variables.Variables import GameScreens
from Game_Variables.enemys import Enemy as en
from Game_Variables.player import Player as pl
from Game_Variables.schuss_elemente_player import Rockets
from Game_Variables.Inventar_system import Inventar as IV

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
    leben, welle, score_coin, coin_gesammelt, player_death = enemy.get()

    pygame.display.set_caption("Dungeon Survivor - Main screen")
    background = pygame.image.load("assets/HR_Fantasy_Landscape.png")
    resized_background = pygame.transform.scale(background, (GV.SCREEN_WIDTH, GV.SCREEN_HEIGHT))
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

    image = pygame.image.load("assets/Ninja Adventure - Asset Pack/Ui/Theme/Wip/ThemeDark/nine_path_panel.png").convert_alpha()
    # KI-Anfang
    # KI: ChatGPT
    # prompt: Wie kann ich von diesem rechteck     starten_text_rect = starten_text.get_rect(center=(GV.SCREEN_WIDTH / 2, 100 + 80)) den länge und die breite bekommen
    res_image = pygame.transform.scale(image, (starten_text_rect.width, starten_text_rect.height))


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
        screen.blit(font.render(f"{score_coin}", True, (0, 0, 0)), coin_int_rect)
        leben, welle, score_coin, coin_gesammelt, player_death = enemy.get()
        pygame.display.flip()
        clock.tick(GV.FPS)

def play_screen(screen, clock):
    coin_score = 0
    rocket_list = Rockets(screen=screen)
    with open("Coin_speicher.txt", "r") as fp:
        inhalt = fp.read()
    if len(inhalt) == 0:
        pass
    else:
        coin_score = int(inhalt)
    enemy = en(screen, rocket_list, coin_score)
    player = pl(screen, rocket_list)
    leben, welle, score_coin, coin_gesammelt, player_death = enemy.get()
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
                return GameScreens.Exit

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return GameScreens.PAUSE
                elif player_death == 1:
                    return GameScreens.GAMEOVER

            player.update_and_shoot(event)


        screen.blit(background_play,(0, 0))
        player.update_and_draw()
        x_pos, y_pos = player.get_pos()
        enemy.update_and_draw(x_pos, y_pos)


        rocket_list.update_and_draw()

        screen.blit(source=Leben, dest=Leben_rect)
        screen.blit(source=Welle, dest=Welle_rect)
        screen.blit(source=Coin, dest=Coin_rect)

        screen.blit(font.render(f"{leben:.0f}", True, (255, 255, 255)), Level_rect)
        screen.blit(font.render(f"{welle:.0f}", True, (255, 255, 255)), welle_int_rect)
        screen.blit(font.render(f"{coin_gesammelt}", True, (255, 255, 255)), coin_int_rect)

        leben, welle, score_coin, coin_gesammelt, player_death = enemy.get()
        pygame.display.flip()
        clock.tick(GV.FPS)

def pause_screen(screen, clock):
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
                    return GameScreens.MAIN

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


def waffen_zeichnen(screen, clock):
    pass
def skins_zeichnen(screen, clock):
    pass

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

def shop_screen(screen, clock):

    pygame.display.set_caption("Dungeon Survivor - Shop")
    background = pygame.image.load("assets/StockCake-Gemütliche_Pixel-Taverne-3432555-medium.png")
    resized_background = pygame.transform.scale(background, (GV.SCREEN_WIDTH, GV.SCREEN_HEIGHT))
    waffen_text = GV.FONT_BIG.render("Waffen", False, "yellow")
    skins_text = GV.FONT_BIG.render("Skins ", False, "gray")

    spielstand = spielstand_auslesen("speichern_spielstand.json")


    waffen_text_rect = waffen_text.get_rect(topleft=(20, 100))
    skins_text_rect = skins_text.get_rect(topleft=(20, 100 + 80))

    # KI-Anfang
    # KI: ChatGPT
    # prompt: warum ist das letzte rechteck nicht ganz zu sehen: schwert_rect = pygame.Rect(40 + waffen_text_rect.width, 60, GV.SCREEN_WIDTH / 2, (GV.SCREEN_HEIGHT - 3 * 10) / 4) axt_rect = pygame.Rect(40 + waffen_text_rect.width, 60 + schwert_rect.height +10, GV.SCREEN_WIDTH / 2, (GV.SCREEN_HEIGHT - 2 * 10) / 4) bogen_rect = pygame.Rect(40 + waffen_text_rect.width, 60 + 2*(schwert_rect.height + 10), GV.SCREEN_WIDTH / 2, (GV.SCREEN_HEIGHT - 2 * 10) / 4) armbrust_rect = pygame.Rect(40 + waffen_text_rect.width, 60 + 3*(schwert_rect.height + 10), GV.SCREEN_WIDTH / 2, (GV.SCREEN_HEIGHT - 2 * 10) / 4)
    margin = 60
    abstand = 10
    anzahl = 4

    hoehe = (GV.SCREEN_HEIGHT - 2 * margin - (anzahl - 1) * abstand) / anzahl
    hoehe_bild = hoehe - 4 * abstand

    x = 40 + waffen_text_rect.width
    y_start = margin

    schwert_headline = GV.FONT_MIDDLE.render("Schwert", False, "darkred")
    axt_headline = GV.FONT_MIDDLE.render("Axt", False, "darkred")
    bogen_headline = GV.FONT_MIDDLE.render("Bogen", False, "darkred")
    armbrust_headline = GV.FONT_MIDDLE.render("Armbrust", False, "darkred")

    schwert_text = GV.FONT_SMALL.render("Der Klassiker", False, "black")
    axt_text = GV.FONT_SMALL.render("Zwar langsam, zerhäckselt aber Gegner", False, "black")
    bogen_text = GV.FONT_SMALL.render("Ausgewogene Fernkampfwaffe", False, "black")
    armbrust_text = GV.FONT_SMALL.render("Töte Mehrere mit einem Schuss", False, "black")

    schwert_preis = GV.FONT_SMALL.render(f"Preis: {spielstand[0]['Schwert']['Coins']}", False, "gold3")
    axt_preis = GV.FONT_SMALL.render(f"Preis: {spielstand[1]['Axt']['Coins']}", False, "gold3")
    bogen_preis = GV.FONT_SMALL.render(f"Preis: {spielstand[2]['Bogen']['Coins']}", False, "gold3")
    armbrust_preis = GV.FONT_SMALL.render(f"Preis: {spielstand[3]['Armbrust']['Coins']}", False, "gold3")

    if spielstand[0]['Schwert']['Verfuegbarkeit'] == "True":
        schwert_kaufen = GV.FONT_MIDDLE.render("Kaufen", False, "green2")
        schwert_kaufen_rect = schwert_kaufen.get_rect(topleft=(x + 260 + hoehe_bild, y_start + 90))
    else:
        schwert_kaufen = GV.FONT_MIDDLE.render("Im Besitz", False, "red2")
        schwert_kaufen_rect = schwert_kaufen.get_rect(topleft=(x + 260 + hoehe_bild, y_start + 90))

    if spielstand[1]['Axt']['Verfuegbarkeit'] == "True":
        axt_kaufen = GV.FONT_MIDDLE.render("Kaufen", False, "green2")
        axt_kaufen_rect = axt_kaufen.get_rect(topleft=(x + 260 + hoehe_bild, y_start + 90 + 1 * (hoehe + abstand)))
    else:
        axt_kaufen = GV.FONT_MIDDLE.render("Im Besitz", False, "red2")
        axt_kaufen_rect = axt_kaufen.get_rect(topleft=(x + 260 + hoehe_bild, y_start + 90 + 1 * (hoehe + abstand)))

    if spielstand[2]['Bogen']['Verfuegbarkeit'] == "True":
        bogen_kaufen = GV.FONT_MIDDLE.render("Kaufen", False, "green2")
        bogen_kaufen_rect = bogen_kaufen.get_rect(topleft=(x + 260 + hoehe_bild, y_start + 90 + 2 * (hoehe + abstand)))
    else:
        bogen_kaufen = GV.FONT_MIDDLE.render("Im Besitz", False, "red2")
        bogen_kaufen_rect = bogen_kaufen.get_rect(topleft=(x + 260 + hoehe_bild, y_start + 90 + 2 * (hoehe + abstand)))

    if spielstand[3]['Armbrust']['Verfuegbarkeit'] == "True":
        armbrust_kaufen = GV.FONT_MIDDLE.render("Kaufen", False, "green2")
        armbrust_kaufen_rect = armbrust_kaufen.get_rect(
            topleft=(x + 260 + hoehe_bild, y_start + 90 + 3 * (hoehe + abstand)))
    else:
        armbrust_kaufen = GV.FONT_MIDDLE.render("Im Besitz", False, "red2")
        armbrust_kaufen_rect = armbrust_kaufen.get_rect(
            topleft=(x + 260 + hoehe_bild, y_start + 90 + 3 * (hoehe + abstand)))

    with open("Coin_speicher.txt", "r") as fp:
        coins = fp.read()

    coins = int(coins)

    coins_text = GV.FONT_MIDDLE.render(f"Coins: {coins}", False, "yellow")
    coin_int_rect = coins_text.get_rect(center=(GV.SCREEN_WIDTH - 100, 47))

    schwert_rect = pygame.Rect(x, y_start, GV.SCREEN_WIDTH / 2, hoehe)
    axt_rect = pygame.Rect(x, y_start + 1 * (hoehe + abstand), GV.SCREEN_WIDTH / 2, hoehe)
    bogen_rect = pygame.Rect(x, y_start + 2 * (hoehe + abstand), GV.SCREEN_WIDTH / 2, hoehe)
    armbrust_rect = pygame.Rect(x, y_start + 3 * (hoehe + abstand), GV.SCREEN_WIDTH / 2, hoehe)

    # KI-Ende

    schwert_image_rect = pygame.Rect(x + 10, y_start + 10, hoehe_bild, hoehe_bild)
    axt_image_rect = pygame.Rect(x + 10, y_start + 10 + 1 * (hoehe + abstand), hoehe_bild, hoehe_bild)
    bogen_image_rect = pygame.Rect(x + 10, y_start + 10 + 2 * (hoehe + abstand), hoehe_bild, hoehe_bild)
    armbrust_image_rect = pygame.Rect(x + 10, y_start + 10 + 3 * (hoehe + abstand), hoehe_bild, hoehe_bild)

    schwert_image = pygame.image.load("assets/Ninja Adventure - Asset Pack/Items/Weapons/Sword2/Sprite.png")
    axt_image = pygame.image.load("assets/Ninja Adventure - Asset Pack/Items/Weapons/AxeTool/Sprite.png")
    bogen_image = pygame.image.load("assets/Ninja Adventure - Asset Pack/Items/Weapons/Bow2/Sprite.png")
    armbrust_image = pygame.image.load("assets/Ninja Adventure - Asset Pack/Items/Weapons/Crossbow/Sprite.png")

    res_schwert_image = pygame.transform.scale(schwert_image, (6 * schwert_image.get_width(), 6 * schwert_image.get_height()))
    res_axt_image = pygame.transform.scale(axt_image, (6 * axt_image.get_width(), 6 * axt_image.get_height()))
    res_bogen_image = pygame.transform.scale(bogen_image, (6 * bogen_image.get_width(), 6 * bogen_image.get_height()))
    res_armbrust_image = pygame.transform.scale(armbrust_image, (6 * armbrust_image.get_width(), 6 * armbrust_image.get_height()))

    tab = "waffen"

    while True:

        for event in pygame.event.get():
            if tab == "waffen":
                waffen_text = GV.FONT_BIG.render("Waffen", False, "yellow")
                skins_text = GV.FONT_BIG.render("Skins", False, "gray")
            else:
                waffen_text = GV.FONT_BIG.render("Waffen", False, "gray")
                skins_text = GV.FONT_BIG.render("Skins", False, "yellow")

            coins_text = GV.FONT_MIDDLE.render(f"Coins: {coins}", False, "yellow")
            if event.type == pygame.QUIT:
                return GameScreens.Exit

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return GameScreens.MAIN



            if event.type == pygame.MOUSEBUTTONDOWN:

                if waffen_text_rect.collidepoint(event.pos):
                    aktueller_tab = "waffen"

                elif skins_text_rect.collidepoint(event.pos):
                    aktueller_tab = "skins"

                elif schwert_kaufen_rect.collidepoint(event.pos) and spielstand[0]['Schwert']['Verfuegbarkeit'] == "True":
                    if coins >= spielstand[0]['Schwert']['Coins']:
                        coins -= spielstand[0]['Schwert']['Coins']
                        spielstand[0]['Schwert']['Verfuegbarkeit'] = "False"
                        muenzen_speichern("Coin_speicher.txt", coins)
                        spielstand_speichern("speichern_spielstand.json", spielstand)
                        schwert_kaufen = GV.FONT_MIDDLE.render("Im Besitz", False, "red2")
                        schwert_kaufen_rect = schwert_kaufen.get_rect(topleft=(x + 260 + hoehe_bild, y_start + 90))

                elif axt_kaufen_rect.collidepoint(event.pos) and spielstand[1]['Axt']['Verfuegbarkeit'] == "True":
                    if coins >= spielstand[1]['Axt']['Coins']:
                        coins -= spielstand[1]['Axt']['Coins']
                        spielstand[1]['Axt']['Verfuegbarkeit'] = "False"
                        muenzen_speichern("Coin_speicher.txt", coins)
                        spielstand_speichern("speichern_spielstand.json", spielstand)
                        axt_kaufen = GV.FONT_MIDDLE.render("Im Besitz", False, "red2")
                        axt_kaufen_rect = axt_kaufen.get_rect(
                            topleft=(x + 260 + hoehe_bild, y_start + 90 + 1 * (hoehe + abstand)))

                elif bogen_kaufen_rect.collidepoint(event.pos) and spielstand[2]['Bogen']['Verfuegbarkeit'] == "True":
                    if coins >= spielstand[2]['Bogen']['Coins']:
                        coins -= spielstand[2]['Bogen']['Coins']
                        spielstand[2]['Bogen']['Verfuegbarkeit'] = "False"
                        muenzen_speichern("Coin_speicher.txt", coins)
                        spielstand_speichern("speichern_spielstand.json", spielstand)
                        bogen_kaufen = GV.FONT_MIDDLE.render("Im Besitz", False, "red2")
                        bogen_kaufen_rect = bogen_kaufen.get_rect(
                            topleft=(x + 260 + hoehe_bild, y_start + 90 + 2 * (hoehe + abstand)))

                elif armbrust_kaufen_rect.collidepoint(event.pos) and spielstand[3]['Armbrust']['Verfuegbarkeit'] == "True":
                    if coins >= spielstand[3]['Armbrust']['Coins']:
                        coins -= spielstand[3]['Armbrust']['Coins']
                        spielstand[3]['Armbrust']['Verfuegbarkeit'] = "False"
                        muenzen_speichern("Coin_speicher.txt", coins)
                        spielstand_speichern("speichern_spielstand.json", spielstand)
                        armbrust_kaufen = GV.FONT_MIDDLE.render("Im Besitz", False, "red2")
                        armbrust_kaufen_rect = armbrust_kaufen.get_rect(
                            topleft=(x + 260 + hoehe_bild, y_start + 90 + 3 * (hoehe + abstand)))





        screen.blit(resized_background, (0, 0))

        pygame.draw.rect(surface=screen, rect=waffen_text_rect, color="black")
        pygame.draw.rect(surface=screen, rect=skins_text_rect, color="black")

        pygame.draw.rect(surface=screen, rect= schwert_rect, color="lightgray")
        pygame.draw.rect(surface=screen, rect= axt_rect, color="lightgray")
        pygame.draw.rect(surface=screen, rect= bogen_rect, color="lightgray")
        pygame.draw.rect(surface=screen, rect= armbrust_rect, color="lightgray")

        pygame.draw.rect(surface=screen, rect= schwert_image_rect, color="black")
        pygame.draw.rect(surface=screen, rect= axt_image_rect, color="black")
        pygame.draw.rect(surface=screen, rect= bogen_image_rect, color="black")
        pygame.draw.rect(surface=screen, rect= armbrust_image_rect, color="black")

        screen.blit(source=waffen_text, dest=waffen_text_rect)
        screen.blit(source=skins_text, dest=skins_text_rect)

        screen.blit(source=schwert_headline, dest= (x+ 20 + hoehe_bild, y_start + 10))
        screen.blit(source=axt_headline, dest= (x+ 20 + hoehe_bild, y_start + 10 + 1 * (hoehe + abstand)))
        screen.blit(source=bogen_headline, dest= (x+ 20 + hoehe_bild, y_start + 10 + 2 * (hoehe + abstand)))
        screen.blit(source=armbrust_headline, dest= (x+ 20 + hoehe_bild, y_start + 10 + 3 * (hoehe + abstand)))

        screen.blit(source=schwert_text, dest= (x+ 20 + hoehe_bild, y_start + 50))
        screen.blit(source=axt_text, dest=(x + 20 + hoehe_bild, y_start + 50 + 1 * (hoehe + abstand)))
        screen.blit(source=bogen_text, dest=(x + 20 + hoehe_bild, y_start + 50 + 2 * (hoehe + abstand)))
        screen.blit(source=armbrust_text, dest=(x + 20 + hoehe_bild, y_start + 50 + 3 * (hoehe + abstand)))

        screen.blit(source=coins_text, dest = coin_int_rect)

        screen.blit(source=schwert_preis, dest = (x+ 20 + hoehe_bild, y_start + 90))
        screen.blit(source=axt_preis, dest = (x+ 20 + hoehe_bild, y_start + 90 + 1 * (hoehe + abstand)))
        screen.blit(source=bogen_preis, dest = (x+ 20 + hoehe_bild, y_start + 90 + 2 * (hoehe + abstand)))
        screen.blit(source=armbrust_preis, dest = (x+ 20 + hoehe_bild, y_start + 90 + 3 * (hoehe + abstand)))

        screen.blit(source=schwert_kaufen, dest= (x+ 260 + hoehe_bild, y_start + 90))
        screen.blit(source=axt_kaufen, dest= (x+ 260 + hoehe_bild, y_start + 90 + 1 * (hoehe + abstand)))
        screen.blit(source=bogen_kaufen, dest= (x+ 260 + hoehe_bild, y_start + 90 + 2 * (hoehe + abstand)))
        screen.blit(source=armbrust_kaufen, dest= (x+ 260 + hoehe_bild, y_start + 90 + 3 * (hoehe + abstand)))

        # KI-Anfang
        # KI: ChatGPT
        # prompt: wie du auf dem bild siehst ist das noch nicht genau zentriert wie kann man das machen
        schwert_pos = res_schwert_image.get_rect(center=schwert_image_rect.center)
        # KI-Ende
        axt_pos = res_axt_image.get_rect(center=axt_image_rect.center)
        bogen_pos = res_bogen_image.get_rect(center=bogen_image_rect.center)
        armbrust_pos = res_armbrust_image.get_rect(center=armbrust_image_rect.center)

        screen.blit(res_schwert_image, schwert_pos)
        screen.blit(res_axt_image, axt_pos)
        screen.blit(res_bogen_image, bogen_pos)
        screen.blit(res_armbrust_image, armbrust_pos)

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

def inventar_screen(screen, clock):

    background = pygame.image.load("assets/redcometnomark.png")
    Skin_text = GV.FONT_BIG.render("Waffe", False, "yellow")
    Waffe_text = GV.FONT_BIG.render("Skin ", False, "yellow")

    waffen_text_rect = Waffe_text.get_rect(topleft=(GV.SCREEN_WIDTH - GV.SCREEN_WIDTH/4, 50))
    skins_text_rect = Skin_text.get_rect(topleft=(GV.SCREEN_WIDTH - GV.SCREEN_WIDTH/1.2, 50))


    with open("speichern_spielstand.json", "r") as fp:
        inhalt = fp.read()

    inventar = IV(inhalt, screen)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameScreens.Exit

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return GameScreens.MAIN



        screen.blit(background, (0, 0))
        inventar.update_and_draw()

        pygame.draw.rect(surface=screen, rect=waffen_text_rect, color="black")
        screen.blit(source=Waffe_text, dest=waffen_text_rect)
        pygame.draw.rect(surface=screen, rect=skins_text_rect, color="black")
        screen.blit(source=Skin_text, dest=skins_text_rect)


        pygame.display.flip()
        clock.tick(GV.FPS)


def Gameover(screen, clock):
    background = pygame.image.load("assets/Background 300x128.png")
    resized_background = pygame.transform.scale(background, (GV.SCREEN_WIDTH, GV.SCREEN_HEIGHT))

    Gameover_text = GV.FONT_BIG.render("GameOver", False, "darkred")
    Gameover_text_rect = Gameover_text.get_rect(center=(GV.SCREEN_WIDTH / 2 - 30, GV.SCREEN_HEIGHT/3))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameScreens.Exit

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return GameScreens.MAIN

        screen.blit(resized_background, (0, 0))
        screen.blit(source=Gameover_text, dest=Gameover_text_rect)
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