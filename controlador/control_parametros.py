# -*- coding: utf-8 -*-
from ConfigParser import ConfigParser

INI = "config.ini"

print "Apertura de Archivo de configuración"
options = ConfigParser()
options.read(INI)
# Parametros Generales
SIZE = str(options.get("GENERAL", "resolucion")).split("x")
TIME = float(options.get("GENERAL", "tiempo"))
FORMATO = str(options.get("GENERAL", "formato"))
CABECERA = str(options.get("GENERAL", "cabecera"))
DIRECTORIO = str(options.get("GENERAL", "imagen_candidatos"))

# Parametros de la Conexión de BD
HOST = options.get("BD", "servidor")
USER = options.get("BD", "usuario")
PASS = options.get("BD", "contrasena")
DB = options.get("BD", "bd")
