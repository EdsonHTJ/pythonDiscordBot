from enum import Enum
from random import seed
from random import random
from random import randint
from discord import File
import copy


deaths = open('./battleRoyale/DEATH.txt', 'r').readlines()
singleKills =  open('./battleRoyale/SINGLEKILL.txt', 'r').readlines()
nothings =  open('./battleRoyale/NOTHING.txt', 'r').readlines()
versus = open('./battleRoyale/VERSUS.txt', 'r').readlines()


versusMask = "[ @l1@ ] @p1@ vs @p2@ [ @l2@ ] \n"

class RandomImages():
    SUN = ["./battleRoyale/images/sun/gretchen-sun.gif", "./battleRoyale/images/sun/teletubbies-sun.gif", "./battleRoyale/images/sun/cursed-sun.gif", "./battleRoyale/images/sun/nicholas-cage-sun.jpeg", "./battleRoyale/images/sun/delicious-sun.png"]
    MOON = ["./battleRoyale/images/moon/im-the-moon.gif", "./battleRoyale/images/moon/wink-moon.gif", "./battleRoyale/images/moon/boa-noite-consagrado.gif", "./battleRoyale/images/moon/zelda-moon.jpeg"]
    
    def randomSunGif():
        return RandomImages.SUN[randint(0, len(RandomImages.SUN)-1)]
    def randomMoonGif():
        return RandomImages.MOON[randint(0, len(RandomImages.MOON)-1)]


class States(Enum):
    ALIVE = 0
    INJURIED = 1
    DEAD = 2

class Events(Enum):
    NOTHING = 0
    SINGLEKILL = 1
    DEATH = 2
    #MULTIKILL = 3
    VERSUS = 4

    def randomEvent(dc, skc, vc):
        value = random()

        if value > dc:
            return Events.DEATH
        elif value > skc:
            return Events.SINGLEKILL
        elif value > vc:
            return Events.VERSUS
        else:
            return Events.NOTHING


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
        self.defaultChances = [0.8, 0.9, 1] #SINGLEKILL, DEATH, VERSUS
        self.randomImages = RandomImages()


    def addPlayer(self, name):
        self.players.append(player(name, self.defaultChances))

    def getPlayers(self):
        output = ""
        for player in self.players:
            output += player.name + "\n"

        return output

    def run(self):
        self.output = []
        #self.alive = self.players.copy()
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
        winner = self.alive[0]
        self.output.append({"colour": 0xffa600,"message": winner.name + " is the winner\n"})

        return self.output

    def execDay(self, counter):
        self.output.append({"colour": 0xfff370, "message": f'Começo do dia {counter} :sunrise:\n'})
        self.output.append({"path": RandomImages.randomSunGif()})
        self.deadToday = []
        for turns in range(len(self.alive)-1 if len(self.alive) > 4 else 4):
            if(len(self.alive) == 1):
                return
            self.execEvent(playerRoulette(self.alive))

    def execNight(self, counter):
        self.output.append({"colour": 0x0b2496, "message": f'Começo da noite {counter} :waxing_gibbous_moon:\n'})
        self.output.append({"path": RandomImages.randomMoonGif()})
        for turns in range(len(self.alive)-1 if len(self.alive) > 3 else 3):
            if(len(self.alive) == 1):
                return
            self.execEvent(playerRoulette(self.alive))
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


    def execEvent(self, player):
        if(len(self.alive) <= 2):
            for player in self.alive:
                player.SINGLEKILLCHANCE = 1
                player.DEATHCHANCE = 1
                player.VERSUSCHANCE = 0.2

        alive = self.alive.copy()
        player, alive = getRandomPlayerFromArray(alive)
        event = Events.randomEvent(player.DEATHCHANCE, player.SINGLEKILLCHANCE, player.VERSUSCHANCE)

        if event == Events.NOTHING:
            self.eventNothing(player)
        if event == Events.DEATH:
            self.eventDeath(player, alive)
        if event == Events.SINGLEKILL:
            self.eventKill(player, alive)
        if event == Events.VERSUS:
            self.eventVersus(player, alive)

    def increaseStamina(self):
        for player in self.alive:
            player.stamina += randint(0, 100 - player.stamina)


    def eventNothing(self, player):

        player.SINGLEKILLCHANCE -= 0.01
        player.DEATHCHANCE -= 0.01

        randomIndex = randint(0, len(nothings) - 1);
        self.output.append({"colour": 0x666666, "message": nothings[randomIndex].replace("@v@", player.name , 1)})
        

    def eventDeath(self, player, alive):

        self.dead.append(player)
        self.deadToday.append(player)
        self.alive = alive.copy()

        rq = randint(0, len(deaths) - 1);
        self.output.append({"colour": 0x000000, "message": deaths[rq].replace("@v@", player.name, 1)})


    def eventKill(self, player, alive):

        playerKilled, alive = getRandomPlayerFromArray(alive)
        self.dead.append(playerKilled)
        self.deadToday.append(playerKilled)
        alive.append(player)
        self.alive = alive.copy()

        rq = randint(0, len(singleKills) - 1);
        out1 = singleKills[rq].replace("@k@", player.name, 1)
        self.output.append({"colour": 0xab1325, "message": out1.replace("@v@", playerKilled.name, 1)})

    def eventVersus(self, player1, alive):
        player2, alive = getRandomPlayerFromArray(alive.copy())

        while(player1.life > 0 and player2.life > 0):

            p1Attack = randint(0, 200)
            p2Attack = randint(0, 200)

            res = abs(p1Attack - p2Attack)

            if(p1Attack > p2Attack):
                player2.life -= res
                k = player1
                v = player2
            elif(p1Attack < p2Attack):
                player1.life -= res
                k = player2
                v = player1
            else:
                continue
            
            rq = randint(0, len(versus) - 1);
            out1 = versus[rq].replace("@v@", v.name, 1)
            out1 = out1.replace("@k@", k.name, 1)
            out1 = out1.replace("\n", '')
            out1 += f" dando {str(res)} de dano"
            colour = 0xc40e0e if p1Attack > p2Attack else 0x170cab
            self.output.append({"colour": colour, "message": out1})

            
            out2 = versusMask.replace("@l1@", str(player1.life), 1)
            out2 = out2.replace("@l2@", str(player2.life), 1)
            out2 = out2.replace("@p1@", player1.name, 1)
            out2 = out2.replace("@p2@", player2.name, 1)
            self.output.append({"colour": 0xfcfcfc, "message": out2})

        if(player1.life <= 0):
            alive.append(player2)
            self.alive = alive
            self.dead.append(player1)
            self.deadToday.append(player1)
            return player2
              
        alive.append(player1)
        self.alive = alive
        self.dead.append(player1)
        self.deadToday.append(player1)
        return player2


def getRandomPlayerFromArray(playerArray):
    player = playerRoulette(playerArray)
    playerArray.remove(player)

    return player, playerArray


def playerRoulette(playerArray):
    rouletteWheelPosition = random() * sum([player.stamina for player in playerArray])
    spinWhell = 0
    staminaSortedPlayers = sorted(playerArray, key = lambda player: player.stamina, reverse = True)
    for i in range(len(staminaSortedPlayers)):
        spinWhell += staminaSortedPlayers[i].stamina;
        if spinWhell >= rouletteWheelPosition:
            return staminaSortedPlayers[i];

    return staminaSortedPlayers[-1];

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
    print(out)
