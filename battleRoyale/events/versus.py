from random import randint
from random import random

versus = open('./battleRoyale/VERSUS.txt', 'r').readlines()
versusMask = "[ @l1@ ] @p1@ vs @p2@ [ @l2@ ] \n"

def eventVersus(player1, refAlive, refDead, refDeadToday, refOutput):
    player2, refAlive = getRandomPlayerFromArray(refAlive.copy())

    refOutput.append({
        "colour": 0xff3700,
        "message": f'{player1.name} e {player2.name} se encontraram e começaram a lutar!',
        "img_url": "https://c.tenor.com/yd7Ntm5sUHMAAAAC/sasuke-naruto.gif",
        "music": "https://www.youtube.com/watch?v=mjjkHg5FOhk",
        "footer": {
            "text": f"Vou matar esse filho da puta! disse {player1.name if random() > 0.5 else player2.name}",
            "icon_url": "https://cdn.iconscout.com/icon/premium/png-256-thumb/boxing-glove-2083061-1754353.png"
        }
    })

    while(player1.life > 0 and player2.life > 0):

        p1Attack = randint(0, 100)
        p2Attack = randint(0, 100)

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
        out2 = versusMask.replace("@l1@", str(player1.life), 1)
        out2 = out2.replace("@l2@", str(player2.life), 1)
        out2 = out2.replace("@p1@", player1.name, 1)
        out2 = out2.replace("@p2@", player2.name, 1)
        colour = 0xe34040 if p1Attack > p2Attack else 0x5ebeeb
        refOutput.append({
            "colour": colour, 
            "message": out1,
            "footer": {
                "text": out2,
                "icon_url": "https://www.seekpng.com/png/full/791-7913808_free-download-minecraft-heart.png"
            }
        })

    if(player1.life <= 0):
        winner = player2
        loser = player1
    else:           
        winner = player1
        loser = player2

    refAlive.append(winner)
    refDead.append(loser)
    refDeadToday.append(loser)

    staminaLost = randint(50, 80)
    staminaLost = staminaLost if staminaLost <= winner.stamina else winner.stamina
    winner.stamina -= staminaLost

    refOutput.append({
        "colour": colour, 
        "message": f'{winner.name} foi o vencedor do combate!',
        "footer": {
            "text": f'saiu com {winner.life} pontos de vida e perdeu {staminaLost} de energia',
            "icon_url": "https://www.seekpng.com/png/full/791-7913808_free-download-minecraft-heart.png"
        }
    })

    
    return refAlive, refDead, refDeadToday, refOutput

def getRandomPlayerFromArray(playerArray):
    player = playerRoulette(playerArray)
    playerArray.remove(player)

    return player, playerArray

def playerRoulette(playerArray):
    rouletteWheelPosition = random() * sum([player.stamina for player in playerArray])
    spinWhell = 0
    staminaSortedPlayers = sorted(playerArray, key = lambda player: player.stamina, reverse = True)
    for i in range(len(staminaSortedPlayers)):
        spinWhell += staminaSortedPlayers[i].stamina
        if spinWhell >= rouletteWheelPosition:
            return staminaSortedPlayers[i]

    return staminaSortedPlayers[-1]