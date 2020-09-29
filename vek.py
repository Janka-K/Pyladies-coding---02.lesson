vek = int(input("Zadej vek: "))

if vek < 0:
  print("Zadej kladne cislo")
elif vek < 3:
  print("Das si sunar?")
elif vek <15:
  print("Das si vodu?")
elif vek < 18:
  limo = input("Das si kolu nebo fantu?")
  if limo == "kolu" or limo == "Kolu":
    print("Tady mas kolu")
  elif limo == "fantu" or limo == "Fantu":
    print("Tady mas fantu")
  else:
    print(limo, "bohuzel nemame")
else:
    pivo = input("Das si pivo?")
    if pivo == "ano":
      druh = input("Das si desitku, dvanactku nebo nealko?")
      if druh == "desitku" or druh == "Desitku": # pokud pouzijeme logicky operator OR
        print("Tady mas desitku")                # je potreba vzdy zopakovat promennou viz priklad
                                                  # pro pivo - promenna druh 
      elif druh == "dvanactku" or druh == "Dvanactku":
        print("Tady mas dvanactku")
      elif druh == "nealko" or druh == "Nealko":
        print("Tady mas nealko")
      else:
        print(druh, "bohuzel nemame")
    else:
      print("Das si kolu nebo fantu?")      
          
          