import pymongo.collection


def join_concert_tickets(ticket_collection: pymongo.collection.Collection):
    pipeline = [
        {
            '$lookup': {
                'from': 'Concerto',
                'localField': 'id_concerto',
                'foreignField': '_id',
                'as': 'concerto'
            }
        },
        {
            '$unwind': '$concerto'
        }
    ]

    return list(ticket_collection.aggregate(pipeline))
