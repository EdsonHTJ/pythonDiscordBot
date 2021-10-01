
from enum import Enum
from random import seed
from random import random
from random import randint


deaths = open('./battleRoyale/DEATH.txt', 'r').readlines()
singleKills =  open('./battleRoyale/SINGLEKILL.txt', 'r').readlines()
nothings =  open('./battleRoyale/NOTHING.txt', 'r').readlines()
versus = open('./battleRoyale/VERSUS.txt', 'r').readlines()


versusMask = "[ @l1@ ] @p1@ vs @p2@ [ @l2@ ] \n"


class States(Enum):
    ALIVE = 0
    INJURIED = 1
    DEAD = 2

class Events(Enum):
    NOTHING = 0
    SINGLEKILL = 1
    DEATH = 2
    #MULTIKILL = 3

    def randomEvent(dc, skc):
        value = random()

        if value > dc:
            return Events.NOTHING
        
        elif value > skc:
            return Events.SINGLEKILL
        
        else:
            return Events.NOTHING



class player():
    def __init__(self, name) -> None:
        self.name = name
        self.status = States.ALIVE
        self.life = 50


class BattleRoyale():
    def __init__(self) -> None:
        self.players = []
        self.alive = []
        self.dead = []
        self.output = ""

        self.SINGLEKILLCHANCE = 0.6
        self.DEATHCHANCE = 0.8


    def addPlayer(self, name):
        self.players.append(player(name))

    def getPlayers(self):
        output = ""
        for player in self.players:
            output += player.name + "\n"

        return output

    def run(self):
        self.alive = self.players
        while(len(self.alive) > 2):
            event = Events.randomEvent(self.DEATHCHANCE, self.SINGLEKILLCHANCE)

            if event == Events.NOTHING:
                self.eventNothing()
            if event == Events.DEATH:
                self.eventDeath()
            if event == Events.SINGLEKILL:
                self.eventKill()

        winner = self.versus(self.alive[0], self.alive[1])

        self.output += winner.name + " is the winner\n"
        return self.output

    def versus(self, player1, player2):
        player1.life = 100
        player2.life = 100

        while(player1.life > 0 and player2.life > 0):

            p1Attack = randint(0, 50)
            p2Attack = randint(0, 50)

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
            out1 += f" dando {str(res)} de dano\n"
            self.output += out1

            
            out2 = versusMask.replace("@l1@", str(player1.life), 1)
            out2 = out2.replace("@l2@", str(player2.life), 1)
            out2 = out2.replace("@p1@", player1.name, 1)
            out2 = out2.replace("@p2@", player2.name, 1)

            self.output += out2

        if(player1.life < 0):
            return player2
        
        return player1






    def eventNothing(self):

        self.SINGLEKILLCHANCE -= 0.01
        self.DEATHCHANCE -= 0.01
        pi = randint(0, len(self.alive) - 1)
        p = self.alive[pi]

        rq = randint(0, len(nothings) - 1);
        self.output += nothings[rq].replace("@v@", p.name , 1)
        

    def eventDeath(self):
        alivecopy = self.alive

        pv, alivecopy = getRandomPlayerFromArray(alivecopy)

        self.dead.append(pv)
        self.alive = alivecopy

        rq = randint(0, len(deaths) - 1);
        self.output += deaths[rq].replace("@v@", pv.name, 1)


    def eventKill(self):
        alivecopy = self.alive

        pv, alivecopy = getRandomPlayerFromArray(alivecopy)

        self.dead.append(pv)
        self.alive = alivecopy
        pk, alivecopy = getRandomPlayerFromArray(alivecopy)


        rq = randint(0, len(singleKills) - 1);
        out1 = singleKills[rq].replace("@v@", pv.name, 1)
        self.output += out1.replace("@k@", pk.name, 1)



    




def getRandomPlayerFromArray(playerArray):
    pi = randint(0, len(playerArray) - 1)
    p = playerArray[pi]
    NewplayerArray = playerArray[:pi] +playerArray[pi+1:]

    return p, NewplayerArray


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
    print(out)
    out = bt.run()
    print(out)
