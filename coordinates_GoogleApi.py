import requests

def geocode(address, key):
    parameters = {'address':address, 'key':key}
    base = 'https://maps.googleapis.com/maps/api/geocode/json'
    response = requests.get(base, params=parameters)
    result = response.json()
    print(result['results'][0]['geometry']['location'])

if __name__ == '__main__':
    address = '10 Downing St, London SW1A 2AB, UK'
    key = 'AIzaSyC1C8-tFe9PI6q2hVJj-6wLalgpnB3Sio4'
    geocode(address, key)

#   https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=
#   AIzaSyC1C8-tFe9PI6q2hVJj-6wLalgpnB3Sio4


