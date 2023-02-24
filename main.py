from Controle.classConexaoBD import ConexaoBD
from Modelo.classLivros import Livros
from Modelo.classCliente import Cliente
from Modelo.classAluguel import Aluguel

import mysql.connector

try:
    con = ConexaoBD()
    print("Conectou")

except(Exception,mysql.connector.Error) as error:
    print("Ocorreu um erro:", error)


print("Bem-vindo a biblioteca")
print('''Menu Principal:
1. Gerenciar Clientes
2. Gerenciar Livros
3. Gerenciar Alugueis
''')
escolha = input("Digite: ")
match escolha:
    case "1":
            print('''
            1. Consultar CLiente
            1. Cadastrar Cliente
            2. Atualizar Cliente
            3. Deletar Cliente
            4. Voltar 
            ''')
            escolha1 = input("Digite: ")
            match escolha1:
                 case "1":
                    escolha = input ("Digite id CLiente")
                    cliente = Cliente(escolha, None, None, None)
                    sql = cliente.consultarClientePorID()
                    resultado = con.consultarBanco(sql)  
                    print (f'{resultado}')

                      

