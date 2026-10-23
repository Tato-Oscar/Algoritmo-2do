from typing import Any, Optional
from Listaheroes import superheroes
from Estructuras import BinaryTree

arbol_mcu = BinaryTree()
for personaje in superheroes:
    arbol_mcu.insert_node(personaje["name"], other_value=personaje)

print("b villanos ordenados alfabeticamente")
arbol_mcu.inorden_villain()

print("c superheroes que empiezan con 'C'")
arbol_mcu.inorden_hero_star_with('C')

print("d cantidad de superheroes en el arbol")
print(f"Total de superheroes {arbol_mcu.count_heroes()}")

print("e corregir nombre de Doctor Strange")
print("Buscando 'strange' por proximidad")
arbol_mcu.proxy_search('strange') 

nodo_mal = arbol_mcu.search("Dr. Strange")
if nodo_mal:
    viejo_nombre = nodo_mal.value
    _, datos_personaje = arbol_mcu.delete_node(viejo_nombre)
    nuevo_nombre = "Doctor Strange"
    datos_personaje["name"] = nuevo_nombre
    arbol_mcu.insert_node(nuevo_nombre, other_value=datos_personaje)
    print(f"Modificacion exitosa de '{viejo_nombre}' a '{nuevo_nombre}'")

print("f superheroes en orden descendente")
arbol_mcu.postorden_hero()

print("g generar bosques de superheroes y otro de villanos")
arbol_heroes = BinaryTree()
arbol_villanos = BinaryTree()

def dividir_bosque(root):
    if root is not None:
        if root.other_values['is_villain']:
            arbol_villanos.insert_node(root.value, root.other_values)
        else:
            arbol_heroes.insert_node(root.value, root.other_values)
        dividir_bosque(root.left)
        dividir_bosque(root.right)

dividir_bosque(arbol_mcu.root)

def contar_nodos_totales(root):
    if root is None:
        return 0
    return 1 + contar_nodos_totales(root.left) + contar_nodos_totales(root.right)

print(f"i Nodos en arbol heroes: {contar_nodos_totales(arbol_heroes.root)}")
print(f"i Nodos en arbol villanos: {contar_nodos_totales(arbol_villanos.root)}")

print("i barrido alfabetico  arbol de heroes")
arbol_heroes.inorden()

print("i barrido alfabetico  arbol de villanos")
arbol_villanos.inorden()