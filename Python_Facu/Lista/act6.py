from super_heroes_data import superheroes


class nodoLista:
    def __init__(self):
        self.info = None
        self.sig = None

class Lista:
    def __init__(self):
        self.inicio = None
        self.tamanio = 0

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

def eliminar(lista, clave, campo=None):
    dato = None
    if lista.inicio is not None and criterio(lista.inicio.info, campo) == clave:
        dato = lista.inicio.info
        lista.inicio = lista.inicio.sig
        lista.tamanio -= 1
    else:
        ant = lista.inicio
        act = lista.inicio.sig if lista.inicio else None
        while act is not None and criterio(act.info, campo) != clave:
            ant = act
            act = act.sig
        if act is not None:
            dato = act.info
            ant.sig = act.sig
            lista.tamanio -= 1
    return dato

def buscar(lista, clave, campo=None):
    aux = lista.inicio
    while aux is not None and criterio(aux.info, campo) != clave:
        aux = aux.sig
    return aux


lista_heroes = Lista()

for heroe in superheroes:
    if heroe['name'] == 'Dr Strannnnnge':
        heroe['name'] = 'Dr. Strange'
        heroe['casa_comic'] = 'DC'
    elif heroe['name'] in ['Batman', 'Linterna Verde', 'Mujer Maravilla', 'Flash']:
        heroe['casa_comic'] = 'DC'
    else:
        heroe['casa_comic'] = 'Marvel'
        
    insertar(lista_heroes, heroe, 'name')


eliminado = eliminar(lista_heroes, 'Linterna Verde', 'name')
if eliminado:
    print(f"a. se elimino a: {eliminado['name']}")
else:
    print("a. linterna Verde no se encuentra en la lista cargada.")

nodo_wolverine = buscar(lista_heroes, 'Wolverine', 'name')
if nodo_wolverine:
    print(f"b. año de aparicion de Wolverine: {nodo_wolverine.info['first_appearance']}")

nodo_strange = buscar(lista_heroes, 'Dr. Strange', 'name')
if nodo_strange:
    nodo_strange.info['casa_comic'] = 'Marvel'
    print("c. se ha cambiado la casa de Dr. Strange a Marvel.")

print("\nd. superheroes con 'traje' o 'armadura' en su biografia:")
aux = lista_heroes.inicio
while aux is not None:
    bio = aux.info['short_bio'].lower()
    if 'traje' in bio or 'armadura' in bio or 'suit' in bio or 'armor' in bio:
        print(f"  - {aux.info['name']}")
    aux = aux.sig

print("\ne. cuperheroes con aparicion anterior a 1963:")
aux = lista_heroes.inicio
while aux is not None:
    if aux.info['first_appearance'] < 1963:
        print(f"  - {aux.info['name']} (Casa: {aux.info['casa_comic']})")
    aux = aux.sig

print("\nf. casa de Capitana Marvel y Mujer Maravilla:")
for nombre in ['Capitana Marvel', 'Mujer Maravilla']:
    nodo = buscar(lista_heroes, nombre, 'name')
    if nodo:
        print(f"  - {nombre} pertenece a la casa: {nodo.info['casa_comic']}")
    else:
        print(f"  - {nombre} no esta registrado bajo ese nombre exacto en los datos.")

print("\ng. nformacion completa de Flash y Star-Lord:")
for nombre in ['Flash', 'Star-Lord']:
    nodo = buscar(lista_heroes, nombre, 'name')
    if nodo:
        print(f"  - {nodo.info}")
    else:
        print(f"  - {nombre} no fue encontrado en la lista de datos.")

print("\nh. superheroes cuyos nombres comienzan con B, M o S:")
aux = lista_heroes.inicio
while aux is not None:
    if aux.info['name'].startswith(('B', 'M', 'S')):
        print(f"  - {aux.info['name']}")
    aux = aux.sig

conteo_marvel = 0
conteo_dc = 0
aux = lista_heroes.inicio
while aux is not None:
    if aux.info['casa_comic'] == 'Marvel':
        conteo_marvel += 1
    elif aux.info['casa_comic'] == 'DC':
        conteo_dc += 1
    aux = aux.sig

print("\ni. cantidad total por casa de comic:")
print(f"  - marvel: {conteo_marvel} personajes.")
print(f"  - dc: {conteo_dc} personajes.")