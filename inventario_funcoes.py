from datetime import datetime
from os import path
import json
from time import sleep
import os

ficheiro_log = "inventario.log"
ficheiro_json = "inventario.json"


def meu_decorador(funcao):
    def wrapper(*args, **kwargs):
        funcao(*args, **kwargs)
        sleep(3)
        os.system("cls")
    return wrapper

def registar_log(mensagem):
    return f"[{datetime.strftime(datetime.now(),"%d-%m-%Y %H:%M:%S")}] - {mensagem}\n"

def visualizar_log():
    if not path.exists(ficheiro_log):
        print("O ficheiro de log não existe ou está em outra localização")
    else:
        with open(ficheiro_log,"r") as f:
            for linha in f.readlines():
                print(linha.strip())

def save_json(inventario, mensagem):
    with open(ficheiro_json,"w") as f:
        json.dump(inventario,f,indent=4)
    print(mensagem)

def load_json():
    if not path.exists(ficheiro_json):
        print("O ficheiro com os dados do inventário não existe ou está em outra localização")
        return []
    with open(ficheiro_json,"r") as f:
        lista = json.load(f)
        print("Dados carregados com sucesso!")
    return lista

@meu_decorador
def view(inventario):
    if len(inventario) == 0:
        print("Não há livros no inventário atual!")
    else:
        for livro in inventario:
            print(f"{livro["titulo"]} (Id {livro["id"]})")
            print(f"Autor: {livro["autor"]}; Stock: {livro["qtde"]}; Preço atual: {livro["preco"]}")
            print("-"*40)

def novo_id(inventario):
    if len(inventario) == 0:
        return 1
    return inventario[len(inventario)-1]["id"] + 1

@meu_decorador
def add(inventario: list):
    print("DADOS DO LIVRO\n")
    titulo = input("Título: ")
    autor = input("Autor: ")
    stock = int(input("Qtde atual: "))
    preco = float(input("Preço de venda: "))

    livro = {"id": novo_id(inventario), "titulo": titulo, "autor": autor, "qtde": stock, "preco": preco}
    inventario.append(livro)
    with open(ficheiro_log,"a") as f:
        f.write(registar_log(f"Novo livro adicionado: {titulo} (Id {livro["id"]})"))
    save_json(inventario,"Livro guardado com sucesso")

@meu_decorador
def update_stock(inventario):
    found = False
    id_search = int(input("Digite o id do livro para atualização do stock: "))
    for livro in inventario:
        if livro["id"] == id_search:
            stock_antigo = livro["qtde"]
            new_stock = int(input("Stock atual: "))
            livro["qtde"] = new_stock
            found = True
            with open(ficheiro_log,"a") as f:
                f.write(registar_log(f"Stock atualizado: {livro["titulo"]} (Id {livro["id"]}) - Stock anterior: {stock_antigo} - Novo stock: {livro["qtde"]}"))
            save_json(inventario,"Stock do livro atualizado com sucesso")
            break
    if not found:
        print("Não existe nenhum livro em stock com o id indicado")

@meu_decorador
def remove(inventario: list):
    found = False
    id_search = int(input("Digite o id do livro para remoção do inventário: "))
    for livro in inventario:
        if livro["id"] == id_search:
            inventario.remove(livro)
            found = True
            with open(ficheiro_log,"a") as f:
                f.write(registar_log(f"Livro removido: {livro["titulo"]} (Id {livro["id"]})"))
            save_json(inventario,"Livro eliminado do inventário com sucesso")
            break
    if not found:
        print("Não existe nenhum livro em stock com o id indicado")

@meu_decorador
def search_by_author_or_title(inventario: list):
    found = False
    search = input("Digite o nome do livro ou do autor: ")
    for livro in inventario:
        autor: str = livro["autor"]
        titulo: str = livro["titulo"]
        if autor.find(search) >= 0 or titulo.find(search) >= 0:
            print(f"- {titulo} ({autor})")
            found = True
    if not found:
        print("Não existe nenhum livro em stock com o id indicado") 

@meu_decorador
def report(inventario):
    valor_inventario = 0
    for livro in inventario:
        valor_inventario += livro["qtde"] * livro["preco"]
    print(f"Valor atual do inventário: {round(valor_inventario,2)} euros")

def menu():
    print("GESTOR INVENTÁRIO\n")
    print("1- Visualizar inventário")
    print("2- Novo livro")
    print("3- Atualizar stock")
    print("4- Remover livro")
    print("5- Pesquisar livros por autor ou título")
    print("6- Valor atual em stock")
    print("7- Consultar histórico de operações")
    print("8- Carregar inventário")
    print("9- Sair")
    op = int(input("\nEscolha uma opção: "))
    return op



