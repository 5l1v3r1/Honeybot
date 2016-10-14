import socket
import sys
import time
import errno
from multiprocessing import Process

#Honeybot made by B3nac
#Python3 honeypot, logs connection attempts.
#Todo
#Make it a honeynet
print('Starting on local address!')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('', 22)
server_address2 = ('', 23)
compname = socket.gethostname()

def honeypot():
    try:
        sock.bind(server_address)
    except socket.error:
        print("Socket error, sudo run or change ports.")
    else:
            while True:
               print('starting up on', server_address, file = sys.stderr)
               sock.getsockname()
               sock.listen(1)
               print('waiting for a connection from sneaky mofackles.', file = sys.stderr)
               connection, client_address = sock.accept()
               try:

                   while True:
                       try:
                           connection.send(bytes('Jokes on you.', 'UTF-8'))
                           data = connection.recv(16)
                           print('recieved "%s"', data, file = sys.stderr)
                           connection.sendall(data)
                       except socket.error as e:
                           if e.args[0] in (errno.EPIPE, errno.ECONNRESET):
                               pass

                       else:
                           logging()
                           break
               finally:
                   print('restarting')

def honeypot2():
    try:
        sock2.bind(server_address2)
    except socket.error:
        print("Socket error, sudo run or change ports.")
    else:
            while True:
               print('starting up on', server_address2, file = sys.stderr)
               sock2.getsockname()
               sock2.listen(1)
               print('waiting for a connection from sneaky mofackles.', file = sys.stderr)
               connection, client_address = sock2.accept()
               try:

                   while True:
                       try:
                           connection.send(bytes('Jokes on you.', 'UTF-8'))
                           data = connection.recv(16)
                           print('recieved "%s"', data, file = sys.stderr)
                           connection.sendall(data)
                       except socket.error as e:
                           if e.args[0] in (errno.EPIPE, errno.ECONNRESET):
                               pass

                       else:
                           logging2()
                           break
               finally:
                   print('restarting')

def logging():
    connection, client_address = sock.accept()
    print('client connected:', client_address, file = sys.stderr)
    f = open("person.txt", "a")
    f.write(str("\n"))
    f.write(str(connection))
    f.write(str(client_address))
    f.write(str(compname))
    f.close()


def logging2():
    connection, client_address = sock2.accept()
    print('client connected:', client_address, file = sys.stderr)
    f = open("person.txt", "a")
    f.write(str("\n"))
    f.write(str(connection))
    f.write(str(client_address))
    f.write(str(compname))
    f.close()


if __name__ == '__main__':
        honey = Process(target=honeypot)
        honey.start()
        honey2 = Process(target=honeypot2)
        honey2.start()
        honey.join()
        honey2.join()
