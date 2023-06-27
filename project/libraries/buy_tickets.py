import pymongo.collection


def buy_tickets(ticket_collection: pymongo.collection.Collection, selected_concerts: list):
    user_choice = input('Do you want to buy a ticket? (y/n): ').lower()

    if user_choice == 'y':
        if len(selected_concerts) == 1:
            concert_index = 0
        else:
            while True:
                try:
                    concert_index = int(input(f'Enter the number of the concert you want to buy a ticket for (1 - {len(selected_concerts)}): '))
                    if 0 < concert_index <= len(selected_concerts):
                        break
                    else:
                        print('Invalid concert number! Please try again.')
                except ValueError:
                    print('Invalid input. Please try again.')

        selected_concert = selected_concerts[concert_index - 1]
        available_tickets = selected_concert["id_concerto"][0]["capienza_massima"] - selected_concert["biglietti_venduti"]

        while True:
            try:
                num_tickets = int(input(f'Enter the number of tickets you want to buy (1 - {available_tickets}): '))
                if 0 < num_tickets <= available_tickets:
                    total_price = num_tickets * selected_concert["prezzo_biglietto"]
                    print(f'The total price is {total_price}€')
                    bought_choice = input('Do you want to buy the tickets? (y/n): ').lower()

                    if bought_choice == 'y':
                        ticket_collection.update_one({'_id': selected_concert['_id']},
                                                     {'$inc': {'biglietti_venduti': num_tickets}})
                        print(f'You bought {num_tickets} tickets for the concert {selected_concert["id_concerto"][0]["nome"]}!')
                        print('Ticket purchased successfully!')
                    elif bought_choice == 'n':
                        print('Ticket purchase canceled!')
                    else:
                        print('Invalid choice. Please try again.')
                    break
                else:
                    print('Too many tickets selected! Please try again.')
            except ValueError:
                print('Invalid input. Please try again.')

    elif user_choice == 'n':
        print('Thank you for using our service!')
    else:
        print('Invalid choice. Please try again.')