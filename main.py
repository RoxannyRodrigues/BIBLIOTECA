from Controle.classConexaoBD import ConexaoBD
from Modelo.classLivros import Livros

import mysql.connector

def mostrarlivros(conexao):

    lista_livros = conexao.consultarBanco('''
    SELECT "ID", "Nome","autor","ano","categoria" FROM "Livros"
    ORDE BY "ID" ASC  
    ''')                                        #ORDE BY "ID" ASC  (serve para ordenar)
    print ("ID | Nome          | Autor  ")
    for liv in lista_livros:
        print(f"{liv[0]} - {liv[1]} \n")

teste = mostrarlivros(None)