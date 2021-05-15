
from PIL import Image
img=Image.open("dnk.png")
img.show

import random

def play():
    p1=input("player 1,Enter tour name")
    p2=input("player 2,Enter your name")
    pp1=0
    pp2=0
    turn=0
    end=100
    while(1):
        if(turn%2==0):
            print(p1," your turn")
            c=int(input("press 1 to continue or 0 to quit"))
            if(c==0):
                print(p1,",your score:",pp1)
                print(p2,",your score:",pp2)
                print("thanks for playing")
                break
            dice=random.randint(1,6)
            print("dice shown:",dice)
            pp1=pp1+dice
            pp1=check_ladder(pp1)
            pp1=check_snake(pp1)
            if(pp1>end):
                pp1=end
            if(pp1==100):
                print(p1," won")
                break
        
        else:
            print(p2," your turn")
            c=int(input("press 1 to continue or 0 to quit"))
            if(c==0):
                print(p1,",your score:",pp1)
                print(p2,",your score:",pp2)
                print("thanks for playing")
                break
            dice=random.randint(1,6)
            print("dice shown:",dice)
            pp2=pp2+dice
            pp2=check_ladder(pp2)
            pp2=check_snake(pp2)
            if(pp2>end):
                pp2=end
            if(pp2==100):
                print(p2," won")
                break
        turn=turn+1

def check_ladder(points):
    if(points==8):
        print("ladder")
        return 26
    elif(points==21):
        print("ladder")
        return 82
    elif(points==43):
        print("ladder")
        return 77
    elif(points==50):
        print("ladder")
        return 91
    elif(points==54):
        print("ladder")
        return 93
    elif(points==62):
        print("ladder")
        return 96
    elif(points==66):
        print("ladder")
        return 87
    elif(points==80):
        print("ladder")
        return 100
    else:
        return points
def check_snake(points):
    if(points==44):
        print("snake")
        return 22
    elif(points==46):
        print("snake")
        return 5
    elif(points==48):
        print("snake")
        return 9
    elif(points==52):
        print("snake")
        return 11
    elif(points==55):
        print("snake")
        return 7
    elif(points==59):
        print("snake")
        return 17
    elif(points==64):
        print("snake")
        return 36
    elif(points==69):
        print("snake")
        return 33
    elif(points==73):
        print("snake")
        return 1
    else:
        return points
    
play()