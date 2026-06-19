#!/bin/python3

import sys
import socket
from datetime import datetime

#define our target

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) # translate hostname into IPv4
else: 	
	print("Invalid amount of arguments.")
	print("Syntax: python3 portscanner.py <IP>")
	
#adding a banner

print("-" * 50)
print("Scanning target: "+target)
print("Time started: " +str(datetime.now()))
print("-" * 50)

try: 
	for port in range(75,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target, port)) 
		if result == 0:
			print(f"port {port} is open")
		s.close()
	
except KeyboardInterrupt:
	print("\nExiting program")
	sys.exit()
	
except socket.gaierror:
	print("Host could not be resolved")
	sys.exit()
	
except socket.error:
	print("Could not connect to the server")
	sys.exit()
	
