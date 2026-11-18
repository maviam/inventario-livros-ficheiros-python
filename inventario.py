from inventario_funcoes import *
from time import sleep
from os import system
from getpass import getpass
livros = []

while True:
    op = menu()
    match op:
        case 1:
            view(livros)
            sleep(3)
            system("cls")
        case 2:
            add(livros)
            sleep(1)
            system("cls")
        case 3:
            update_stock(livros)
            sleep(3)
            system("cls")
        case 4:
            remove(livros)
            sleep(3)
            system("cls")
        case 5:
            search_by_author_or_title(livros)
            sleep(3)
            system("cls")
        case 6:
            report(livros)
            sleep(3)
            system("cls")
        case 7:
            visualizar_log()
            getpass("\nPrima ENTER para voltar ao menu ...")
            system("cls")
        case 8:
            livros = load_json()
            sleep(2)
            system("cls")
        case 9:
            break

print("Aplicação finalizada!")
    
