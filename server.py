#   Random number generator array server written in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"{array of random numbers}"
#

import time
import zmq
import random

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    message = socket.recv()
    print(f"Received request: {message}. Calculating values, please wait.")


    # Can be used for variable input
    # numberOfVals = int(input("How many random numbers? "))
    # rangeLower = int(input("What's the lower range? "))
    # rangeHigher = int(input("What's the higher range? "))

    numberOfVals = 10
    rangeLower = 1
    rangeHigher = 100

    randomNumbers = []
    for cycle in range(numberOfVals):
        randomNumbers.append(random.randrange(rangeLower, rangeHigher))
    # print(randomNumbers)


    # Ordinarily 1 second; it's just set longer here for the demonstration video
    time.sleep(3)
    # time.sleep(1)


    #  Send reply back to client
    # socket.send_string("World")
    socket.send_string(str(randomNumbers))
