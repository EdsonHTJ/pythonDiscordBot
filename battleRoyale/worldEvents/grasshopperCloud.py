from random import random
from random import randint

ghC_deaths = open('./battleRoyale/worldEvents/masks/ghC_deaths.txt', 'r').readlines()
ghC_survival = open('./battleRoyale/worldEvents/masks/ghC_survive.txt', 'r').readlines()

def grasshopper_cloud(alive, deathChance):
    output = [{
        "colour": 0x000000,
        "message": "Uma nuvem de gafanhotos está passando pela arena",
        "img_url": "https://i.imgur.com/gk3io.gif"
    }]
    playersKilled = []
    for player in alive:
        if(random() <= deathChance):
            rq = randint(0, len(ghC_deaths) - 1);
            output.append({
                "colour": 0x000000, 
                "message": ghC_deaths[rq].replace("@v@", player.name, 1)
            })
            playersKilled.append(player)
        else:
            rq = randint(0, len(ghC_survival) - 1);
            output.append({
                "colour": 0xffffff, 
                "message": ghC_survival[rq].replace("@v@", player.name, 1)
            })
    for player in playersKilled:
        alive.remove(player)
        
    return output, playersKilled, alive