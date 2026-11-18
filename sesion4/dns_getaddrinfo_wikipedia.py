# Conecta con la web de Wikipedia usando getaddrinfo() y pide "/"
# Uso: python dns_getaddrinfo_wikipedia.py [4|6]   (por defecto IPv4)
import socket
import sys

HOST = "en.wikipedia.org"
familia = socket.AF_INET6 if len(sys.argv) > 1 and sys.argv[1] == "6" else socket.AF_INET

# Formas posibles de conectar con el servicio www de ese host
opciones = socket.getaddrinfo(HOST, "www", familia, socket.SOCK_STREAM)
print("Opciones:", opciones)

# Usamos la primera: (familia, tipo, protocolo, nombre_canonico, direccion)
family, type_, proto, canonname, sockaddr = opciones[0]
s = socket.socket(family, type_, proto)
s.connect(sockaddr)
print("Conectado a", sockaddr)

peticion = ("GET / HTTP/1.1\r\n"
            "Host: %s\r\n"
            "Connection: close\r\n"
            "\r\n" % HOST)
s.sendall(peticion.encode("ascii"))

# Recibir hasta que el servidor cierre la conexión
respuesta = b""
while True:
    datos = s.recv(4096)
    if not datos:
        break
    respuesta += datos
s.close()

print(respuesta.decode("utf-8", errors="replace"))
