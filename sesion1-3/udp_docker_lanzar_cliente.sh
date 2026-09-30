#!/bin/bash
# Le pasaremos la IP de broadcast como argumento al ejecutar el script ($1)
IP_BROADCAST=$1

# Lanzamos el cliente de forma interactiva (-it) para ver su salida y que se borre al terminar (--rm)
docker run -it --rm --network pruebas -v $(pwd):/app python:3.9 python /app/udp_cliente6_broadcast.py $IP_BROADCAST