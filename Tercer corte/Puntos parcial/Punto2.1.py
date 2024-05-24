# Numero de asientos disponibles en el sistema de boletos
NUM_SEATS = 500

class TicketSystem:
    
    def __init__(self):
        self.available_tickets = list(range(1, NUM_SEATS + 1))  # Lista de todos los asientos disponibles inicialmente
        self.returned_tickets = []  # Lista de boletos que han sido devueltos

    def has_tickets(self):
        # Devuelve True si hay boletos disponibles, ya sea en la lista de devueltos o en la lista de disponibles
        return bool(self.available_tickets) or bool(self.returned_tickets)

    def next_ticket(self):
        # Si hay boletos devueltos, vende el primero de la lista de devueltos
        if self.returned_tickets:
            return self.returned_tickets.pop(0)
        # Si no hay boletos devueltos, vende el siguiente en la lista de disponibles
        elif self.available_tickets:
            return self.available_tickets.pop(0)
        # Si no hay boletos disponibles, devuelve -1
        else:
            return -1

    def return_ticket(self, ticket):
        # Añade el boleto devuelto a la lista de devueltos
        self.returned_tickets.append(ticket)