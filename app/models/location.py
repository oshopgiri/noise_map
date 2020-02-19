from app import mongo


class Location:

    @classmethod
    def list(cls):
        location_data = mongo.db.locations.find()
        locations = {}
        for location in location_data:
            locations[location['number']] = {
                'name': location['name'],
                'latitude': location['latitude'],
                'longitude': location['longitude']
            }
        return locations
