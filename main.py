import json
import socket
import subprocess
import time
from chars import *

host = "localhost"
port = 65432

s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_process = subprocess.Popen(["python", "./lcd.py"])

time.sleep(1)

column = 0

def writechar(input, row, column):
    data = {"input": input, "row": row, "column": column}
    s1.sendto(json.dumps(data).encode(), (host, port))

def setup():
    pass

def loop():
    pass

if __name__ == "__main__":
    setup()
    while server_process.poll() is None:
        loop()
        time.sleep(0.01)