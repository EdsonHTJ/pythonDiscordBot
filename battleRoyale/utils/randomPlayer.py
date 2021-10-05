from random import randint
from random import random

def getRandomPlayerFromArray(playerArray):
    player = playerRoulette(playerArray)
    playerArray.remove(player)

    return player

def playerRoulette(playerArray):
    rouletteWheelPosition = random() * sum([player.stamina for player in playerArray])
    spinWhell = 0
    staminaSortedPlayers = sorted(playerArray, key = lambda player: player.stamina, reverse = True)
    for i in range(len(staminaSortedPlayers)):
        spinWhell += staminaSortedPlayers[i].stamina
        if spinWhell >= rouletteWheelPosition:
            return staminaSortedPlayers[i]

    return staminaSortedPlayers[-1]