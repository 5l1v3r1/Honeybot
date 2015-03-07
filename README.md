#Beku_Scrud
Honeypot using Python3.

------------
Instructions Windows
------------
1.Install Python 3.3 or later.

2. Run Beku_Skrud and input port. May be prompted by windows firewall.

-------------
Instructions Linux
-------------
1. Open terminal

2. Type Sudo python3 Beku_Skrud. This is for socket permissions.

3. The program should now be running waiting for anyone to attempt to connect to the port. 

You can also test it by opening another cmd prompt and typing ncat ip port and the program should display the user and ip that connected and will also make a person.txt log.

-----------
To-do
-----------

1. Monitor more ports and restart automatically while monitoring after gettng a connection.
