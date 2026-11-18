# Muestra From y Subject de todos los correos de gmail,
# hablando POP3 directamente por un socket SSL
import getpass
import socket
import ssl
import sys


def RecvReply(s):
    respuesta = s.recv(1024)
    print(respuesta.decode("utf-8", errors="replace"), end="")
    if respuesta[:3] != b"+OK":
        print("ERROR: se esperaba +OK")
        sys.exit(1)
    return respuesta


server = "pop.gmail.com"
port = 995

username = input("Usuario: ")
password = getpass.getpass("Contraseña: ")

s = socket.socket()
s.connect((server, port))
context = ssl.create_default_context()
sc = context.wrap_socket(s, server_hostname=server)
RecvReply(sc)

sc.send(("USER %s\r\n" % username).encode("ascii"))
RecvReply(sc)
sc.send(("PASS %s\r\n" % password).encode("utf-8"))
RecvReply(sc)

sc.send(b"STAT\r\n")
stat = RecvReply(sc)
num_msgs = int(stat.split()[1])
print("Hay", num_msgs, "mensajes")

for n in range(1, num_msgs + 1):
    sc.send(("RETR %d\r\n" % n).encode("ascii"))
    datos = sc.recv(1024)
    if datos[:3] != b"+OK":
        print("ERROR en RETR:", datos.decode("utf-8", errors="replace"))
        sys.exit(1)
    while not datos.endswith(b"\r\n.\r\n"):
        datos += sc.recv(1024)

    print("--- Mensaje", n)
    cabeceras = datos.split(b"\r\n\r\n", 1)[0]
    for linea in cabeceras.split(b"\r\n"):
        if linea.startswith(b"From:") or linea.startswith(b"Subject:"):
            print(linea.decode("utf-8", errors="replace"))

sc.send(b"QUIT\r\n")
RecvReply(sc)
sc.close()
