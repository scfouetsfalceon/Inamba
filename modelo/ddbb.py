import MySQLdb

from controlador import control_parametros


class dbase:
    def __init__(self):
        config = control_parametros
        self.conex = MySQLdb.connect(host=config.HOST, user=config.USER, passwd=config.PASS, db=config.DB)

    def votos(self, consejo, corte):
        self.cursor = self.conex.cursor()
        sql = "INSERT INTO `votos` VALUES (NULL, 1)"
        print sql
        self.cursor.execute(sql)

        cn = consejo.keys()
        for v in cn:
            sql = "INSERT INTO `consejo` VALUES (NULL, %i)" % v
            print sql
            self.cursor.execute(sql)

        ch = corte.keys()
        for v in ch:
            sql = "INSERT INTO `corte` VALUES (NULL,  %i)" % v
            print sql
            self.cursor.execute(sql)

        self.conex.commit()

    def vaciar(self):
        self.cursor = self.conex.cursor()
        sql = "TRUNCATE `consejo`;TRUNCATE `corte`;TRUNCATE `votos`;"
        self.cursor.execute(sql)
        #self.conex.commit()

    def __del__(self):
        self.cursor.close()
        self.conex.close()
