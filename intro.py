# try:
#     f = open("dados.txt","r",encoding="utf-8")
#     conteudo = f.read()
#     print(conteudo)
#     f.close()
# except FileNotFoundError as e:
#     print(f"Erro ao abrir o ficheiro: {e}")

# f = open("data.txt","a",encoding="utf-8")
# f.write("Dados da terceira linha\n")
# f.write("Dados da quarta linha\n")
# f.close()

# f = open("data.txt","r+",encoding="utf-8")
# f.seek(0,2)
# f.write("Nova linha\n")
# f.seek(0,0)
# conteudo = f.read()
# f.close()
# print(conteudo)

# with open("data.txt","r") as f:
#     i = 1
#     conteudo = f.readline()
#     while conteudo != "":
#         print(f"{i}: {conteudo}",end="")
#         i = i + 1
#         conteudo = f.readline()

# with open("data.txt","r") as f:
#     i = 1
#     conteudo = f.readlines()
#     print(conteudo,"\n")
#     for frase in conteudo:
#         print(f"{i}: {frase}",end="")
#         i = i +1
