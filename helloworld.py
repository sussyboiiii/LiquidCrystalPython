import json
import socket
import subprocess
import time
from chars import *

# server address details
host = "localhost"
port = 65432

# create a UDP socket using IPv4 address family
s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# start a separate process for the server
server_process = subprocess.Popen(["python", "./lcd.py"])  # update path if necessary

time.sleep(1)  # allow some time for the server to start

column = 0  # initial column for moving text

def setup():  # function to perform initial actions
    pass

def writechar(input, row, column):
    # create a dictionary to hold character data
    # input: the character to be written
    # row: the row on the screen where the character should be displayed
    # column: the column on the screen where the character should be displayed
    data = {"input": input, "row": row, "column": column}

    # send the data as a JSON object via the socket to the server
    s1.sendto(json.dumps(data).encode(), (host, port))

def loop():  # function to periodically update the screen
    global column
    for n in range(20):
        # when at the end of the screen, clear the top line and wrap to the left
        if n == 19:
            writechar("                    ", 0, column)
            column = (column + 1) % 4
            n = 0
        # determine the position for the next character
        position = (n - 1) if n > 0 else 0
        # clear a space for the character to enter the screen
        writechar(" ", position, column)
        # write the character to the screen
        writechar("Hello, World!", n, column)
        time.sleep(0.05)  # pause between iterations

if __name__ == "__main__":
    setup()  # perform initial actions
    # continue updating the screen while the server process is running
    while server_process.poll() is None:
        loop()
        time.sleep(0.01)  # pause between iterations