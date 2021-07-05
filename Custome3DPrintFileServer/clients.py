import socket
import os
import sys
import ntpath
from glob import glob as exists
def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)



def main():
    BUFFER = 2**32
    path = sys.argv[1]
    if not exists(path):
        exit(1)
    filename = path_leaf(path)
    s = socket.socket()
    s.connect(("192.168.0.24",4444))
    try:
        DATA = filename+"$*|*$"
        DATA = DATA.encode("utf-8")
        f = open(path,"rb")
        while True:
            bytes_read = f.read(BUFFER)
            if not bytes_read:
                break
            DATA+=bytes_read
        s.sendall(DATA)
        f.close()
        s.close()
        print(f"[+] {filename} has sent.")
    except Exception:
        print(f"[-] Unable to send the file: {filename}")
        return
if __name__ == "__main__":
    main()