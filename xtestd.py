#!/usr/bin/env python
# coding=utf-8

import socket
import os
import sys

SOCK_FILE = '/tmp/xtest'
BUF_SIZE = 10

def recv_all(conn):
    message = buf = conn.recv(BUF_SIZE)
    # 首条数据：10|server list blabla...
    total, buf = buf.split('|')
    recvs = len(buf)
    while recvs < int(total):
        buf = conn.recv(10)
        if not buf:
            break
        message += buf
        recvs += len(buf)
    return message

def serve():
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    if os.path.exists(SOCK_FILE):
        os.remove(SOCK_FILE)
    sock.bind(SOCK_FILE)
    sock.listen(10)
    print("xtest start ...")

    try:
        while True:
            conn, addr = sock.accept()
            data = recv_all(conn)
            conn.sendall(data)
    finally:
        conn.close()

if __name__ == "__main__":
    serve()