import settings
class SMBInfo:
    token = settings.TOKEN
    locations_array = settings.LOCATION_ARRAY
    radius = settings.SEARCH_RADIUS
    base_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='
    start_urls = [f'{base_url}${locations_array[0][1]}&radius=${radius}&key=${token["key"]}']

