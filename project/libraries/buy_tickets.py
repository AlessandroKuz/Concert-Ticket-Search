import pymongo.collection


def buy_tickets(ticket_collection: pymongo.collection.Collection, selected_concerts: list):
    user_choice = input('Do you want to buy a ticket? (y/n): ').lower().strip()

    if user_choice == 'y':
        if len(selected_concerts) == 1:
            selected_concert = selected_concerts[0]
        else:
            concert_index = get_concert_choice(selected_concerts)
            selected_concert = selected_concerts[concert_index]

        available_tickets = selected_concert["concerto"]["capienza_massima"] - selected_concert["biglietti_venduti"]

        if available_tickets > 0:
            num_tickets = get_ticket_quantity(available_tickets)
            total_price = calculate_price(num_tickets, selected_concert["prezzo_biglietto"])
            print(f'The total price is {total_price}€')
            bought_choice = input('Do you want to buy the tickets? (y/n): ').lower()

            if bought_choice == 'y':
                update_tickets_sold(ticket_collection, selected_concert['_id'], num_tickets)
                print_ticket_details(num_tickets, selected_concert["concerto"]["nome"], available_tickets)
            elif bought_choice == 'n':
                print('Ticket purchase canceled!')
            else:
                print('Invalid choice. Please try again.')
        else:
            print('No more tickets available for this concert!')
    elif user_choice == 'n':
        print('Thank you for using our service!')
    else:
        print('Invalid choice. Please try again.')


def print_ticket_details(num_tickets, concert_name, available_tickets):
    print(f'You bought {num_tickets} tickets for the concert {concert_name}!')

    for ticket in range(num_tickets):
        ticket_code = str(available_tickets - ticket).zfill(6)
        print(f'Your ticket code is {ticket_code}')

    print('Ticket purchased successfully!')


def update_tickets_sold(ticket_collection, concert_id, num_tickets):
    ticket_collection.update_one({'_id': concert_id}, {'$inc': {'biglietti_venduti': num_tickets}})


def calculate_price(num_tickets, ticket_price):
    return num_tickets * ticket_price


def get_concert_choice(selected_concerts):
    while True:
        try:
            concert_index = int(
                input(f'Enter the number of the concert you want to buy a ticket for (1 - {len(selected_concerts)}): '))
            if 0 < concert_index <= len(selected_concerts):
                return concert_index - 1
            else:
                print('Invalid concert number! Please try again.')
        except ValueError:
            print('Invalid input. Please try again.')


def get_ticket_quantity(available_tickets):
    while True:
        try:
            num_tickets = int(input(f'Enter the number of tickets you want to buy (1 - {available_tickets}): '))
            if 0 < num_tickets <= available_tickets:
                return num_tickets
            else:
                print('Number of tickets not valid! Please try again.')
        except ValueError:
            print('Invalid input. Please try again.')
