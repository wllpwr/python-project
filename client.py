import socket


HOST = "68.9.129.231"
PORT = 1234

# Create a TCP/IPv4 socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (HOST, PORT)
print(f'connecting to {server_address}')
try:
    sock.connect(server_address)
except TimeoutError:
    print("connection failed...")

data = sock.recv(24)
data = data.decode("ascii")
print(data)



print("Hello World!")