# -*- coding: utf-8 -*-

# -------------------------------------------- #
#
# Copyright (C) 2009 - 2010 Jaro Marval (Jamp)
# Fecha: 16/11/2010
# Inamba - Terminal de Votación Scout
# correo: jampgold@gmail.com
#
# -------------------------------------------- #

import wx
import socket
import threading

class login(wx.Frame):

    def __init__(self, parent):
        self.parent = parent
        wx.Frame.__init__(self, None, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(int(parent.resolucion[0]), int(parent.resolucion[1])), style=0 | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"Bienvenido\nPor favor espere que el operador desbloquee el terminal", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE)
        self.m_staticText1.Wrap(-1)
        self.m_staticText1.SetFont(wx.Font(24, 74, 90, 90, False, "Sans"))
        bSizer2.Add(self.m_staticText1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"Desbloquear", wx.DefaultPosition, wx.Size(200, 50), 0)
        self.m_button1.SetFont(wx.Font(9, 74, 90, 92, False, "Sans"))
        self.m_button1.SetBackgroundColour(wx.Colour(84, 131, 235))
        bSizer2.Add(self.m_button1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer1.Add(bSizer2, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)
        self.m_button1.Bind(wx.EVT_BUTTON, self.Desbloquear)

    def Desbloquear(self, event):
        print "Desbloqueo del Terminal"
        self.parent.respuestaConsole('Intento desbloquearla')
        # self.parent.votar()
        # self.Close()
