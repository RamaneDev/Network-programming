import socket

portByServerName = socket.getservbyname('telnet')
print(portByServerName)

serverByPort = socket.getservbyport(22)
print(serverByPort)