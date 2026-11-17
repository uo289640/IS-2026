import socket
import sys
import random

puerto = int(sys.argv[1]) if len(sys.argv) > 1 else 9999
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", puerto))

# Aquí guardaremos los IDs de los mensajes que ya hemos procesado
procesados = set() 

print(f"Servidor UDP Mejorado escuchando en puerto {puerto}...")

while True:
    datagrama, origen = s.recvfrom(1024)
    texto = datagrama.decode("utf-8")
    
    # Simulamos pérdida de red (30% de probabilidad para probar los reintentos)
    if random.random() < 0.3:
        print(f"[!] Simulando pérdida en la red del paquete: {texto}")
        continue

    # Asumimos que el formato que nos llega es "ID:Mensaje"
    partes = texto.split(":", 1)
    if len(partes) == 2:
        id_msg = partes[0]
        
        # Filtro de duplicados
        if id_msg in procesados:
            print(f"[-] Duplicado detectado y omitido (ID: {id_msg}). Reenviando solo el OK.")
        else:
            procesados.add(id_msg)
            print(f"[+] Procesando mensaje nuevo de {origen}: {texto}")
        
        # Siempre enviamos el ACK incluyendo el ID que estamos confirmando
        respuesta = f"OK:{id_msg}"
        s.sendto(respuesta.encode("utf-8"), origen)