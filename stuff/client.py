import socket

ip = input("enter the desired ip")
my_socket = socket.socket()
try:
    my_socket.connect((ip, 8970))
except Exception as e:
    print(e)

while True:
    inp = input("system is UP! for help type help PLEASE REMEMBER TO USE FULL PATH WHEN MESSING AROUND WITH FILES")
    my_socket.send(inp.encode())
    data = my_socket.recv(1024).decode()
    if data == "close":
        break
    elif data == "pic":
        scb = my_socket.recv(99999999)
        inp = input("enter the diretory you want to save")
        file = open(inp,'wb')
        file.write(scb)
        continue
    print(data)
my_socket.close()

