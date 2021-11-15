import os
import socket

ip = input("enter the desired ip")
my_socket = socket.socket()
connected = True
try:
    my_socket.connect((ip, 8970))
    print("CONNECTED")
except Exception as e:
    connected = False
    print(e)
data = my_socket.recv(999999).decode()
print(data)

while connected == True:
    inp = input("system is UP! for help type help \n PLEASE REMEMBER TO USE FULL PATH WHEN MESSING AROUND WITH FILES")
    my_socket.send(inp.encode())
    data = my_socket.recv(1024).decode()
    if data == "close":
        break
    elif data == "pic":
        scb = my_socket.recv(9999999999)
        inp = input("enter the diretory you want to save")
        filename = input("now enter the picture name ")
        filelst = filename.split(".")
        if not filelst[-1].find("png"):
            filename + ".png"
        inpList = inp.split("\\")
        if not inpList[-1].find(".png"):
            inp += filename
        try:
            file = open(inp,'wb')
            file.write(scb)
            os.startfile(inp)
        except Exception as e:
            print(e)
        continue
    print(data)
my_socket.close()

