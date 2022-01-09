from random import random
from random import randint

tC_deaths = open('./battleRoyale/worldEvents/masks/tC_deaths.txt', 'r').readlines()
tC_survival = open('./battleRoyale/worldEvents/masks/tC_survive.txt', 'r').readlines()

def toxic_cloud(refAlive, refDead, refDeadToday, refOutput, deathChance):
    refOutput.append({
        "colour": 0x18b52a,
        "message": "Uma nuvem tóxica começa a emanar das bordas da arena",
        "img_url": "https://i.pinimg.com/originals/65/e1/59/65e159269a9efc656460a230fd3bbaee.gif"
    })
    for player in refAlive:
        if(random() <= deathChance):
            rq = randint(0, len(tC_deaths) - 1);
            refOutput.append({
                "colour": 0x000000, 
                "message": tC_deaths[rq].replace("@v@", player.name, 1)
            })
            refAlive.remove(player)
            refDead.append(player)
            refDeadToday.append(player)
        else:
            rq = randint(0, len(tC_survival) - 1);
            refOutput.append({
                "colour": 0xffffff, 
                "message": tC_survival[rq].replace("@v@", player.name, 1)
            })