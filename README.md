#Beku_Scrud
Honeypot using Python3 and Python3 cmdline.
-------------
Instructions
-------------
1. Open terminal

2. Type Sudo Python3 #need sudo for socket permissions.

3. When Python3 starts the Python3 terminal go to Beku_Scrud.py directory and type import Beku_Scrud.

4. After importing Beku_Scrud type Beku_Scrud.honeypot('theip', port). #replace theip with actual ip and port with port number.

5. The program should now be running waiting for anyone to attempt to connect to it. 

You can also test it by opening another cmd prompt and typing ncat ip port and the program should display the user and ip that connected and will also make a person.txt log.

-----------
To-do
-----------
1. Make it easier to initiate. Probably will just add a input for ip address and port. Then it will run with just Python3 Beku_Scrud.py.

2. Monitor more ports and restart automatically while monitoring after gettng a connection.
