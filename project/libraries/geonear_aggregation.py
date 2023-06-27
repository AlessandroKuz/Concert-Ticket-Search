from geopy.geocoders import Nominatim
import pymongo.collection


def find_nearby_concerts(concert_collection: pymongo.collection.Collection):
    location = get_coordinates_from_name()

    while True:
        try:
            max_distance = int(input('Insert the search area (Km): ')) * 1000
            if max_distance:
                break
        except ValueError:
            print('Invalid input. Please try again.')

    pipeline = [
        {
            '$geoNear': {
                'near': {'type': 'Point', 'coordinates': location},
                'distanceField': 'distance',
                'maxDistance': max_distance,
                'includeLocs': 'location',
                'spherical': True
            }
        }
    ]

    return list(concert_collection.aggregate(pipeline))


def get_coordinates_from_name():
    while True:
        try:
            location_name = input('Insert the location name: ')
            geolocator = Nominatim(user_agent="myGeocoder")
            location = geolocator.geocode(location_name)

            if location:
                return [location.longitude, location.latitude]
            else:
                raise ValueError('Name of the location not valid!')
        except ValueError as err:
            print('Error:', err)
