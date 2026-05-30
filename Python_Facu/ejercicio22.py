
class PersonajeMCU:
    def __init__(self, nombre, superheroe, genero):
        self.nombre = nombre
        self.superheroe = superheroe
        self.genero = genero

class Cola:
    def __init__(self):
        self.items = []
    
    def encolar(self, item):
        self.items.append(item)
    
    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        return None
        
    def esta_vacia(self):
        return len(self.items) == 0

def procesar_mcu(cola_original):
    cola_aux = Cola()
    
    
    nombre_capitana_marvel = None
    superheroe_scott_lang = None
    carol_danvers_presente = False
    superheroe_carol = None
    
    print("--- RESULTADOS DURANTE EL RECORRIDO ---")
    
    while not cola_original.esta_vacia():
        pj = cola_original.desencolar()
        
        # a determinar el nombre del personaje de la superhéroe Capitana Marvel;
        if pj.superheroe == "Capitana Marvel":
            nombre_capitana_marvel = pj.nombre
            
        # b. mostrar los nombre de los superhéroes femeninos;
        if pj.genero == "F":
            print(f"[Punto B] Superhéroe Femenino: {pj.superheroe}")
            
        # c. mostrar los nombres de los personajes masculinos;
        if pj.genero == "M":
            print(f"[Punto C] Personaje Masculino: {pj.nombre}")
            
        # d. determinar el nombre del superhéroe del personaje Scott Lang;
        if pj.nombre == "Scott Lang":
            superheroe_scott_lang = pj.superheroe
            
        # e. mostrar todos datos de los superhéroes 
        # o personaje cuyos nombres comienzan
        # con la letra S;
        if pj.nombre.startswith("S") or pj.superheroe.startswith("S"):
            print(f"[Punto E] Empieza con 'S': {pj.nombre} (Héroe: {pj.superheroe}, Género: {pj.genero})")
            
        # f. determinar si el personaje Carol Danvers 
        # se encuentra en la cola e indicar su nombre
        #    de superhéroes;
        if pj.nombre == "Carol Danvers":
            carol_danvers_presente = True
            superheroe_carol = pj.superheroe
            
        
        cola_aux.encolar(pj)
        
    
    while not cola_aux.esta_vacia():
        cola_original.encolar(cola_aux.desencolar())
    
    print("\n resultados")
    if nombre_capitana_marvel:
        print(f"[Punto A] El nombre real de Capitana Marvel es: {nombre_capitana_marvel}")
        
    if superheroe_scott_lang:
        print(f"[Punto D] El superhéroe de Scott Lang es: {superheroe_scott_lang}")
        
    if carol_danvers_presente:
        print(f"[Punto F] Carol Danvers SE ENCUENTRA en la cola. Su superhéroe es: {superheroe_carol}")
    else:
        print("[Punto F] Carol Danvers NO se encuentra en la cola.")


if __name__ == "__main__":
    cola_mcu = Cola()
    
    cola_mcu.encolar(PersonajeMCU("Tony Stark", "Iron Man", "M"))
    cola_mcu.encolar(PersonajeMCU("Steve Rogers", "Capitán América", "M"))
    cola_mcu.encolar(PersonajeMCU("Natasha Romanoff", "Black Widow", "F"))
    cola_mcu.encolar(PersonajeMCU("Carol Danvers", "Capitana Marvel", "F"))
    cola_mcu.encolar(PersonajeMCU("Scott Lang", "Ant-Man", "M"))
    cola_mcu.encolar(PersonajeMCU("Stephen Strange", "Doctor Strange", "M")) 
    cola_mcu.encolar(PersonajeMCU("Peter Parker", "Spider-Man", "M")) 

    procesar_mcu(cola_mcu)