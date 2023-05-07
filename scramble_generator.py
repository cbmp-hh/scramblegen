import random as rnd
import os

while True:
    length = int(input("Enter scramble length... "))
    face = ["U", "D", "R", "L", "F", "B"]
    lol = ["2", "'", ""]
    scramble = ""
    lastface = ""
    for x in range(length):
        randface = face[rnd.randint(0,5)]
        
        while randface == lastface:
            randface = face[rnd.randint(0,5)]
            
        scramble += randface + lol[rnd.randint(0,2)] + " "
        lastface = randface

    print(scramble)
    os.system("pause")
    print("\033c", end="")