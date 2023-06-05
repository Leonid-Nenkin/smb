import json

SEARCH_RADIUS = 1500
TOKEN = json.load(open('token.json'))
LOCATION_ARRAY = json.load(open('smb_study_zone.json'))['features'][0]['geometry']['coordinates'][0]
