from random import random
from random import randint

ghC_deaths = open('./battleRoyale/worldEvents/masks/ghC_deaths.txt', 'r').readlines()
ghC_survival = open('./battleRoyale/worldEvents/masks/ghC_survive.txt', 'r').readlines()

def grasshopper_cloud(refAlive, refDead, refDeadToday, refOutput, deathChance):
    refOutput.append({
        "colour": 0x000000,
        "message": "Uma nuvem de gafanhotos está passando pela arena",
        "img_url": "https://i.imgur.com/gk3io.gif"
    })
    for player in refAlive:
        if(random() <= deathChance):
            rq = randint(0, len(ghC_deaths) - 1);
            refOutput.append({
                "colour": 0x000000, 
                "message": ghC_deaths[rq].replace("@v@", player.name, 1)
            })
            refAlive.remove(player)
            refDead.append(player)
            refDeadToday.append(player)
        else:
            rq = randint(0, len(ghC_survival) - 1);
            refOutput.append({
                "colour": 0xffffff, 
                "message": ghC_survival[rq].replace("@v@", player.name, 1)
            })