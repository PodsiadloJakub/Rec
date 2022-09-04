from tkinter import *
import configparser
#test
objects_list = configparser.ConfigParser()
objects_list.read("objects.ini")

window = Tk()
window.title("NezEye")
window.minsize(width=1820, height=480,)


def listbox_used(event):
    print(listbox.get(listbox.curselection()))

def ServerConfig():
    configwindow = Tk()
    configwindow.title("Konfiguracja połączenia")
    configwindow.minsize(width=350, height=200)
    configwindow.mainloop()

objects = []

listbox = Listbox(height=50)
for id in objects:
    listbox.insert(objects.index(id), id)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(row=2, column=1)

server_button = Button(text="Start Server")
server_button.grid(row=1, column=1,)
server_config_button = Button(text="Config Server", command=ServerConfig)
server_config_button.grid(row=1, column=2,)

window.mainloop()
