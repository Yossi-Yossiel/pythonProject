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
def send (data):
    data = str(data)
    try:
        my_socket.send(data.encode())
    except Exception as e:
        print(e)
        return False
def recv(num):
    num = int(num)
    try:
        d = my_socket.recv(num).decode()
        return d
    except Exception as e:
        print(e)
        return False

while connected == True:
    inp = input("system is UP! for help type help \n PLEASE REMEMBER TO USE FULL PATH WHEN MESSING AROUND WITH FILES")
    send(inp)
    data = recv(1024)
    if data == "close" or data == False:
        break
    elif data == "pic":
        scb = recv(9999999999)
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

