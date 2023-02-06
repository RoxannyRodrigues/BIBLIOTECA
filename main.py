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
            ''')[0]
            #livro = Livros(livroConsulta[0],livroConsulta[1],livroConsulta[2],livroConsulta[3],livroConsulta[4]) # explicação
            opcoes = input('''
            Seleciona o que você deseja alterar:
            1 - Nome
            2 - Autor
            3 - Ano
            4 - Categoria 
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

                    novoAno = input("Digite o Novo Ano: ")
                    atualizacaoescolhida = conexao.manipularBanco(f'''
                    UPDATE livros SET ano = {novoAno} WHERE id = {livroEscolhido}''')
                    print("Alterado com sucesso")

                case "4":

                    novaCategoria = input("Digite a Nova Categoria: ")
                    atualizacaoescolhida = conexao.manipularBanco(f'''
                    UPDATE livros SET categoria = "{novaCategoria}" WHERE id = {livroEscolhido}''')
                    print("Alterado com sucesso")                    

            

teste = menuAlterarLivro(con)