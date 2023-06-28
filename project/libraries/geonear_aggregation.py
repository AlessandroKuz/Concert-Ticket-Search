from geopy.geocoders import Nominatim
import pymongo.collection


def find_nearby_concerts(concert_collection: pymongo.collection.Collection):
    pipeline = [
        {
            '$geoNear': {
                'near': {'type': 'Point', 'coordinates': get_coordinates_from_name()},
                'distanceField': 'distance',
                'maxDistance': get_max_distance(),
                'includeLocs': 'location',
                'spherical': True
            }
        }
    ]

    return list(concert_collection.aggregate(pipeline))


def get_coordinates_from_name():
    while True:
        try:
            location = input('Insert a location: ')
            geolocator = Nominatim(user_agent='concerts')
            coordinates = geolocator.geocode(location)
            if coordinates:
                return [coordinates.longitude, coordinates.latitude]
        except AttributeError:
            print('Invalid location. Please try again.')


def get_max_distance():
    while True:
        try:
            max_distance = int(input('Insert the search area (Km): ')) * 1000
            if max_distance:
                return max_distance
        except ValueError:
            print('Invalid input. Please try again.')
