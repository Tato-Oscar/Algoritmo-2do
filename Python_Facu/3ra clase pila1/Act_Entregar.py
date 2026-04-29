
from stack import Stack
# Ejercicio 22
# class Mision:
#     def __init__(self, planeta, captura, recompensa): 
#         self.planeta = planeta 
#         self.captura = captura
#         self.recompensa = recompensa

# def procesar_bitacora(pila_misiones, nombre_cazador):
#     pila_aux = Stack() 


#     while pila_misiones.size() > 0:
#         pila_aux.push(pila_misiones.pop())

#     print(f" bitacora de {nombre_cazador}")
#     print("Planetas visitados:")

#     total_recaudado = 0
#     cantidad_capturas = 0
#     mision_numero = 1
#     mision_han_solo = None


#     while pila_aux.size() > 0:
#         mision = pila_aux.pop()


#         print(f" - {mision.planeta}")

#         total_recaudado += mision.recompensa
#         cantidad_capturas += 1

#         if mision.captura == "Han Solo":
#             mision_han_solo = mision_numero

#         pila_misiones.push(mision)
#         mision_numero += 1


#     print(f"Total créditos: {total_recaudado}")
#     print(f"Capturas: {cantidad_capturas}")
#     if mision_han_solo is not None:
#         print(f"Misión Han Solo: {mision_han_solo} (desde el fondo)")
    
#     return total_recaudado

# pila_boba = Stack()
# pila_boba.push(Mision("Kamino", "Rebelde", 5000))
# pila_boba.push(Mision("Tatooine", "Han Solo", 250000)) 
# pila_boba.push(Mision("Coruscant", "Ladrón", 15000))


# pila_din = Stack()
# pila_din.push(Mision("Nevarro", "Mythrol", 4000))
# pila_din.push(Mision("Arvala-7", "Grogu", 0))


# creditos_boba = procesar_bitacora(pila_boba, "Boba Fett")
# creditos_din = procesar_bitacora(pila_din, "Din Djarin")

# print(" resultado final")
# if creditos_boba > creditos_din:
#     print(" Boba Fett obtuvo mayor fortuna.")
# elif creditos_din > creditos_boba:
#     print("Din Djarin obtuvo mayor fortuna.")
# else:
#     print("Ambos recaudaron lo mismo.")

#Ejercicio 24
# class Personaje:
#     def __init__(self, nombre, peliculas):
#         self.nombre = nombre
#         self.peliculas = peliculas

# def analizar_personajes_mcu(pila):
#     pila_aux = Stack()
    
#     posicion = 1
#     pos_rocket = None
#     pos_groot = None
#     mas_de_5_peliculas = []
#     peliculas_viuda_negra = 0
#     nombres_cdg = []
    
#     while pila.size() > 0:
#         pj = pila.pop()
        
#         if pj.nombre == "Rocket Raccoon":
#             pos_rocket = posicion
#         elif pj.nombre == "Groot":
#             pos_groot = posicion
            
#         if pj.peliculas > 5:
#             mas_de_5_peliculas.append((pj.nombre, pj.peliculas)) 
            
#         if pj.nombre == "Black Widow" or pj.nombre == "Viuda Negra":
#             peliculas_viuda_negra = pj.peliculas
            
#         primera_letra = pj.nombre[0].upper()
#         if primera_letra in ['C', 'D', 'G']:
#             nombres_cdg.append(pj.nombre)
            
#         pila_aux.push(pj)
#         posicion += 1
        
#     while pila_aux.size() > 0:
#         pila.push(pila_aux.pop())
        

#     print("Posiciones desde la cima:")
#     print(f"   - Rocket Raccoon: {pos_rocket if pos_rocket else 'No está'}")
#     print(f"   - Groot: {pos_groot if pos_groot else 'No está'}")
    
#     print(" Personajes en más de 5 películas:")
#     for nombre, cant in mas_de_5_peliculas:
#         print(f"   - {nombre} ({cant} películas)")
        
#     print(f"La Viuda Negra participó en {peliculas_viuda_negra} películas.")
    
#     print("Personajes que empiezan con C, D o G:")
#     for nombre in nombres_cdg:
#         print(f"   - {nombre}")


# pila_mcu = Stack()
# pila_mcu.push(Personaje("Groot", 4))          
# pila_mcu.push(Personaje("Captain America", 9))
# pila_mcu.push(Personaje("Doctor Strange", 4))
# pila_mcu.push(Personaje("Iron Man", 10))
# pila_mcu.push(Personaje("Black Widow", 8))
# pila_mcu.push(Personaje("Rocket Raccoon", 5)) 

# analizar_personajes_mcu(pila_mcu)