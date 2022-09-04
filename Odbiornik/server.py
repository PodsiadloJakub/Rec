import socket as s
from tkinter import *
import configparser
config_srv = configparser.ConfigParser()
config_srv.read("config_srv.ini")
dbparam = config_srv["ServerConfig"]

HOST = dbparam["host"]
PORT = dbparam["port"]
BUFFER = dbparam["buffer"]

def Status():
	print("Serwer uruchomiony")
	print(f"Adres IP serwera: {HOST}:{int(PORT)}")
def Read():
	wiadomosc = client_socket.recv(int(BUFFER)).decode("utf8")
	print(f"{wiadomosc}")

server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
server_socket.bind((HOST, int(PORT)))
server_socket.listen(2)
Status()
while True:
	client_socket, address = server_socket.accept()
	Read()


