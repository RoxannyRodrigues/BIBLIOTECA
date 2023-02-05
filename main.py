from Controle.classConexaoBD import ConexaoBD
from Modelo.classLivros import Livros

import mysql.connector

try:
    con = ConexaoBD("localhost", "root", "biblioteca")
    print("Conectou")

except(Exception,mysql.connector.Error) as error:
    print("Ocorreu um erro:", error)

def mostrarlivros(conexao):

    lista_livros = conexao.consultarBanco('''
    SELECT id, nome, autor, ano, categoria FROM livros
    ORDER BY id ASC
    ''')                                        #ORDER BY "ID" ASC  (serve para ordenar)     # ORDER BY "id" ASC  
    
    for liv in lista_livros:
        print(f"ID: {liv[0]} - Nome: {liv[1]} - Autor: {liv[2]} - Ano: {liv[3]} - Categoria: {liv[4]} \n")

teste = mostrarlivros(con)