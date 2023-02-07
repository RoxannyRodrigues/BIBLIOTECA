import mysql.connector

class Cliente:
    def __init__(self, id, nome, cpf, limitedelivros):
        self._id = id
        self._nome = nome
        self._cpf = cpf
        self._limitedelivros = limitedelivros
    
    def imprimirCliente(self):

        print(f'''
        ID - {self._id}
        Nome - {self._nome}
        CPF - {self._cpf}
        Limite de livros - {self._limitedelivros}
        ''')

    def consultarClientePorID(self):
        sql = f'''
        SELECT * FROM "cliente"
        WHERE "id" = '{self._id}'
        '''
        return sql

    def consultarClientePorCPF(self):
        sql = f'''
        SELECT * FROM "cliente"
        WHERE "cpf" = '{self._cpf}'
        '''
        return sql

    def consultarClientePorNome(self):
        sql = f'''
        SELECT * FROM "cliente"
        WHERE "nome" = '{self._nome}'
        '''
        return sql

    def consultarAlugueis(self):
        sql = f'''
        SELECT * FROM "aluguel"
        WHERE "id_cliente" = '{self._id}'
        '''
        return sql

    def inserirCliente(self):
        sql = f'''
        INSERT INTO "cliente"
        VALUES(default, '{self._nome}', '{self._cpf}')      
        '''
        return sql


    def atualizarCliente(self,tabela):
        sql = f'''
        UPDATE "{tabela}"
        SET "nome" = '{self.nome}', "cpf" = '{self.cpf}, "limitedelivros" = '{self._limitedelivros}'
        WHERE "id" = '`{self.id}'''

 
