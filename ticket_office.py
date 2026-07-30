"""
Ticket Office Module for Issue #25: Kibbitzing before act 2.... please wait

This module simulates a ticket office for selling €500 seats with live operators.
It provides a simple CLI to buy tickets and logs purchases.
"""

import logging

logging.basicConfig(
    filename='ticket_office.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class TicketOffice:
    def __init__(self, total_seats=100):
        self.total_seats = total_seats
        self.sold_seats = 0

    def sell_ticket(self):
        if self.sold_seats >= self.total_seats:
            print("Sorry, all tickets are sold out.")
            return False
        self.sold_seats += 1
        seat_number = self.sold_seats
        print(f"Ticket #{seat_number} sold for €500. Thank you for your purchase!")
        logging.info(f"Ticket #{seat_number} sold.")
        return True

def main():
    print("Welcome to the Ticket Office for the Colosseum Event!")
    office = TicketOffice()
    while True:
        user_input = input("Type 'buy' to purchase a ticket or 'exit' to quit: ").strip().lower()
        if user_input == 'buy':
            if not office.sell_ticket():
                break
        elif user_input == 'exit':
            print("Thank you for visiting the Ticket Office. Goodbye!")
            break
        else:
            print("Invalid input. Please type 'buy' or 'exit'.")

if __name__ == "__main__":
    main()
