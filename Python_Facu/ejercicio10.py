
class Notificacion:
    def __init__(self, hora, app, mensaje):
        self.hora = hora       
        self.app = app
        self.mensaje = mensaje

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

class Pila:
    def __init__(self):
        self.items = []
        
    def apilar(self, item):
        self.items.append(item)
        
    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None
        
    def esta_vacia(self):
        return len(self.items) == 0


# a. escribir una función que elimine 
#    de la cola todas las notificaciones de Facebook;
def eliminar_facebook(cola_original):
    cola_aux = Cola()
    
    
    while not cola_original.esta_vacia():
        notif = cola_original.desencolar()
        
        if notif.app != 'Facebook':
            cola_aux.encolar(notif)
            
    
    while not cola_aux.esta_vacia():
        cola_original.encolar(cola_aux.desencolar())


# b. escribir una función que muestre todas 
#    las notificaciones de Twitter, cuyo mensaje incluya
#    la palabra ‘Python’, si perder datos en la cola;
def mostrar_twitter_python(cola_original):
    cola_aux = Cola()
    
    while not cola_original.esta_vacia():
        notif = cola_original.desencolar()
        
        
        if notif.app == 'Twitter' and 'Python' in notif.mensaje:
            print(f"[{notif.hora}] {notif.app}: {notif.mensaje}")
            
        cola_aux.encolar(notif)
        
    while not cola_aux.esta_vacia():
        cola_original.encolar(cola_aux.desencolar())

# c. utilizar una pila para almacenar temporáneamente 
#    las notificaciones producidas entre las
#    11:43 y las 15:57, y determinar cuántas son.
def procesar_notificaciones_por_hora(cola_original):
    cola_aux = Cola()
    pila_temporal = Pila()
    contador = 0
    
    while not cola_original.esta_vacia():
        notif = cola_original.desencolar()
        
        if "11:43" <= notif.hora <= "15:57":
            pila_temporal.apilar(notif)
            contador += 1
            
        cola_aux.encolar(notif)
        
    while not cola_aux.esta_vacia():
        cola_original.encolar(cola_aux.desencolar())
        
    return contador, pila_temporal


if __name__ == "__main__":
    cola_celular = Cola()

    cola_celular.encolar(Notificacion("10:15", "Facebook", "A María le gusta tu foto."))
    cola_celular.encolar(Notificacion("11:45", "Twitter", "Nuevo curso de Python desde cero.")) 
    cola_celular.encolar(Notificacion("13:20", "Instagram", "Juan comentó tu historia.")) 
    cola_celular.encolar(Notificacion("15:00", "Facebook", "Tienes un nuevo recordatorio de evento.")) 
    cola_celular.encolar(Notificacion("16:30", "Twitter", "Me encanta programar en Python.")) 
    cola_celular.encolar(Notificacion("17:00", "WhatsApp", "Mensaje nuevo de mamá."))

    print("--- INICIANDO PRUEBAS ---")

    
    print("\n[Punto B] Buscando notificaciones de Twitter con 'Python':")
    mostrar_twitter_python(cola_celular)

    
    print("\n[Punto C] Procesando notificaciones entre 11:43 y 15:57:")
    cantidad, pila_resultado = procesar_notificaciones_por_hora(cola_celular)
    print(f"Cantidad de notificaciones en ese rango: {cantidad}")
    print("Extrayendo de la pila temporal (saldrán en orden inverso al que entraron):")
    while not pila_resultado.esta_vacia():
        notif_pila = pila_resultado.desapilar()
        print(f" -> [{notif_pila.hora}] {notif_pila.app}")

    
    print("\n[Punto A] Eliminando notificaciones de Facebook...")
    eliminar_facebook(cola_celular)

    print("\n--- ESTADO FINAL DE LA COLA ---")
    while not cola_celular.esta_vacia():
        notif_final = cola_celular.desencolar()
        print(f"[{notif_final.hora}] {notif_final.app}: {notif_final.mensaje}")