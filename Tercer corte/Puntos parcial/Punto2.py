NUM_asientos = 500

class TicketSystem:
    def _init_(self):
        self.asientos_regresados = []
        self.ticket_siguiente = 1
        
    def has_tickets(self):
        if self.ticket_siguiente <= NUM_asientos or len(self.asientos_regresados) > 0:
            return True
        else:
            return False
    def next_ticket(self):
        if self.asientos_regresados:
            return self.asientos_regresados.pop(0)
        elif self.ticket_siguiente <= NUM_asientos:
            actual = self.ticket_siguiente
            self.ticket_siguiente += 1
            return actual
        else:
            return -1
    def return_ticket(self, asiento):
        self.asientos_regresados.append(asiento)

#Explicación del código
#Lectura del archivo y construcción del diccionario:

#Leemos el archivo línea por línea y construimos un diccionario (best_friends) donde cada clave es una persona y el valor es su mejor amigo.
#Función has_cycle para detectar ciclos:

#Utilizamos un algoritmo de búsqueda en profundidad (DFS) para detectar ciclos en el grafo representado por las relaciones de amistad.
#visited es un conjunto que mantiene un registro de todas las personas que han sido visitadas.
#stack es un conjunto que mantiene un registro de las personas en la pila de recursión actual.
#Si encontramos una persona que ya está en la pila de recursión (stack), significa que hemos encontrado un ciclo.
#Detección de ciclos:

#Iteramos sobre cada persona en el diccionario.
#Si una persona no ha sido visitada, llamamos a has_cycle para verificar si hay un ciclo comenzando desde esa persona.
#Si has_cycle devuelve True, entonces hay un ciclo y la función contains_loop devuelve True.
#Si no se encuentra ningún ciclo después de verificar todas las personas, la función devuelve False.
#Ejemplo de uso
#Puedes probar esta función con diferentes archivos de datos para verificar su funcionamiento.
#En el ejemplo proporcionado, data.txt contiene un ciclo, noloops.txt no contiene ningún ciclo, y loveyourself.txt contiene un ciclo porque Pat es su propio mejor amigo.

