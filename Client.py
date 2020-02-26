import sys
import socket
import threading


class Client():

    def __init__(self, client_name):

        # Create a TCP/IP socket and connect the socket to the port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = ('localhost', 8080)
        self.socket.connect(self.server_address)
        self.socket.setblocking(1)

        self.client_name = client_name
        send = threading.Thread(target=self._client_send)
        send.start()
        receive = threading.Thread(target=self._client_receive)
        receive.start()

    def _client_send(self):
        self.socket.send(bytes(self.client_name, encoding='utf-8'))  
        while True:
            try:
                c = input()
                sys.stdout.write("\x1b[1A\x1b[2K") # Delete previous line
                self.socket.send(bytes(c, encoding='utf-8')) 
            except:
                self.socket.close()
                return

    def _client_receive(self):
        while True:
            try:
                print(self.socket.recv(1024).decode("utf-8"))
            except:
                self.socket.close()
                return


if __name__ == "__main__":
    client_name = sys.argv[1]
    Client(client_name)