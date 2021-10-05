from random import randint

SUN = ["https://i.imgur.com/G6H8Ydk.gif", "https://i.imgur.com/pvF0xRx.gif", "https://i.imgur.com/58aSPjU.jpg", "https://i.imgur.com/jJMLO3f.gif", "https://i.imgur.com/JBew5Iq.jpg"]
MOON = ["https://i.imgur.com/Y8PnM4q.gif", "https://i.imgur.com/2E10VH1.gif", "https://i.imgur.com/jVJ6Wj1.gif", "https://i.imgur.com/dxZJogU.jpg"]

def randomDayImage():
    return SUN[randint(0, len(SUN)-1)]

def randomNightImage():
    return MOON[randint(0, len(MOON)-1)]