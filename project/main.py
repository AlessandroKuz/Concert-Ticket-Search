from libraries.display_menu import display_menu
from libraries.search_by_artist import search_by_artist
from libraries.search_date import search_by_date
from libraries.search_place import search_by_place


def main():
    while True:
        print('\n=== Buy my tickets! ===')
        display_menu()
        choice = input('Enter your action (1-3): ').lower().strip()

        match choice:
            case '1':  # Cerca concerti per artista
                artist = input('\nEnter artist name: ').lower().strip()
                search_by_artist(artist)
            case '2':  # Cerca concerti per artista
                search_by_date()
            case '3':  # Cerca concerti per artisti
                search_by_place()
            case 'q':  # Esci dal programma
                print("Exiting the program...")
                break
            case _:
                print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
