import mysql.connector

from Controle.classConexaoBD import *

class Livros():
    def __init__(self, id , nome, autor, categoria):
        self.id = id
        self.nome = nome
        self.autor = autor
        self.categoria = categoria
    
    def incluir (self,tabela):
        sql = f'''
        INSERT INTO "{tabela}"
        VALUES (default,'{self.nome}','{self.autor}', {self.categoria} )'''

        return sql
    
    def visualizar (self):

        print(f'''
        Informações do Livros:
        ID - {self.id}
        Nome - {self.nome}
        Autor - {self.autor}
        Categoria - {self.categoria}''')
    
    def atualizarLivro(self,tabela):
        sql = f'''
        UPDATE "{tabela}"
        SET "Nome" = '{self.nome}', "Autor" = '{self.autor}', "Categoria" = '{self.categoria}'
        WHERE "ID" = '`{self.id}'''

    def consultarAlugueis(self):
        sql = f'''
        SELECT * FROM "aluguel"
        WHERE "id_cliente" = '{self.id}'
        '''
        return sql