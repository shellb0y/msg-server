# -*- coding: utf-8 -*-
from socket import *

HOST = 'localhost'
PORT = 16908
BUFSIZ = 1024
ADDR = (HOST, PORT)
tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)


def get_sms(com):
    tcpCliSock.send('AP$SMS=%s,0\r\n' % com)
    data = tcpCliSock.recv(BUFSIZ)
    return data.strip().decode("gbk")


# def send_sms(com, data):
#     tcpCliSock.send('AP$TASK=%d,%s,%s\r\n' % (len(data), com, data))
#     data = tcpCliSock.recv(BUFSIZ)
#     return data.strip().decode("gbk")


def get_coms():
    tcpCliSock.send('AP$PORTS?\r\n')
    data = tcpCliSock.recv(BUFSIZ)
    return data.strip().split(',"')[1].replace('"', '').split(',')


def get_coms_status():
    data = []
    for com in get_coms():
        tcpCliSock.send('AP$PINFO=%s\r\n' % com)
        data.append(tcpCliSock.recv(BUFSIZ))
    return data


def close():
    tcpCliSock.close()
