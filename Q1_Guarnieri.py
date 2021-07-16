import os
from pathlib import Path
import numpy as np

pasta ='C:/Users/Mateus Jácome/Documents/GitHub/VF_PEE_2021/Compras'
lista_arquivos = os.listdir(pasta)

Dicionario = {}
material = []
arquivos = []
Problematico = []

for arquivo in lista_arquivos:
    if arquivo != 'Relatório.txt':
        aux = Path('C:/Users/Mateus Jácome/Documents/GitHub/VF_PEE_2021/Compras/' + arquivo)
        arquivos.append(open(aux, 'r'))

for arquivo in arquivos:
    lista = arquivo.readlines()
    aux1 = np.array(lista)
    tam = len(aux1)
    aux1.shape = (tam, 1)
    for i in range(tam):
        mat = str(aux1[i])[2:].split(',')[0]
        if mat in material:
            Dicionario[mat].append(str(aux1[i])[2:].split(',')[1] + ' ' + (str(aux1[i])[2:].split(',')[2])[0:10])

        if mat not in material:
            material.append(mat)
            Dicionario[mat] = []
            Dicionario[mat].append(str(aux1[i])[2:].split(',')[1] + ' ' + (str(aux1[i])[2:].split(',')[2])[0:10])

for arquivo in arquivos:
   arquivo.close()

#Comparando os preços
for mat in material:
    menor = str(Dicionario[mat][0]).split(' ')[0]
    for i in range(len(Dicionario[mat])):
        if str(Dicionario[mat][i]).split(' ')[0] < menor:
            menor = str(Dicionario[mat][i]).split(' ')[0]
    for i in range(len(Dicionario[mat])):
        if float(str(Dicionario[mat][i]).split(' ')[0]) > 1.25*float(menor) and mat not in Problematico:
            Problematico.append(mat)

#Montando o arquivo do Relatório
rela = open('C:/Users/Mateus Jácome/Documents/GitHub/VF_PEE_2021/Compras/Relatório.txt', 'w')

rela.write('Item')

max = 0
for probl in Problematico:
    if len(Dicionario[probl]) > max:
        max = len(Dicionario[probl])


for i in range(max):
    rela.write('\t Preço ' + str(i+1) + '\t Data ' + str(i+1))

for probl in Problematico:
    rela.write('\n' + str(probl) + '\t')
    for i in range(len(Dicionario[probl])):
        rela.write('\t' + (Dicionario[probl])[i].split(' ')[0] + '\t' + (Dicionario[probl])[i].split(' ')[1])
    
rela.close()
