import time
import random

pengar = 100

def Skitgubbe():
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
    Kort_siffra_list = {"14", "2", "3", "4", "5", "6", "7", "8", "9", "10","11", "12", "13"}
    Kort_farg_list = {"♥", "♦", "♣", "♠", "♥", "♦", "♣", "♠", "♥", "♦", "♣", "♠", "♥", "♦", "♣", "♠"}
    
    while o != 4:
        for n in (Kort_siffra_list):
            Kort_lek.append(n)
        o += 1
        for f in (Kort_farg_list):
            Kort_lek_farg.append(f)

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
        print(Kort_lek_farg)
        Kort_farg = random.choice(Kort_lek_farg)
        AI_kort_på_bord_gömda_farg.append(Kort_farg)
        Kort_lek_farg.remove(Kort_farg)
        Kort_farg = random.choice(Kort_lek_farg)
        AI_kort_i_hand_farg.append(Kort_farg)
        Kort_lek_farg.remove(Kort_farg)

        k += 1
    print(Kort_i_Hand)
    print(Kort_på_bord_gömda)
    print(Kort_på_bord)

    print(Kort_i_Hand_farg)
    print(Kort_på_bord_farg)
    print(Kort_på_bord_gömda_farg)

    print(AI_kort_i_han)
    print(AI_kort_på_bord)
    print(AI_kort_på_bord_gömda)

    while match == 0:
        print(f""" Nu är matchen i gång
                  Du kan se dina längst ner och motståndarens kort längst upp  

                                    Måtståndare:
                                      Påbordet:
                            {AI_kort_på_bord_farg[0],AI_kort_på_bord[0]} {AI_kort_på_bord_farg[1],AI_kort_på_bord[1]} {AI_kort_på_bord_farg[2],AI_kort_på_bord[2]}



                        
                  """)
        match += 1



    print(Kort_i_Hand)
    print(Kort_på_bordet_gömda)
    print(Kort_på_bordet)

Skitgubbe()