from random import randint

deaths = open('./battleRoyale/DEATH.txt', 'r').readlines()

def eventDeath(player, refAlive, refDead, refDeadToday, refOutput):
    refDead.append(player)
    refDeadToday.append(player)

    rq = randint(0, len(deaths) - 1);
    refOutput.append({
        "colour": 0x000000, 
        "message": deaths[rq].replace("@v@", player.name, 1)
    })