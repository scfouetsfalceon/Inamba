# -*- coding: utf-8 -*-

# -------------------------------------------- #
#
# Copyright(C) 2009 - 2010 Jaro Marval(Jamp)
# Fecha: 16/11/2010
# Inamba - Terminal de Votación Scout
# correo: jampgold@gmail.com
#
# -------------------------------------------- #

# Generales
import wx, os
from datetime import datetime
# Modelo
from modelo import ddbb
# Controlador
from controlador import control_remoto, control_configuracion, control_parametros, control_procesar, control_imprimir  # , control_desbloquear
# Vista
from vista import votar, login
from twisted.internet import reactor


class Votandito(wx.Frame):

    def __init__(self):
        self.protocol = None
        self.estado = None
        self.configurar()
        self.login()

    def configurar(self):
        # Parametros
        configuracion = control_configuracion.Candidatos()
        self.resolucion = control_parametros.SIZE
        parametros = configuracion.parametros
        self.formato = control_parametros.FORMATO
        self.cabecera = control_parametros.CABECERA
        self.directorio = control_parametros.DIRECTORIO
        self.candidatosconsejo = configuracion.consejo
        self.candidatoscorte = configuracion.corte
        self.candidatos = self.candidatosconsejo

        # Resultado
        self.vconsejo = []
        self.vcorte = []
        self.votando = control_procesar.procesarVoto(parametros[0], parametros[1])
        # self.bloqueo = control_desbloquear.hiloEstado(self, control_parametros.TIME)

    def cambiar(self):
        self.votando.tipoVoto(1)
        self.candidatos = self.candidatoscorte
        self.respuestaConsole('Terminal Cambio a Corte')
        self.votar()

    def reiniciar(self):
        print "Reiniciar"
        self.votando.tipoVoto(0)
        self.candidatos = self.candidatosconsejo
        # self.login()
        self.respuestaConsole('Terminal Reiniciado')
        self.votar()

    def bloquear(self):
        print "Bloquear"
        self.votando.tipoVoto(0)
        self.candidatos = self.candidatosconsejo
        self.login()
        self.respuestaConsole('Terminal Bloqueado')
        # self.votar()

    def votar(self):
        print "Votar"
        self.terminal_votar = votar.ventana(self)
        self.terminal_votar.Show(True)
        self.respuestaConsole('Terminal Iniciando Votacion')
        print "Mostrar"

    def imprimir(self):
        control_imprimir.imprimirComprobante(self.cabecera, self.votando.cconsejo, self.votando.ccorte, self.votando.consejo, self.votando.corte, self.formato)
        dbase = ddbb.dbase()
        dbase.votos(self.votando.consejo, self.votando.corte)
        self.respuestaConsole('Terminal Imprimiendo')
        self.bloquear()

    def login(self):
        self.terminal = login.login(self)
        self.terminal.Show(True)
        #self.respuestaConsole('Terminal Abierto')

    def DesbloquearRemoto(self, mensaje):
        if mensaje == 'desbloquear':
            self.votar()
            self.terminal.Close()
        elif mensaje == 'bloquear':
            self.terminal_votar.Close()
            self.votando.tipoVoto(0)
            self.candidatos = self.candidatosconsejo
            self.login()
        elif mensaje == 'EstoySeguroDeReiniciarTodo!!!':
            print "Todo Reiniciado"
            self.reiniciarTodo()

    def reiniciarTodo(self):
        dbase = ddbb.dbase()
        dbase.vaciar()
        os.system("rm -rf /tmp/*.txt")
        now = datetime.now()
        hoy = str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute)
        os.system("mv ./auditoria/votacion.txt ./auditoria/votacion.txt.%s" % hoy)
        #os.system("reboot")

    # def desbloquear(self):
    #     print "Iniciando Hilo de Bloqueo de terminal"
    #     self.bloqueo.start()
    #     self.bloqueo.join()

    def respuestaConsole(self, mensaje):
        # self.estado = mensaje
        if self.protocol:
            self.protocol.interactionClient(mensaje)

if __name__ == '__main__':
    app = wx.App()
    inamba = Votandito()
    reactor.registerWxApp(app)
    reactor.listenTCP(5001, control_remoto.EchoServerFactory(inamba))
    reactor.run()
    app.MainLoop()
