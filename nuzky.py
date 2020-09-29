from random import randrange

i = 0 

while i < 5:
  
 tah_cloveka = input("Uved zda davas kamen,nuzky nebo papir: ")
 tah_pocitace = randrange(3)


 if tah_cloveka == "kamen" and tah_pocitace == 0 or tah_cloveka == "nuzky" and tah_pocitace == 1 or  tah_cloveka == "papir" and tah_pocitace == 2:
   print("Plichta")
 elif tah_cloveka == "kamen" and tah_pocitace == 1 or tah_cloveka == "nuzky" and tah_pocitace ==  2 or  tah_cloveka == "papir" and tah_pocitace == 0:
   print("Vitezis")
 elif tah_cloveka == "kamen" and tah_pocitace == 2 or tah_cloveka == "nuzky" and tah_pocitace == 0 or  tah_cloveka == "papir" and tah_pocitace == 1:
   print("Pocitac vitezi")
 else:
   exit()
 i += 1 

