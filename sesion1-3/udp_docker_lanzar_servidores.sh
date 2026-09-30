#!/bin/bash
# 1. Creamos la subred aislada llamada 'pruebas'
docker network create pruebas 2>/dev/null || true

# 2. Lanzamos 3 contenedores idénticos en segundo plano (-d) con nombres distintos
docker run -d --name serv1 --network pruebas -v $(pwd):/app python:3.9 python /app/udp_servidor6_broadcast.py
docker run -d --name serv2 --network pruebas -v $(pwd):/app python:3.9 python /app/udp_servidor6_broadcast.py
docker run -d --name serv3 --network pruebas -v $(pwd):/app python:3.9 python /app/udp_servidor6_broadcast.py

echo "Tres servidores lanzados. Usa 'docker ps' para verlos."