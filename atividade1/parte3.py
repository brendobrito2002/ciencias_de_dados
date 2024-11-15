import os
import pandas as pd

# 1) Crie um Dataframe (Cidades) (Vide Tabela 1)
# O Dataframe deve possuir 5 colunas e 5 linhas. Obs. (uma coluna é criada automaticamente e recebe o número
#  referente ao Id do registro criado.)

Cidades = pd.DataFrame({ 
    'ESTADO': ['Paraíba', 'Rio Grande Do Norte', 'Pernambuco', 'Ceará', 'Bahia'],
    'CIDADE': ['João Pessoa', 'Natal', 'Recife', 'Fortaleza', 'Salvador'],
    'HABITANTES': [604564, 765298, 890765, 149087, 1920613],
    'MÉDIA SALARIAL': [1500, 2000, 3023, 3200, 2199]
})

# 2) Para o Dataframe Cidades, faça/exiba (Usando funções básicas do Pandas):
# O Dataframe
print("2)a) ")
print(Cidades)

# Apenas as 2 primeiras linhas
print("\n2)b) ")
print(Cidades.head(2))

# Apenas as 2 últimas linhas
print("\n2)c) ")
print(Cidades.tail(2))

# Número de linhas e colunas. Ex.:(3, 6)
print("\n2)d) ")
print(Cidades.shape)

# Informações Gerais
print("\ne) ")
print(Cidades.info())

# O nome de todas as colunas
print("\nf) ")
print(Cidades.columns)

# As medidas estatísticas para os campos Média Salarial e Habitantes
print("\ng) ")
print(Cidades.describe())

# As informações gerais
print("\nh) ")
print(Cidades.info())

# Os tipos de dados
print("\ni) ")
print(Cidades.dtypes)

# Altere o tipo de dados da coluna Habitantes para float
print("\nj) ")
Cidades['HABITANTES'] = Cidades['HABITANTES'].astype(float)
print(Cidades.dtypes)

# Insira uma nova coluna chamada Data no formato “dia, mês e ano” e insira 5 datas aleatórias.
print("\nk) ")
Cidades['DATA'] = ['01/01/2001', '02/02/2002', '03/03/2003', '04/04/2004', '05/05/2005']
print(Cidades)

# Renomeei as colunas: Habitantes para N° Habitantes e Data para Data–Censo
print("\nl) ")
Cidades.rename(columns={'HABITANTES': 'N° HABITANTES'}, inplace=True)
Cidades.rename(columns={'DATA': 'DATA-CENSO'}, inplace=True)
print(Cidades.columns)

# Localize as informações apenas da cidade de Natal
print("\nm) ")
print(Cidades.loc[Cidades['CIDADE'] == 'Natal'])

# Localize as informações das cidades de João Pessoa e Fortaleza
print("\nn) ")
print(Cidades.loc[Cidades['CIDADE'].isin(['João Pessoa', 'Fortaleza'])])

# Localize as informações entre as cidades de Recife e Salvador
print("\no) ")
print(Cidades.iloc[2:5])

# Todas as linhas e apenas as duas primeiras colunas
print("\np) ")
print(Cidades.iloc[:, :2])

# As duas primeiras linhas e as 3 primeiras colunas
print("\nq) ")
print(Cidades.iloc[:2, :3])

# Todas as linhas e apenas as colunas na ordem: Cidade, Média Salarial, Estado e No Habitantes
print("\nr) ")
print(Cidades.loc[:, ['CIDADE', 'MÉDIA SALARIAL', 'ESTADO', 'N° HABITANTES']])

# Insira uma coluna chamada: Sigla, na posição [2] e insira os dados das siglas de cada estado existente
print("\ns) ")
Cidades.insert(2, "SIGLA", ['PB', 'RN', 'PE', 'CE', 'BA'])
print(Cidades)

# Adicione novamente a mesma coluna com nome: Sigla-Repetida e mesmos dados
print("\nt) ")
Cidades.insert(3, "SIGLA-REPETIDA", ['PB', 'RN', 'PE', 'CE', 'BA'])
print(Cidades)

# Usando Pop exclua a coluna Sigla-Repetida
print("\nu) ")
Cidades.pop('SIGLA-REPETIDA')
print(Cidades)

# Adicione novamente a mesma coluna com nome: Sigla-Repetida e mesmos dados
print("\nv) ")
Cidades.insert(3, "SIGLA-REPETIDA", ['PB', 'RN', 'PE', 'CE', 'BA'])
print(Cidades)

# Usando Drop exclua a coluna Sigla-Repetida
print("\nw) ")
Cidades.drop(columns=['SIGLA-REPETIDA'], inplace=True)
print(Cidades)

# Os dados que possuem Média Salarial menor que 2100 R$.
print("\nx) ")
print(Cidades.loc[Cidades['MÉDIA SALARIAL'] < 2100])

# Apenas os dados das cidades do estado de PE.
print("\ny) ")
print(Cidades.loc[Cidades['SIGLA'] == 'PE'])

# As cidades que possuem Número de Habitantes entre 500000 e 1500000
print("\nz) ")
print(Cidades.loc[(Cidades['N° HABITANTES'] > 500000) & (Cidades['N° HABITANTES'] < 1500000)])

# Ordenar os dados por ordem alfabética da coluna Cidades
print("\nA) ")
print(Cidades.sort_values(by='CIDADE'))

# Ordenar os dados por valor do Salário Médio
print("\nB) ")
print(Cidades.sort_values(by='MÉDIA SALARIAL'))

## 3) Crie um Dataframe (cidades_salarios) usando o Pandas (Vide Tabela 2)
# O Dataframe deve possuir 3 colunas e 5 linhas. Obs. (uma coluna é criada automaticamente e recebe o 
# número referente ao Id do registro criado.)
cidades_salarios = pd.DataFrame({
    'ESTADO': ['Paraíba', 'Rio Grande Do Norte', 'Pernambuco', 'Ceará', 'Bahia'],
    'CIDADE': ['João Pessoa', 'Natal', 'Recife', 'Fortaleza', 'Salvador'],
    'MÉDIA SALARIAL': [1500, 2000, 3023, 3200, 2199]
})
print("\nC) ", cidades_salarios)

# 4) Crie um Dataframe (cidades_pop) usando o Pandas (Vide Tabela 3)
# O Dataframe deve possuir 2 colunas e 5 linhas. Obs. (uma coluna é criada automaticamente e recebe o 
# número referente ao Id do registro criado.)
cidades_pop = pd.DataFrame({
    'CIDADE': ['João Pessoa', 'Natal', 'Recife', 'Fortaleza', 'Salvador', 'Teresina'],
    'HABITANTES': [604564, 765298, 890765, 149087, 1920613, 1678943]
})
print("\nD) ", cidades_pop)

# 5) Para os Dataframes cidades_salarios e cidades_pop, faça/exiba usando merge:
# Faça a união (Inner Join) dos dois Dataframes criados pela coluna Cidade
inner_join = pd.merge(cidades_salarios, cidades_pop, on='CIDADE', how='inner')
print("\nE) ", inner_join)

# Faça a união (full Outer Join) dos dois Dataframes criados pela coluna Cidade
# (Obs:. Registros do tipo NaN serão criados)
full_join = pd.merge(cidades_salarios, cidades_pop, on='CIDADE', how='outer')
print("\nF) ", full_join)

# 6) Crie dois Dataframes (cidades_df1) e (cidades_df2) respectivamente, usando o Pandas (Vide Tabela 4 e 5)
# O Dataframe deve possuir 3 colunas e 5 linhas. Obs. (uma coluna é criadaautomaticamente e recebe o 
# número referente ao Id do registro criado.)
cidades_df1 = pd.DataFrame({
    'CIDADE': ['João Pessoa', 'Natal', 'Recife'],
    'HABITANTES': [604564, 765298, 890765]
})
print("\nG) ", cidades_df1)

cidades_df2 = pd.DataFrame({
    'CIDADE': ['Salvador', 'Teresina'],
    'HABITANTES': [1920613, 1678943]
})
print("\nH) ", cidades_df2)

# Para os Dataframes cidades_df1 e cidades_df2, faça/exiba usando concat:
# o Combine os Dataframes em um único não ignorando os Index
combinados_df1 = pd.concat([cidades_df1, cidades_df2])
print("\nI) ", combinados_df1)

# o Combine os Dataframes em um único ignorando os Index
combinados_df2 = pd.concat([cidades_df1, cidades_df2], ignore_index=True)
print("\nJ) ", combinados_df2)

# 7) Salve o Dataframe cidades nos seguintes formatos:
# Cid_01.csv
Cidades.to_csv('atividade1/parte3-saves/Cid_01.csv', index=False)

# Cid_01.html
Cidades.to_html('atividade1/parte3-saves/Cid_01.html', index=False)

# Cid_01.json
Cidades.to_json('atividade1/parte3-saves/Cid_01.json', orient='records')

print("\nK) Arquivos salvos na pasta: parte3-saves")

# 8) Ler uma base csv de um link e apresentar os primeiros dados dessa base (sugestão:
# http://files.grouplens.org/datasets/movielens/ml-100k/u.user).
url = 'http://files.grouplens.org/datasets/movielens/ml-100k/u.user' 
colunas = ['ID', 'IDADE', 'GENERO', 'OCUPAÇÃO', 'ZIP-CODE']
df = pd.read_csv(url, delimiter='|', names=colunas)
print("\nL) ", df.head())

# 9) Ler uma base csv do arquivo do seu computador local e apresentar os primeiros dados dessa base.
df_local = pd.read_csv('atividade1/parte3-saves/Cid_01.csv')
print("\nM) ", df_local.head())