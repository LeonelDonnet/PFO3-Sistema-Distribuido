import threading
import queue

cola_tareas = queue.Queue()


def worker():
    while True:
        tarea = cola_tareas.get()

        print(f"Worker procesando: {tarea}")

        resultado = eval(tarea)

        print(f"Resultado: {resultado}")

        cola_tareas.task_done()


for i in range(3):
    hilo = threading.Thread(target=worker, daemon=True)
    hilo.start()