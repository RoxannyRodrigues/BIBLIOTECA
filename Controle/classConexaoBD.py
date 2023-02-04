import mysql.connector


class ConexaoBD():


    def __init__(self, host = "localhost", user = "root", db = "biblioteca" ):
        self.host = host
        self.user = user
        self.db= db

    def conecta (self):
        self.con = mysql.connector.connect(host = self.host, 
                                           user = self.user, 
                                           db   = self.db)
        self.cur = self.con.cursor()

    def desconecta (self):
        self.con.close()

    def consultarBanco(self, sql):  #comandos select
        self.conecta()
        self.cur.execute(sql)
        resultado = self.cur.fetchall()
        self.desconecta()
        return resultado


    def executa_DML(self,sql): #INSERT UPDATE DELETE
        self.conecta()
        self.cur.execute(sql)
        self.con.commit()
        self.desconecta()
       
        
