from enum import Enum

class States(Enum):
    ALIVE = 0
    INJURIED = 1
    DEAD = 2

class player():
    def __init__(self, name, chances) -> None:
        self.name = name
        self.status = States.ALIVE
        self.life = 100
        self.stamina = 100
        self.SINGLEKILLCHANCE = chances[0]
        self.DEATHCHANCE = chances[1]
        self.VERSUSCHANCE = chances[2]
    
    def __str__(self):
        return f'name: {self.name}, status: {self.status}, life: {self.life}, stamina: {self.stamina}, skc: {self.SINGLEKILLCHANCE}, dc: {self.DEATHCHANCE}, vc: {self.VERSUSCHANCE}'

    def __copy__(self):
        return player(self.name, [self.SINGLEKILLCHANCE, self.DEATHCHANCE, self.VERSUSCHANCE])