#!/usr/bin/python
import nmap
import re
import collections
import signal  
import os  
import sys
import colorama as cr

#Gotta make it pretty
cr.init(autoreset=True)

#Introduction
print(f"{cr.Back.BLACK}{cr.Fore.BLUE}Port Attack Vectors{cr.Style.RESET_ALL} by {cr.Fore.BLUE}BT{cr.Fore.RED}RH!{cr.Style.RESET_ALL}\n")

#The program utilizes the Exploit DB using the searchsploit function
installCheck = input(f'Is {cr.Back.BLACK}{cr.Fore.GREEN}SearchSploit{cr.Style.RESET_ALL} already installed on this computer?: ')
if installCheck == 'n' or installCheck == 'N' or installCheck == 'no' or installCheck == 'NO':
	os.system('sudo apt -y install exploitdb')

#program starts by running an NMAP scan against the inputted IPv4 Address
#We make the scanner
scanner = nmap.PortScanner()

#Ask for the IP address
ip_addr = input(f'\nPlease enter your {cr.Fore.RED}target IPv4 address{cr.Style.RESET_ALL}: ')

#We run the scan
scanner.scan(ip_addr,'1-1024', '-sV -Pn')

#Print the various results of the scan
print('IP Status: ', scanner[ip_addr].state())
print(scanner[ip_addr].all_protocols())

results = str(scanner[ip_addr]['tcp'].keys())

#Here we list the available TCP ports that can be expoited 
x = re.findall('\d+', results)

def addToDictionary(dict, key, value):
    if key in dict:
        print('')
    else:
        dict[key] = value

filename = 'dictionary.txt'
f = open(filename, 'r')
dict1 = {}
for line in f:
    line = line.lstrip('')
    line = line.rstrip('\n')
    tokenizedLine = line.split(',')
    addToDictionary(dict1, tokenizedLine[0], tokenizedLine[1])
    
print(f'{cr.Fore.BLACK}{cr.Back.BLUE}Here is the list of exploitable ports: ', x)

#and ask the user to pick one to search
y = input('Please enter the number of the port you would like to research from the list above! (1-x; x for all): ')
if y == 'x' or y == 'X':
	for a in x:
		input = dict1[a]
		print(f'\n{cr.Fore.BLACK}{cr.Back.BLUE}You selected port ', a, 'which runs service :', input)
		print(f'{cr.Fore.BLACK}{cr.Back.BLUE}Attack vectors for port', a)
		try:
			base = "searchsploit " + input[1:input.index(' '):]
			os.system(base)
		except:
			base = "searchsploit " + input
			os.system(base)
else:	
	y = int(y) - 1
	input = dict1[x[y]]
	print(f'{cr.Fore.BLACK}{cr.Back.BLUE}You selected port', x[y], 'which runs service :', input)

	#Then we open MSFconsole and search the service for potential attack vectors
	base = "searchsploit " + input[1:input.index(' '):]

	print(f'Processing potential attack vectors in searchsploit...{cr.Style.RESET_ALL}')
	os.system(base)
	
print(f"\n{cr.Back.BLACK}{cr.Fore.BLUE}HAPPY HUNTING!!!{cr.Style.RESET_ALL}")
