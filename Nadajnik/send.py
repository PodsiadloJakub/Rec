import socket as s
import random
import configparser

config_obj = configparser.ConfigParser()
config_obj.read("config.ini")
dbparam = config_obj["SenderConfig"]

HOST = dbparam["host"]
PORT = dbparam["port"]
ADRES = "Adres: " + dbparam["adres"]
MAPA = "Link do map: " + dbparam["mapa"]
OBJECT_ID = "ID Obiektu: " + dbparam["id"]
OBJECT_NAME = "Nazwa obiektu: " + dbparam["name"]
client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
client_socket.connect((HOST, int(PORT)))

def Action(value):
    switcher = {
        1: "Włamanie! ",
        2: "Sabotaż! ",
        3: "Napad! ",
        4: "Pożar! ",
    }
    return switcher.get(value, "")


nothing = "\n"


def SendAddress(value):
    client_socket.send(Action(value).encode("utf8"))
    client_socket.send(OBJECT_NAME.encode("utf8"))
    client_socket.send(nothing.encode("utf8"))
    client_socket.send(OBJECT_ID.encode("utf8"))
    client_socket.send(nothing.encode("utf8"))
    client_socket.send(ADRES.encode("utf8"))
    client_socket.send(nothing.encode("utf8"))
    client_socket.send(MAPA.encode("utf8"))
def SimulateObject():
    x = random.randint(1, 4)
    SendAddress(x)
    

SimulateObject()

