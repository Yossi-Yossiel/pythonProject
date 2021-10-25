import os
import shutil
import socket
import subprocess
import pyautogui

def dir(data):
    try:
        os.chdir(data)
        dire = os.listdir()
        return dire
    except Exception as e:
        print("there was an error \n", e)
        return e
def execute(data):
    try:
        subprocess.call(comm[1])
    except Exception as e:
        print("there was an error\n" + e)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0',8970))
server_socket.listen()
print("server up")
client_socket,client_adress = server_socket.accept()
print("client connected")
data = client_socket.recv(1024).decode()
print("client sent " + data)
comm = data.split(" ")
print(comm)

outp = ""
ischecking = True
while ischecking:
    if comm[0] == "dir":
        x = dir(comm[1])
        for i in x:
            outp += i
            outp += "\n"
    elif comm[0] == "exec":
        execute(data)
    elif comm[0] == "prtsc":
        try:
            img = pyautogui.screenshot
            img.save(r'C:\screen.jpg')

        except Exception as e:
            print(e)
    elif comm[0] == "copy":
        filep1 = comm[1]
        filep2 = comm[2]
        shutil.copy(filep1, filep2)
    elif comm[0] == "del" or comm[0] == "delete":
        filep3 = comm[1]
        os.remove(filep3)
    inp = input("have you done? (y/n)")
    if inp == "n":
        ischecking = False
client_socket.send(outp.encode())


client_socket.close()
server_socket.close()