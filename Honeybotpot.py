import socket
import sys
import time 
import errno

#Beku_Scrud made by B3nac
#Python3 honeypot, logs connection attempts.
#Todo
#Make it a honeynet

def honeypot():
    print('Starting on local address!')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('', 22)
    compname = socket.gethostname()

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
                   print('client connected:', client_address, file = sys.stderr)
                   f = open("person.txt", "a")
                   f.write(str("\n"))
                   f.write(str(connection))
                   f.write(str(client_address))
                   f.write(str(compname))
                   f.close()
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
                           break
               finally:
                   print('restarting')
                   
if __name__ == '__main__':
	honeypot()
