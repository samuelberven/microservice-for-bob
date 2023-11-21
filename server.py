#   Random number generator array server written in Python
#   Binds REP socket to tcp://*:5555
#   Expects a json from client with three values: the number of random numbers to return, 
#   the value lower limit (optional, default=1), and the upper limit (optional, default=100);
#   replies with b"{array of random numbers}"
import time
import zmq
import random
import json

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    request_json = socket.recv()

    # request_json contains three values: the number of random numbers 
    # to return, the value lower limit, and the upper  lower limit
    print(f"Received request: {request_json}. Calculating values, please wait.")
    request_data = json.loads(request_json)

    # converts three values into separate int variables
    numberOfVals = request_data[0]
    rangeLower = request_data[1]
    rangeHigher = request_data[2]

    randomNumbers = []
    for cycle in range(numberOfVals):
        randomNumbers.append(random.randrange(rangeLower, rangeHigher))

    # Ordinarily 1 second; it's just set to 3 seconds for the demonstration video
    # time.sleep(3)
    time.sleep(1)

    # Converts array of random numbers to json object
    response_data = json.dumps(randomNumbers)

    # Send reply back to client
    socket.send_string(response_data)
