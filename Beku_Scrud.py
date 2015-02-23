import socket
import sys
import time 

#Beku_Scrud made by B3nac
#Python3 honeypot, logs connection attempts.
#Todo
#Make it a honeynet

def honeypot(server_address, port):
    print('start!')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('', port)
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
               compname = socket.gethostname()
               try:
                   print('client connected:', client_address, file = sys.stderr)
                   print('Computer name:', compname, file = sys.stderr)
                   while True:
                       data = connection.recv(16)
                       print('recieved "%s"', data, file = sys.stderr)
                       if data:
                           connection.sendall(data)
                           f = open("person.txt", "a")
                           f.write(str("\n"))
                           f.write(str(connection))
                           f.write(str(client_address))
                           f.write(str(compname))
                           f.close()
                           
                       else:
                           break
               finally:
                   print('restarting')
                   
if __name__ == '__main__':
	honeypot()
