from enum import Enum
from random import random

class Events(Enum):
    NOTHING = 0
    SINGLEKILL = 1
    DEATH = 2
    #MULTIKILL = 3
    VERSUS = 4

    def randomEvent(dc, skc, vc):
        value = random()
        if value > dc:
            return Events.DEATH
        elif value > skc:
            return Events.SINGLEKILL
        elif value > vc:
            return Events.VERSUS
        else:
            return Events.NOTHING