import socket as s


HOST = '192.168.1.105'
PORT = 38012
BUFFER = 1924
server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(2)


print("Serwer uruchomiony")
print(f"Adres IP serwera: {HOST}:{PORT}")
def Read():
	wiadomosc = client_socket.recv(BUFFER).decode("utf8")
	print(f"{wiadomosc}")

while True:
	client_socket, address = server_socket.accept()
	Read()
