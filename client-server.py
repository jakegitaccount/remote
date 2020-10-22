import sys
import subprocess
import getopt
import os
import threading
import socket


target_ip = ""
target_port = 0
server_listen = False
buffer_size = 4096


def design():
	print("                          -----#######-----------Welcome to Jake net tools--------#######------")
	print("\t\t")
	print("\t\t")
	print("\t\t")
	print("                                  #######        $$ $$         $$       $$  $$$$$$$$$$$$$")
	print("                                       $$       $$   $$        $$      $$   $$")
	print("                                       $$      $$     $$       $$    $$     $$")
	print("                                       $$     $$       $$      $$  $$       $$")
	print("                                       $$    $$$$$$$$$$$$$     $$$$         $$$$$$$$")
	print("                                       $$   $$           $$    $$  $$       $$")
	print("                              $$       $$  $$             $$   $$    $$     $$")
	print("                              $$      $$  $$               $$  $$      $$   $$")
	print("                                $$ $$    $$                 $$ $$        $$ $$$$$$$$$$$$$$")
	pass



design()


print("\t\t")
print("\t\t")

def procedure():
	print("Usage: <filename> -t <target_ip> -p <target_port>")
	print("For Help: <filename> -h")
	print("\t\t")
	print("-h --help                 - open help menu")
	print("-l --listen               - listen for connection")
	print("-t --target               - specify target ip address")
	print("-p --port                 - specify target port number")
	print("exit                      - close connection")
	print("\t\t")
	print("\t\t")
	print("Examples:")
	print("\t\t")
	print("<filename> -t 192.157.21.12 -p 3212")
	print("<filename> -l -t 192.189.10.14 -p 9999  ##(Specially For server site)")
	pass



# now start main program.........

def server_handler(ip,port):
	global buffer_size
	server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server.bind((ip,port))
	server.listen(5)
	print("[*]Server is listening.......")
	conn,addr = server.accept()
	print(f'receive from {addr[0]}:{addr[1]}')
	outdata = conn.recv(buffer_size).decode()
	print(outdata)
	print("[+]Please wait......")
	conn.send(b'[+]Connection established....')

	while True:
		mydata = conn.recv(buffer_size).decode()
		if mydata =='exit':
			break
		print("[#]Message: ",mydata)
		myvalue = input('<server-$> ').encode()
		print('[+]Please wait.......')
		print("\t")
		conn.send(myvalue)
		if myvalue==b'exit':
			break

	pass
	conn.close()
	print('connection break!!!...')


# now this is client handler function...

def client_handler(ip,port):
	global buffer_size
	c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	c.connect((ip,port))
	c.send(b'[+]Connected...')
	print(c.recv(buffer_size).decode())

	while True:
		value = input('<client-$> ').encode()
		print('[+]Please waite.........')
		print("\t")
		c.send(value)
		if value==b'exit':
			break
		data = c.recv(buffer_size).decode()
		print("[#]Message: ",data)
		if data=='exit':
			break
		pass
	c.close()
	print('connection break!!....')


def main():
	global target_ip
	global target_port
	global server_listen
	# first check wheither value is passing or not...
	# if len(sys.argv[1:])==0:
	# 	print('You did not specify command line options. See help line..\ntype: filename.py -h')
	# 	pass


	try:
		opts,args = getopt.getopt(sys.argv[1:],"hlt:p:",["listen=","target=","port"])
	except:
		print("command line error!!..see the help menu")

	# now assign value for each command line parameter
	for opt,arg in opts:
		if opt in ["-h"]:
			procedure()
			sys.exit()
		elif opt in ["-l","--listen"]:
			server_listen = True
		elif opt in ["-t","--target"]:
			target_ip = arg
		elif opt in ["-p","--port"]:
			target_port = int(arg)
		else:
			print('invalid provided options!..')

	# this is main command process section...
	try:
		if server_listen:
			server_handler(target_ip,target_port)
		else:
			client_handler(target_ip,target_port)
	except:
		print('First run help section by typing.....\nUsage: <filename> -h')




# now show the result


main()
