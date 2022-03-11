import random 
import time


pengar=100
raknare2=0
spelarepoang=0
fraga=""
fraga2=""
dealerpoang=0

#starthistoria
def Historia():
    time.sleep(1)

    print('''
            Du står på en häftig marknad
            Där finns fyra spännande ställen du går fram till det första
            Men du blir stoppad av väktare Andärz   ''')
    time.sleep(1)

    print('''
            |______|
             |x  x|
             |\__/|
             |    | 
          Väktare Andärz:
          "Hörududu du har ju inga pengar här kostar det 1000 kronor för att komma in i marknadens VIP
          Du får spela lite"''')
    time.sleep(2)
          
    print(''' 
          Du blir rädd av Andärz otroliga maskulinitet och backar
          Du kollar mot de andra 3 ställena

          Vid stället till vänster ser du folk med pilar i fötterna
          Vid stället i mitten ser du ledsamma typer lämna ett rum utan pengar
          Vid stället till höger ser du en skit gubbe''')
    time.sleep(1)
    print('''
          Vart går du du kan välja mellan:
          (vänster = v) (framåt = f) (höger = h) (bakåt = b)

          Du kollar i din ficka och ser hundra spänn som din mamma gav dig
          skriv "pengar" närsomhelst för att se hur mycket pengar du har''' )
    time.sleep(2)
    start()

#startplatsen
def start():
    global pengar
    print(f'''
          vart vill du gå?
          (vänster = v) (framåt = f) (höger = h) (bakåt = b) (pengar = Visar pengar) ''')
    fraga=str(input(">>"))
    fraga=fraga.lower()
    if fraga == "f":
        print(f'''
          Du kommer fram till dörren och ser att det står Blackjack!
          Vill du spela Blackjack? Ja eller nej''')
        fraga4=input(">>")
        fraga4=fraga4.lower()
        if fraga4 == "ja":
            blackjack()
        else:
            start()
    if fraga == "pengar":
        print(f"{pengar}")
        start()
    if fraga == "v":
        print(f'''
          du går mot stället med personer med pilar i fötterna
          Men du kommer fram så möter en väldigt hunkig man dig!
          ''')
        time.sleep(4)
        pilspel()
    if fraga == "h":
        print('''
        Du går in i rummet och där möts du av världsmästaren i skitgubbe
        RAGNAR!!! Hans explosiva vader ger dig rysningar''')
        time.sleep(1)
        Skitgubbe()
    if fraga == "b":
        time.sleep(2)
        if pengar < 1000:
            print(f'''
          "För i helvete, du har ju inte råd än"
          Säger Andärz argt samtidigt som han slungar iväg dig med en sjujävla fart!
          Så hårt och med sådan fantastisk precision att träffar bullseye med ditt huvud på piltavlan!
          du går därifrån med en brutal huvudvärk. :(
            
            |______|
             |x\/x|
             |┌──┐|
             |    | 

            ''')
            start()
        elif pengar >= 1000:
            print(f'''
          "WOW du har råd att komma in nu, GRATTIS!!!"
          Säger Andärz samtidigt som han låser upp dörren till rummet!
          Du betalar summan till Andärz och han lägger det direkt i fickan
          Du går in i rummet och framför ser du dig ett bord!
          På bordet ligger en ouppblåst badboll och en presentkort värt 100 spänn på ICA kvantum i Falkenberg!
            |______|
             |x  x|
             |\__/|
             |    | 
            
             ''')
            pengar-=1000 
            print(f'''
          Vill du gå tillbaka ut och spela igen eller vill du sluta spela?
                            <Fortsätta>   <Avsluta>
             ''')
            fraga2=str(input(">>"))
            fraga2=fraga2.lower()
            if fraga2 == "avsluta":
                print(f'''
          Tråkiga fan stick härifrån! :(
                ''')
            elif fraga2 == "fortsätta":
                print(f'''
          Vad kul att du vill fortsätta förlora pengar :)
          Observera att du har {pengar} Kvar!
                ''')
                time.sleep(2)
                start()
    if fraga == "avbryt":
        print('''
          Hejdå! :(
        ''')
    else:
        print(f''' 
          Skriv rätt Noob!''')
        start()

#blackjack gjort av Oscar Sköld!!!!!!
def blackjack():
    def randomkort():
        kort=random.choice(kortsiffra)
        return kort
    
    def randomtio():
        tiorand=random.choice(vardtio)
        return tiorand
    #spelarens kort funktion
    def spelplanprint():
        global raknare2
        s=spelare[0]
        if raknare2 == 0:
            s=spelare[0]
            print(f"Ditt första kort är!")
        elif raknare2 == 2:
            s=spelare[1]
            print(f"Ditt andra kort är!")
        elif raknare2 > 2:
            s=spelare[-1]
            print(f"Du fick!")
        randfarg=random.choice(kortfarg) 
        time.sleep(1)
        print(f'''
            ┌───────┐
            |   {randfarg}   |
            |       |
            |   {s}   |
            |       |
            |   {randfarg}   |
            └───────┘
        
        ''')
        raknare2=raknare2+1
        if raknare2 > 4:
            raknare2=4
    #Dealern kort funktioner
    def dealerplan():
        global raknare2
        d=dealer[0]
        if raknare2 == 1:
            d=dealer[0]
            print(f"Lennarts första kort är!")
            randfarg=random.choice(kortfarg)
            time.sleep(1)
            print(f'''
            ┌───────┐
            |   {randfarg}   |
            |       |
            |   {d}   |
            |       |
            |   {randfarg}   |
            └───────┘
                
            ''')
        elif raknare2 == 3:
            d=dealer[1]
            print(f"Lennarts andra kort är gömt!")
            print(f'''
            ┌───────┐
            |///////|
            |///////|
            |///////|
            |///////|
            |///////|
            └───────┘
        
        ''')

        elif raknare2 == 4:
            d=dealer[-1]
            randfarg=random.choice(kortfarg)
            print(f"Lennarts vänder på sitt andra kort och det är!")
            time.sleep(1)
            print(f'''
            ┌───────┐
            |   {randfarg}   |
            |       |
            |   {d}   |
            |       |
            |   {randfarg}   |
            └───────┘
                
            ''')
            print(f"Och har nu totalt {dealerpoang}")           

        elif raknare2 > 4:
            d=dealer[-1]
            randfarg=random.choice(kortfarg)
            print(f"Lennart drar ett till kort och får!")
            print(f'''
            ┌───────┐
            |   {randfarg}   |
            |       |
            |   {d}   |
            |       |
            |   {randfarg}   |
            └───────┘
                
            ''')
            print(f"Och har nu totalt {dealerpoang}")           
        raknare2=raknare2+1
    def spelargiv():
        global spelarepoang
        kort=randomkort()
        tiorand=randomtio()
        for x in kortsiffra:
            if x == kort:
                if x == 11:
                    spelare.append("A")
                elif x == 10:
                    spelare.append(tiorand)
                else:
                    spelare.append(kort)
        spelarepoang+=kort
    def dealergiv():
        global dealerpoang
        kort=randomkort()
        tiorand=randomtio()
        for x in kortsiffra:
            if x == kort:
                if x == 11:
                    dealer.append("A")
                elif x == 10:
                    dealer.append(tiorand)
                else:
                    dealer.append(kort)
        dealerpoang+=kort


    spelare=[ ]
    dealer=[ ]
    kortsiffra=(11,2,3,4,5,6,7,8,9,10)
    kortfarg=("♥","♦","♣","♠")
    vardtio=("J","Q","K",10)
    raknare=0
    bet=0
    betkoll=0
    fraga3=""
    global pengar
    global raknare2
    global spelarepoang
    global dealerpoang
    print(f'''
        ┌------------------------------------------------┐
        |          Välkommen till blackjack!             |
        |Det är jag som är Lennart och jag är din dealer!|           
        └------------------------------------------------┘
                                      
                            ┌────┐
                            |    |
                            |    |
                            |    |
                            |    |
                            |    |
                            |    |
                            |    |
                            |    |
                          __|____|__
                            |x  x|
                            |\__/|
                            |    | 
        
           
          
          ''')
    time.sleep(3)
    #spelarens hand
    while fraga3 !="nej":
        print(f"hur mycket vill du betta?")
        print(f"Du har: {pengar}")
        betfraga=int(input(">>"))
        bet=betfraga
        if pengar >= bet:
            pengar=pengar-bet
            betkoll=1
        if pengar < bet:
            while betkoll !=1:
                print(f"Du har inte så mycket pengar\nDu har: {pengar}\nBetta mindre!")
                bet=0
                betfraga=int(input(">>"))
                bet=betfraga
                if pengar >= bet:
                    pengar-=bet
                    betkoll=1
        while raknare != 2:
            spelargiv()
            raknare +=1
            #spelarepoang+=kort
        #Dealerns hand 
        while raknare !=4:
            dealergiv()
            raknare+=1

        #printar ut korten
        print(f'''
            Okej nu kör vi!
        ''')
        time.sleep(2)
        spelplanprint()
        time.sleep(2)
        dealerplan()
        time.sleep(2)
        spelplanprint()
        time.sleep(2)
        dealerplan()
        time.sleep(3)
        if "A" or "K" or "Q" or "J" or 10 in dealer[0]:
            print(f"Lennart kollar om han har fått en blackjack!")
            time.sleep(2)
            if dealerpoang == 21:
                print(f"WOW Lennart fick blackjack!\nTyvärr så förlorade du nu :(")
                start()
            else: 
                print(f"Som tur va så va de ingen blackjack!")
        if spelarepoang == 21:
            print(f"WOW, du fick en blackjack.\n grattis nu vann du! :)")
            pengar=(bet*2.5)+pengar
            start()
            
        if spelarepoang > 21:
            if "A" in spelare:
                spelarepoang -= 10
                spelare.remove("A")

        if dealerpoang > 21:
            if "A" in dealer:
                dealerpoang -=10
                dealer.remove("A")
        #frågar om du vill ha ett till kort och berättar poängen
        print(f"\nDu har just nu totalt {spelarepoang}\noch dealern har vad vi vet {dealer[0]}!")
        print(f"Vill du ha ett till kort? Ja eller nej!")
        fraga=str(input(">>"))
        fraga=fraga.lower()
        fraga2=""
        if fraga=="ja":
            while fraga2 != "nej":
                spelargiv()
                time.sleep(2)
                spelplanprint()
                if spelarepoang > 21:
                    if "A" in spelare:
                        spelarepoang-=10 
                        spelare.remove("A")                       
                    else:
                        print(f"Du har nu totalt {spelarepoang}\nvilket tyvärr är mer än 21 så du har förlorat:(")
                        raknare=0
                        raknare2=0
                        dealerpoang=0
                        spelarepoang=0
                        spelare.clear()
                        dealer.clear()
                        start()
                        
                print(f"Du har nu totalt {spelarepoang}\nvill du ha ett till kort?")
                fraga2=input(str(">>"))
        #vänder på dealerns andra kort
        time.sleep(2)
        dealerplan()
        time.sleep(3)
        #kollar poängen och bestämmer om dealern ska dra fler kort till sig själv
        if spelarepoang > 21:
            break        
        if dealerpoang < 17 and spelarepoang <= 21:
            while dealerpoang < 17:
                dealergiv()
        #skriver ut vad dealern får på sina nya kort
                dealerplan()
                time.sleep(2)
        #kollar vem som vann och ger ut rätt mängd pengar
        if dealerpoang > 21:
            print(f"Grattis! Dealern fick mer än 21!")
            print(f"Nu får du det dubbla du betta!")
            pengar=(bet*2)+pengar
        elif spelarepoang > dealerpoang:
            print(f"Grattis du vann!")
            print(f"Nu får du det dubbla du betta!")
            pengar=(bet*2)+pengar
            print(f"Du har nu: {pengar}!")
        elif spelarepoang < dealerpoang:
            print(f"Tyvärr du förlorade:(")
            print(f"Försök igen då vinner du kanske:)")
        elif spelarepoang == dealerpoang:
            print(f"Ni fick lika mycket!")
            print(f"Då får du tillbaka lika mycket som du betta!")
            pengar+=bet
        time.sleep(2)
        print(f"Vill du köra igen?")
        fraga3=input(">>")
        fraga3=fraga3.lower()
        if fraga3 == "nej":
            print(f"Din jävla tråkmåns stick härifrån! skriker Lennart")
            raknare=0
            raknare2=0
            dealerpoang=0
            spelarepoang=0
            spelare.clear()
            dealer.clear()
            start()

        raknare=0
        raknare2=0
        dealerpoang=0
        spelarepoang=0
        spelare.clear()
        dealer.clear()
#Oskars pilspel!!!!!
def pilspel():    

#Mina tavlor


    Brutus=('''
         \______/
          |x  x|
          |\__/|
          |    |
      |¯¯¯      ¯¯¯|
      | |        | |
     |T|          |T|
     ¯¯¯ | |¯¯| | ¯¯¯
         | |  | |
       |¯¯ |  | ¯¯|
       ¯¯¯¯    ¯¯¯¯  ''')
    Tom=('''
        ┌───────────┐
        |           |
        |           |
        |           |
        |           |
        |           |
        └───────────┘''')

    Bullseye=('''
        ┌───────────┐
        |           |
        |     _     |
        |    (x)    |
        |     ⎺     |
        |           |
        └───────────┘''')
    
    n1=('''
        ┌───────────┐
        |  _        |
        | (x)       |
        |  ⎺        |
        |           |
        |           |
        └───────────┘''')    
    n2=('''
        ┌───────────┐
        |        _  |
        |       (x) |
        |        ⎺  |
        |           |
        |           |
        └───────────┘''')
    
    n3=('''
        ┌───────────┐
        |           |
        |           |
        |        _  |
        |       (x) |
        |        ⎺  |
        └───────────┘''')
    
    n4=('''
        ┌───────────┐
        |           |
        |           |
        |  _        |
        | (x)       |
        |  ⎺        |
        └───────────┘''')
    
    b1=('''
        ┌───────────┐
        |           |
        |           |
        |           |      
        |           |      _
        |           |     (x)
        └───────────┘      ⎺  ''')
    
    b2=('''
        ┌───────────┐      _
        |           |     (x)
        |           |      ⎺
        |           |      
        |           |     
        |           |     
        └───────────┘''')
    
    b3=('''
        ┌───────────┐
        |           |
        |           |
        |           |      
 _      |           |     
(x)     |           |      
 ⎺      └───────────┘''')

    b4=('''
 _      ┌───────────┐
(x)     |           |
 ⎺      |           |
        |           |      
        |           |     
        |           |      
        └───────────┘''')
    
    #Min globala variabel
    global pengar
    
  

 #min första print utanför loopen
    slutfraga=""
    print(f'''
┌----------------------------------------------------------------┐
| Hallå jag heter Väktare Brutus och Välkommen till pilbågskytte |
| Om du skjuter dig i foten så ringer vi inte ambulansen         |
| Det kostar att spela så slösa inte på pengarna                 |
└----------------------------------------------------------------┘
            {Brutus}''')

#Min första while loop   
    while slutfraga != "nej":
        
        #Mina variabler
        nestan=n1,n2,n3,n4
        W= random.choice(nestan)
        Lengd= int(random.randrange(1, 26))
        Hojd= int(random.randrange(1, 31))
        antalpilar = 0
        Kraft=0
        Vinkel=0
        vinkelsvar = Hojd * 3
        kraftsvar = Lengd * 2
        DosSvar=vinkelsvar, kraftsvar
        Hint= random.choice(DosSvar)
        
        pengfraga=input("\nVill du spela pilskytte?\nDet kostar 25 Pengar\n(ja=kör)\n>>")
        pengfraga=pengfraga.lower()
        if pengfraga==("nej"):
            time.sleep(1)
            print("Noob grinda lite då")
            start()
    
        elif pengfraga=="ja" and pengar >=25:
            pengar -= 25
            print(f"Nu har du {pengar} pengar")
            
        else:
            start()

        if pengar < 25:
            time.sleep(1)
            print(f"Noob grinda mer pengar du har inte råd")
            time.sleep(1)
            start()
    
        #min andra loop
        while antalpilar != 3:
            
            #mer variabler som behövs inuti min andra loop
            fel=b1,b2,b3,b4
            L= random.choice(fel)

            #Mina första inputs
            time.sleep(1)
            print (f"\nTavlan är {Hojd} meter upp och den är {Lengd} meter bort")
            print(f"Här är tavlan\n {Tom}\n")
            Vinkel=int(input("Vid vilken vinkel skjuter du\nvälj mellan 0-90\n>>"))
            Kraft=int(input("Hur kraftfullt drar du pilbågen?\nvälj mellan 1-50\n>>"))
            antalpilar +=1
            
            #Hur programmet räknar och bestämmer poäng
            if Vinkel>90 or Kraft>50 or 0>Vinkel or 0>Vinkel:
                time.sleep(1)
                print("Kan du inte läsa du gjorde fel!!!\nVäktare Brutus är besviken >:(")
                time.sleep(1)


            elif Vinkel == vinkelsvar and Kraft == kraftsvar:
                time.sleep(1)
                print(Tom)
                time.sleep(1)
                print(Bullseye)  
                time.sleep(1)
                pengar += 75
                print(f"WOW Du träffa bullseye, du vann 75 pengar och nu har du {pengar} pengar")
                slutfraga=input("Bra jobbat! vill du köra igen\n>>")
                slutfraga=slutfraga.lower()
                if slutfraga==("nej"):
                    start()
    
                break
            
    
            elif Vinkel >= vinkelsvar-10 and Kraft >= kraftsvar-10 and Vinkel + Kraft < vinkelsvar+10 + kraftsvar+10 or Vinkel <= vinkelsvar+10 and Kraft <= kraftsvar+10 and Vinkel + Kraft > vinkelsvar-10 + kraftsvar-10:
                time.sleep(1)
                print(Tom)
                time.sleep(1)
                print(W)
                pengar += 50  
                time.sleep(1)
                print(f"Du träffade nästan bullseye, du vann 50 pengar och nu har du {pengar} pengar")
                slutfraga=input("Bra jobbat! vill du köra igen\n>>")
                slutfraga=slutfraga.lower()
                if slutfraga==("nej"):
                    start()
                break
            
            elif Vinkel >= vinkelsvar-15 and Kraft >= kraftsvar-15 and Vinkel + Kraft < vinkelsvar+15 + kraftsvar+15 or Vinkel + Kraft <= vinkelsvar+15 + kraftsvar+15 and Vinkel + Kraft > vinkelsvar-15 + kraftsvar-15:
                time.sleep(1)
                print(Tom)
                time.sleep(1)
                print(W)
                pengar += 25
                time.sleep(1)
                print(f"Du träffade knappt tavlan, du vann 25 pengar och nu har du {pengar} pengar")
                slutfraga=input("Bra jobbat! vill du köra igen\n>>")
                slutfraga=slutfraga.lower()
                if slutfraga==("nej"):
                    start()
                break

            elif Vinkel <= vinkelsvar and Kraft <= kraftsvar /2  or Vinkel >= vinkelsvar and Kraft >= kraftsvar *2:
                time.sleep(1)
                print(Tom)
                time.sleep(1)
                print(L)
                pengar += 0
                time.sleep(1)
                print(f"Du träffade inte ens tavlan, du vann 0 pengar och nu har du {pengar} pengar\nKör igen så du träffar kompis")
                time.sleep(2)
          
            else:
                print("Du missa kör igen")
            
            #Mitt system för att ge ledtrådar
            if antalpilar == 2:
                print(f"Här får du en ledtråd\nEn storhet är {Hint} du får gissa vilken som är vilken")
                time.sleep(1)
            
            if antalpilar == 3:
                time.sleep(1)
                print(f"Du missa alla försök detta var de rätta svaren\nkraften = {kraftsvar} och vinkeln var {vinkelsvar}\nbättre lycka till nästa gång!")
                slutfraga=input("vill du köra igen\n>>")
                slutfraga=slutfraga.lower()
                if slutfraga==("nej"):
                    start()
                break                
#Vilgot spel!!!!
def Skitgubbe():

    #Kollar om spelaren har vunnit, förlkorat eller om det är lika
    def vinnst():
        global pengar
        if (Kort_i_Hand[0] < Spelade_kort[0]) and (Kort_i_Hand[1] < Spelade_kort[0]) and (Kort_i_Hand[2] < Spelade_kort[0]) and (AI_kort_i_han[0] < Spelade_kort[0]) and (AI_kort_i_han[1] < Spelade_kort[0]) and (AI_kort_i_han[2] < Spelade_kort[0]) and (len(Kort_lek) == 0):
            print("Det blev oavgjort")
            input1 = input("Vill du köra igen? Y/N\n")
            input1 = input1.lower()
            if input1 == "y":
                Skitgubbe()
            if input1 == "n":
                ()
        if len(AI_kort_på_bord_gömda) == 0:
            print("Du förlorade")
            print(F"Du har nu {pengar} pengar kvar")

        if len(Kort_på_bord_gömda) == 0:
            print("Du vann")
            pengar = pengar + (beting *2)
            print(f"Du har nu {pengar} pengar")
            start()
        chek_kort()

    #äe den delen då du kan läga de kort som finns på bordet och de gömda korten
    def kort_på_bord():
        global pengar
        if len(Kort_på_bord) > 0:
            if (Kort_på_bord[0] < Spelade_kort[0]) and (Kort_på_bord[1] < Spelade_kort[0]) and (Kort_på_bord[2] < Spelade_kort[0]):
                print("Du har inte tilräklig höga kort det är din motståndares tur")
                AI_spelar()

            else:
                print(f"Dett senaste spelade kortet är {Spelade_kort[0]}\noch dina kort på bordet är {Kort_på_bord_farg[0]}{Kort_på_bord[0]} {Kort_på_bord_farg[1]}{Kort_på_bord[1]} {Kort_på_bord_farg[2]}{Kort_på_bord[2]}\n")
                input_kort = int(input(f"Vilket kort vil du spela?\n1.(första) 2.(andra) 3.(tredie)\n"))
                if input_kort == 1:
                    if Kort_på_bord >= Spelade_kort:
                        Kort = Kort_på_bord.pop(0)
                        Kort_på_bord_farg.pop(0)
                        Spelade_kort.append(Kort)
                        AI_spelar()
                    else:
                        print("Kan inte läga ett kort som är lägre än de senast spelade kort")
                        kort_på_bord()
                    
                if input_kort == 2:
                    if Kort_på_bord >= Spelade_kort:
                        Kort = Kort_på_bord.pop(1)
                        Kort_på_bord_farg.pop(1)
                        Spelade_kort.append(Kort)
                        AI_spelar()
                    else:
                        print("Kan inte läga ett kort som är lägre än de senast spelade kort")
                        kort_på_bord()

                if input_kort == 3:
                    if Kort_på_bord >= Spelade_kort:
                        Kort = Kort_på_bord.pop(2)
                        Kort_på_bord_farg.pop(2)
                        Spelade_kort.append(Kort)
                        AI_spelar()
                    else:
                        print("Kan inte läga ett kort som är lägre än de senast spelade kort")
                        kort_på_bord()
        #kolar om du har några av de synliga korteen på bordet kvar inan du kan läga de gömda
        if len(Kort_på_bord) == 0:
            print(f"Dett senaste spelade kortet är {Spelade_kort[0]}\nnu har du bara dina gömda kort kvar")
            input_kort = int(input(f"Vilket kort vil du spela?\n1.(första) 2.(andra) 3.(tredie)\n"))
            if input_kort == 1:
                Kort = Kort_på_bord_gömda.pop(0)
                Kort_på_bord_gömda_farg.pop(0)
                Spelade_kort.append(Kort)
                AI_spelar()
            
            if input_kort == 2:
                Kort = Kort_på_bord_gömda.pop(1)
                Kort_på_bord_gömda_farg.pop(1)
                Spelade_kort.append(Kort)
                AI_spelar()

            if input_kort == 3:
                Kort = Kort_på_bord_gömda.pop(2)
                Kort_på_bord_gömda_farg.pop(2)
                Spelade_kort.append(Kort)
                AI_spelar()
            else: 
                print("Kan inte läga ett kort som är lägre än de senast spelade kort")
                kort_på_bord()
    #kolar om dina kort är tillräkligt höga för att kuna bli spealde
    def chek_kort():
        if (Kort_i_Hand[0] < Spelade_kort[0]) and (Kort_i_Hand[1] < Spelade_kort[0]) and (Kort_i_Hand[2] < Spelade_kort[0]):
                #Om du inte har tilräkligt höga kort så byter du ut ett valfrit kort här
                print(f"Dett senaste spelade kortet är {Spelade_kort[0]}\nDina kort är {Kort_i_Hand_farg[0]}{Kort_i_Hand[0]} {Kort_i_Hand_farg[1]}{Kort_i_Hand[1]} {Kort_i_Hand_farg[2]}{Kort_i_Hand[2]}\n")
                input_kort2 = int(input(f"Vilket kort vill du byta till ett nyt?\n1.(första) 2.(andra) 3.(tredie)"))
                if input_kort2 == 1:
                    Kort = Kort_i_Hand.pop(0)
                    Kort_farg = Kort_i_Hand_farg.pop(0)
                    Kort_lek.append(Kort)
                    Kort_lek_farg.append(Kort_farg)
                    kort = random.choice(Kort_lek)
                    Kort_i_Hand.append(kort)
                    Kort_lek.remove(kort)
                    Kort_farg = random.choice(Kort_lek_farg)
                    Kort_i_Hand_farg.append(Kort_farg)
                    Kort_lek_farg.remove(Kort_farg)
                    vinnst()

                if input_kort2 == 2:
                    Kort = Kort_i_Hand.pop(1)
                    Kort_farg = Kort_i_Hand_farg.pop(1)
                    Kort_lek.append(Kort)
                    Kort_lek_farg.append(Kort_farg)
                    kort = random.choice(Kort_lek)
                    Kort_i_Hand.append(kort)
                    Kort_lek.remove(kort)
                    Kort_farg = random.choice(Kort_lek_farg)
                    Kort_i_Hand_farg.append(Kort_farg)
                    Kort_lek_farg.remove(Kort_farg)
                    vinnst()

                if input_kort2 == 3:
                    Kort = Kort_i_Hand.pop(2)
                    Kort_farg = Kort_i_Hand_farg.pop(2)
                    Kort_lek.append(Kort)
                    Kort_lek_farg.append(Kort_farg)
                    kort = random.choice(Kort_lek)
                    Kort_i_Hand.append(kort)
                    Kort_lek.remove(kort)
                    Kort_farg = random.choice(Kort_lek_farg)
                    Kort_i_Hand_farg.append(Kort_farg)
                    Kort_lek_farg.remove(Kort_farg)
                    vinnst()
                else: 
                    print("Kan inte läga ett kort som är lägre än de senast spelade kort")
                    chek_kort()

        Kort_spel_spelare()
    #Här väljer du vilket kort du vil spela och det kolar om de är tillräkligt höga för att kuna bli spelade
    def Kort_spel_spelare():
        print(f"Dett senaste spelade kortet är {Spelade_kort[0]}\nDina kort är {Kort_i_Hand_farg[0]}{Kort_i_Hand[0]} {Kort_i_Hand_farg[1]}{Kort_i_Hand[1]} {Kort_i_Hand_farg[2]}{Kort_i_Hand[2]}\n")
        if len(Kort_lek) > 0:
            input_kort = int(input("Vilket kort vil du spela\n1.(första) 2.(andra) 3.(tredie)"))
            if input_kort == 1:
                if Kort_i_Hand[0] >= Spelade_kort[0]:
                    L = Kort_i_Hand.pop(0)
                    Kort_i_Hand_farg.pop(0)
                    Spelade_kort.insert(0, L)
                    Spelar_kort()
                else: 
                    print("Kan inte läga ett kort som är lägre än de senast spelade kort")
                    Kort_spel_spelare()
            if input_kort == 2:
                if Kort_i_Hand[1] >= Spelade_kort[0]:
                    L = Kort_i_Hand.pop(1)
                    Kort_i_Hand_farg.pop(1)
                    Spelade_kort.insert(0, L)
                    Spelar_kort()
                else: 
                    print("Kan inte läga ett kort som är lägre än de senast spelade kort")
                    Kort_spel_spelare()
            if input_kort == 3:
                if Kort_i_Hand[2] >= Spelade_kort[0]:
                    L = Kort_i_Hand.pop(2)
                    Kort_i_Hand_farg.pop(2)
                    Spelade_kort.insert(0, L)
                    Spelar_kort()
                else: 
                    print("Kan inte läga ett kort som är lägre än de senast spelade kort")
                    Kort_spel_spelare()
            if   input_kort > 3:
                print("Finns inte")
                Kort_spel_spelare() 
        elif Kort_lek == 0:
            kort_på_bord() 
    #Här leger den till ett kort i din hand efter att du har splelat
    def Spelar_kort():
        Kort = random.choice(Kort_lek)
        Kort_i_Hand.append(Kort)
        Kort_lek.remove(Kort)
        Kort_farg = random.choice(Kort_lek_farg)
        Kort_i_Hand_farg.append(Kort_farg)
        Kort_lek_farg.remove(Kort_farg)
        AI_chek_kort()
    #Här kolar den om AIns kort är tillräkligt höga för att kuna bli spelade
    def AI_chek_kort():
        if (AI_kort_i_han[0] < Spelade_kort[0]) and (AI_kort_i_han[1] < Spelade_kort[0]) and (AI_kort_i_han[2] < Spelade_kort[0]):
            AI_kort_i_han.sort()
            Kort = AI_kort_i_han.pop(0)
            Kort_farg = AI_kort_i_hand_farg.pop(0)
            Kort_lek.append(Kort)
            Kort_lek_farg.append(Kort_farg)
            kort = random.choice(Kort_lek)
            AI_kort_i_han.append(kort)
            Kort_lek.remove(kort)
            Kort_farg = random.choice(Kort_lek_farg)
            AI_kort_i_hand_farg.append(Kort_farg)
            Kort_lek_farg.remove(Kort_farg)
            AI_chek_kort()
        AI_spelar()

    #Här är där AIn väjler och separ sina kort
    def AI_spelar():
        i = 0
        if len(AI_kort_i_han) != 0:
           
            while i < 1:
                Kort = random.choice(AI_kort_i_han)
                if Kort >= Spelade_kort[0]:
                    Spelade_kort.insert(0, Kort)
                    for x in AI_kort_i_han:
                        if Kort == x:
                            L = AI_kort_i_han.index(x)
                    AI_kort_i_han.pop(L)
                    AI_kort_i_hand_farg.pop(L)
                    i += 1

            if len(Kort_lek) != 0:
                if len(AI_kort_i_han) < 3:
                    kort = random.choice(Kort_lek)
                    AI_kort_i_han.append(kort)
                    Kort_lek.remove(kort)
                    Kort_farg = random.choice(Kort_lek_farg)
                    AI_kort_i_hand_farg.append(Kort_farg)
                    Kort_lek_farg.remove(Kort_farg)
        if len(AI_kort_i_han) == 0:
            i = 0
            while i < 1:
                Kort = random.choice(AI_kort_på_bord)
                if Kort >= Spelade_kort[0]:
                    Spelade_kort.insert(0, Kort)
                    for x in AI_kort_på_bord:
                        if Kort == x:
                            L = AI_kort_på_bord.index(x)
                    AI_kort_på_bord.pop(L)
                    AI_kort_på_bord_farg.pop(L)
        if len(AI_kort_på_bord) == 0:
            i = 0
            while i < 1:
                Kort = random.choice(AI_kort_på_bord_gömda)
                if Kort >= Spelade_kort[0]:
                    Spelade_kort.insert(0, Kort)
                    for x in AI_kort_på_bord_gömda:
                        if Kort == x:
                            L = AI_kort_på_bord_gömda.index(x)
                    AI_kort_på_bord_gömda.pop(L)
                    AI_kort_på_bord_gömda_farg.pop(L)

        vinnst()

    #de variablar och lister som används
    global pengar
    global namn
    global beting
    global AI_kort_i_han, Spelade_kort, AI_kort_i_hand_farg, Kort_siffra_list, Kort_lek, Kort_lek_farg, Kort_i_Hand, Kort_i_Hand_farg, Kort_på_bord, Kort_på_bord_farg, Kort_på_bord_gömda, Kort_på_bord_gömda_farg, AI_kort_på_bord, AI_kort_på_bord_farg, AI_kort_på_bord_gömda, AI_kort_på_bord_gömda_farg
    o = 0
    u = 1
    k = 0
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
    Kort_siffra_list = [14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    Kort_farg_list = ["♥", "♦", "♣", "♠"]
    #Här skapas en kortlek
    while o != 52:
        kort = random.choice(Kort_siffra_list)
        Kort_lek.append(kort)
        Kort_farg = random.choice(Kort_farg_list)
        Kort_lek_farg.append(Kort_farg)
        o += 1
    #Här delas jkort utt till både AIn och spelaren
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
    
    #Intro
    print('''
           ______
          /|x  x|\\
       ____|\__/|____
      /||          ||\\
      ||            ||
       |  |______|  |
       [|I|]    [|I|]
       [|O|]    [|O|]
    ___[|I|]    [|I|]___
    |______|    |______|
    ''')
    time.sleep(2)
    print('''
    ┌--------------------------------------------------------------┐
    | Hihihi Jag är RAGNAR universums bästa skitgubbe              |                                                 
    | Ingen har nånsin ens kommit nära att slå mig                 |
    | Förra personen jag körde emot fick scoliosis när han förlora |
    | Jag kommer totalt äga dig noob!!!                            |
    └--------------------------------------------------------------┘
    ''')
    time.sleep(1)


    print(f"Jag har några speciella regler")
    time.sleep(2)
    print(f"Det som är annorlunda är\n1. korten har inga speciella egenskaper")
    time.sleep(1.5)
    print(f"2. Lägger du fyra av samma så vänds inte högen bort")
    time.sleep(1.5)
    print(f"3. Jag börjar alltid")
    time.sleep(1.5)
    print(f"4. Pågrund av att jag aldrig har gillat att man har mer en tre kort i handen så om du inte har tillräckligt höga kort så kan du byta utt ett kort i taget till det är tillräkligt högt")
    time.sleep(2)

    print(f"Dina kort i din hand är {Kort_i_Hand_farg[0]}{Kort_i_Hand[0]} {Kort_i_Hand_farg[1]}{Kort_i_Hand[1]} {Kort_i_Hand_farg[2]}{Kort_i_Hand[2]}")
    print(f"Dina kort på bordet är {Kort_på_bord_farg[0]}{Kort_på_bord[0]} {Kort_på_bord_farg[1]}{Kort_på_bord[1]} {Kort_på_bord_farg[2]}{Kort_på_bord[2]}")
    time.sleep(1)
    print(f"\nDina motstådares kort på bordet är {AI_kort_på_bord_farg[0]}{AI_kort_på_bord[0]} {AI_kort_på_bord_farg[1]}{AI_kort_på_bord[1]} {AI_kort_på_bord_farg[2]}{AI_kort_på_bord[2]}")
    time.sleep(2)
    while u == 1:
        print(f"Hur mycket vill du beta?\nDU har {pengar} pengar kvar")
        #Här bestämer du hur mycket du vil beta
        beting = int(input(""))
        if beting > pengar:
            print("Du har inte tilräkligt mycke pengar")
            time.sleep(3)
        else:
            pengar = pengar - beting
            u += 1
            time.sleep(3)
    Kort = random.choice(AI_kort_i_han)
    Spelade_kort.insert(0, Kort)
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
    AI_chek_kort()

Historia()