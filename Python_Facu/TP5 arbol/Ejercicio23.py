from typing import Any, Optional
from Criaturas import datos_criaturas
from Estructuras import BinaryTree

arbol_mitos = BinaryTree()

for c in datos_criaturas:
    c["descripcion"] = "Sin descripcion"
    c["capturada"] = None 
    arbol_mitos.insert_node(c["name"], other_value=c)

print("a listado inorden de criaturas y quien las derroto")
def inorden_derrotados(root):
    if root is not None:
        inorden_derrotados(root.left)
        derrotado = root.other_values.get("derrotado_por") or "Nadie"
        print(f"Criatura: {root.value:25} | Derrotada por: {derrotado}")
        inorden_derrotados(root.right)
inorden_derrotados(arbol_mitos.root)

print("b Cargar una breve descripcion sobre una criatura")
nodo = arbol_mitos.search("Talos")
if nodo:
    nodo.other_values["descripcion"] = "Gigante de bronce que protegia a Creta."
    print("Descripcion de Talos cargada.")

print(" c Mostrar toda la informacion de la criatura Talos")
nodo = arbol_mitos.search("Talos")
if nodo:
    print(f"Nombre: {nodo.value}")
    for clave, valor in nodo.other_values.items():
        print(f"- {clave.capitalize()}: {valor}")

print("d Los 3 heroes/dioses que derrotaron mas criaturas")
conteo_heroes = {}
def contar_derrotas(root):
    if root is not None:
        heroe = root.other_values.get("derrotado_por")
        if heroe:
            conteo_heroes[heroe] = conteo_heroes.get(heroe, 0) + 1
        contar_derrotas(root.left)
        contar_derrotas(root.right)
contar_derrotas(arbol_mitos.root)

top_3 = sorted(conteo_heroes.items(), key=lambda x: x[1], reverse=True)[:3]
for i, (heroe, cantidad) in enumerate(top_3, 1):
    print(f"{i}. {heroe}: {cantidad} derrotas")

print("e Listar las criaturas derrotadas por heracles")
def derrotadas_por(root, heroe_buscado):
    if root is not None:
        if root.other_values.get("derrotado_por") == heroe_buscado:
            print(f"- {root.value}")
        derrotadas_por(root.left, heroe_buscado)
        derrotadas_por(root.right, heroe_buscado)
derrotadas_por(arbol_mitos.root, "heracles")

print("f Listar las criaturas que no han sido derrotadas")
def no_derrotadas(root):
    if root is not None:
        if not root.other_values.get("derrotado_por"):
            print(f"- {root.value}")
        no_derrotadas(root.left)
        no_derrotadas(root.right)
no_derrotadas(arbol_mitos.root)

print("h. Modificar nodos de criaturas")
a_capturar = ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabali de Erimanto"]
for nombre in a_capturar:
    nodo = arbol_mitos.search(nombre)
    if nodo:
        nodo.other_values["capturada"] = "heracles"
        print(f"{nombre} modificado con éxito.")

print("i. Busqueda por coincidencia")
def busqueda_coincidencia(root, termino):
    if root is not None:
        if termino.lower() in root.value.lower():
            print(f"Coincidencia encontrada: {root.value}")
        busqueda_coincidencia(root.left, termino)
        busqueda_coincidencia(root.right, termino)
busqueda_coincidencia(arbol_mitos.root, "Cer")

print("j Eliminar al basilisco y a las Sirena")
for borrar in ["Basilisco", "Sirenas"]:
    valor, datos = arbol_mitos.delete_node(borrar)
    if valor:
        print(f"{borrar} fue eliminado del arbol")

print("k Modificar Aves del Estinfalo")
nodo = arbol_mitos.search("Aves del Estinfalo")
if nodo:
    nodo.other_values["derrotado_por"] = "heracles (derroto a varias)"
    print("Aves del Estinfalo modificado")

print("l Modificar el nombre de 'Ladon' por 'Dragon Ladon'")
nodo = arbol_mitos.search("Ladon")
if nodo:
    viejo_nombre = nodo.value
    _, datos_ladon = arbol_mitos.delete_node(viejo_nombre)
    datos_ladon["name"] = "Dragon Ladon"
    arbol_mitos.insert_node("Dragon Ladon", other_value=datos_ladon)
    print("Ladon ha sido renombrado a Dragon Ladon")

print("m Realizar un listado por nivel del arbol")
arbol_mitos.by_level()

print("n Mostrar las criaturas capturadas por heracles")
def capturadas_por(root, heroe_buscado):
    if root is not None:
        if root.other_values.get("capturada") == heroe_buscado:
            print(f"- {root.value}")
        capturadas_por(root.left, heroe_buscado)
        capturadas_por(root.right, heroe_buscado)
capturadas_por(arbol_mitos.root, "heracles")