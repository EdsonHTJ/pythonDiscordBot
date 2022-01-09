from enum import Enum
from random import random
from battleRoyale.worldEvents.grasshopperCloud import grasshopper_cloud
from battleRoyale.worldEvents.toxic_cloud import toxic_cloud

class worldEvents():
    def __init__(self, refAlive, refDead, refDeadToday, refOutput) -> None:
        self.alive = refAlive
        self.dead = refDead
        self.deadToday = refDeadToday
        self.output = refOutput

    def execEvent(self):
        eventsHandler.randomEvent(self.alive, self.dead, self.deadToday, self.output)

class eventsHandler(Enum):
    TOXIC_CLOUD = lambda refAlive, refDead, refDeadToday, refOutput: toxic_cloud(refAlive, refDead, refDeadToday, refOutput, 0.5)
    GRASSHOPPER = lambda refAlive, refDead, refDeadToday, refOutput: grasshopper_cloud(refAlive, refDead, refDeadToday, refOutput, 0.5)

    def randomEvent(refAlive, refDead, refDeadToday, refOutput):
        enumLength = 2
        equalOdds = 1/enumLength
        value = random()

        if value > equalOdds:
            return eventsHandler.TOXIC_CLOUD(refAlive, refDead, refDeadToday, refOutput)
        else:
            return eventsHandler.GRASSHOPPER(refAlive, refDead, refDeadToday, refOutput)