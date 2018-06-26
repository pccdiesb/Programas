# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 09:35:12 2018

@author: rodrigo aragao pinto

"""



import numpy as np
import pandas as pd

# importando arquivos (trocar caminho para máquina local)

file = 'C:\\Users\\rodar\\Documents\\Ciencia de Dados\\IESB\\Introducao CD - Sergio Cortes\\PCCD\\2011-CEAPS.xls'
df_2011 = pd.read_excel(file)

file = 'C:\\Users\\rodar\\Documents\\Ciencia de Dados\\IESB\\Introducao CD - Sergio Cortes\\PCCD\\2012-CEAPS.xls'
df_2012 = pd.read_excel(file)

file = 'C:\\Users\\rodar\\Documents\\Ciencia de Dados\\IESB\\Introducao CD - Sergio Cortes\\PCCD\\2013-CEAPS.xls'
df_2013 = pd.read_excel(file)

file = 'C:\\Users\\rodar\\Documents\\Ciencia de Dados\\IESB\\Introducao CD - Sergio Cortes\\PCCD\\2014-CEAPS.xls'
df_2014 = pd.read_excel(file)

file = 'C:\\Users\\rodar\\Documents\\Ciencia de Dados\\IESB\\Introducao CD - Sergio Cortes\\PCCD\\2015-CEAPS.xls'
df_2015 = pd.read_excel(file)

file = 'C:\\Users\\rodar\\Documents\\Ciencia de Dados\\IESB\\Introducao CD - Sergio Cortes\\PCCD\\2016-CEAPS.xls'
df_2016 = pd.read_excel(file)

file = 'C:\\Users\\rodar\\Documents\\Ciencia de Dados\\IESB\\Introducao CD - Sergio Cortes\\PCCD\\2017-CEAPS.xls'
df_2017 = pd.read_excel(file)

file = 'C:\\Users\\rodar\\Documents\\Ciencia de Dados\\IESB\\Introducao CD - Sergio Cortes\\PCCD\\2018-CEAPS.xls'
df_2018 = pd.read_excel(file)


# concatenando os arquivos
frames = [df_2011, df_2012, df_2013, df_2014, df_2015, df_2016, df_2017, df_2018]

ceaps = pd.concat(frames)

ceaps.describe

# apagando colunas do data frame
del ceaps['DOCUMENTO']
del ceaps['DATA']
del ceaps['DETALHAMENTO']
del ceaps['MES']

ceaps.dtypes

#convertendo tipos das colunas
ceaps['VALOR_REEMBOLSADO'] = pd.to_numeric(ceaps['VALOR_REEMBOLSADO'], errors='coerce')

ceaps.dtypes

ceaps.describe().T


## criando grupos de análise
ceaps = ceaps[ceaps['VALOR_REEMBOLSADO'] > 0]

ceaps_ate100 = ceaps[ceaps['VALOR_REEMBOLSADO'] < 100]

ceaps_ate100.describe().T

ceaps_entre_100e1000 = ceaps.query('VALOR_REEMBOLSADO>100 and VALOR_REEMBOLSADO<1000')

ceaps_entre_100e1000.describe().T

ceaps_maior_1000 = ceaps.query('VALOR_REEMBOLSADO>1000')

ceaps_maior_1000.describe().T

## apagando mais colunas e agrupando por ano / senador
ceaps_1 = ceaps[ceaps['VALOR_REEMBOLSADO'] > 0]
del ceaps_1['TIPO_DESPESA']
del ceaps_1['CNPJ_CPF']
del ceaps_1['FORNECEDOR']

ceaps_1.describe().T

qtde_reembolso_ano = ceaps_1.groupby('ANO').count()
total_ano = ceaps_1.groupby('ANO').sum()
media_ano = ceaps_1.groupby('ANO').mean()
desv_padrao_ano = ceaps_1.groupby('ANO').std()

qtde_ree_por_senador = ceaps_1.groupby('SENADOR').count()

qtde_ree_por_senador.describe().T

total_ano.describe().T

print (qtde_reembolso_ano, total_ano, media_ano)


PorAno = ceaps.groupby('ANO')

PorAno.mean()
PorAno.sum()
df_PorAno = PorAno.describe().T

df_PorAno.describe

senador = ceaps.groupby('SENADOR')

senador.mean()
senador.sum()
senador.describe().T

ceaps_1.to_csv('C:\\Users\\rodar\\Documents\\Ciencia de Dados\\cesp_resumo.csv', sep=';',  encoding='utf-8')


## Definir função de cálculo de erros padrão
#Importar bibliotecas
'''
import numpy as np
from scipy import stats

def erro_padrao(ceaps_1):
    ceaps_1 = ceaps_1[~np.isnan(ceaps_1)]

    numerador = np.std(ceaps_1, ddof=1)
    denominador = np.sqrt(len(ceaps_1))
    
    return numerador / denominador
'''


