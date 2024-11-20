import numpy as np
import pandas as pd

df = pd.DataFrame({
    'A': [1, np.nan, 3, np.nan, ' '],
    'B': [4, np.nan, np.nan, np.nan, 3],
    'C': [7, np.nan, 9, np.nan, 11],
    'D': [5, 4, 9, np.nan, ' ']
})
print(df)

# Exibir e identificar a quantidade de dados ausentes de cada atributo do dataset. (OBS.: O pandas não 
# considera valores “ “ como ausentes, nesse caso devemos substituir “ “ por valores NaN. Isso não ocorre 
# quando fazemos a leitura de um arquivo .csv. Não os substitua agora).
r1 = df.isna().sum()
print("\na) ")
print(r1)

# Remover os objetos com valor ausente em qualquer atributo usando ‘any’ (Percebam que todas as linhas que 
# contenham pelo menos 1 atributo vazio será eliminada do dataset).
r2 = df.dropna(how='any')
print("\nb) ")
print(r2)

# Remover os objetos com valor ausente em todos os atributos usando ‘all (Percebam que apenas as linhas em 
# que todos os dados dos atributos eram ausentes foram eliminadas.
r3 = df.dropna(how='all')
print("\nc) ")
print(r3)

# Substitua todos os valores “ “ por NaN e reaplique os códigos anteriores e analise os resultados obtidos.
df.replace(" ", np.nan, inplace=True)
print("\nd) ")
print(df)

r4 = df.isna().sum()
print("\ne) ")
print(r4)

r5 = df.dropna(how='any')
print("\nf) ")
print(r5)

r6 = df.dropna(how='all')
print("\ng) ")
print(r6)

# Carregar a tabela de usuários
url_users = "http://files.grouplens.org/datasets/movielens/ml-100k/u.user"
colunas_users = ["user_id", "age", "gender", "occupation", "zip_code"]
usuarios = pd.read_csv(url_users, sep='|', names=colunas_users, encoding='latin-1')
print("Tabela de Usuários:")
print(usuarios.head())

# Carregar a tabela de filmes
url_filmes = "http://files.grouplens.org/datasets/movielens/ml-100k/u.item"
colunas_filmes = ["movie_id", "movie_title", "release_date", "video_release_date", "IMDb_URL", "unknown", "Action", "Adventure", "Animation", "Children", "Comedy", "Crime", "Documentary", "Drama", "Fantasy", "FilmNoir", "Horror", "Musical", "Mystery", "Romance", "SciFi", "Thriller", "War", "Western"]
filmes = pd.read_csv(url_filmes, sep='|', names=colunas_filmes, encoding='latin-1')
print("\nTabela de Filmes:")
print(filmes.head())

# Carregar a tabela de avaliações
url_avaliacoes = "http://files.grouplens.org/datasets/movielens/ml-100k/u.data"
colunas_avaliacoes = ["user_id", "movie_id", "rating", "timestamp"]
avaliacoes = pd.read_csv(url_avaliacoes, sep='\t', names=colunas_avaliacoes, encoding='latin-1')
print("\nTabela de Avaliações:")
print(avaliacoes.head())

# Ajustar tipos de Dados
# Com os dados carregados faça:

# Note que a coluna gênero é categórica, mas o tipo de dado apresentado para ela é object com a função 
# astype transforme esses valores em category.
usuarios['gender'] = usuarios['gender'].astype('category')
print("\nh) ")
print(usuarios.dtypes)

# Altere os rótulos de M e F para Masculino e Feminino
usuarios['gender'] = usuarios['gender'].replace({'M': 'Masculino', 'F': 'Feminino'})
print("\ni) ")
print(usuarios)

# Para ocupação e cep também são do tipo Object deixe-os como category.
usuarios['occupation'] = usuarios['occupation'].astype('category')
usuarios['zip_code'] = usuarios['zip_code'].astype('category')
print("\nh) ")
print(usuarios.dtypes)

# Na tabela filmes note que video_release_date não esta no formato adequado, transforme para o formato 
# "%d-%b-%Y" e formato datetime64.
filmes['video_release_date'] = pd.to_datetime(filmes['video_release_date'], format='%d-%b-%Y', errors='coerce')
print("\ni) ")
print(filmes.dtypes)

# Na tabela avaliacoes exiba: os valeres únicos da coluna rating ordenados de forma crescente e explique 
# cada argumento do código abaixo.
# o avaliacoes.rating = avaliacoes.rating.astype(CategoricalDtype(categories=avaliacoes.rati g.unique().sort(), ordered=True)).
r7 = sorted(avaliacoes['rating'].unique())
print("\nj) ")
print(r7)

print("\navaliacoes.rating: Refere-se à coluna rating do DataFrame avaliacoes.") 
print("\nastype(CategoricalDtype(...)): Converte a coluna rating para o tipo categórico.") 
print("\ncategories=avaliacoes.rating.unique().sort(): Define as categorias para a coluna categórica. Onde avaliacoes.rating.unique() retorna os valores únicos da coluna rating, e sort() ordena esses valores de forma crescente.") 
print("\nordered=True: Indica que as categorias têm uma ordem específica.")

# Apresente uma descrição estatística da coluna rating.
print("\nk) ")
print(avaliacoes["rating"].describe())

# Converta o tipo de dados da coluna timestamp para datetime e apresente uma descrição estatística para 
# essa coluna.

avaliacoes['timestamp'] = pd.to_datetime(avaliacoes['timestamp'], unit='s')
print("\nl) ")
print(avaliacoes.dtypes)
print("\n")
print(avaliacoes["timestamp"].describe())

# Valores Ausentes
# Com os dados carregados faça:

# Verifique se na tabela filmes existem dados ausentes, se sim quantos em cada coluna?
r8 = filmes.isna().sum()
print("\nm) ")
print(r8)

# Remova as linhas da tabela filmes que possuem valores ausentes (NaN) nas colunas release_date e/ou IMDb_URL.
print("\nn) ")
filmes = filmes.dropna(subset=["release_date", "IMDb_URL"])
print(filmes.isna().sum())

# Remova as colunas da tabela filmes que têm todos os seus valores como NaN (ausentes).
print("\no) ")
filmes = filmes.dropna(axis=1, how='all')
print(filmes.isna().sum())

# Note que 1 valor de um filme não possui release_data, veja se esse valor é inconsistente, procure o filme,
#  se for inconsistente (e é) elimine apenas esse filme.
r9 = filmes[filmes["release_date"].isnull()]
if not r9.empty:
    filmes = filmes.drop(r9.index)

print("\np) ")
print(r9)

# A função fillna preenche dados ausentes, preencha com a moda, a moda é são os valores mais frequentes.
r10 = filmes.mode(numeric_only=False).iloc[0]
r11 = filmes.fillna(r10)
print("\nq) ")
print(r11)

# Crie um dataframe e teste preencher os valores ausentes com moda, média, mediana e valor mais próximo.
df2 = pd.DataFrame({ 
    'A': [1, np.nan, 3, np.nan, 5], 
    'B': [4, np.nan, np.nan, 8, 10], 
    'C': [7, np.nan, 9, np.nan, 11], 
    'D': [5, 4, 9, np.nan, np.nan]
})
print(df2)

moda = df2.mode().iloc[0]
r12 = df2.fillna(moda)
print("\nr) ")
print(r12)

media = df2.mean()
r13 = df2.fillna(media)
print("\ns) ")
print(r13)

mediana = df2.median()
r14 = df2.fillna(mediana)
print("\nt) ")
print(r14)

r15 = df2.fillna(method='ffill')
print("\nu) ")
print(r15)

# Valores redundantes
# Com os dados carregados faça:

# Verifique se há na tabela avaliacoes dados duplicados e quantos dados são duplicados.
print("\nv) ")
print(avaliacoes.duplicated().sum())

# Verifique se há na tabela avaliacoes, especificamente na coluna movie_id dados duplicados e quantos 
# dados são duplicados.
print("\nw) ")
print(avaliacoes["movie_id"].duplicated().sum())

# Remova os dados duplicados da coluna movie_id.
print("\nx) ")
avaliacoes = avaliacoes.drop_duplicates(subset=["movie_id"])
print(avaliacoes["movie_id"].duplicated().sum())