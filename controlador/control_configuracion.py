# -*- coding: utf-8 -*-

import os
from ConfigParser import ConfigParser

class Candidatos:
    def __init__( self ):
        self.cfg = "boleta.cfg"
        self.boleta = ConfigParser()
        self.existeCFG()
        self.parametros = []
        self.consejo = []
        self.corte = []
        self.leerParametros()
        self.armarConsejo()
        self.armarCorte()

    def existeCFG( self ):
        if os.path.isfile(self.cfg):
            self.boleta.read(self.cfg)
            print "Existe"
        else:
            print "No Existe"

    def leerParametros( self ):
        self.parametros.append(int(self.boleta.get("VOTOS","asamblea")))
        self.parametros.append(int(self.boleta.get("VOTOS","corte")))
        self.parametros.append(int(self.boleta.get("VOTOS","tiempo")))

    def armarConsejo( self ):
        for i in range(1,10):
            candidato = []
            posicion = "CONSEJO" + str(i)
            if self.boleta.get(posicion,"nombre") != "":
                candidato.append(self.boleta.get(posicion,"nombre"))
                candidato.append(self.boleta.get(posicion,"linea1"))
                candidato.append(self.boleta.get(posicion,"linea2"))
                candidato.append(self.boleta.get(posicion,"linea3"))
                candidato.append(self.boleta.get(posicion,"imagen"))
                self.consejo.append(candidato)

    def armarCorte( self ):
        for i in range(1,10):
            candidato = []
            posicion = "CORTE" + str(i)
            if self.boleta.get(posicion,"nombre") != "":
                candidato.append(self.boleta.get(posicion,"nombre"))
                candidato.append(self.boleta.get(posicion,"linea1"))
                candidato.append(self.boleta.get(posicion,"linea2"))
                candidato.append(self.boleta.get(posicion,"linea3"))
                candidato.append(self.boleta.get(posicion,"imagen"))
                self.corte.append(candidato)
    