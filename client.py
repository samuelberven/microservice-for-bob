#   Random number generator array request client written in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends a stringified int to server, expects a stringified array of random numbers back
#

import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to random number generator server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response
for request in range(1):
    print(f"Sending request {request} ...")
    socket.send_string("10")

    #  Get the reply.
    message = socket.recv()
    print(f"Received reply {request} [ {message} ]")

    