from tkinter import *

import sqlalchemy
import configparser


config_obj = configparser.ConfigParser()
config_obj.read("config.ini")
dbparam = config_obj["SenderConfig"]


window = Tk()
window.title("Konfiguracja połączenia")
window.minsize(width=350, height=200)

config_label = Label(text="Konfiguracja połączenia", font=("Arial", 12, "normal"))
config_label.grid(row=1, column=2)


def SaveSettings():
    print("Settings Saved!")
    config = configparser.ConfigParser()

    config.add_section('SenderConfig')
    config.set('SenderConfig', 'host', IP.get())
    config.set('SenderConfig', 'port', PORT.get())
    config.set('SenderConfig', 'id', OBJECT_ID.get())
    config.set('SenderConfig', 'name', OBJECT_NAME.get())
    config.set('SenderConfig', 'adres', ADDRESS.get())
    config.set('SenderConfig', 'mapa',  GOOGLE_MAPS.get())
    with open(r"config.ini", "w") as configfile:
        config.write(configfile)

#Buttons
IP = Entry(width=40)
IP_LABEL = Label(text="Adres IP Serwera: ", font=("Arial",8 , "normal"))
IP.insert(END, dbparam["host"])
IP_LABEL.grid(row=2, column=1)
IP.grid(row=2, column = 2)

PORT = Entry(width=40)
PORT_LABEL = Label(text="Port Serwera: ", font=("Arial",8 , "normal"))
PORT.insert(END, dbparam["port"])
PORT_LABEL.grid(row=3, column=1)
PORT.grid(row=3, column = 2)

OBJECT_NAME = Entry(width=40)
OBJECT_NAME_LABEL = Label(text="Nazwa Obiektu: ", font=("Arial",8 , "normal"))
OBJECT_NAME.insert(END, dbparam["name"])
OBJECT_NAME_LABEL.grid(row=4, column=1)
OBJECT_NAME.grid(row=4, column = 2)

OBJECT_ID = Entry(width=40)
OBJECT_ID.insert(END, dbparam["id"])
OBJECT_ID_LABEL = Label(text="ID Obiektu: ", font=("Arial",8 , "normal"))
OBJECT_ID_LABEL.grid(row=5, column=1)
OBJECT_ID.grid(row=5, column = 2)

ADDRESS = Entry(width=40)
ADDRESS_LABEL = Label(text="Adres Obiektu: ", font=("Arial",8 , "normal"))
ADDRESS.insert(END, dbparam["adres"])
ADDRESS_LABEL.grid(row=6, column=1)
ADDRESS.grid(row=6, column = 2)

GOOGLE_MAPS = Entry(width=40)
GOOGLE_MAPS_LABEL = Label(text="Google Maps: ", font=("Arial",8 , "normal"))
GOOGLE_MAPS.insert(END, dbparam["mapa"])
GOOGLE_MAPS_LABEL.grid(row=7, column=1)
GOOGLE_MAPS.grid(row=7, column = 2)

SAVE_BUTTON = Button(text="Zapisz", command=SaveSettings)
SAVE_BUTTON.place(x=225, y=175)








window.mainloop()

