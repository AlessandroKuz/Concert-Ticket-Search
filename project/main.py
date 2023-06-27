import datetime

from libraries.display_menu import display_menu
from libraries.search_by_artist import search_by_artist
from libraries.search_date import search_by_date
from libraries.search_place import search_by_place


def main():
    while True:
        print('\n=== Buy my tickets! ===')
        display_menu()
        choice = input('Enter your action (1-3): ')

        match choice:
            case '1':  # Cerca concerti per artista
                # errore aggiungi search solo nome e cognome
                artist = input('Enter artist name: ').lower().strip()
                search_by_artist(artist)
            case '2':  # Cerca concerti per artista
                while True:
                    try:
                        start_date = input('Enter start date (dd/mm/yyyy): ')
                        start_date = datetime.datetime.strptime(start_date, '%d/%m/%Y')
                        if start_date > datetime.datetime.now():
                            break
                        else:
                            raise ValueError('Error: start date must be in the future!')
                    except ValueError as err:
                        print(err)

                while True:
                    try:
                        end_date = input('Enter end date (dd/mm/yyyy): ')
                        end_date = datetime.datetime.strptime(end_date, '%d/%m/%Y')
                        if start_date < end_date:
                            break
                        else:
                            raise ValueError('Error: end date must be after start date!')
                    except ValueError as err:
                        print(err)

                search_by_date(start_date, end_date)

            case '3':  # Cerca concerti per artista

                search_by_place()

            case 'q':  # Esci dal programma
                print("Exiting the program...")
                break
            case _:
                print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
