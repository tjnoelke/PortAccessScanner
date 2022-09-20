TLDR: This python program is designed to automate an aggressive nmap scan and provide potential weakness to chosen TCP ports in Linux.

Long Version: This program was developed for a cybersecurity final where we needed to summarize what we learned in either developing or showcasing a new tool. I love Python but have never programmed solely in Linux, so I decided to automate some recon steps with a program.

How it works is: The program will ask the user if ExploitDB is installed on the system. If yes, it moves on. If not, it runs a bash script to install it. The program will then prompt the user for an IPv4 address and run an aggressive nmap scan (-sV -Pn) against the IP address and search for available TCP ports. Once the scan is complete, the program will provide the user with a list of ports. The user can choose to check vulnerabilities of one or all of the ports. Once the choice is made, the program will run the port(s) against a dictionary list of TCP ports, and find a common service that runs on that port. The service is then searched against the ExpliotDB Database (sorry if that reads redundant) and displays potential vulnerabilities and attack vectors for the user to use in their respective pentest. I added some colored output to make it easier to read and well... pretty.

How to use: Download both the PAV and dictionary, throw them in the same directory/folder, then run the python program in the terminal (ex. python PAV.py).

DISCLAIMER: THIS IS A PROGRAM DESIGNED AND INTENDED FOR ETHICAL PENTESTING PURPOSES. ANY LAWS BROKEN, FOREIGN OR DOMESTIC, WITH SAID TOOL ARE AT THE DISCRETION AND SOLE CHOICE OF THE USER. DON'T BE STUPID, DO SOME GOOD, AND HAPPY HUNTING

