
vstup = input("Zadej delku strany: ")
strana = float(vstup)
#print(4 * strana)

delka_je_kladna = strana > 0

if delka_je_kladna:
  obvod = 4 * strana 
  obsah = strana ** 2

  print("Nasledujici hodnoty jsou spravne", delka_je_kladna)

#objem = strana ** 3
# obvod ctverce 4 * strana
# obsah ctverce strana * strana nebo strana ** 


  print("Obvod čtverce se stranou", strana , "cm je", obvod ,"cm")
  print("Obsah čtverce se stranou", strana,  "cm je" ,obsah,"cm2")
#print("Objem krychle se stranou", strana, "cm je", objem, "cm3")

  print("Obsah / obvod je", obsah / obvod)

else:
  print("Zadej kladne cislo")