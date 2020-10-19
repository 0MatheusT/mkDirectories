''' 
Gerador de diretórios com base em arquivos de texto
Feito por Matheus Tavares.
Importante: Arquivo deve conter nomes das pastas separados por quebras de linhas.
Nomes das pastas não podem ter caracteres especiais.
'''
# -*- coding: UTF-8 -*-
import os

arq= open("arquivo.txt", "r", encoding="utf8")

dir = './Diretórios/'       


for line in arq:
    if(len(line)>0):
        os.makedirs( dir + line.rstrip("\n") )
        print ("Foi criado um novo diretório para: " + line)


arq.close()