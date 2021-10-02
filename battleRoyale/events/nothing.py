from random import randint

nothings =  open('./battleRoyale/NOTHING.txt', 'r').readlines()

def eventNothing(player, refAlive, refDead, refDeadToday, refOutput):
    staminaLost = randint(5, 15)
    staminaLost = staminaLost if staminaLost <= player.stamina else player.stamina
    player.stamina -= staminaLost
    player.SINGLEKILLCHANCE -= 0.01
    player.DEATHCHANCE -= 0.01
    randomIndex = randint(0, len(nothings) - 1)
    refAlive.append(player)
    refOutput.append({
        "colour": 0x666666, 
        "message": nothings[randomIndex].replace("@v@", player.name , 1),
        "footer": {
            "text": f'perdeu {staminaLost} de energia no processo',
            "icon_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Emoji_u26a1.svg/1200px-Emoji_u26a1.svg.png"
        }
    })
    
    return refAlive, refDead, refDeadToday, refOutput