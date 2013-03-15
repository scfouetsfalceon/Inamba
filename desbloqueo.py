#!/usr/bin/env python
# -*- coding: utf-8 -*-
# cliente.py
import socket

s = socket.socket()
s.connect(("localhost", 8080))
# s.send(mensaje)

while True:
    mensaje = raw_input("> ")
    s.send(mensaje)
    if mensaje == "quit":
        break

print "adios"

s.close()
