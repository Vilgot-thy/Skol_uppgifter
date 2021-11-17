#mina funktioner 
def add(a, b):
    sum = a + b
    return sum

def multi(a, b):
    sum = a * b
    return sum

def divi(a, b):
    sum = a / b
    return sum

def sub(a, b):
    sum = a - b
    return sum

#inputs om tal och beräkning
tal_1 = int(input("Skriv in dit första tal "))

tal_2 = int(input("Skriv in dit andra tal "))

print("skriv in vilket sät du vill annvända dina tal. DU kan använda multi (muliplikation) divi (divition) add (addera) sub (subtraktion)")
input = input("")

#If satser, räkningen samt utskriften
if input == "add":
    beräkning = add

if input == "divi":
    beräkning = divi

if input == "multi":
    beräkning = multi

if input == "sub":
    beräkning = sub

summa = beräkning(tal_1, tal_2)

print(summa)