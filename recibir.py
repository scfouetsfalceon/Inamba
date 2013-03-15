#!/usr/bin/env python
# -*- coding: utf-8 -*-
# servidor.py
import socket

s = socket.socket()
s.bind(("localhost", 9999))
s.listen(10)

sc, addr = s.accept()

while True:
    recibido = sc.recv(1024)
    if recibido == "quit":
        break
    print "Recibido:", recibido
    sc.send(recibido)

print "adios"

sc.close()
s.close()
