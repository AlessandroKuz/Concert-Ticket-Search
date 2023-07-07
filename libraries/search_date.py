from libraries.mongo_connection import collection_connection
from libraries.join_concert_tickets import join_concert_tickets
from libraries.display_concerts import display_concerts
from libraries.buy_tickets import buy_tickets
import datetime


def search_by_date():
    ticket_collection = collection_connection('Compravendita-Concerti', 'Biglietto')
    tickets = join_concert_tickets(ticket_collection)

    start_date, end_date = get_dates()
    selected_tickets = [ticket for ticket in tickets if start_date <= ticket['concerto']['data_ora'] <= end_date]

    if selected_tickets:
        display_concerts(selected_tickets)
        buy_tickets(ticket_collection, selected_tickets)
    else:
        print(f"\nNo concerts found between '{start_date.date()}' and '{end_date.date()}'")


def get_dates():
    while True:
        try:
            start_date = input('\nEnter start date (dd/mm/yyyy): ')
            start_date = datetime.datetime.strptime(start_date, '%d/%m/%Y')
            if start_date >= datetime.datetime.now():
                break
            else:
                print('\nError: start date must be in the future!')
        except ValueError:
            print('\nError: invalid date format!')

    while True:
        try:
            end_date = input('Enter end date (dd/mm/yyyy): ')
            end_date = datetime.datetime.strptime(end_date, '%d/%m/%Y')
            if start_date < end_date:
                break
            else:
                print('\nError: end date must be after start date!')
        except ValueError:
            print('\nError: invalid date format!')

    return start_date, end_date
