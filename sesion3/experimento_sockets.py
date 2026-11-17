import socket

# Creamos el socket y conectamos al puerto 23 (Telnet)
s = socket.socket()
s.connect(("localhost", 23))

# Recibimos la respuesta del servidor
respuesta = s.recv(1024)

# Mostramos cada byte recibido en formato hexadecimal
print("Respuesta en hexadecimal:")
for byte in respuesta:
    print(hex(byte), end=" ")
print()