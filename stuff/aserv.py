import shutil
import os
import socket
import subprocess
import pyautogui


def execute(name):
    try:
        subprocess.call(name)
    except Exception as e:
        send(e)
        print(e)


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
        print(e)
        send(e)



def delete(file):
    try:
        os.remove(file)
        send("success")
    except Exception as e:
        print(e)
        send(e)


def copy(file1, file2):
    try:
        shutil.copy(file1, file2)
        send("success")
    except Exception as e:
        send(e)
        print(e)


def screen_shootin():
    try:
        scrien = pyautogui.screenshot()
        scrien.save("C:\LOL\screenshot.png")
        send("success")
        return "C:\LOL\screenshot.png"
    except Exception as e:
        send(e)
        print(e)


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
data = client_socket.recv(1024).decode()
print("client sent " + data)
data = data.split()


