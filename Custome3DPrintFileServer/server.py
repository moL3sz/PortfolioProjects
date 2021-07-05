import os
import socket
import time
from threading import Thread
BUFFER = 2**32
global s
connections = []
def printlog(t : str, s : str):
    types = {"i":"[*]","e":"[-]","s":"[+]"}
    if t in types:
        print(f"{types[t]} {s}")
    else:
        return 

    pass
def createServer():
    global s
    try:
        s = socket.socket()
        s.bind(("192.168.0.24",4444)) ##listening on IPv4 and 4444
        s.listen(1)
        printlog("s","Successfuly created")
    except Exception:
        printlog("e","Unable to create a server")
        printlog("i","Retrying in 2 sec...")
        time.sleep(2)
    pass
def handleConnection():
    global s
    while True:
        try:
            con,addr = s.accept()
            printlog("i",f"Got a connection from: {addr[0]}:{addr[1]}")
            connections.append(con)
        except Exception:
            printlog("e","An error has occured")
def handleData():
    while True: 
        for con in connections:
            data = con.recv(2**32)
            if data:
                print(data)
                filename,data = data.split(b"$*|*$")
                filename = filename.decode("utf-8")
                printlog("i",f"File: {filename}")
                filename, ext = filename.split(".")
                saveFile(filename+"_RECVD."+ext,data)
            if not data:
                con.close()
                connections.remove(con)
    pass
def saveFile(filename,data):
    with open(filename,"wb") as f:
        f.write(data)
    pass
def transferFileTo3DPrint():
    pass
def handleThreads():
    dataThread = Thread(target=handleData)
    connectionThread = Thread(target=handleConnection)
    dataThread.start()
    connectionThread.start()
    dataThread.join()
    connectionThread.join()

def main():
    createServer()
    handleThreads()
    pass

if __name__ == "__main__":
    main()