# -*- coding: utf-8 -*- 

# -------------------------------------------- #
#
# Copyright (C) 2009 - 2010 Jaro Marval (Jamp)
# Fecha: 16/11/2010
# Inamba - Terminal de Votación Scout
# correo: jampgold@gmail.com
#
# -------------------------------------------- #

import wx, os

class ventana ( wx.Frame ):
    def __init__( self, parent ):
        print "Entramos"
        self.parent = parent
        self.candidatos = []

        #wx.Frame( self, parent, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( int(parent.resolucion[0]), int(parent.resolucion[1]) ), 0|wx.TAB_TRAVERSAL )
        wx.Frame.__init__ ( self, None, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( int(parent.resolucion[0]), int(parent.resolucion[1]) ), style = 0|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.Colour( 233, 233, 233 ) )
        principal = wx.GridSizer( 1, 1, 0, 0 )
        
        cuerpo = wx.FlexGridSizer( 3, 1, 0, 0 )
        cuerpo.SetFlexibleDirection( wx.BOTH )
        cuerpo.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.lbl_titulo = wx.StaticText( self, wx.ID_ANY, u"Espere..", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lbl_titulo.Wrap( -1 )
        self.lbl_titulo.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        
        cuerpo.Add( self.lbl_titulo, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        fgSizer2 = wx.FlexGridSizer( 3, 3, 0, 0 )
        fgSizer2.SetFlexibleDirection( wx.BOTH )
        fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
            
        print "bucle"
        i = 1
        for a in self.parent.candidatos:
# ----- Capsula para votar --------
            contenedor = wx.FlexGridSizer( 1, 2, 0, 0 )
            contenedor.SetFlexibleDirection( wx.BOTH )
            contenedor.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
            img = str(self.parent.directorio) + '/' + a[4]
            if (os.path.exists(img)):
                print "Existe Foto"
                print img
            else:
                print "No hay Foto"
                img = u"imagenes/silueta.png"

            self.img_candidato = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( img, wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 125,112 ), 0 )
            contenedor.Add( self.img_candidato, 0, wx.ALL, 5 )
            
            boton = a[0] + "\n" + a[1] + "\n" + a[2] + "\n" + a[3]
            self.btn_candidato = wx.Button( self, i, boton, wx.DefaultPosition, wx.Size( 200,112 ), 0 )
            self.btn_candidato.SetFont( wx.Font( 9, 74, 90, 80, False, "Sans" ))
            contenedor.Add( self.btn_candidato, 0, wx.ALL|wx.EXPAND, 5 )
            self.btn_candidato.Bind( wx.EVT_BUTTON, self.OnVotar )
            
            fgSizer2.Add( contenedor, 1, wx.ALL|wx.EXPAND, 20 )
            i += 1
# ----- Capsula para votar --------
        print "bucle"
        cuerpo.Add( fgSizer2, 1,  wx.EXPAND, 5 )
        
        self.btn_votar = wx.Button( self, wx.ID_ANY, u"Espere..", wx.DefaultPosition, wx.Size( 200,50 ), 0 )
        self.btn_votar.SetFont( wx.Font( 9, 74, 90, 92, False, "Sans" ) )
        self.btn_votar.SetBackgroundColour( wx.Colour( 84, 131, 235 ) )
        cuerpo.Add( self.btn_votar, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        principal.Add( cuerpo, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        #print self.app
        self.SetSizer( principal )
        self.Layout()

        self.Centre( wx.BOTH )
        self.btn_votar.Bind( wx.EVT_BUTTON, self.OnVotando )
        self.armarTarjeton()
        print "Tarjeton Armado"

    def OnVotar( self, event ):
        id = event.GetEventObject().GetId()
        datos = event.GetEventObject().GetLabelText()
        if self.parent.votando.reciboVoto(id, datos):
            event.GetEventObject().SetBackgroundColour( wx.Colour( 151, 204, 51 ) )
            event.GetEventObject().SetForegroundColour( wx.Colour( 255, 255, 255 ) )
            event.GetEventObject().SetFont( wx.Font( 9, 74, 90, 92, False, "Sans" ) )
            print "Voto"
        else:            
            event.GetEventObject().SetBackgroundColour( wx.NullColor )
            event.GetEventObject().SetForegroundColour( wx.NullColor )
            event.GetEventObject().SetFont( wx.Font( 9, 74, 90, 80, False, "Sans" ))
            print "Desvoto"

    def OnVotando( self, event ):

        if self.parent.votando.getVoto() >= 1 and self.parent.votando.getVoto() <= self.parent.votando.getMinimo():
            if self.parent.votando.getTipo() == 0:
                self.parent.cambiar()
                self.Close()
            else:
                msg = self.parent.votando.getMsgVotos()
                terminar = wx.MessageBox(msg, u"Voto Válidado", wx.YES_NO)
                if terminar == wx.YES:
                    print "Acepto!!!"
                    # Linea para Imprimir
                    self.parent.respuestaConsole('Voto!!!')
                    self.parent.imprimir()
                    self.Close()
                else:
                    print "No acepto :'("
                    self.parent.reiniciar()
                    self.Close()
        else:
            if self.parent.votando.getVoto() == 0:
                wx.MessageBox("Debe elegir al menos una persona por la cual votar", u"Voto Vacío", wx.OK | wx.ICON_ERROR)
            else:
                Mensaje = "Debe elegir a %s personas como máximo por las cuales votar" % self.parent.votando.getMinimo()
                wx.MessageBox(Mensaje, u"Voto Vacío", wx.OK | wx.ICON_ERROR)

    def armarTarjeton(self):
        if self.parent.votando.getTipo() == 0:
            txt_info = "Por Favor elija sus candidatos para el Consejo"
            txt_votar = "Siguiente"
        else:
            txt_info = "Por Favor elija sus candidatos para la Corte de Honor"
            txt_votar = "Votar"

        self.lbl_titulo.SetLabel(txt_info)
        self.btn_votar.SetLabel(txt_votar)
