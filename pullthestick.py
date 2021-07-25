# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 19:33:31 2021

"""
import random
playertaken = 0
computertaken = 0
difficulty = 0
sticks = 0


def smartai(x):
    if sticks == 4:  # lost
        x = random.randint(1, 2)
    if sticks % 3 == 0:
        x = 2
    elif sticks % 2 == 0:
        x = 1
    elif sticks == 5 or 11:
        x = 1
    else:
        x = random.randint(1, 2)
    return x


name = input("What is your name : ")
while sticks <= 0:
    sticks = int(input("how many sticks in the pile? : "))
    if sticks <= 0:
        print("You can't use that number try again")
        sticks = 0
    elif sticks < 5:
        print("You need at least 5 sticks for this game")
        sticks = 0
while difficulty > 2 or difficulty < 1:
    difficulty = int(
        input("Choose AI play style, 1 = Normal Random, 2 = Intelligently : "))
    if difficulty > 2 or difficulty < 1:
        print("invalide play style, try again")
if difficulty == 1:
    print(name, "has selected Normal Random AI\n")
elif difficulty == 2:
    print(name, "has selected Intelligently AI\n")
print("There are", sticks, "sticks in the pile.\n")
while sticks > 0:
    if difficulty == 1:
        computertaken = random.randint(1, 2)
    elif difficulty == 2:
        computertaken = smartai(computertaken)
    if computertaken > sticks:
        computertaken = 1
        sticks = 0
    else:
        sticks = sticks-computertaken
    print("I take {0} stick(s).\nThere are {1} sticks in the pile".format(
        computertaken, sticks))
    if sticks <= 0:
        print("\nPython take the last stick,", name, "WON")
        break
    while 0 <= playertaken <= 2:
        playertaken = int(
            input(str(name) + ", how many stick(s) you will take? (1 or 2) : "))
        if 0 < playertaken <= 2:
            if playertaken <= sticks:
                sticks -= playertaken
                print("There are", sticks, "stick(s) left in the pile.\n")
                playertaken = 0
                if sticks <= 0:
                    print("You take the last stick, I WON (Python WON)")
                    break
                break
            elif playertaken > sticks:
                print("There are not enough stick(s) to take")
        elif (playertaken <= 0):
            print("No you cannot take less than 1 stick!")
        elif (playertaken > 2):
            print("No you cannot take more than 2 sticks!")
        playertaken = 0
