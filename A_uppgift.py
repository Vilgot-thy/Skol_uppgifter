#importerade moduler
import time

#Funktioner
def area_cirkel():
    a = int(input("Ange cirkelns radie i cm \n"))
    sum = a*a*3.14
    return sum

def omkräts_cirkel():
    a = int(input("Ange cirkelns diameter \n"))
    sum = a *3.14
    return sum

def volym_rätblock():
    a = int(input("Ange höjden av rätblock i cm \n"))
    b = int(input)("Ange djupet av rätblock i cm \n")
    c = int(input("Ange längden av rätblock i cm \n"))
    sum = a*b*c
    return sum

def volym_sfär():
    a = int(input("Age radien för sfären i cm "))
    sum = (4*3.14*a**3)/3
    return sum

#while
i = 0

while i < 2:
    #Huvudfråga
    print("Vad vill du göra ")
    print("1. Vill du beräkna arean på en cirkel? ")
    print("2. vill du beräkna omkrätsen av en cirkel? ")
    print("2. vill du beräkna omkrätsen av en cirkel? ")
    print("3. Vill du beräkna volymen av en sfär? ")
    print("4. Vill du beräkna volymen av ett rätblock? ")
    print("5. Avsluta ")
    input_1 = input()
    input_1.lower()

    #if-satser
    if input_1 == "1":
        summa = area_cirkel()
        print(f"Cirkens area är {summa} cm")
        time.sleep(3)
    if input_1 == "2":
        summa = omkräts_cirkel()
        print(f"Cirkelns omkräts är {summa} cm")
        time.sleep(3)
    if input_1 == "3":
        summa = volym_sfär()
        print(f"Sfärens volym är {summa} cm")
        time.sleep(3)
    if input_1 == "4":
        summa = volym_rätblock()
        print(f"Rätblockets volym är {summa} cm")
        time.sleep(3)
    if input_1 == "5":
        i = 2
        print("Tack för att du annvände mitt pogram :)")
        time.sleep(1)
