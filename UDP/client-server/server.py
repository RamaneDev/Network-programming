import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 3000))
print('Listening to {}'.format(sock.getsockname()))

data, address = sock.recvfrom(1024)
text = data.decode('ascii')
print('Client at {} date : {}'.format(address, text))
text = 'The client data was {} bytes long'.format(len(data))
data = text.encode('ascii')
sock.sendto(data, address)