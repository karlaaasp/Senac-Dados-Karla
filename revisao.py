import pandas as pd

dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
#sempre se atender a qual é o delimitador do csv, nesse caso é o ';'

df = pd.read_csv(dados, encoding= 'latin1', sep=';')

print(df.head(10))
#df.head(10) - imprime as 10 primeiras linhas 
#df.tail(10) - imprime as 10 últimas linhas 

df_furto_celular_cisp = df.groupby('cisp')['furto_celular'].sum().reset_index()
#.groupby - comando do pandas que agrupa 
#importante - para agrupar é regra dentro de (são as variaveis qualitativas) e [variaveis quantitativas]
#.sum() - somando a variavel que dentro dos colchetes
#.reset_index - retornar ao indice ja existente no arquivo

print(df_furto_celular_cisp)