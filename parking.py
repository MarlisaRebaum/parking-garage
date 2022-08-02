class ParkingGarage():
    """
        The ParkingGarage will allow users to pay for a parking ticket.

        Attributes for the class:
        -tickets: expected to be a list
        -parking_spaces: expected to be a list
        -current_ticket: expected to be a dictionary
    """

    def __init__(self, tickets, parking_spaces, current_ticket):
        self.tickets = tickets
        self.used_tickets = []
        self.parking_spaces = parking_spaces
        self.used_spaces = []
        self.current_ticket = current_ticket
        current_ticket = {'paid': False}

    def show_spots(self):
        print('Number of available parking spots: ')
        print(self.parking_spaces[-1])

    def show_tickets(self):
        print('Number of available tickets: ')
        print(self.tickets[-1])

    def take_ticket(self):
        print('Please take a ticket. You will pay your ticket when returning.')
        self.used_tickets.append(self.tickets.pop(-1))
        self.used_spaces.append(self.parking_spaces.pop(-1))
    
    def pay_for_parking(self):
        buy_ticket = input('Please select the amount of hours for your stay: ')
        if buy_ticket != "":
            print('Thank you, your ticket has been paid. You have 15 minutes to \
leave the parking garage.')
            self.current_ticket['paid'] = True
            self.tickets.append(self.used_tickets.pop(-1))
            self.parking_spaces.append(self.used_spaces.pop(-1))
        else:
            print('Please enter an amount to pay.')

    def leave_garage(self):
        if self.current_ticket == {'paid': False}:
            print('Please pay for your ticket to leave the parking garage.')
        else:
            print('Thank you, have a nice day!')
            self.current_ticket['paid'] = False


current_parking = ParkingGarage([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], {'paid': False})

def run():
    
    while True:
        response = input('What would you like to do?: Take ticket [take], pay \
ticket [pay], leave parking garage [leave], check available spaces \
[spaces], check available tickets [tickets], or quit [quit]. ')

        if response.lower() == 'take':
            current_parking.take_ticket()
        elif response.lower() == 'pay':
            current_parking.pay_for_parking()
        elif response.lower() == 'leave':
            current_parking.leave_garage()
        elif response.lower() == 'spaces':
            current_parking.show_spots()
        elif response.lower() == 'tickets':
            current_parking.show_tickets()
        elif response.lower() == 'quit':
            break
        else:
            print("invalid input")

run()