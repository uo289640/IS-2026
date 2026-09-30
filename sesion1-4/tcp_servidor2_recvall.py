import socket
import sys
import time  # Importamos time aquí arriba

def recvall(sock, num_bytes):
    datos = b""
    while len(datos) < num_bytes:
        fragmento = sock.recv(num_bytes - len(datos))
        if not fragmento:
            break
        datos += fragmento
    return datos

puerto = int(sys.argv[1]) if len(sys.argv) > 1 else 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", puerto))
s.listen(5)

print(f"Servidor TCP (recvall) escuchando en puerto {puerto}...")

while True:
    print("Esperando un cliente...")
    sd, origen = s.accept()
    
    # EXPERIMENTO: Retardo de 1 segundo para forzar la acumulación de mensajes
    time.sleep(1)
    
    print(f"Nuevo cliente conectado desde {origen}")
    continuar = True
    
    while continuar:
        datos = recvall(sd, 5)
        texto = datos.decode("ascii")
        
        if texto == "":
            print("Conexión cerrada de forma inesperada por el cliente.")
            sd.close()
            continuar = False
        elif texto == "FINAL":
            print("Recibido mensaje de finalización. Cerrando socket.")
            sd.close()
            continuar = False
        else:
            print(f"Recibido mensaje: {texto}")