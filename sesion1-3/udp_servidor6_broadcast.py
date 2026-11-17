import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Activar modo broadcast en el servidor
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(("", 12345))

print("Servidor HOLA escuchando en puerto 12345...")

while True:
    datagrama, origen = s.recvfrom(1024)
    texto = datagrama.decode("utf-8")
    
    if texto == "BUSCANDO HOLA":
        s.sendto(b"IMPLEMENTO HOLA", origen)
    elif texto == "HOLA":
        respuesta = f"HOLA: {origen[0]}"
        s.sendto(respuesta.encode("utf-8"), origen)