#   Random number generator array request client written in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends json to server with three values: the number of random numbers to return, the value lower 
#   limit (optional, default=1), and the upper limit (optional, default=100);
#   expects b"{array of random numbers}" json object back

import zmq
import json

context = zmq.Context()

#  Socket to talk to server
print("Connecting to random number generator server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

def randomNumGenerator(num_vals, lower_limit=1, upper_limit=100):
    # Combines three required values into single array
    print(f"Sending request {num_vals} value(s), range {lower_limit} to {upper_limit}...")

    # 1 added to upper-limit because range() is upper limit-exclusive
    request_details = [num_vals, lower_limit, upper_limit + 1]

    # converts array to json object and sends it
    request_data = json.dumps(request_details)
    socket.send_string(request_data)

    response_message = socket.recv()
    return_data = json.loads(response_message)

    # prints response array
    print(f"Received reply [ {return_data} ]")

    # can the socket automatically close?
    socket.close()

    return return_data


# randomNumGenerator(10)