# Ecrivez votre code ici
def salaire_mensuel(salaire_annuel) :
  return salaire_annuel / 12

def salaire_hebdomadaire(salaire_mensuel) :
  return salaire_mensuel / 4

def salaire_horaire(salaire_hebdomadaire, heures_travaillees) :
  return salaire_hebdomadaire / heures_travaillees

salaire_an = print("Veuillez renseigner votre salaire annuel.")
h_travaillees = print("Veuillez renseigner le nombre d'heures par semaine.")

salaire_an = float(salaire_an)
h_travaillees = float(h_travaillees)

salaire_m = salaire_mensuel(salaire_an)
salaire_hebdo = salaire_hebdomadaire(salaire_m)
salaire_h = salaire_horaire(salaire_hebdo, h_travaillees)



