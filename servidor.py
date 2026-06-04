import socket
import queue
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

    cola_resultado = queue.Queue()

    cola_tareas.put((tarea, cola_resultado))

    resultado = cola_resultado.get()

    client_socket.send(resultado.encode())

    client_socket.close()

    