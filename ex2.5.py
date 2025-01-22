# __author__ = Florentin
# __version__ = 0.1

nom_article = input("Veuillez entrer le nom de l'article : ")
prix_htva = float(input("Veuillez entrer le prix de l'article : "))
taux_tva = float(input("Veuillez entrer le taux de TVA (en pourcentage) : "))
nombre_article = int(input("Veuillez entrer le nombre d'articles : "))

tvac = prix_htva * (1 + taux_tva / 100) * nombre_article

print(f"Le prix TVAC de '{nom_article}' est de : {tvac:.2f} €")
