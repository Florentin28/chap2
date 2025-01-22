# __author__ = Florentin
# __version__ = 0.1

a = int(input("Entrez la valeur de a : "))  
b = int(input("Entrez la valeur de b : "))  
c = int(input("Entrez la valeur de b : "))  

print(f"Avant l'échange: a = {a}, b = {b}, c= {c}")

d=a
e=b
a=c
b=d
c=e

print(f"Après l'échange: a = {a}, b = {b}, c= {c}")
