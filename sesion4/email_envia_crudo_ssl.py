# Envía un correo por SMTP en crudo a través de gmail,
# con STARTTLS y autenticación AUTH LOGIN
import base64
import email.message, email.utils
import getpass
import socket
import ssl
import sys


def RecvReply(s, codigo):
    respuesta = s.recv(1024)
    print(respuesta.decode("utf-8", errors="replace"), end="")
    if respuesta[:3] != codigo:
        print("ERROR: se esperaba", codigo.decode(), "y se recibió", respuesta[:3].decode())
        sys.exit(1)


server = "smtp.gmail.com"
port = 587
fromaddr = "raquelmglez16@gmail.com"
toaddr = "raquelmglez16@gmail.com"
subject = "Prueba SMTP en crudo con SSL"
data = "Hola, este correo se ha enviado por gmail con STARTTLS desde un socket."

mensaje = email.message.EmailMessage()
mensaje['To'] = toaddr
mensaje['From'] = fromaddr
mensaje['Subject'] = subject
mensaje['Date'] = email.utils.formatdate(localtime=True)
mensaje['Message-ID'] = email.utils.make_msgid()
mensaje.set_content(data)
message = mensaje.as_bytes() + b"\r\n.\r\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server, port))
RecvReply(s, b"220")

s.send(b"EHLO " + socket.gethostname().encode("ascii") + b"\r\n")
RecvReply(s, b"250")

s.send(b"STARTTLS\r\n")
RecvReply(s, b"220")

# Negociar el canal seguro: a partir de aquí se usa sc
context = ssl.create_default_context()
sc = context.wrap_socket(s, server_hostname=server)

# Tras STARTTLS hay que volver a saludar
sc.send(b"EHLO " + socket.gethostname().encode("ascii") + b"\r\n")
RecvReply(sc, b"250")

sc.send(b"AUTH LOGIN\r\n")
RecvReply(sc, b"334")

username = input("Usuario: ")
password = getpass.getpass("Contraseña: ")

sc.send(base64.b64encode(username.encode("ascii")) + b'\r\n')
RecvReply(sc, b"334")

sc.send(base64.b64encode(password.encode("utf8")) + b'\r\n')
RecvReply(sc, b"235")

sc.send(("MAIL FROM:<%s>\r\n" % fromaddr).encode("ascii"))
RecvReply(sc, b"250")

sc.send(("RCPT TO:<%s>\r\n" % toaddr).encode("ascii"))
RecvReply(sc, b"250")

sc.send(b"DATA\r\n")
RecvReply(sc, b"354")

sc.sendall(message)
RecvReply(sc, b"250")

sc.send(b"QUIT\r\n")
RecvReply(sc, b"221")
sc.close()
