import socket

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

tarea = input("Ingrese una operación: ")

client.send(tarea.encode())

resultado = client.recv(1024).decode()

print(f"Resultado recibido: {resultado}")

client.close()