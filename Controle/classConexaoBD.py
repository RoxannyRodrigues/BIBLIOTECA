import mysql.connector


class ConexaoBD():
  
    def __init__(self, host = "localhost", user = "root", password = 7289, database = "biblioteca"):
        self._host = host
        self._user = user
        self._password = password
        self._database = database

    def conecta(self):
        self.con = mysql.connector.connect (host = self._host, 
                                            user = self._user, 
                                            password = self._password,
                                            database = self._database)
        
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
       
        
