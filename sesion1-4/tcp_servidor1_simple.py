import socket
import sys

puerto = int(sys.argv[1]) if len(sys.argv) > 1 else 9999
# SOCK_STREAM indica que usamos TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", puerto))
s.listen(5) # Máximo de clientes en cola de espera

print(f"Servidor TCP escuchando en puerto {puerto}...")

while True:
    print("Esperando un cliente...")
    sd, origen = s.accept()
    print(f"Nuevo cliente conectado desde {origen}")
    continuar = True
    
    while continuar:
        # Intentamos leer exactamente 5 bytes
        datos = sd.recv(5)
        texto = datos.decode("ascii")
        
        if texto == "":
            print("Conexión cerrada de forma inesperada por el cliente.")
            sd.close()
            continuar = False
        elif texto == "FINAL":
            print("Recibido mensaje de finalización. Cerrando socket de datos.")
            sd.close()
            continuar = False
        else:
            print(f"Recibido mensaje: {texto}")