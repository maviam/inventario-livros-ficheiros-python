from inventario_funcoes import *
from getpass import getpass
from os import system

livros = []

while True:
    op = menu()
    match op:
        case 1:
            view(livros)
        case 2:
            add(livros)
        case 3:
            update_stock(livros)
        case 4:
            remove(livros)
        case 5:
            search_by_author_or_title(livros)
        case 6:
            report(livros)
        case 7:
            visualizar_log()
            getpass("\nPrima ENTER para voltar ao menu ...")
            system("cls")
        case 8:
            livros = load_json()
            sleep(3)
            system("cls")
        case 9:
            break

print("Aplicação finalizada!")
    
