# PING CLIENT PROGRAM
#
# This is a client-side program makes ping requests to the server.

import sys

total = len(sys.argv)
cmdargs = str(sys.argv)

from socket import *
import time

server_name = '127.0.0.1'
server_port = 12000 # change port number if required
client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.settimeout(1)

seq_num = 0
while seq_num < 10:
	# transmit data to server, receive from server
	try:
		send_time = time.time()
		timestamp = str(send_time)
		#ping = 'Ping to ' + server_name + ', seq = ' + str(seq_num) + ', ' + timestamp
		ping = 'PING ' + str(seq_num) + ' ' + timestamp + ' \r\n'
		client_socket.sendto(ping, (server_name, server_port))
		reply, server_address = client_socket.recvfrom(2048)
		recv_time = time.time()
		time.sleep(1)
	# timeout exception
	except timeout:
		print 'No response from server, packet dropped'
		seq_num += 1
		continue
	# calculate RTT, print server response with RTT
	RTT = round(recv_time - send_time, 3) * 1000
	print 'Ping to ' + server_name + ', seq = ' + str(reply[5]) + ', rtt = ' +  str(RTT) + 'ms'
	seq_num += 1

client_socket.close()

