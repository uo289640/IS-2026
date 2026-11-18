# Lee el primer correo de gmail usando poplib
import getpass
import poplib

server = "pop.gmail.com"

username = input("Usuario: ")
password = getpass.getpass("Contraseña: ")

pop3_mail = poplib.POP3_SSL(server)
pop3_mail.set_debuglevel(2)

pop3_mail.user(username)
pop3_mail.pass_(password)

num_msgs, tam = pop3_mail.stat()
print("Hay", num_msgs, "mensajes")

if num_msgs > 0:
    # retr() devuelve (respuesta, lista de líneas, tamaño)
    respuesta, lineas, octetos = pop3_mail.retr(1)
    print(respuesta)
    for linea in lineas:
        print(linea.decode("utf-8", errors="replace"))

pop3_mail.quit()
