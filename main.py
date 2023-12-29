import subprocess
import socket
import time
import json
from chars import*
host = "localhost"
port = 65432
s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_process = subprocess.Popen(["python", "./lcd.py"]) # or wherever your path is or you're running it from

# Wait for the server to start
time.sleep(1) 

# Optional (to test ebike repo)
# ph = "ph1234567890"
# km = "km1234567890"
# ah = "ah1234567890"
# dgC = "dgC1234567890"
# k1 = "k11234567890"
# mt = "mt1234567890"
# ms = "ms1234567890"
# bat = "bat1234567890"

def writechar(input, row, column):
    data = {
        'input': input,
        'row': row,
        'column': column
    }
    s1.sendto(json.dumps(data).encode(), (host, port))

column = 0

def setup(): # Stuff to be run once
    pass

def loop(): # Loops, make hello world move across screen, bit scuffed but you can see how powerful this lcd library is :-)
    global column
    for n in range(20):
        if n == 19:
            writechar("                    ", 0, column)
            column += 1
            n = 0
            if column > 3:
                column = 0
                writechar("                    ", 0, column)
        writechar(" ", n -1, column)
        writechar("Hello, World!", n, column)
        time.sleep(0.25)

if __name__ == "__main__":
    setup()
    while True:
        if server_process.poll() is not None:
            break
        time.sleep(0.01)
        loop()