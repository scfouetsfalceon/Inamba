# -*- coding: utf-8 -*- 

import wx
from controlador import control_hilo

class entrada ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, None , id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( int(parent.resolucion[0]), int(parent.resolucion[1]) ), style = 0|wx.TAB_TRAVERSAL )
        #wx.Frame.__init__ ( self, None , id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 300, 300 ), style = 0|wx.TAB_TRAVERSAL )
        self.parent = parent
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        gSizer4 = wx.GridSizer( 1, 1, 0, 0 )
        
        sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Identificate" ), wx.VERTICAL )
        
        gSizer1 = wx.wx.FlexGridSizer( 3, 1, 0, 0 )
        
        self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"imagenes/vacio.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_bitmap1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Por Favor Acerque su Babero a la Cámara\r                  ", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.m_staticText1.Wrap( -1 )
        gSizer1.Add( self.m_staticText1, 0, wx.ALL, 30 )
        
        self.btn_alt = wx.Button( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.btn_alt, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        sbSizer1.Add( gSizer1, 0, 0, 0 )
        
        gSizer4.Add( sbSizer1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0 )
        
        self.SetSizer( gSizer4 )
        self.Layout()
      
        self.Centre( wx.BOTH )

    def __del__( self ):
        pass
    
    def Cerrar( self ):
        self.Close(True)

    def erroresText( self, error ):
        if error == 1:
            self.m_staticText1.SetLabel("Por Favor Acerque su Babero a la Cámara\r Votante No válido" )
        elif error == 2:
            self.m_staticText1.SetLabel( "Por Favor Acerque su Babero a la Cámara\r Ya voto" )