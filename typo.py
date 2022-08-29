# Typo Library
# version 0.1
import random

def dropLetter(targetString):
    # drop a letter from the string
    x = len(targetString)
    nuke = random.randint(1,x-1)
    outputString = (targetString[0:nuke]) + (targetString[nuke+1:])
    return outputString 

def transposeLetters(targetString):
    # swap two letters in the string
    x = len(targetString)
    targetLetter = random.randint(1,x-1)
    A = targetString[targetLetter]
    if (targetLetter == 1):
        A = A.toLower
        swapLetter = 2
    elif (targetLetter == x-1):
        swapLetter = x-2


def alterCaps(targetString):
    x = random.randint(1,100)
    if (x >= 1) and (x <= 49):
        targetString = targetString.upper()
    elif (x >= 50) and (x < 100):
        targetString = targetString.lower()
    else:
        # only for 100 
        targetString = targetString.swapcase()
    return targetString


    return targetString

def insertLetter(targetString):
    return targetString

def wrongLetter(targetString):
    return targetString

def doubleCaps(targetString):
    return targetString

# randomly drop a character, except the very first
print(dropLetter("Octopodes"))
print(alterCaps("Holy shit, people, what are you thinking?"))