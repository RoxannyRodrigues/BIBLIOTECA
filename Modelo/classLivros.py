import mysql.connector

from Controle.classConexaoBD import *

class Livros():
    def __init__(self, id , nome, autor, ano, categoria):
        self.id = id
        self.nome = nome
        self.autor = autor
        self.ano = ano
        self.categoria = categoria
    
    def incluir (self,tabela):
        sql = f'''
        INSERT INTO "{tabela}"
        VALUES (default,'{self.nome}','{self.autor}',{self.ano}',{self.categoria} )'''

        return sql
    
    def visualizar (self):

        print(f'''
        Informações do Livros:
        ID - {self.id}
        Nome - {self.nome}
        Autor - {self.autor}
        Ano - {self.ano}
        Categoria - {self.categoria}''')
    
    def atualizarLivro(self,tabela):
        sql = f'''
        UPDATE "{tabela}"
        SET "Nome" = '{self.nome}', "Autor" = '{self.autor}, "Ano" = '{self.Ano}', "Categoria" = '{self.categoria}'
        WHERE "ID" = '`{self.id}'''

    def consultarAlugueis(self):
        sql = f'''
        SELECT * FROM "aluguel"
        WHERE "id_cliente" = '{self._id}'
        '''
        return sql