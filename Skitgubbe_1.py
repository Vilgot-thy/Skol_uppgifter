import time
import random

def spelplan(a,b,c,d,e,f,g,h,j,k,l,m,n):
    print(f"""   
    ┌───────────────────────────┐
    |   ┌───┐   ┌───┐   ┌───┐   | ┌───┐ ┌───┐ ┌───┐
    |   |   |   |   |   |   |   | |   | |   | |   |
    |   |{g}|   |{h}|   |{j}|   | |{k}| |{l}| |{m}|
    |   └───┘   └───┘   └───┘   | └───┘ └───┘ └───┘
    |                           |
    |           ┌───┐           |
    |           |   |           |
    |           |{n}|           |
    |           └───┘           |
    |                           |
    |   ┌───┐   ┌───┐   ┌───┐   | ┌───┐ ┌───┐ ┌───┐
    |   |   |   |   |   |   |   | |   | |   | |   |   
    |   |{d}|   |{e}|   |{f}|   | |{a}| |{b}| |{c}|
    |   └───┘   └───┘   └───┘   | └───┘ └───┘ └───┘
    └───────────────────────────┘   
                """)
    
def spelplan_2(a,b,c,d,e,f,g,h,j,k,l,m,n):
    print(f"""   
    ┌───────────────────────────┐
    |   ┌───┐   ┌───┐   ┌───┐   | ┌───┐ ┌───┐ ┌───┐
    |   |   |   |   |   |   |   | |   | |   | |   |
    |   |{g}|   |{h}|   |{j}|   | |{k}| |{l}| |{m}|
    |   └───┘   └───┘   └───┘   | └───┘ └───┘ └───┘
    |                           |
    |           ┌───┐           |
    |           |   |           |
    |           |{n}|           |
    |           └───┘           |
    |                           |
    |   ┌───┐   ┌───┐   ┌───┐   |
    |   |   |   |   |   |   |   |   
    |   |{d}|   |{e}|   |{f}|   |
    |   └───┘   └───┘   └───┘   |
    └───────────────────────────┘   
                """)
                
def spelplan_3(a,b,c,d,e,f,g,h,j,k,l,m,n):
    print(f"""   
    ┌───────────────────────────┐
    |   ┌───┐   ┌───┐   ┌───┐   |
    |   |   |   |   |   |   |   |   
    |   |{g}|   |{h}|   |{j}|   |
    |   └───┘   └───┘   └───┘   |
    |                           |
    |           ┌───┐           |   
    |           |   |           |
    |           |{n}|           |
    |           └───┘           |
    |                           |
    |   ┌───┐   ┌───┐   ┌───┐   | ┌───┐ ┌───┐ ┌───┐
    |   |   |   |   |   |   |   | |   | |   | |   |   
    |   |{d}|   |{e}|   |{f}|   | |{a}| |{b}| |{c}|
    |   └───┘   └───┘   └───┘   | └───┘ └───┘ └───┘
    └───────────────────────────┘     
                """)

def spelplan_4(a,b,c,d,e,f,g,h,j,k,l,m,n):
    print(f"""   
    ┌───────────────────────────┐
    |   ┌───┐   ┌───┐   ┌───┐   |
    |   |   |   |   |   |   |   |   
    |   |{g}|   |{h}|   |{j}|   |
    |   └───┘   └───┘   └───┘   |
    |                           |
    |           ┌───┐           |   
    |           |   |           |
    |           |   |           |
    |           └───┘           |
    |                           |
    |   ┌───┐   ┌───┐   ┌───┐   |
    |   |   |   |   |   |   |   |   
    |   |{a}|   |{b}|   |{c}|   |
    |   └───┘   └───┘   └───┘   |
    └───────────────────────────┘   
                """)

def Skitgubbe():
    o = 0
    k = 0
    pengar = 0
    Kort_i_Hand = []
    Kort_på_bordet_gömda = []
    Kort_på_bordet = []
    Spelade_kort = []
    Kort_lek = []
    Kort_siffra = {"14", "2", "3", "4", "5", "6", "7", "8", "9", "10","11", "12", "13"}
    Kort_farg = {"♥", "♦", "♣", "♠"}
    
    while o != 4:
        for n in (Kort_siffra):
            for f in (Kort_farg):
                Kort_lek.append([f, n])
        o += 1
# Kort_på_bordet_gömda[0], Kort_på_bordet_gömda[1], Kort_på_bordet_gömda[2]
    while k != 3:
        kort = random.choice(Kort_lek)
        Kort_på_bordet.append(kort)
        kort = random.choice(Kort_lek)
        Kort_på_bordet_gömda.append(kort)
        kort = random.choice(Kort_lek)
        Kort_i_Hand.append(kort)
        spelplan(Kort_i_Hand[0], Kort_i_Hand[1], Kort_i_Hand[2], Kort_på_bordet[0], Kort_på_bordet[1], Kort_på_bordet[2])
        k += 1
    print(Kort_i_Hand)
    print(Kort_på_bordet_gömda)
    print(Kort_på_bordet)

spelplan()
Skitgubbe()