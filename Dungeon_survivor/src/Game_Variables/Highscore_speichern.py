from email.utils import specialsre


class highscores:

    def __init__(self):
        self.highscore_list = []

    def speichern(self, leben, welle, coins):
        with open("Highscores.txx", "r") as fp:
            highscore_inhalt = fp.read()

        print(highscore_inhalt)


        with open("Highscores.txx", "a") as fp:
            fp.write(f"{leben, welle, coins}")

    def update_and_save(self, leben, welle, coins):
        self.speichern(leben, welle, coins)
