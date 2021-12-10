import time
import random
from typing import Union

pengar = 100
namn = ""

def AI_spelar():    
    Kort = random.choice(AI_kort_i_han)
    Spelade_kort.append(Kort)
    for x in AI_kort_i_han:
        if Kort == x:
            L = AI_kort_i_han.index(x)
    AI_kort_i_han.pop(L)
    AI_kort_i_hand_farg.pop(L)

    if len(Kort_lek) != 0:
        if len(AI_kort_i_han) < 3:
            kort = random.choice(Kort_lek)
            AI_kort_i_han.append(kort)
            Kort_lek.remove(kort)
            Kort_farg = random.choice(Kort_lek_farg)
            AI_kort_i_hand_farg.append(Kort_farg)
            Kort_lek_farg.remove(Kort_farg)


def beting():
    global pengar
    u = 1
    while u == 1:
        print(f"Hur mycket vill du beta?\nDU har {pengar} pengar kvar")
        beting = int(input(""))
        if beting > pengar:
            print("Du har inte tilräkligt mycke pengar")
            time.sleep(3)
        else:
            pengar = pengar - beting
            u += 1
            time.sleep(3)



def Skitgubbe():
    global pengar
    global namn
    global AI_kort_i_han, Spelade_kort, AI_kort_i_hand_farg, Kort_siffra_list, Kort_lek, Kort_lek_farg
    u = 1
    o = 0
    k = 0
    match = 0
    Kort_i_Hand = []
    Kort_på_bord_gömda = []
    Kort_på_bord = []
    Kort_i_Hand_farg = []
    Kort_på_bord_gömda_farg = []
    Kort_på_bord_farg = []
    Spelade_kort = []
    AI_kort_i_han = []
    AI_kort_på_bord = []
    AI_kort_på_bord_gömda = []
    AI_kort_i_hand_farg = []
    AI_kort_på_bord_farg = []
    AI_kort_på_bord_gömda_farg = []
    Kort_lek = []
    Kort_lek_farg = []
    Kort_siffra_list = ["14", "2", "3", "4", "5", "6", "7", "8", "9", "10","11", "12", "13"]
    Kort_farg_list = ["♥", "♦", "♣", "♠"]



    while o != 52:
        kort = random.choice(Kort_siffra_list)
        Kort_lek.append(kort)
        Kort_farg = random.choice(Kort_farg_list)
        Kort_lek_farg.append(Kort_farg)
        o += 1

    while k != 3:
        kort = random.choice(Kort_lek)
        Kort_på_bord.append(kort)
        Kort_lek.remove(kort)
        kort = random.choice(Kort_lek)
        Kort_på_bord_gömda.append(kort)
        Kort_lek.remove(kort)
        kort = random.choice(Kort_lek)
        Kort_i_Hand.append(kort)
        Kort_lek.remove(kort)

        Kort_farg = random.choice(Kort_lek_farg)
        Kort_på_bord_farg.append(Kort_farg)
        Kort_lek_farg.remove(Kort_farg)
        Kort_farg = random.choice(Kort_lek_farg)
        Kort_på_bord_gömda_farg.append(Kort_farg)
        Kort_lek_farg.remove(Kort_farg)
        Kort_farg = random.choice(Kort_lek_farg)
        Kort_i_Hand_farg.append(Kort_farg)
        Kort_lek_farg.remove(Kort_farg)

        Kort = random.choice(Kort_lek)
        AI_kort_i_han.append(Kort)
        Kort_lek.remove(Kort)
        Kort = random.choice(Kort_lek)
        AI_kort_på_bord.append(kort)
        Kort_lek.remove(Kort)
        Kort = random.choice(Kort_lek)
        AI_kort_på_bord_gömda.append(kort)
        Kort_lek.remove(Kort)

        Kort_farg = random.choice(Kort_lek_farg)
        AI_kort_på_bord_farg.append(Kort_farg)
        Kort_lek_farg.remove(Kort_farg)
        Kort_farg = random.choice(Kort_lek_farg)
        AI_kort_på_bord_gömda_farg.append(Kort_farg)
        Kort_lek_farg.remove(Kort_farg)
        Kort_farg = random.choice(Kort_lek_farg)
        AI_kort_i_hand_farg.append(Kort_farg)
        Kort_lek_farg.remove(Kort_farg)
        k += 1


    
    print(f"Hej I detta rumet kommer vi köra några omgångar av skitgubbe MED MIN REGLER!")
    time.sleep(3)
    print(f"Det som är anorlunda med mina regler är\n1. korten har inga spesiela egenskaper")
    print(f"2. Läger du fyra av sama så vänds inte högen bort")
    print(f"3. Jag börjar altid")




    print(f"Dina kort i din hand är {Kort_i_Hand_farg[0]}{Kort_i_Hand[0]} {Kort_i_Hand_farg[1]}{Kort_i_Hand[1]} {Kort_i_Hand_farg[2]}{Kort_i_Hand[2]}")
    print(f"Dina kort på bordet är {Kort_på_bord_farg[0]}{Kort_på_bord[0]} {Kort_på_bord_farg[1]}{Kort_på_bord[1]} {Kort_på_bord_farg[2]}{Kort_på_bord[2]}")
    time.sleep(2)
    print(f"\nDina motstådares kort på bordet är {AI_kort_på_bord_farg[0]}{AI_kort_på_bord[0]} {AI_kort_på_bord_farg[1]}{AI_kort_på_bord[1]} {AI_kort_på_bord_farg[2]}{AI_kort_på_bord[2]}")

    beting()

    AI_spelar()


    
    

Skitgubbe()
