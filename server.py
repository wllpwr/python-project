# Server code for server testing

import socket
import psutil
import os

HOST = "localhost"
PORT = 1234


class ServerTesting:
	"""Test script to experiment with server management via Python."""

	def __init__(self, host, port):
		"""Initialize the socket."""

		address_tuple = (host, port)
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind(address_tuple)


	def run_server(self):
		"""Actually run the server."""

		self.sock.listen()
		print("Waiting for connections...")
		while True:
			connection, address = self.sock.accept()
			print("Client connected!")
            connection.sendall("peepee poopoo".encode("ascii"))


if __name__ == "__main__":
    server = ServerTesting(HOST, PORT)
    server.run_server()

