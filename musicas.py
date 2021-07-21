import os
from tkinter import filedialog

def musica():
    return procurar()

def procurar():
    pasta = filedialog.askdirectory()
    return queue(pasta)

def queue(pasta):
    lista_de_musicas = list()
    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            lista_de_musicas.append(os.path.join(diretorio, arquivo))
    print(lista_de_musicas)
    return lista_de_musicas


