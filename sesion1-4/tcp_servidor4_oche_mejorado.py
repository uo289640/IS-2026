import socket
import sys
import time

def recibe_mensaje(sock):
    """Lee byte a byte hasta encontrar \\r\\n"""
    buffer = []
    while True:
        byte = sock.recv(1)
        if not byte:
            break # El cliente cerró la conexión
        
        buffer.append(byte)
        
        # Si ya tenemos al menos 2 bytes, comprobamos si los últimos son \r\n
        if len(buffer) >= 2 and buffer[-2:] == [b'\r', b'\n']:
            break
            
    return b"".join(buffer)

puerto = int(sys.argv[1]) if len(sys.argv) > 1 else 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", puerto))
s.listen(5)

print(f"Servidor Oche (Mejorado) escuchando en puerto {puerto}...")

while True:
    print("Esperando un cliente...")
    sd, origen = s.accept()
    
    time.sleep(1) # Mantenemos el retardo para probar que ahora sí funciona
    
    print(f"Nuevo cliente conectado desde {origen}")
    
    while True:
        # Usamos nuestra función inteligente en lugar de recv(80)
        datos = recibe_mensaje(sd)
        if not datos:
            print("El cliente ha cerrado la conexión.")
            sd.close()
            break
            
        mensaje = datos.decode("utf-8")
        linea = mensaje[:-2] # Quitamos el \r\n
        linea_invertida = linea[::-1]
        
        respuesta = linea_invertida + "\r\n"
        sd.sendall(respuesta.encode("utf-8"))