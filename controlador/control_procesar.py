# -*- coding: utf-8 -*- 

class procesarVoto:
    def __init__(self, cconsejo, ccorte):
        self.consejo = {}
        self.corte = {}
        self.cconsejo = cconsejo
        self.ccorte = ccorte
        self.tVoto = 0
        self.tipoVoto(0)
        
    def tipoVoto(self, tipo):
        if tipo == 0:
            self.consejo.clear()
            self.corte.clear()
            self.guardar = self.consejo
            self.minimo = self.cconsejo
            self.tVoto = tipo
        else:
            self.guardar = self.corte
            self.minimo = self.ccorte
            self.tVoto = tipo
            
    def reciboVoto(self, id, voto):
        if self.guardar.has_key(id):
            del self.guardar[id]
            print self.guardar
            return False
        else:
            voto = voto.split("\n")
            self.guardar[id] = voto[0]
            print self.guardar
            return True

    def getMinimo( self ):
        return int(self.minimo)

    def getTipo(self):
        return self.tVoto
    
    def getVoto(self):
        return len(self.guardar)
    
    def getMsgVotos(self):
        ticket = u"Elegiste para:\n Consejo\n"
        print self.consejo
        print self.corte
        for aa in self.consejo:
            ticket += u" - %s\n" % self.consejo[aa]
        ticket += u"Corte de Honor\n"
        for aa in self.corte:
            ticket += u" - %s\n" % self.corte[aa]
        ticket += u"¿Estás seguro de tu voto?\n                                                                                          "
        return ticket
