#noi vogliamo programmare la roulettte
profitto=0
soldi=50
colori=["verde","rosso","nero"]
numeri=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38]
caselle=[]
for numero in numeri:
    if numero==0:
        casella=numero,colori[0]
        caselle.append(casella)
    
    elif numero%2==0:
        casella=numero,colori[1]
        caselle.append(casella)
    elif numero%2!=0:
        casella=numero,colori[2]
        caselle.append(casella)
print(caselle)
from random import choice
while soldi>0:
  modalità_gioco=input("cosa vuoi giocare?colore o numero?").lower()
  while modalità_gioco!="colore" and modalità_gioco!="numero":
      print("bro fai il serio e digita la modalità di gioco")
      modalità_gioco=input("cosa vuoi giocare?colore o numero?")
  if modalità_gioco=="colore":
     puntata=input("che colore vuoi giocare?").lower()
     while puntata.lower()!="rosso" and puntata.lower()!="nero" and puntata.lower()!="verde":
         print("Bro fai il serio")
         puntata=input("fai il serio e dimmi che colore vuoi giocare!")
     somma_giocata=int(input("quanti soldi vuoi giocare?"))
     while somma_giocata>soldi:
         print("Bro, mi sa che hai perso i conti, i tuoi soldi sono:",soldi)
         somma_giocata=int(input("quanti soldi vuoi giocare seriamente"))
     soldi=soldi-somma_giocata
     casella_casuale=choice(caselle)
     print("la casella vincente era",casella_casuale)
     if puntata.lower()==casella_casuale[1].lower():
         guadagno=somma_giocata*2
         print("bravo hai vinto ",guadagno)
         soldi=soldi+guadagno
         profitto=profitto+somma_giocata
     else:
         print("bro hai perso ",somma_giocata)
         profitto=profitto-somma_giocata
   
     print("il tuo profitto/perdita è di",profitto)
  elif modalità_gioco=="numero":
     casella_casuale=choice(caselle)
     puntata=int(input("che numero vuoi giocare?"))
     while puntata<0 or puntata>38:
         print("digita un numero corretto!")
         puntata=int(input("che numero vuoi giocare?"))

     somma_giocata=int(input("quanti soldi vuoi giocare?"))
     while somma_giocata>soldi:
         print("bro hai perso il conto, i tuoi soldi sono:",soldi)
         somma_giocata=int(input("quanti soldi vuoi giocare?"))
     
     if puntata==casella_casuale[0]:
         print("complimenti bro hai azzeccato il numero e hai vinto:",somma_giocata*36)
         profitto=profitto+somma_giocata*35
         soldi=soldi+(somma_giocata*35)
     else:
         print("bro hai perso",somma_giocata)
         soldi=soldi-somma_giocata
         profitto=profitto-somma_giocata
     print("la casella vincente era:",casella_casuale)
  print("i tuoi soldi sono:",soldi,"e il tuo profitto/perdita è:",profitto)


print("bro sei stirato")


       

    
