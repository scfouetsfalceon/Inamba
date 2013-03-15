# -*- coding: utf-8 -*-
import Image
import PSDraw
from datetime import datetime
from random import randint
import os

class imprimirComprobante:

    def __init__(self, cabecera, cconsejo, ccorte, consejo, corte, tipo):
        # Creando nombre de archivo
        nombre = randint(12387912837812739812, 12873918273912236753423987124)
        self.cabecera = cabecera

        # Momento del Voto
        # now = datetime.now()
        # self.tiempo1 = "       Fecha: " + str(now.day) + "/" + str(now.month) + "/" + str(now.year) + "\r\n"
        # self.tiempo2 = "         Hora: " + str(now.hour) + ":" + str(now.minute) + "\n\r\n"
        self.tiempo1 = "\r\n"
        self.tiempo2 = "\n\r\n"


        # Votantes
        self.cantidadconsejo = cconsejo
        self.consejo = consejo
        self.cantidadcorte = ccorte
        self.corte = corte
        if tipo == "text":
            self.archivito = "/tmp/" + str(nombre) + ".txt"
            self.crearTickettxt()
        elif tipo == "ps":
            self.archivito = "/tmp/" + str(nombre) + ".ps"
            self.crearTicketps()
        else:
            self.archivito = "/tmp/" + str(nombre) + ".txt"
            self.crearTickettxt()

    def crearTickettxt(self):
        #Aperturando Archivo
        ticket = open(self.archivito, "w")

        # Cabecera
        ticket.write("    Comprobante de Votaci\xf3n\r\n")
        ticket.write("     " + self.cabecera + "\r\n")

        ticket.write("" + self.tiempo1)
        #ticket.write(self.tiempo2)

        # Cuerpo del Ticket
        ticket.write("Consejo Nacional\r\n")

        a = 0
        # Armando Votos asamblea
        for i in self.consejo:
            ticket.write("- " + self.consejo[i] + "\r\n")
            a += 1

        ticket.write("Corte de Honor\r\n")

        a = 0
        # Armando Votos consejo
        for i in self.corte:
            ticket.write("- " + self.corte[i] + "\r\n")
            a += 1

        # Cerrando Archivos
        ticket.close()

    def crearTicketps(self):
        archivo = file(self.archivito, "w")
        ticket = PSDraw.PSDraw(archivo)
        letter = (1.0*72, 1.0*72, 7.5*72, 10.0*72)
        ticket.begin_document()

        # Cabecera
        ticket.setfont("Arial-Bold", 10)
        ticket.text((letter[0]-35, letter[1]+700), "Comprobante de Votaci\xf3n")
        ticket.text((letter[0]-30, letter[1]+690), "Asamblea Falc\xf3n 2011")
        ticket.setfont("Arial", 10)
        ticket.text((letter[0]-40, letter[1]+675), self.tiempo1)
        ticket.text((letter[0]-40, letter[1]+665), self.tiempo2)

        # Cuerpo del Ticket
        ticket.setfont("Arial-Bold", 10)
        ticket.text((letter[0]-40, letter[1]+650), "Consejo Nacional")
        ticket.setfont("Arial", 10)

        a = 0
        # Armando Votos asamblea
        for i in self.consejo:
            vertical = letter[1] + (640 - (10 * a))
            ticket.text((letter[0]-40, vertical), "- " + self.consejo[i])
            a += 1

        ticket.setfont("Arial-Bold", 10)
        ticket.text((letter[0]-40,  vertical - 15), "Corte de Honor")
        ticket.setfont("Arial", 10)

        a = 0
        # Armando Votos consejo
        for i in self.corte:
            ticket.text((letter[0]-40, vertical - (15 + (10 * (a+1)))), "- " + self.corte[i])
            a += 1
        #self.ticket.text((self.letter[0]-60, self.letter[1]+605), "- Fulano Detal")
        #self.ticket.text((self.letter[0]-60, self.letter[1]+595), "- Megano Detal")

        # Cerrando Archivos
        ticket.end_document()

    def __del__(self):
        comando = "lp %s" % self.archivito
        os.system(comando)
        comando = "cat %s >> ./auditoria/votacion.txt" % self.archivito
        os.system(comando)
        comando = "echo '' >> ./auditoria/votacion.txt"
        os.system(comando)
