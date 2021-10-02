from enum import Enum
from random import seed
from random import random
from random import randint
from discord import File
from battleRoyale.worldEvents.worldEvents import worldEvents
from battleRoyale.events.events import execEvent
import copy


versusMask = "[ @l1@ ] @p1@ vs @p2@ [ @l2@ ] \n"

class RandomImages():
    SUN = ["https://i.imgur.com/G6H8Ydk.gif", "https://i.imgur.com/pvF0xRx.gif", "https://i.imgur.com/58aSPjU.jpg", "https://i.imgur.com/jJMLO3f.gif", "https://i.imgur.com/JBew5Iq.jpg"]
    MOON = ["https://i.imgur.com/Y8PnM4q.gif", "https://i.imgur.com/2E10VH1.gif", "https://i.imgur.com/jVJ6Wj1.gif", "https://i.imgur.com/dxZJogU.jpg"]
    
    def randomSunGif():
        return RandomImages.SUN[randint(0, len(RandomImages.SUN)-1)]
    def randomMoonGif():
        return RandomImages.MOON[randint(0, len(RandomImages.MOON)-1)]


class States(Enum):
    ALIVE = 0
    INJURIED = 1
    DEAD = 2


class player():
    def __init__(self, name, chances) -> None:
        self.name = name
        self.status = States.ALIVE
        self.life = 100
        self.stamina = 100
        self.SINGLEKILLCHANCE = chances[0]
        self.DEATHCHANCE = chances[1]
        self.VERSUSCHANCE = chances[2]
    
    def __str__(self):
        return f'name: {self.name}, status: {self.status}, life: {self.life}, stamina: {self.stamina}, skc: {self.SINGLEKILLCHANCE}, dc: {self.DEATHCHANCE}, vc: {self.VERSUSCHANCE}'

    def __copy__(self):
        return player(self.name, [self.SINGLEKILLCHANCE, self.DEATHCHANCE, self.VERSUSCHANCE])


class BattleRoyale():
    def __init__(self) -> None:
        self.players = []
        self.alive = []
        self.dead = []
        self.output = []
        self.deadToday = []
        self.defaultChances = [0.6, 0.8, 1] #SINGLEKILL, DEATH, VERSUS
        self.randomImages = RandomImages()
        self.worldEventsChances = 0


    def addPlayer(self, name):
        self.players.append(player(name, self.defaultChances))

    def getPlayers(self):
        output = ""
        for player in self.players:
            output += player.name + "\n"

        return output

    def run(self):
        self.output = []
        self.alive = []
        for player in self.players:
            self.alive.append(copy.copy(player))
        isDay = True
        day = 1
        while(len(self.alive) >= 2):
            if isDay:
                self.execDay(day)
            else:
                self.execNight(day)
                day += 1
            isDay = not isDay
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
            "music" : "https://www.youtube.com/watch?v=FpnQvVV7gB4",
            "footer": {
                "text": "Mensagens aleatórias de campeões",
                "icon_url": "https://pngimg.com/uploads/crown/crown_PNG23872.png"
            }
        })

        return self.output

    def execDay(self, counter):
        self.output.append({
            "img_url": RandomImages.randomSunGif(), 
            "colour": 0xfff370, 
            "message": f'   Começo do dia {counter} -- :sunrise:\n',
            "footer": {
                "text": "Mensagens aleatórias motivacionais",
                "icon_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Emoji_u2600.svg/1200px-Emoji_u2600.svg.png"
            }
        })
        self.deadToday = []
        if(random() <= self.worldEventsChances):
            output, playersKilled, alive = worldEvents(self.alive).execEvent()
            self.output += output
            self.deadToday += playersKilled
            self.alive = alive
        else: 
            for turns in range(len(self.alive)-1 if len(self.alive) > 4 else 4):
                if(len(self.alive) == 1):
                    return
                self.alive, self.dead, self.deadToday, self.output = execEvent(self.alive, self.dead, self.deadToday, self.output)

    def execNight(self, counter):
        self.output.append({
            "img_url": RandomImages.randomMoonGif(), 
            "colour": 0x0b2496, 
            "music" : "https://www.youtube.com/watch?v=s_eHTKuCkpc&t=28s",
            "message": f'   Começo da noite {counter} -- :waxing_gibbous_moon:\n'})
        if(random() <= self.worldEventsChances):
            output, playersKilled, alive = worldEvents(self.alive).execEvent()
            self.output += output
            self.deadToday += playersKilled
            self.alive = alive
        else: 
            for turns in range(len(self.alive)-1 if len(self.alive) > 4 else 4):
                if(len(self.alive) == 1):
                    return
                self.alive, self.dead, self.deadToday, self.output = execEvent(self.alive, self.dead, self.deadToday, self.output)
        self.increaseStamina()
        self.payRespect()
        

    def payRespect(self):
        if(len(self.deadToday) == 0):
            return
        self.output.append({"colour": 0x000000, "message": f':fireworks: Canhões ecoam pela noite. {len(self.deadToday)} participantes morreram :fireworks:.\n'})
        output = 'Participantes mortos: '
        for player in self.deadToday:
            output += player.name + ' '
        self.output.append({"colour": 0x000000, "message": f'{output}\n'})


    def increaseStamina(self):
        for player in self.alive:
            player.stamina += randint(0, 100 - player.stamina)

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
    #print(out)
