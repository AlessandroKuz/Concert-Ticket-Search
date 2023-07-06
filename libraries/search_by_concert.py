from libraries.mongo_connection import collection_connection
from libraries.join_concert_tickets import join_concert_tickets
from libraries.display_concerts import display_concerts
from libraries.buy_tickets import buy_tickets


def search_by_concert(selected_concert: str):
    ticket_collection = collection_connection('Compravendita-Concerti', 'Biglietto')
    tickets = join_concert_tickets(ticket_collection)

    selected_tickets = [ticket for ticket in tickets if
                        ticket['concerto']['nome'].lower().startswith(selected_concert) or
                        ticket['concerto']['nome'].lower().endswith(selected_concert)]

    if selected_tickets:
        display_concerts(selected_tickets)
        buy_tickets(ticket_collection, selected_tickets)
    else:
        print(f'No concerts found with name {selected_concert}!')
