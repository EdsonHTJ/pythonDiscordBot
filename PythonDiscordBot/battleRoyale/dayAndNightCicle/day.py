from random import random
from battleRoyale.events.events import execEvent
from battleRoyale.worldEvents.worldEvents import worldEvents
from battleRoyale.utils.randomImages import randomDayImage, randomNightImage

def execDay(counter, worldEventsChances, refAlive, refDead, refDeadToday, refOutput):
    refOutput.append({
        "img_url": randomDayImage(), 
        "colour": 0xfff370, 
        "message": f'   Começo do dia {counter} -- :sunrise:\n',
        "footer": {
            "text": "Mensagens aleatórias motivacionais",
            "icon_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Emoji_u2600.svg/1200px-Emoji_u2600.svg.png"
        }
    })
    while(len(refDeadToday) > 0):
        refDeadToday.pop()

    if(random() <= worldEventsChances):
        worldEvents(refAlive, refDead, refDeadToday, refOutput).execEvent()
    else:
        for turns in range(8 if len(refAlive) >= 8 else len(refAlive)-1 if len(refAlive) > 4 else 4):
            if(len(refAlive) == 1):
                return
            execEvent(refAlive, refDead, refDeadToday, refOutput)