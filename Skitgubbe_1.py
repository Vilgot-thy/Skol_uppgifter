import time
import random

def spelplan(a,b,c,d,e,f,g,h,j,k,l,m,n,o,p,q,r,s,t,v,u,x,y,z,å,ä):
    print(f"""   
    ┌───────────────────────────┐
    |   ┌───┐   ┌───┐   ┌───┐   | ┌───┐ ┌───┐ ┌───┐
    |   |{u}|   |{x}|   |{y}|   | |{z}| |{å}| |{ä}|
    |   |{g}|   |{h}|   |{j}|   | |{k}| |{l}| |{m}|
    |   └───┘   └───┘   └───┘   | └───┘ └───┘ └───┘
    |                           |
    |           ┌───┐           |
    |           |{v}|           |
    |           |{n}|           |
    |           └───┘           |
    |                           |
    |   ┌───┐   ┌─────┐   ┌───┐   | ┌───┐ ┌───┐ ┌───┐
    |   |{r}|     |  {s} |   |{t}|   | |{o}| |{p}| |{q}|   
    |   |{d}|    |  {e} |   |{f}|   | |{a}| |{b}| |{c}|
    |   └───┘   └─────┘   └───┘   | └───┘ └───┘ └───┘
    └───────────────────────────┘   
                """)
    
def spelplan_2(d,e,f,g,h,j,k,l,m,n,r,s,t,v,u,x,y,z,å,ä):
    print(f"""   
    ┌───────────────────────────┐
    |   ┌───┐   ┌───┐   ┌───┐   | ┌───┐ ┌───┐ ┌───┐
    |   |{u}|   |{x}|   |{y}|   | |{z}| |{å}| |{ä}|
    |   |{g}|   |{h}|   |{j}|   | |{k}| |{l}| |{m}|
    |   └───┘   └───┘   └───┘   | └───┘ └───┘ └───┘
    |                           |
    |           ┌───┐           |
    |           |{v}|           |
    |           |{n}|           |
    |           └───┘           |
    |                           |
    |   ┌───┐   ┌───┐   ┌───┐   |
    |   |{r}|   |{s}|   |{t}|   |   
    |   |{d}|   |{e}|   |{f}|   |
    |   └───┘   └───┘   └───┘   |
    └───────────────────────────┘   
                """)
                
def spelplan_3(a,b,c,d,e,f,g,h,j,n,o,p,q,r,s,t,v,u,x,y):
    print(f"""   
    ┌───────────────────────────┐
    |   ┌───┐   ┌───┐   ┌───┐   |
    |   |{u}|   |{x}|   |{y}|   |
    |   |{g}|   |{h}|   |{j}|   |
    |   └───┘   └───┘   └───┘   |
    |                           |
    |           ┌───┐           |
    |           |{v}|           |
    |           |{n}|           |
    |           └───┘           |
    |                           |
    |   ┌───┐   ┌───┐   ┌───┐   | ┌───┐ ┌───┐ ┌───┐
    |   |{r}|   |{s}|   |{t}|   | |{o}| |{p}| |{q}|   
    |   |{d}|   |{e}|   |{f}|   | |{a}| |{b}| |{c}|
    |   └───┘   └───┘   └───┘   | └───┘ └───┘ └───┘
    └───────────────────────────┘   
                """)

def spelplan_4(d,e,f,g,h,j,n,r,s,t,v,u,x,y):
    print(f"""   
    ┌───────────────────────────┐
    |   ┌───┐   ┌───┐   ┌───┐   |
    |   |{u}|   |{x}|   |{y}|   |
    |   |{g}|   |{h}|   |{j}|   |
    |   └───┘   └───┘   └───┘   |
    |                           |
    |           ┌───┐           |
    |           |{v}|           |
    |           |{n}|           |
    |           └───┘           |
    |                           |
    |   ┌───┐   ┌───┐   ┌───┐   |
    |   |{r}|   |{s}|   |{t}|   |   
    |   |{d}|   |{e}|   |{f}|   |
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
    Kort_i_Hand_farg = []
    Kort_på_bordet_gömda_farg = []
    Kort_på_bordet_farg = []
    Kort_lek = []
    Kort_lek_farg = []
    Kort_siffra_list = {"14", "2", "3", "4", "5", "6", "7", "8", "9", "10","11", "12", "13"}
    Kort_farg_list = {"♥", "♦", "♣", "♠", "♥", "♦", "♣", "♠", "♥", "♦", "♣", "♠", "♥", "♦", "♣", "♠"}
    
    while o != 4:
        for n in (Kort_siffra_list):
            Kort_lek.append(n)
        for f in (Kort_farg_list):
            Kort_lek_farg.append(f) 
        o += 1
# Kort_på_bordet_gömda[0], Kort_på_bordet_gömda[1], Kort_på_bordet_gömda[2]
    while k != 3:
        kort = random.choice(Kort_lek)
        Kort_lek.remove(kort)
        Kort_på_bordet.append(kort)
        kort = random.choice(Kort_lek)
        Kort_lek.remove(kort)
        Kort_på_bordet_gömda.append(kort)
        kort = random.choice(Kort_lek)
        Kort_lek.remove(kort)
        Kort_i_Hand.append(kort)

        Kort_farg = random.choice(Kort_lek_farg)
        Kort_lek_farg.remove(Kort_farg)
        Kort_på_bordet_farg.append(Kort_farg)
        Kort_farg = random.choice(Kort_lek_farg)
        Kort_lek_farg.remove(Kort_farg)
        Kort_på_bordet_gömda_farg.append(Kort_farg)
        Kort_farg = random.choice(Kort_lek_farg)
        Kort_lek_farg.remove(Kort_farg)
        Kort_i_Hand_farg.append(Kort_farg)  

        k += 1
    spelplan(Kort_i_Hand[0], Kort_i_Hand[1], Kort_i_Hand[2], Kort_på_bordet[0], Kort_på_bordet[1], Kort_på_bordet[2], 1, 2, 3, 4, 5, 6, 7,Kort_i_Hand_farg[0],Kort_i_Hand_farg[1],Kort_i_Hand_farg[2],Kort_på_bordet_farg[0],Kort_på_bordet_farg[1],Kort_på_bordet_farg[2],1,2,3,4,5,6,7)

    print(Kort_i_Hand)
    print(Kort_på_bordet_gömda)
    print(Kort_på_bordet)

Skitgubbe()
spelplan()