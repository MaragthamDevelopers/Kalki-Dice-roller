#Dice roller script v1.0 by MaragthamDevelopers






import random
import time
while(True):
    times = int( input('Amount of rolls: '))
    if(times > 0):
        break
    else:
        print("The amount of rolls must be at least one")
while(True):
    sides = int( input('Amount of sides: '))
    if(sides > 3):
        break
    else:
        print("The dice needs to have at least four faces")
while(True):
    numberOfDice = int( input('Number of dice per roll: '))
    if(numberOfDice > 0):
        break
    else:
        print("The number of dice needs to be at least one")
while(True):    
    wait = float( input('Seconds in between each roll: '))
    if(wait >= 0):
        break
    else:
        print("The interval between each roll must be equal or greater than 0")
timesSoFar = int(0)
while timesSoFar != times:
    print([random.randint(1, sides) for ndice in range(0,numberOfDice)])
    timesSoFar += 1
    time.sleep(wait)
while timesSoFar == timesSoFar:
    time.sleep(1)
