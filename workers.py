import threading
import queue

cola_tareas = queue.Queue()


def worker():
    while True:
        tarea, cola_resultado = cola_tareas.get()

        try:
            resultado = str(eval(tarea))
        except Exception as e:
            resultado = f"Error: {e}"

        cola_resultado.put(resultado)

        cola_tareas.task_done()


for i in range(3):
    hilo = threading.Thread(target=worker, daemon=True)
    hilo.start()