from libraries.mongo_connection import collection_connection
from libraries.join_concert_tickets import join_concert_tickets
from libraries.display_concerts import display_concerts
from libraries.buy_tickets import buy_tickets
from libraries.geonear_aggregation import find_nearby_concerts


def search_by_place():
    ticket_collection = collection_connection('Compravendita-Concerti', 'Biglietto')
    concert_collection = collection_connection('Compravendita-Concerti', 'Concerto')

    concerts = find_nearby_concerts(concert_collection)
    tickets = join_concert_tickets(ticket_collection)

    selected_tickets = [ticket for ticket in tickets for concert in concerts if
                        ticket['concerto']['_id'] == concert['_id']]

    if selected_tickets:
        display_concerts(selected_tickets)
        buy_tickets(ticket_collection, selected_tickets)
    else:
        print(f"\nNo concerts found near you!")
