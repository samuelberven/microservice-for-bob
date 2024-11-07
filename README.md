# <span style="color: #2C3E50;">Random Number Generator Microservice</span>
A simple microservice built with <span style="color: #27AE60;">ZeroMQ</span> to communicate between a client and server. The client sends a request (in the form of a stringified integer) to the server, which responds with a JSON array containing a specified number of random integers.

## <span style="color: #E67E22;">Features</span>
- <span style="color: #3498DB;">ZeroMQ Communication</span>: The server and client communicate over ZeroMQ using socket-based messaging.
- <span style="color: #3498DB;">Random Number Generation</span>: The server generates a list of random integers based on the client’s request.
- <span style="color: #3498DB;">Customizable Parameters</span>: Clients can specify the number of random numbers, as well as optional upper and lower bounds for the values.

## <span style="color: #E67E22;">Installation</span>
To get started with the project, follow these installation steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/samuelberven/random_number_python_microservice.git

2. **Navigate** into the project directory:
   ```bash
    cd random_number_python_microservice
    ```

3. **Install** dependencies:
   ```bash
    pip install pyzmq
   ```

## How It Works
The client sends a request containing the following information:

- <span style="color: #9B59B6;">Number of random numbers</span> to generate.
- <span style="color: #9B59B6;">Lower limit</span> (optional, default is 1).
- <span style="color: #9B59B6;">Upper limit</span> (optional, default is 100).

The server listens for the request, generates the specified number of random integers within the given limits, and returns them as a JSON array.


### Example Request and Response
1. Client Request:
The **client** sends a JSON object with the following array:
   ```python
    request_details = [num_vals, lower_limit, upper_limit + 1]
    request_data = json.dumps(request_details)
    socket.send_string(request_data)
    ```
2. Server Response:
The <span style="color: #E67E22;">server</span> generates the specified number of random integers and sends them back in a <span style="color: #9B59B6;">JSON object</span>:
   <div style="background-color: #9B59B6; color: white; padding: 10px; border-radius: 4px;"> ```json { "random_numbers": [26, 44, 74, 49] } ``` </div>


### Request Details:
    ```num_vals```: The number of random numbers to generate.
    ```lower_limit```: The lower bound for the random numbers (default: 1).
    ```upper_limit```: The upper bound for the random numbers (default: 100).

### Example Flow:
1. **Client** (```client.py```) sends a request:
   ```python
   request_details = [10, 1, 100]
   request_data = json.dumps(request_details)
   socket.send_string(request_data)
   ```

2. **Server** (```server.py```) processes the request and generates 10 random numbers between 1 and 100:
    ```json
    {
      "random_numbers": [26, 44, 74, 49, 92, 51, 33, 81, 68, 29]
    }
    ```

## How to Run
### 1. Start the server: To start the server, run the following command:
    ```bash
    python server.py
    ```
### Run the client: After the server is running, you can start the client to send requests. Example:
    ```bash
    python client.py
    ```
### Request format: The client sends a JSON object containing:
- Number of random numbers to generate.
- Lower limit (optional).
- Upper limit (optional).
The server responds with a JSON object containing the array of random numbers.

### Dependencies
**pyzmq**: This library is used for communication between the server and client using ZeroMQ.
Install it via pip:
    ```bash
    pip install pyzmq
    ```

## License
This project is licensed under the MIT License

## References
- [ZeroMQ Documentation](https://zeromq.org/documentation/) - Official documentation for ZeroMQ.
- [Python `pyzmq` Library](https://pyzmq.readthedocs.io/en/latest/) - Python bindings for ZeroMQ.
- [JSON Documentation](https://www.json.org/json-en.html) - Official JSON format documentation.
