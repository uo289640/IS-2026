import socket
import sys

def main():
    port = 9999
    addr = "localhost"
    if len(sys.argv) > 1:
        port = int(sys.argv[1])

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.bind(("", args.puerto))
    try:
        while True:
            datagrama, origen = s.recvfrom(1024)
            print("Datagrama recibido desde {origen}")
    finally:
        s.close()