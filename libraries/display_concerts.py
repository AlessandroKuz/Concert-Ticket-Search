
def display_concerts(tickets: list):
    print(f'\n=== Concert List ===\n')
    for index, ticket in enumerate(tickets):
        concert = ticket['concerto']
        print(
            f'- Concert {index + 1} -',
            f'Nome: {concert["nome"]}',
            f'Artista: {concert["artista_principale"]}',
            f'Altri Artisti: {", ".join(concert["altri_artisti"])}',
            f'Data: {concert["data_ora"].strftime("%d/%m/%Y %H:%M")}',
            f'Luogo: {concert["location"]["name"]}',
            f'Prezzo: {ticket["prezzo_biglietto"]}€',
            f'Biglietti Disponibili: {concert["capienza_massima"] - ticket["biglietti_venduti"]}',
            sep='\n', end='\n\n'
        )
