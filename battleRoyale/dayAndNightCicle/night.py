from random import random
from random import randint
from battleRoyale.events.events import execEvent
from battleRoyale.worldEvents.worldEvents import worldEvents
from battleRoyale.utils.randomImages import randomNightImage

def execNight(counter, worldEventsChances, refAlive, refDead, refDeadToday, refOutput):
    refOutput.append({
        "img_url": randomNightImage(),
        "colour": 0x0b2496, 
        "message": f'   Começo da noite {counter} -- :waxing_gibbous_moon:\n',
        "footer": {
            "text": "Mensagens aleatórias motivacionais",
            "icon_url": "https://snipstock.com/assets/cdn/png/ba1ab80ab5c41f4ed9031496422a4855.png"
        }
    })
    if(random() <= worldEventsChances):
        worldEvents(refAlive, refDead, refDeadToday, refOutput).execEvent()
    else: 
        for turns in range(8 if len(refAlive) >= 8 else len(refAlive)-1 if len(refAlive) > 4 else 4):
            if(len(refAlive) == 1):
                return
            execEvent(refAlive, refDead, refDeadToday, refOutput)
        increaseStamina(refAlive)
        payRespect(refAlive, refDead, refDeadToday, refOutput)

def payRespect(refAlive, refDead, refDeadToday, refOutput):
    if(len(refDeadToday) == 0):
        return
    refOutput.append({"colour": 0x000000, "message": f':fireworks: Canhões ecoam pela noite. {len(refDeadToday)} participantes morreram :fireworks:.\n'})
    output = 'Participantes mortos: '
    for player in refDeadToday:
        output += player.name + ', '
    refOutput.append({"colour": 0x000000, "message": f'{output}\n'})


def increaseStamina(refAlive):
    for player in refAlive:
        player.stamina += randint(0, 100 - player.stamina)