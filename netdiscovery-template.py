from udp import *
from time import *

def onUDPReceive(ip, port, data):
	print("Reply from " + ip)

socket = UDPSocket()
socket.onReceive(onUDPReceive)
socket.begin(1235)

network = "10.87.169."
	
for host in range(255):

	ip = (network + str(host))

	socket.send(ip, 1235, "")
	delay(1)