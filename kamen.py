#Zkus napsat hru Kámen, nůžky, papír. Jak na to:

#Vytvoř si dvě proměnné, tah_cloveka a tah_pocitace
#Nastav tah_pocitace na "kámen", na tah_cloveka se uživatele zeptej
#Vypiš výsledky hry dle tahu člověka - buď 'Plichta.', 'Počítač vyhrál.' nebo 'Vyhrála jsi!'. #Vyhodnocení výsledku hry naprogramuj tak, jako by počítač mohl náhodně losovat 
#ze všech tří variant - naučíš ho to v příští lekci.
#Pokud nevíš, odevzdej i nekompletní řešení, koučové tě navedou!

'''from random import randrange

tah_cloveka = input("Uved zda davas kamen,nuzky nebo papir: ")
tah_pocitace = "kamen"

if tah_cloveka == tah_pocitace:
  print("Plichta")
elif tah_cloveka == "nuzky":
  print("Pocitac vyhral")
else:
  print("Vyhrala jsi")'''

from random import randrange

i = 0 

while i < 5:
  
  tah_cloveka = input("Uved zda davas kamen,nuzky nebo papir: ")
  tah_pocitace = randrange(3)


  if tah_cloveka == "kamen":
    if tah_pocitace == 0:
      print("Plichta")
    elif tah_pocitace == 1:
      print("Vyhrala jsi")
    else:
      print("Pocitac vyhral")
  elif tah_cloveka == "nuzky":
    if tah_pocitace == 0:
      print("Pocitac vyhral")
    elif tah_pocitace == 1:
      print("Plichta")
    else:
      print("Vyhrala jsi")
  elif tah_cloveka == "papir":
    if tah_pocitace == 0:
      print("Vyhrala jsi")
    elif tah_pocitace == 1:
      print("Pocitac vyhral")
    else:
      print("Plichta")
  i += 1 


  