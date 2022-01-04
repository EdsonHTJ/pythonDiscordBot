from random import random
from random import randint
from battleRoyale.utils.randomPlayer import getRandomPlayerFromArray

singleKills =  open('./battleRoyale/SINGLEKILL.txt', 'r').readlines()

def eventKill(player, refAlive, refDead, refDeadToday, refOutput):
    staminaLost = randint(30, 55)
    staminaLost = staminaLost if staminaLost <= player.stamina else player.stamina
    player.stamina -= staminaLost

    playerKilled = getRandomPlayerFromArray(refAlive)
    refAlive.append(player)
    refDead.append(playerKilled)
    refDeadToday.append(playerKilled)

    rq = randint(0, len(singleKills) - 1);
    out1 = singleKills[rq].replace("@k@", player.name, 1)
    refOutput.append({
        "colour": 0xab1325, 
        "message": out1.replace("@v@", playerKilled.name, 1),
        "footer": {
            "text": f'perdeu {staminaLost} de energia no processo',
            "icon_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Emoji_u26a1.svg/1200px-Emoji_u26a1.svg.png"
        }
    })