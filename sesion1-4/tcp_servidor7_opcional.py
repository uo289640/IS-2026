import socket
import sys
import struct

# Función segura para leer exactamente 'n' bytes
def recvall(sock, n):
    buffer = b""
    while len(buffer) < n:
        chunk = sock.recv(n - len(buffer))
        if not chunk:
            return b""
        buffer += chunk
    return buffer

puerto = int(sys.argv[1]) if len(sys.argv) > 1 else 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("", puerto))
s.listen(5)
print(f"Servidor Oche (Longitud Binaria) escuchando en puerto {puerto}...")

while True:
    print("Esperando cliente...")
    sd, origen = s.accept()
    print(f"Cliente conectado desde {origen}")
    
    while True:
        # 1. Leer EXACTAMENTE 2 bytes binarios (que contienen la longitud)
        bytes_longitud = recvall(sd, 2)
        if not bytes_longitud:
            print("Cliente desconectado.")
            break
            
        # 2. Desempaquetar esos 2 bytes a un número entero (">H" = Big Endian, unsigned short)
        # unpack devuelve una tupla, nos quedamos con el primer número [0]
        longitud = struct.unpack(">H", bytes_longitud)[0]
        
        # 3. Leer EXACTAMENTE la cantidad de bytes que nos ha dicho
        datos = recvall(sd, longitud)
        mensaje = datos.decode("utf8")
        print(f"Recibido mensaje de {longitud} bytes: {mensaje}")
        
        # 4. Invertir el mensaje y pasarlo a bytes
        datos_respuesta = mensaje[::-1].encode("utf8")
        
        # 5. Empaquetar la nueva longitud en 2 bytes y enviar todo (longitud + datos)
        bytes_long_resp = struct.pack(">H", len(datos_respuesta))
        sd.sendall(bytes_long_resp + datos_respuesta)
        
    sd.close()