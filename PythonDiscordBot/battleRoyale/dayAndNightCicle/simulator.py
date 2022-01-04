from battleRoyale.dayAndNightCicle.day import execDay
from battleRoyale.dayAndNightCicle.night import execNight

class simulator():
    def __init__(self, isDay, worldEventsChances):
        self.isDay = not isDay
        self.day = 1
        self.worldEventsChances = worldEventsChances

    def cicle(self, refAlive, refDead, refDeadToday, refOutput):
        self.isDay = not self.isDay
        if self.isDay:
            self.day += 1
            return execDay(self.day-1, self.worldEventsChances, refAlive, refDead, refDeadToday, refOutput)
        else:
            return execNight(self.day, self.worldEventsChances, refAlive, refDead, refDeadToday, refOutput)