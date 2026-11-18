# Envía un correo a través de gmail usando smtplib
import email.message, email.utils
import getpass
import smtplib

server = "smtp.gmail.com"
port = 587
fromaddr = "raquelmglez16@gmail.com"
toaddr = "raquelmglez16@gmail.com"
subject = "Prueba con smtplib"
data = "Hola, este correo se ha enviado con smtplib."

mensaje = email.message.EmailMessage()
mensaje['To'] = toaddr
mensaje['From'] = fromaddr
mensaje['Subject'] = subject
mensaje['Date'] = email.utils.formatdate(localtime=True)
mensaje['Message-ID'] = email.utils.make_msgid()
mensaje.set_content(data)
binario = mensaje.as_bytes()

username = input("Usuario: ")
password = getpass.getpass("Contraseña: ")

s = smtplib.SMTP(server, port)
s.set_debuglevel(1)
s.starttls()
s.login(username, password)
# smtplib añade el punto final por nosotros
s.sendmail(fromaddr, [toaddr], binario)
s.quit()
