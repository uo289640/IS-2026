import socket
import sys

ip_servidor = sys.argv[1] if len(sys.argv) > 1 else "localhost"
puerto = int(sys.argv[2]) if len(sys.argv) > 2 else 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip_servidor, puerto))

palabras = ["HOLA", "REDES", "PYTHON"]

for palabra in palabras:
    # Añadimos el delimitador \r\n a cada mensaje
    mensaje = palabra + "\r\n"
    print(f"Enviando: {repr(mensaje)}")
    s.sendall(mensaje.encode("utf-8"))
    
    # Esperamos la respuesta
    respuesta_bytes = s.recv(80)
    respuesta_texto = respuesta_bytes.decode("utf-8")
    print(f"Respuesta recibida: {repr(respuesta_texto)}\n")

s.close()