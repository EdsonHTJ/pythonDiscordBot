from random import seed
from random import random
from random import randint
from discord import File
from battleRoyale.worldEvents.worldEvents import worldEvents
from battleRoyale.events.events import execEvent
from battleRoyale.dayAndNightCicle.simulator import simulator
from battleRoyale.player import player
import copy

versusMask = "[ @l1@ ] @p1@ vs @p2@ [ @l2@ ] \n"

class BattleRoyale():
    def __init__(self) -> None:
        self.players = []
        self.alive = []
        self.dead = []
        self.output = []
        self.deadToday = []
        self.defaultChances = [0.6, 0.8, 1] #SINGLEKILL, DEATH, VERSUS
        self.worldEventsChances = 0.1
        self.simulator = simulator(True, self.worldEventsChances)

    def run(self):
        self.output = []
        self.alive = []

        for player in self.players:
            self.alive.append(copy.copy(player))

        while(len(self.alive) >= 2):
            self.simulator.cicle(self.alive, self.dead, self.deadToday, self.output)

        if(len(self.alive) == 0):
            self.output.append({
                "colour": 0x000000,
                "message": "E todo mundo morreu",
            })
            return self.output

        winner = self.alive[0]
        self.output.append({
            "colour": 0xffa600,
            "message": winner.name + " is the winner",
            "img_url": "https://media0.giphy.com/media/mCdhhsCLGluNi/giphy.gif",
            "footer": {
                "text": "Mensagens aleatórias de campeões",
                "icon_url": "https://pngimg.com/uploads/crown/crown_PNG23872.png"
            }
        })

        return self.output


    def addPlayer(self, name):
        self.players.append(player(name, self.defaultChances))

    def getPlayers(self):
        output = ""
        for player in self.players:
            output += player.name + "\n"

        return output

if __name__ == "__main__":
    print("hi from main")
    bt = BattleRoyale()
    bt.addPlayer("Jose")
    bt.addPlayer("Jair")
    bt.addPlayer("claudio")
    bt.addPlayer("cleito")
    bt.addPlayer("ruberval")
    bt.addPlayer("xande")
    bt.addPlayer("mariele")

    out = bt.getPlayers()

    out = bt.run()