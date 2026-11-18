import poplib
import getpass
import email
import email.header

def imprime_resumen_mensaje(msg_bytes):
    msg = email.message_from_bytes(msg_bytes)
    remite = msg.get("From", "<desconocido>")
    asunto = msg.get("Subject", "<sin asunto>")
    
    remite = email.header.make_header(email.header.decode_header(remite))
    asunto = email.header.make_header(email.header.decode_header(asunto))
    
    cuerpo = msg.get_payload()
    if type(cuerpo) == list:
        parte_1 = cuerpo[0].get_payload()
        cuerpo = "---Multipart. Parte 1\n" + str(parte_1)
        
    print("From:", remite)
    print("Subject:", asunto)
    if isinstance(cuerpo, str):
        print(cuerpo[:500])
        if len(cuerpo) > 500:
            print("...[omitido]")
    print("-" * 80)

server = "pop.gmail.com"
username = input("Usuario: ")
password = getpass.getpass("Contraseña: ")

try:
    pop3_mail = poplib.POP3_SSL(server)
    pop3_mail.user(username)
    # Quitamos los espacios de la contraseña por si acaso
    pop3_mail.pass_(password.replace(" ", "")) 
    
    num_mensajes = len(pop3_mail.list()[1])
    print(f"\nHay {num_mensajes} mensajes disponibles para leer:\n" + "="*40)
    
    for i in range(1, num_mensajes + 1):
        respuesta, lineas, octetos = pop3_mail.retr(i)
        msg_bytes = b"\r\n".join(lineas)
        imprime_resumen_mensaje(msg_bytes)
        
    pop3_mail.quit()
except Exception as e:
    print(f"Error POP3: {e}")
