#Honeybot
Turn your raspberry pi into a honeypot and physical intrusion detection system. An Arduino feeds the physical detection to the Raspberry pi. I still need to upload the Arduino scripts and list sensors I'm using.

-------------
Instructions 
-------------
1. Open terminal

2. Type Sudo python3 Honeybotpot.py. This is for socket permissions.

3. The program should now be running waiting for anyone to attempt to connect to the port. 

You can also test it by opening another cmd prompt and typing ncat ip port and the program should display the user and ip that connected and will also make a person.txt log.

-----------
To-do
-----------

1. Monitor more ports and restart automatically while monitoring after gettng a connection.

2. Refining the physical detection on the arduino side.

3. Upload Arduino scripts

4. List sensors being used.
