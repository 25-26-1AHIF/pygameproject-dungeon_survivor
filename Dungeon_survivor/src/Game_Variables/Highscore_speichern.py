import json


class Highscores:

    def __init__(self):
        self.datei = "highscores.json"

    def laden(self):
        try:
            with open(self.datei, "r") as fp:
                return json.load(fp)
        except:
            return []

    def speichern(self, name, coins, welle):
        highscores = self.laden()

        highscores.append({
            "Name": name,
            "Coins": coins,
            "Welle": f"{welle:.2f}"
        })

        with open(self.datei, "w") as fp:
            json.dump(highscores, fp, indent=4)