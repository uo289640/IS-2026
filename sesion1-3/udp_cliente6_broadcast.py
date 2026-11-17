import socket
import sys

# Se requiere pasar la IP de broadcast como argumento
if len(sys.argv) < 2:
    print("Uso: python udp_cliente6_broadcast.py <IP_BROADCAST>")
    sys.exit(1)

ip_broadcast = sys.argv[1]
puerto = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Activar modo broadcast en el cliente
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.settimeout(2.0) # Tiempo de espera para descubrir servidores

print(f"Buscando servidores HOLA en {ip_broadcast}...")
s.sendto(b"BUSCANDO HOLA", (ip_broadcast, puerto))

servidores = []
try:
    while True:
        respuesta, origen = s.recvfrom(1024)
        if respuesta.decode("utf-8") == "IMPLEMENTO HOLA":
            print(f"Servidor encontrado en: {origen[0]}")
            servidores.append(origen[0])
except socket.timeout:
    print("Fin de la búsqueda.")

if servidores:
    primer_servidor = servidores[0]
    print(f"\nProbando el servicio HOLA con el primer servidor ({primer_servidor})...")
    # Ya no enviamos por broadcast, enviamos directamente a la IP
    s.sendto(b"HOLA", (primer_servidor, puerto))
    try:
        # Re-usamos el timeout configurado antes
        respuesta, origen = s.recvfrom(1024)
        print(f"Respuesta del servidor: {respuesta.decode('utf-8')}")
    except socket.timeout:
         print("No hubo respuesta a la prueba HOLA.")
else:
    print("No se encontraron servidores.")
s.close()