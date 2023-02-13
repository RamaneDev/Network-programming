import http.client
import json
from urllib.parse import quote_plus

def geocode(address, key):
    base = '/maps/api/geocode/json'
    path ='{}?address={}&key={}'.format(base, quote_plus(address), key)
    connection = http.client.HTTPSConnection('maps.googleapis.com')
    connection.request('GET', path)
    result = json.loads(connection.getresponse().read().decode('utf-8'))
    print(result['results'][0]['geometry']['location'])

if __name__ == '__main__':
    address = '10 Downing St, London SW1A 2AB, UK'
    key = 'AIzaSyC1C8-tFe9PI6q2hVJj-6wLalgpnB3Sio4'
    geocode(address, key)