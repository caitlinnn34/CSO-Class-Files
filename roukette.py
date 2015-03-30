import random

def randomNumber():
    number = random.randint(1,10)
    return number
    
def rouletteSimulation(numberGuess, evenOrOdd, colorGuess):
    blackList = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 29, 31, 33, 35]