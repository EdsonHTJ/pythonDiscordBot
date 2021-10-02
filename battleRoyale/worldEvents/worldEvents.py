from enum import Enum
from random import random
from battleRoyale.worldEvents.grasshopperCloud import grasshopper_cloud
from battleRoyale.worldEvents.toxic_cloud import toxic_cloud

class worldEvents():
    def __init__(self, players) -> None:
        self.alive = players

    def execEvent(self):
        alive = self.alive.copy()
        output, playersKilled, alive = eventsHandler.randomEvent(alive)
        return output, playersKilled, alive

class eventsHandler(Enum):
    TOXIC_CLOUD = lambda players: toxic_cloud(players, 0.5)
    GRASSHOPPER = lambda players: grasshopper_cloud(players, 0.5)

    def randomEvent(players):
        enumLength = 2
        equalOdds = 1/enumLength
        value = random()

        if value > equalOdds:
            return eventsHandler.TOXIC_CLOUD(players)
        else:
            return eventsHandler.GRASSHOPPER(players)