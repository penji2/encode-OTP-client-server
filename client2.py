import socket
import sys
import errno
from coder import main,decrypting
HEADER_LENGTH = 10
trace=0
trace1=0
IP = "192.168.1.5"
PORT = 1234
my_username = input("Username: ")

"""
Create a socket
socket.AF_INET - address family, IPv4, some otehr possible are AF_INET6, AF_BLUETOOTH, AF_UNIX
socket.SOCK_STREAM - TCP, conection-based, socket.SOCK_DGRAM - UDP, connectionless, datagrams,
socket.SOCK_RAW - raw IP packets
"""
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

""" Connect to a given ip and port """
client_socket.connect((IP, PORT))

""" Set connection to non-blocking state, so .recv() call won;t block, just return some exception we'll handle """
client_socket.setblocking(False)

"""
Prepare username and header and send them
We need to encode username to bytes, then count number of bytes and prepare header of fixed size,
that we encode to bytes as well
"""
username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)

while True:

    """ Wait for user to input a message """
    message = input(f'{my_username} > ')
    """ If message is not empty - send it """
    if message:
        paslen=len(message)
        """ Encode message to bytes, prepare header and convert to bytes, like for username above, then send """
        f=open("key.dat",mode="r")
        f.seek(trace)
        message=main(message,f.read(paslen))


        trace+=paslen


        f.close()
        message = message.encode('utf-8')
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(message_header + message)

    try:
        """ Now we want to loop over received messages (there might be more than one) and print them """
        while True:

            """ Receive our "header" containing username length, it's size is defined and constant """
            username_header = client_socket.recv(HEADER_LENGTH)

            """
            
            If we received no data, server gracefully closed a connection,
            for example using socket.close() or socket. shutdown(socket.SHUT_RDWR) 
            
            """
            if not len(username_header):
                print('Connection closed by the server')
                sys.exit()

            """ Convert header to int value """
            username_length = int(username_header.decode('utf-8').strip())

            """ Receive and decode username """
            username = client_socket.recv(username_length).decode('utf-8')

            """ 
            
            Now do the same for message (as we received username, we received whole message,
            there's no need to check if it has any length)
            
            """
            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')
            paslen=len(message)
            f1=open("key1.dat",mode="r")
            f1.seek(trace1)
            message=decrypting(message,f1.read(paslen))
            trace1+=paslen
            f1.close()
            """ Print message """
            print(f'{username} > {message}')
    except:
        pass