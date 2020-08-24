# simple code snippet to bulk convert .csv files into .xlsx
# script simples para conversao de multilplos arquivos .csv em .xlsx

import pandas as pd
import os

# change those two strings
# alterar essas duas strings

#################################################################
importacao = '' # this one is the path to .csv files (origin) // essa com o diretorio de origem dos arquivos csv
exportacao = '' # this one is the path to .xlsx files (destiny) // essa com o diretorio para exportacao dos arquivos xlsx
#################################################################

lista = os.listdir(importacao)

if os.path.isdir(exportacao) == True: pass
else: os.mkdir(exportacao)

for i in lista:
    dados = pd.read_csv(importacao + i)
    nome, extensao = os.path.splitext(i)
    dados.to_excel(exportacao + nome + '.xlsx',
                   header = True,
                   index = False)

# *ps: the files keep their original names
# *obs: os arquivos serao exportados com o mesmo nome de origem