import shutil
import os
import socket
import subprocess
import pyautogui

def error(e):
    print(e)
    send(e)

def help(helpFile):
    print(helpFile)
    send(helpFile)


def execute(name):
    try:
        subprocess.call(name)
        return "success"
    except Exception as e:
        error(e)


def send(datas):
    datas = str(datas)
    try:
        client_socket.send(datas.encode())
    except Exception as e:
        client_socket.send(str(e).encode())
        print(e)


def dir(dire):
    try:
        lisd = os.listdir(dire)
        stri = ""
        for i in lisd:
            stri += (i + '\n')
        return stri
    except Exception as e:
        error(e)



def delete(file):
    try:
        os.remove(file)
        send("success")
    except Exception as e:
        error(e)


def copy(file1, file2):
    try:
        shutil.copy(file1, file2)
        send("success")
    except Exception as e:
        error(e)


def screen_shootin():
    try:
        scrien = pyautogui.screenshot()
        scrien.save("C:\LOL\screenshot.png")
        return "C:\LOL\screenshot.png"
    except Exception as e:
        error(e)


def escape():
    send("close")
    server_socket.close()
    client_socket.close()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 8970))
server_socket.listen()
print("server up")
client_socket, client_adress = server_socket.accept()
print("client connected")
helpFile = "help.txt"
helpOpen = open(helpFile)
helpRead = helpOpen.read()
help(helpRead)
while True:
    data = client_socket.recv(1024).decode()
    print("client sent " + data)
    data = data.split()
    if data[0].upper() == "EXEC":
        send(execute(data[1]))
    elif data[0].upper() == "DIR":
        send(dir(data[1]))
    elif data[0].upper() == "COPY":
        copy(data[1], data[2])
    elif data[0].upper() == "SCREENSHOT":
        client_socket.send("pic".encode())
        filep = screen_shootin()
        try:
            scb = open(filep, 'rb')
            scn = scb.read()
            client_socket.send(scn)
        except Exception as e:
            error(e)
    elif data[0].upper() == "DELETE":
        delete(data[1])
    elif data[0].upper() == "HELP":
        help(helpRead)
    elif data[0].upper() == "EXIT":
        break
    else:
        print("sorry not a valid command")
        send("sorry not a valid command, type \"HELP\" for help")
escape()
