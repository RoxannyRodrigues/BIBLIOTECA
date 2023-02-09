from Controle.classConexaoBD import ConexaoBD
from Modelo.classLivros import Livros
from Modelo.classCliente import Cliente
from Modelo.classAluguel import Aluguel

import mysql.connector

try:
    con = ConexaoBD("biblioteca", "localhost",3306, "root", 7289)
    print("Conectou")

except(Exception,mysql.connector.Error) as error:
    print("Ocorreu um erro:", error)


#OPÇÕES DE LIVRO

def mostrarlivros(conexao):

    lista_livros = conexao.consultarBanco('''
    SELECT * FROM livros
    ''')                                        #ORDER BY "ID" ASC  (serve para ordenar)     # ORDER BY "id" ASC  
    
    for liv in lista_livros:
        print(f'ID: {liv[0]} - Nome: "{liv[1]}" - Autor: "{liv[2]}" - Categoria: "{liv[3]}" \n')

def menuAlterarLivro (conexao):

    print('''
    1. Atualizar Livro
    2. Remover Livro
    ''')

    opcoes = input("Digite o número da opção desejada: ")

    match opcoes:
        case "1":
            livroEscolhido = input("Escolha o id do livro deseja alterar: ")    #Criar busca também por nome
            livroConsulta = conexao.consultarBanco(f'''
            SELECT * FROM livros
            WHERE ID = {livroEscolhido}
            ''')
            opcoes = input('''
            Seleciona o que você deseja alterar:
            1 - Nome
            2 - Autor
            3 - Categoria 
            Digite:
            ''')
            match opcoes:
                case "1":
                    
                    novoNome = input("Digite o Novo Nome: ")
                    atualizacaoescolhida = conexao.manipularBanco(f'''
                    UPDATE livros SET nome = "{novoNome}" WHERE id = {livroEscolhido}''')
                    print("Alterado com sucesso")
                
                case "2":

                    novoAutor = input("Digite o Novo Autor: ")
                    atualizacaoescolhida = conexao.manipularBanco(f'''
                    UPDATE livros SET autor = "{novoAutor}" WHERE id = {livroEscolhido}''')
                    print("Alterado com sucesso")
                
                case "3":

                    novaCategoria = input("Digite a Nova Categoria: ")
                    atualizacaoescolhida = conexao.manipularBanco(f'''
                    UPDATE livros SET categoria = "{novaCategoria}" WHERE id = {livroEscolhido}''')
                    print("Alterado com sucesso")                    

            

#OPÇÕES DE CLIENTES

def mostrarClientes(conexao):
    print("Lista de Cliente")
    listacliente = conexao.consultarBanco('''
    SELECT id, nome, cpf,  `limite de livros` FROM cliente
   
    ''')

    for cliente in listacliente:
        print(f"ID: {cliente[0]} - Nome: '({cliente[1]})' - CPF: '({cliente[2]})' - Limite de Livros: '({cliente[3]})' \n")


def menuAlterarClientes(conexao):
    print(f'''
    
    Escolha uma das opções:
    1. Buscar Cliente
    2. Inserir novo Cliente
    ''')
    opcoes = input("Digite: ")
    match opcoes:
        case "1":
            print(f'''
            Buscar por:
            1. ID
            2. CPF
            ''')
            escolha = input("Digite: ")
            match escolha:
                case "1":
                    iddocliente = input("Digite o ID: ")
                    visualizacaocliente = conexao.consultarBanco(f'''
                    SELECT * FROM cliente
                    WHERE ID = {iddocliente}
                    ''')
                    for client in visualizacaocliente:
                        print(f"ID: {client[0]} - Nome: {client[1]} - CPF: {client[2]} - Limite de Livros: {client[3]} \n")

                case "2":
                    cpfdocliente = input("Digite o CPF: ")
                    visualizacaocliente = conexao.consultarBanco(f'''
                    SELECT * FROM cliente
                    WHERE cpf = {cpfdocliente}
                    ''')
                    for cpfclient in visualizacaocliente:
                        print(f"ID: {cpfclient[0]} - Nome: {cpfclient[1]} - CPF: {cpfclient[2]} - Limite de Livros: {cpfclient[3]} \n")
                        print(f'''
                        Deseja atualizar Cliente:
                        1. SIM
                        2. NÃO
                        ''')


teste = mostrarlivros(con)