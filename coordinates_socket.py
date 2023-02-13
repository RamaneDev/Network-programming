import socket
import ssl
from urllib.parse import quote_plus

request_text = """\
GET /maps/api/geocode/json?address={}&key={} HTTP/1.0\r\n
Host: maps.googleapis.com:443\r\n
\r\n
"""

def geocode(address, key):
    hostname = 'maps.googleapis.com'
    context = ssl.create_default_context()
 
    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
           # print(ssock.version())
           request = request_text.format(quote_plus(address), key)
           ssock.sendall(request.encode('ascii'))
           result = b''
           while True:
            data = ssock.recv()
            if not data:
                break
            result += data           
           result = result.decode('utf-8')
           print(result)

if __name__ == '__main__':
    address = '10 Downing St, London SW1A 2AB, UK'
    key = 'AIzaSyC1C8-tFe9PI6q2hVJj-6wLalgpnB3Sio4'
    geocode(address, key)

