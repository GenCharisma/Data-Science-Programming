# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 19:33:31 2021

"""
import random
playertaken = 0
computertaken = 0
difficulty = 0
sticks = 0
pull = 0


def smartai(x):
    for i in smartlist:
        if (sticks+2) % (pull+1) == i:
            if pulllist[smartlist.index(i)] == 0:
                x = random.randint(1, pull)
            else:
                x = pulllist[smartlist.index(i)]
    return x


print("The Sticks Pulling Game : the last player who pick the last stick lose\n")
name = input("What is your name? : ")

while pull <= 0:
    pull = int(input("What is maximum sticks that can be pulled at one time? : "))
    if pull <= 0:
        print("You can't use that number try again")
        pull = 0

smartpull = pull + 1
pulllist = list(range(smartpull))
pulllistnum = list(range(smartpull))
smartlist = list(range(smartpull))

for i in pulllist:
    pulllistnum[i] = (pulllist[i]+1)
    smartlist[i] = (pulllistnum[i]+2) % (smartpull)

while sticks <= 0:
    sticks = int(input("how many sticks in the pile? : "))
    if sticks <= 0:
        print("You can't use that number try again")
        sticks = 0
    elif sticks < pull:
        print("You need at least", pull, "sticks for this game")
        sticks = 0
while difficulty > 2 or difficulty < 1:
    difficulty = int(
        input("Choose AI play style, 1 = Normal Random, 2 = Intelligently : "))
    if difficulty > 2 or difficulty < 1:
        print("invalide play style, try again")
if difficulty == 1:
    print("\n", name, "has selected Normal Random AI")
elif difficulty == 2:
    print(name, "has selected Intelligently AI\n")
print("There are", sticks, "sticks in the pile.\n")
while sticks > 0:
    if difficulty == 1:
        computertaken = random.randint(1, pull)
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
    while 0 <= playertaken <= pull:
        playertaken = int(
            input("\n" + str(name) + ", how many stick(s) you will take? (from 1 to " + str(pull) + ") : "))
        if 0 < playertaken <= pull:
            if playertaken <= sticks:
                sticks -= playertaken
                print("There are", sticks, "stick(s) left in the pile.\n")
                playertaken = 0
                if sticks <= 0:
                    print("You take the last stick, AI WON (Python WON)")
                    break
                break
            elif playertaken > sticks:
                print("There are not enough stick(s) to take")
        elif (playertaken <= 0):
            print("No, you cannot take less than 1 stick!")
        elif (playertaken > pull):
            print("No, you cannot take more than", pull, "sticks!")
        playertaken = 0
