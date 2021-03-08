#!/usr/bin/env python
# coding=utf-8

import socket
import sys

import xtestd

def main():
    try:
        sock =  socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.connect(xtestd.SOCK_FILE)
        command = ' '.join(sys.argv[1:])
        # 发送 10|server list blabla...
        sock.sendall("{0}|{1}".format(len(command), command))
        _, result = xtestd.recv_all(sock).split('|')
        print('Received:', result)
    finally:
        sock.close()

if __name__ == "__main__":
    main()