

class Lista:
    def __init__(self):
        self.inicio = None
        self.tamanio = 0

class nodoLista:
    def __init__(self):
        self.info = None
        self.sig = None
        self.sublista = Lista()

def criterio(dato, campo=None):
    if isinstance(dato, dict) and campo in dato:
        return dato[campo]
    elif hasattr(dato, '__dict__') and campo in dato.__dict__:
        return dato.__dict__[campo]
    return dato

def insertar(lista, dato, campo=None):
    nodo = nodoLista()
    nodo.info = dato
    if lista.inicio is None or criterio(lista.inicio.info, campo) > criterio(dato, campo):
        nodo.sig = lista.inicio
        lista.inicio = nodo
    else:
        ant = lista.inicio
        act = lista.inicio.sig
        while act is not None and criterio(act.info, campo) <= criterio(dato, campo):
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    lista.tamanio += 1

def buscar(lista, clave, campo=None):
    aux = lista.inicio
    while aux is not None and criterio(aux.info, campo) != clave:
        aux = aux.sig
    return aux


lista_entrenadores = Lista()


entrenadores_data = [
    {'nombre': 'Ash', 'torneos_ganados': 4, 'batallas_perdidas': 15, 'batallas_ganadas': 85},
    
    {'nombre': 'Misty', 'torneos_ganados': 2, 'batallas_perdidas': 20, 'batallas_ganadas': 60},
    
    {'nombre': 'Brock', 'torneos_ganados': 1, 'batallas_perdidas': 30, 'batallas_ganadas': 70},
    
    {'nombre': 'Cynthia', 'torneos_ganados': 8, 'batallas_perdidas': 5, 'batallas_ganadas': 95}
]

for e in entrenadores_data:
    insertar(lista_entrenadores, e, 'nombre')


pokemons_data = [
    {'nombre': 'Pikachu', 'nivel': 50, 'tipo': 'eléctrico', 'subtipo': 'ninguno', 'entrenador': 'Ash'},
    
    {'nombre': 'Charizard', 'nivel': 65, 'tipo': 'fuego', 'subtipo': 'volador', 'entrenador': 'Ash'},
    
    {'nombre': 'Starmie', 'nivel': 45, 'tipo': 'agua', 'subtipo': 'psíquico', 'entrenador': 'Misty'},
    
    {'nombre': 'Gyarados', 'nivel': 55, 'tipo': 'agua', 'subtipo': 'volador', 'entrenador': 'Misty'},
    
    {'nombre': 'Starmie', 'nivel': 45, 'tipo': 'agua', 'subtipo': 'psíquico', 'entrenador': 'Misty'},
    
    {'nombre': 'Onix', 'nivel': 40, 'tipo': 'roca', 'subtipo': 'tierra', 'entrenador': 'Brock'},
    
    {'nombre': 'Tyrantrum', 'nivel': 55, 'tipo': 'roca', 'subtipo': 'dragón', 'entrenador': 'Brock'},

    {'nombre': 'Garchomp', 'nivel': 75, 'tipo': 'dragón', 'subtipo': 'tierra', 'entrenador': 'Cynthia'},
    
    {'nombre': 'Terrakion', 'nivel': 70, 'tipo': 'roca', 'subtipo': 'lucha', 'entrenador': 'Cynthia'}
]

for p in pokemons_data:
    nodo_entrenador = buscar(lista_entrenadores, p['entrenador'], 'nombre')
    if nodo_entrenador:
        insertar(nodo_entrenador.sublista, p, 'nombre')



entrenador_a = 'Ash' or 'ash'
nodo_a = buscar(lista_entrenadores, entrenador_a, 'nombre')
if nodo_a:
    print(f"a. {entrenador_a} tiene {nodo_a.sublista.tamanio} Pokmons.")


print("\nb. entrenadores con mas de 3 torneos ganados:")
aux = lista_entrenadores.inicio
while aux is not None:
    if aux.info['torneos_ganados'] > 3:
        print(f"  {aux.info['nombre']} ({aux.info['torneos_ganados']} torneos)")
    aux = aux.sig


print("\nc.pokemon de mayor nivel del entrenador con mas torneos ganados:")
aux = lista_entrenadores.inicio
entrenador_top = None
max_torneos = -1

while aux is not None:
    if aux.info['torneos_ganados'] > max_torneos:
        max_torneos = aux.info['torneos_ganados']
        entrenador_top = aux
    aux = aux.sig

if entrenador_top and entrenador_top.sublista.inicio:
    paux = entrenador_top.sublista.inicio
    poke_max = paux.info
    while paux is not None:
        if paux.info['nivel'] > poke_max['nivel']:
            poke_max = paux.info
        paux = paux.sig
    print(f"   entrenador: {entrenador_top.info['nombre']} - pokemon: {poke_max['nombre']} (nivel: {poke_max['nivel']})")

entrenador_d = 'Cynthia' or 'cynthia'
print(f"\nd. Datos completos del entrenador '{entrenador_d}':")
nodo_d = buscar(lista_entrenadores, entrenador_d, 'nombre')
if nodo_d:
    print(f"   - Info: {nodo_d.info}")
    paux = nodo_d.sublista.inicio
    while paux is not None:
        print(f"     * {paux.info}")
        paux = paux.sig

print("\ne. entrenadores con porcentaje de victorias > 79%:")
aux = lista_entrenadores.inicio
while aux is not None:
    total_batallas = aux.info['batallas_ganadas'] + aux.info['batallas_perdidas']
    if total_batallas > 0:
        porcentaje = (aux.info['batallas_ganadas'] / total_batallas) * 100
        if porcentaje > 79:
            print(f"   - {aux.info['nombre']} ({porcentaje:.1f}%)")
    aux = aux.sig

print("\nf. entrenadores con pokemones de la clase fuego/planta o agua/volador:")
aux = lista_entrenadores.inicio
while aux is not None:
    paux = aux.sublista.inicio
    cumple = False
    while paux is not None:
        t, st = paux.info['tipo'], paux.info['subtipo']
        if (t == 'fuego' and st == 'planta') or (t == 'agua' and st == 'volador'):
            cumple = True
            break
        paux = paux.sig
    if cumple:
        print(f"   - {aux.info['nombre']}")
    aux = aux.sig


entrenador_g = 'Ash' or 'ash'
nodo_g = buscar(lista_entrenadores, entrenador_g, 'nombre')
if nodo_g and nodo_g.sublista.tamanio > 0:
    suma_niveles = 0
    paux = nodo_g.sublista.inicio
    while paux is not None:
        suma_niveles += paux.info['nivel']
        paux = paux.sig
    promedio = suma_niveles / nodo_g.sublista.tamanio
    print(f"\ng. promedio de nivel de pokemons de {entrenador_g}: {promedio:.1f}")


pokemon_h = 'Starmie' or 'starmie'
contador_entrenadores = 0
aux = lista_entrenadores.inicio
while aux is not None:
    paux = aux.sublista.inicio
    tiene_pokemon = False
    while paux is not None:
        if paux.info['nombre'] == pokemon_h:
            tiene_pokemon = True
            break
        paux = paux.sig
    if tiene_pokemon:
        contador_entrenadores += 1
    aux = aux.sig
print(f"\nh. cantidad de entrenadores que tienen a {pokemon_h}: {contador_entrenadores}")


print("\ni. entrenadores con pokemones repetidos")
aux = lista_entrenadores.inicio
while aux is not None:
    nombres_vistos = []
    repetido = False
    paux = aux.sublista.inicio
    while paux is not None:
        if paux.info['nombre'] in nombres_vistos:
            repetido = True
            break
        nombres_vistos.append(paux.info['nombre'])
        paux = paux.sig
    if repetido:
        print(f"   - {aux.info['nombre']}")
    aux = aux.sig


print("\nj. entrenadores que tienen a Tyrantrum, Terrakion o Wingull:")
objetivos = ['Tyrantrum', 'Terrakion', 'Wingull']
aux = lista_entrenadores.inicio
while aux is not None:
    paux = aux.sublista.inicio
    tiene_objetivo = False
    while paux is not None:
        if paux.info['nombre'] in objetivos:
            tiene_objetivo = True
            break
        paux = paux.sig
    if tiene_objetivo:
        print(f"   - {aux.info['nombre']}")
    aux = aux.sig

entrenador_x = 'Cynthia' or 'cynthia'
pokemon_y = 'Garchomp' or 'garchomp'
print(f"\nk. busqueda de {pokemon_y} en el equipo de {entrenador_x}:")
nodo_k_entr = buscar(lista_entrenadores, entrenador_x, 'nombre')
if nodo_k_entr:
    nodo_k_poke = buscar(nodo_k_entr.sublista, pokemon_y, 'nombre')
    if nodo_k_poke:
        print(f"   datos entrenador: {nodo_k_entr.info}")
        print(f"   datos pokemon: {nodo_k_poke.info}")
    else:
        print(f"   {entrenador_x} no posee a {pokemon_y}.")
else:
    print(f"   entrenador {entrenador_x} no fue encontrado.")