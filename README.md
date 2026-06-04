# PFO3-Sistema-Distribuido
PFO 3 - Rediseño de un sistema distribuido Cliente-Servidor utilizando sockets en Python.

# PFO 3 - Sistema Distribuido Cliente-Servidor

## Descripción

Este proyecto implementa una arquitectura cliente-servidor utilizando sockets en Python. El servidor recibe tareas enviadas por los clientes y las distribuye a un conjunto de workers para su procesamiento.

## Tecnologías utilizadas

* Python 3
* Sockets TCP
* Threads (threading)
* Queue

## Estructura del proyecto

* cliente.py: Cliente que envía tareas y recibe resultados.
* servidor.py: Servidor principal que recibe conexiones.
* workers.py: Pool de workers encargado de procesar las tareas.

## Ejecución

### Iniciar servidor

```bash
python servidor.py
```

### Iniciar cliente

```bash
python cliente.py
```

## Funcionamiento

1. El cliente envía una operación matemática.
2. El servidor recibe la tarea.
3. La tarea se coloca en una cola.
4. Un worker procesa la tarea.
5. El resultado se devuelve al cliente.

## Autor

Leonel Donnet
