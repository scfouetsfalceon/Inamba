from twisted.internet import wxreactor
wxreactor.install()

from twisted.internet import protocol
from twisted.protocols import basic
import time


def t():
    return "[" + time.strftime("%H:%M:%S") + "] "


class EchoProtocol(basic.LineReceiver):
    def __init__(self):
        self.output = None

    def connectionMade(self):
        print "Connection from: " + self.transport.getPeer().host
        self.factory.clients.append(self)
        self.factory.gui.protocol = self
        self.sendLine("Welcome to The Matrix, Wizzard")
        self.sendLine("")

    def connectionLost(self, reason):
        print " Connection lost!!!"
        self.factory.clients.remove(self)

    def lineReceived(self, line):
        if line == 'quit':
            self.sendLine("Goodbye.")
            self.transport.loseConnection()
        else:
            self.sendMsg("Recibido: " + line)
            print "Recibido: " + line
            self.writeConsole(line)

    def sendMsg(self, message):
        self.sendLine(t() + message)

    def writeConsole(self, message):
        self.factory.gui.DesbloquearRemoto(message)

    def interactionClient(self, message):
        if len(self.factory.clients) != 0:
            self.sendMsg(message)

    def whatHappen(self):
        self.interactionClient(self.factory.gui.estado)


class EchoServerFactory(protocol.ServerFactory):
    def __init__(self, gui):
        self.gui = gui
        self.protocol = EchoProtocol
        self.clients = []
