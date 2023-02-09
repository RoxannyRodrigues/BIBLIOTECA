import mysql.connector


class ConexaoBD():


    def __init__(self, db = "biblioteca", host = "localhost", port = 3306, user = "root", password = 7289):
        self._db= db
        self._host = host
        self._port = port
        self._user = user
        self._password = password

    def conecta (self):
        self.con = mysql.connector.connect (db  = self._db,
                                           host = self._host, 
                                           port = self._port,
                                           user = self._user, 
                                           password = self._password)
        self.cur = self.con.cursor()


    def desconecta (self):
        self.con.close()

    def consultarBanco(self, sql):  #comandos select
        self.conecta()
        self.cur.execute(sql)
        resultado = self.cur.fetchall()
        self.desconecta()
        return resultado

    def manipularBanco(self,sql): #INSERT UPDATE DELETE
        self.conecta()
        self.cur.execute(sql)
        self.con.commit()
        self.desconecta()
       
        
