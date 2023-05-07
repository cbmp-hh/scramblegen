import random as rnd
import os

print("Welcome to the first official realease of Python Rubik's cube scramble generator, v1.0 ")
os.system("pause")
print("\033c", end="")

while True:
    length = int(input("Input scramble length: "))
    face = ["U", "D", "R", "L", "F", "B"]
    lol = ["", "'", "2"]
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