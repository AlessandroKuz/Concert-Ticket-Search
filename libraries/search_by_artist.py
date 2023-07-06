from libraries.mongo_connection import collection_connection
from libraries.join_concert_tickets import join_concert_tickets
from libraries.display_concerts import display_concerts
from libraries.buy_tickets import buy_tickets


def search_by_artist(selected_artist: str):
    ticket_collection = collection_connection('Compravendita-Concerti', 'Biglietto')
    tickets = join_concert_tickets(ticket_collection)

    selected_tickets = [ticket for ticket in tickets if
                        ticket['concerto']['artista_principale'].lower().startswith(selected_artist) or
                        ticket['concerto']['artista_principale'].lower().endswith(selected_artist)]

    if selected_tickets:
        display_concerts(selected_tickets)
        buy_tickets(ticket_collection, selected_tickets)
    else:
        print(f"\nNo concerts found for artist '{selected_artist}'")
