import socket
import sys

def recibe_mensaje(sock):
    buffer = []
    while True:
        byte = sock.recv(1)
        if not byte:
            break
        buffer.append(byte)
        if len(buffer) >= 2 and buffer[-2:] == [b'\r', b'\n']:
            break
    return b"".join(buffer)

ip_servidor = sys.argv[1] if len(sys.argv) > 1 else "localhost"
puerto = int(sys.argv[2]) if len(sys.argv) > 2 else 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip_servidor, puerto))

palabras = ["HOLA", "REDES", "PYTHON"]

# 1. Enviar TODO de golpe (provocando la congestión)
for palabra in palabras:
    mensaje = palabra + "\r\n"
    print(f"Enviando: {repr(mensaje)}")
    s.sendall(mensaje.encode("utf-8"))

# 2. Leer las respuestas de forma segura
for i in range(3):
    # Usamos la función inteligente
    respuesta_bytes = recibe_mensaje(s)
    respuesta_texto = respuesta_bytes.decode("utf-8")
    print(f"Respuesta recibida: {repr(respuesta_texto)}")

s.close()