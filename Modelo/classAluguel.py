import mysql.connector

from Controle.classConexaoBD import *


class Aluguel:
    def __init__(self, id, dataaluguel, idcliente,idlivro):
        self._id = id
        self._dataaluguel = dataaluguel
        self._idcliente = idcliente
        self._idlivro = idlivro
    
    def imprimirAluguel(self):

        print(f'''
        ID - {self._id}
        dataaluguel - {self._dataaluguel}
        idcliente - {self._idcliente}
        idlivro - {self.__idlivro}
        ''')

    def consultaAluguelID(self):
        sql = f'''
        SELECT * FROM "aluguel"
        WHERE "id" = '{self._id}'
        '''
        return sql

