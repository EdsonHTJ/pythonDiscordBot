from random import random
from random import randint
from battleRoyale.events.death import eventDeath
from battleRoyale.events.kill import eventKill
from battleRoyale.events.nothing import eventNothing
from battleRoyale.events.versus import eventVersus
from battleRoyale.events.eventsEnum import Events

def execEvent(refAlive, refDead, refDeadToday, refOutput):
    if(len(refAlive) <= 2):
        for player in refAlive:
            player.SINGLEKILLCHANCE = 1
            player.DEATHCHANCE = 1
            player.VERSUSCHANCE = 0.2

    player, refAlive = getRandomPlayerFromArray(refAlive)
    event = Events.randomEvent(player.DEATHCHANCE, player.SINGLEKILLCHANCE, player.VERSUSCHANCE)

    if event == Events.NOTHING:
        return eventNothing(player, refAlive, refDead, refDeadToday, refOutput)
    if event == Events.DEATH:
        return eventDeath(player, refAlive, refDead, refDeadToday, refOutput)
    if event == Events.SINGLEKILL:
        return eventKill(player, refAlive, refDead, refDeadToday, refOutput)
    if event == Events.VERSUS:
        return eventVersus(player, refAlive, refDead, refDeadToday, refOutput)

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

    