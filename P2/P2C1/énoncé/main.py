nombre1 = input("Entrez le nombre 1 :  ")
nombre2 = input("Entrez le nombre 2 : ")

if nombre1.isnumeric() and nombre2.isnumeric() :
  nombre1 = int(nombre1)
  nombre2 = int(nombre2)

  operation = input("Quelle operation souhaitez-vous realiser ?")

  match operation : 
    case "+" : 
      resultat = nombre1 + nombre2
    case "-" : 
      resultat = nombre1 - nombre2
    case "*" :
      resultat = nombre1 * nombre2
    case "/" :
      if nombre2 == 0 :
        raise SystemExit("Nombre 2 doit etre different de 0")
      else : 
        resultat = round(nombre1 / nombre2, 2)
    case _ : 
      raise SystemExit("Veuillez choisir un bon operateur")


  print(resultat)
  
else : 
  raise SystemExit("Fin du programme")