import socket
from workers import cola_tareas

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Servidor escuchando en {HOST}:{PORT}")

while True:
    client_socket, addr = server.accept()

    print(f"Conexión desde {addr}")

    tarea = client_socket.recv(1024).decode()

    print(f"Tarea recibida: {tarea}")

    cola_tareas.put(tarea)

    client_socket.send("Tarea enviada al worker".encode())

    client_socket.close()
    