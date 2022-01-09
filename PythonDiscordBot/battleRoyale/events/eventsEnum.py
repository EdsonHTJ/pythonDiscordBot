from enum import Enum
from random import random

class Events(Enum):
    NOTHING = 0
    SINGLEKILL = 1
    DEATH = 2
    #MULTIKILL = 3
    VERSUS = 4

    def randomEvent(dc, skc, vc):
        chances = [{"chance":dc, "event":Events.DEATH},
                    {"chance":skc,"event":Events.SINGLEKILL},
                    {"chance":vc, "event":Events.VERSUS}]

        rouletteWheelPosition = random()*sum([chance['chance'] for chance in chances ])
        chances = sorted(chances,key = lambda chance: chance['chance'],reverse=True)
        spinWhell = 0
        for i in range(len(chances)):
            spinWhell +=  chances[i]["chance"]
            if rouletteWheelPosition < spinWhell:
                return chances[i]['event']

        return Events.NOTHING