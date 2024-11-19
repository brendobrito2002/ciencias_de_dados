import pandas as pd

# Criando o DataFrame Usuario
Usuario = pd.DataFrame({ 
    'pk': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 
    'nome': ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo', 'Fernanda', 'Gabriel', 'Helena', 'Igor', 'Juliana', 'Lucas', 'Mariana', 'Nina', 'Otávio', 'Paula', 'Ricardo', 'Sofia', 'Thiago', 'Ursula', 'Vitor'], 
    'idade': [34, 35, 19, 22, 17, 29, 41, 30, 62, 33, 15, 28, 40, 47, 32, 13, 26, 39, 9, 51] 
})

# Criando o DataFrame Cidade
Cidade = pd.DataFrame({ 
    'pk': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 
    'cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Porto Alegre', 'Salvador', 'Fortaleza', 'Brasília', 'Manaus', 'Recife', 'Campinas', 'Niterói', 'Uberlândia', 'Londrina', 'Caxias do Sul', 'Feira de Santana', 'Juazeiro do Norte', 'Taguatinga', 'Belém', 'Olinda'], 
    'estado': ['SP', 'RJ', 'MG', 'PR', 'RS', 'BA', 'CE', 'DF', 'AM', 'PE', 'GO', 'ES', 'MG', 'SC', 'RS', 'BA', 'CE', 'DF', 'PA', 'PE']
})

# SELECT nome, idade FROM Usuario
r1 = Usuario[['nome', 'idade']]
print("\nResultado da consulta: SELECT nome, idade FROM Usuario")
print(r1)

# SELECT * FROM Usuario WHERE idade > 35
r2 = Usuario[Usuario['idade'] > 35]
print("\nResultado da consulta: SELECT * FROM Usuario WHERE idade > 35")
print(r2)

# SELECT * FROM Usuário Us INNER JOIN Cidade Ci ON Us.pk = Ci.pk
r3 = pd.merge(Usuario, Cidade, on='pk')
print("\nResultado da consulta: SELECT * FROM Usuário Us INNER JOIN Cidade Ci ON Us.pk = Ci.pk")
print(r3)

# SELECT nome, estado, COUNT(*) FROM Cidade GROUP BY estado
r4 = Cidade.groupby('estado').size().reset_index(name='count')
print("\nResultado da consulta: SELECT * FROM Usuário Us INNER JOIN Cidade Ci ON Us.pk = Ci.pk")
print(r4)

# SELECT estado, SUM(idade) FROM Usuário Us INNER JOIN Cidade Ci ON Us.pk = Ci.pk GROUP BY estado
r5 = pd.merge(Usuario, Cidade, on='pk').groupby('estado')['idade'].sum().reset_index()
print("\nResultado da consulta: SELECT estado, SUM(idade) FROM Usuário Us INNER JOIN Cidade Ci ON Us.pk = Ci.pk GROUP BY estado")
print(r5)

# SELECT * FROM Usuario ORDER BY idade
r6 = Usuario.sort_values(by='idade')
print("\nResultado da consulta: SELECT * FROM Usuario ORDER BY idade")
print(r6)

# SELECT * FROM Usuario LIMIT 3
r7 = Usuario.head(3) 
print("\nResultado da consulta: SELECT * FROM Usuario LIMIT 3") 
print(r7)

# SELECT * FROM Usuario ORDER BY idade DESC LIMIT 6
r8 = Usuario.sort_values(by='idade', ascending=False).head(6)
print("\nResultado da consulta: SELECT * FROM Usuario ORDER BY idade DESC LIMIT 6") 
print(r8)

# Quantas linhas tem a tabela Usuário e a tabela Cidade? (COUNT)
r9 = len(Usuario)
r10 = len(Cidade)
print("\nQuantidade de linhas na tabela Usuario: ", r9) 
print("Quantidade de linhas na tabela Cidade: ", r10)

# Qual a média das idades dos Usuários? (AVG)
r11 = Usuario['idade'].mean()
print("\nMédia das idades dos Usuários:", r11)

# Qual a soma das idades dos Usuários? (SUM)
r12 = Usuario['idade'].sum()
print("\nSoma das idades dos Usuários:", r12)

# SELECT * FROM Usuario WHERE idade IN (19,47)
r13 = Usuario[Usuario['idade'].isin([19, 47])]
print("\nResultado da consulta: SELECT * FROM Usuario WHERE idade IN (19,47)") 
print(r13)

# SELECT * FROM Usuario WHERE idade NOT IN (19,47)
r14 = Usuario[~Usuario['idade'].isin([19, 47])]
print("\nResultado da consulta: SELECT * FROM Usuario WHERE idade NOT IN (19,47)")
print(r14)

# SELECT * FROM Usuario WHERE idade BETWEEN 23 AND 50
r15 = Usuario[(Usuario['idade'] >= 23) & (Usuario['idade'] <= 50)]
print("\nResultado da consulta: SELECT * FROM Usuario WHERE idade BETWEEN 23 AND 50")
print(r15)

# SELECT DISTINCT estado FROM Cidade
r16 = Cidade['estado'].drop_duplicates().reset_index(drop=True)
print("\nResultado da consulta: SELECT DISTINCT estado FROM Cidade")
print(r16)

# SELECT DISTINCT nome, estado FROM Cidade
r17 = Cidade[['cidade', 'estado']].drop_duplicates().reset_index(drop=True)
print("\nResultado da consulta: SELECT DISTINCT nome, estado FROM Cidade")
print(r17)

# SELECT id, nome, idade, CASE WHEN idade > 18 THEN ‘ADULTO’ ELSE 'ADOLESCENTE END AS categoria FROM Usuario
Usuario['categoria'] = Usuario['idade'].apply(lambda x: 'ADULTO' if x > 18 else 'ADOLESCENTE')
r18 = Usuario[['pk', 'nome', 'idade', 'categoria']]
print("\nResultado da consulta: SELECT id, nome, idade, CASE WHEN idade > 18 THEN ‘ADULTO’ ELSE 'ADOLESCENTE END AS categoria FROM Usuario")
print(r18)

# SELECT estado, COUNT(*) FROM Cidade GROUP BY estado HAVING COUNT(*) > 1
r19 = Cidade.groupby('estado').filter(lambda x: len(x) > 1).groupby('estado').size().reset_index(name='count')
print("\nResultado da consulta: SELECT estado, COUNT(*) FROM Cidade GROUP BY estado HAVING COUNT(*) > 1")
print(r19)

# SELECT * FROM (SELECT * FROM Usuario WHERE idade > 31) WHERE nome LIKE ‘A%’
r20 = Usuario[(Usuario['idade'] > 31) & (Usuario['nome'].str.startswith('A'))]
print("\nResultado da consulta: SELECT * FROM (SELECT * FROM Usuario WHERE idade > 31) WHERE nome LIKE A%")
print(r20)

# SELECT * FROM Usuario WHERE nome LIKE ‘a%’
r21 = Usuario[Usuario['nome'].str.lower().str.startswith('a')]
print("\nResultado da consulta: SELECT * FROM Usuario WHERE nome LIKE a%")
print(r21)

# ALTER TABLE Usuario ADD COLUMN sobrenome VARCHAR
Usuario['sobrenome'] = None
print("\nResultado da consulta: ALTER TABLE Usuario ADD COLUMN sobrenome VARCHAR")
print(Usuario)

# UPDATE Usuario SET idade = idade + 1 WHERE nome = ‘Ana Lis’
Usuario.loc[Usuario['nome'] == 'Ana', 'idade'] += 1
print("\nResultado da consulta: UPDATE Usuario SET idade = idade + 1 WHERE nome = Ana Lis")
print(Usuario)

# DELETE FROM Usuario WHERE idade < 15
Usuario = Usuario[Usuario['idade'] >= 15]
print("\nResultado da consulta: DELETE FROM Usuario WHERE idade < 15")
print(Usuario)

# CREATE INDEX idx_nome ON Usuario (nome)
# (Pandas não suporta índices explícitos como SQL, mas podemos ordenar ou usar índices no DataFrame.)
print("\nResultado da consulta: CREATE INDEX idx_nome ON Usuario (nome)")
print("Índices automáticos em Pandas são implícitos.")

# SELECT id, nome FROM Usuario UNION SELECT id, nome, estado FROM Cidade (Union)
r22 = pd.concat([Usuario[['pk', 'nome']], Cidade[['pk', 'cidade']].rename(columns={'cidade': 'nome'})]).drop_duplicates()
print("\nResultado da consulta: SELECT id, nome FROM Usuario UNION SELECT id, nome, estado FROM Cidade")
print(r22)

# SELECT id, nome FROM Usuario UNION ALL SELECT id, nome, estado FROM Cidade (Union All)
r23 = pd.concat([Usuario[['pk', 'nome']], Cidade[['pk', 'cidade']].rename(columns={'cidade': 'nome'})])
print("\nResultado da consulta: SELECT id, nome FROM Usuario UNION ALL SELECT id, nome, estado FROM Cidade")
print(r23)

# SELECT nome AS nome_usuario FROM Usuario
r24 = Usuario[['nome']].rename(columns={'nome': 'nome_usuario'})
print("\nResultado da consulta: SELECT nome AS nome_usuario FROM Usuario")
print(r24)