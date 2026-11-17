import socket
import sys
import random

puerto = int(sys.argv[1]) if len(sys.argv) > 1 else 9999
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", puerto))

print(f"Servidor UDP (con pérdidas) en puerto {puerto}...")

while True:
    datagrama, origen = s.recvfrom(1024)
    texto = datagrama.decode("utf-8")
    
    # Simular pérdida con un 50% de probabilidad
    if random.random() < 0.5:
        print(f"Simulando paquete perdido: {texto}")
    else:
        print(f"Recibido de {origen}: {texto}")