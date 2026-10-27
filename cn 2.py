import socket

s = socket.socket()

host = input("Enter hostname or host IP: ")
port = 8080

s.connect((host, port))

print("Connected to chat server")

while True:
    incoming_message = s.recv(1024).decode()

    if not incoming_message:
        print("Server disconnected.")
        break

    print("Server:", incoming_message)
    print()

    message = input(">> ")
    s.send(message.encode())

    print("Sent")
    print()

s.close()
