nombres = input("Saisissez les nombres")

liste = nombres.split(',')
liste_entiers = []

for nombre in liste : 
  liste_entiers.append(int(nombre))


somme = sum(liste_entiers)
moyenne = somme / len(liste_entiers)

print(f"La somme est: {somme}")
print(f"La moyenne est: {moyenne}")

n_sup = 0

for nombre in liste_entiers : 
  if nombre > moyenne :
    n_sup += 1

print(n_sup)