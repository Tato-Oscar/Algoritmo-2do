
#Ejercicio 5
#romano a decimal
print("act5")

def romano(n):
    if n=="":
        return 0
    elif n[-1]=="i" or n[-1]=="I":
        return 1+romano(n[:-1])
    elif n[-1]=="v" or n[-1]=="V":
        return 5+romano(n[:-1])
    elif n[-1]=="x" or n[-1]=="X":
        return 10+romano(n[:-1])
    elif n[-1]=="l" or n[-1]=="L":
        return 50+romano(n[:-1])
    elif n[-1]=="c" or n[-1]=="C":
        return 100+romano(n[:-1])
    elif n[-1]=="d" or n[-1]=="D":
        return 500+romano(n[:-1])
    elif n[-1]=="m" or n[-1]=="M":
        return 1000+romano(n[:-1])
print(romano("MMXXVI")) 
print(romano("mmxxvi"))

print("---------------------------------------------------------")

#ejercicio 22
#mochila jedi
print("act22")

mochila=["manzana","telefono","cartera","libro","lapiz", "sable de luz"]

def usar_la_fuerza(mochila = str , cont = 0): 
    if not mochila:
        return False, cont
    objeto=mochila[0]

    if objeto=="sable de luz":
        return True, cont+1
    
    return usar_la_fuerza(mochila[1:], cont + 1)
objetoencontrado, cantidad = usar_la_fuerza(mochila)

print("El objeto se encuentra en la mochila:",objetoencontrado)
print("Cantidad de objetos revisados:",cantidad)

