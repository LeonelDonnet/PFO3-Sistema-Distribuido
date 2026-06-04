import socket

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

tarea = input("Ingrese una tarea: ")

client.send(tarea.encode())

respuesta = client.recv(1024).decode()

print("Servidor:", respuesta)

client.close()
