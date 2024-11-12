import numpy as np

# 1) Crie 1 array com 3 elementos distintos

a = np.array([1, 2, 3])
print("1) ", a)

# 2) Crie 1 array de zeros

b = np.zeros(3)
print("2) ", b)

# 3) Crie 1 array de uns

c = np.ones(4)
print("3) ", c)

# 4) Crie 1 array de 4 elementos arbitrários

d = np.array([1, True, "Hello World!", a[2]])
print("4) ", d)

# 5) Crie 1 array a partir de um intervalo de números (sequência)

e = np.arange(5)
print("5) ", e)

# 6) Crie 1 array a partir de um intervalo de números e que apresente uma sequência de 3 em 3.

f = np.arange(3, 12, 3)
print("6) ", f)

# 7) Explique o resultado desse código: np.linspace(0,22,5)

g = np.linspace(0,22,5)
print("7) ", g)
print('7) A função np.linspace cria um array de valores espaçados linearmente dentro de um intervalo especificado. No caso do código np.linspace(0, 22, 5), o array começa em 0, termina em 22 e contém exatamente 5 elementos, distribuídos de forma equidistante entre esses valores.')

# 8) Crie um array de 21 elementos e exiba:
# a. Tipo
# b. Número de elementos
# c. Consumo de bytes por elementos
# d. Número de elementos
# e. Número de dimensões

h = np.arange(21)
print("8) ", h)
print("8)a)Tipo: ", h.dtype)
print("8)b)Número de elementos: ", h.size)
print("8)c)Consumo de bytes por elementos: ", h.itemsize)
print("8)d)Número de elementos: ", h.size)
print("8)e)Número de dimensões: ", h.ndim)

# 9) Criar uma lista A de 3 listas com 3 elementos

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("9) ", A)

# 10) Copiar a lista do item anterior para um array multidimensional chamado multi_B

multi_B = A.copy()
print("10) ", multi_B)

# 11) Exibir o número de elementos em cada dimensão do array lista A e B

print("11)A: ", A.shape)
print("11)multi_B: ", multi_B.shape)

# 12) Usando o comando reshape crie transforme uma lista de 12 elementos em 1 array (3,4)

i = np.arange(12)
print("12) ", i)
j = i.reshape(3, 4)
print("12) ", j)

# 13) Usando o comando reshape transforme o array anterior em uma lista de 12 elementos

k = j.reshape(-1)
print("13) ", k)

# 14) Usando o comando reshape transforme a lista anterior em um array (2,2,3)

l = k.reshape(2, 2, 3)
print("14) ", l)

# 15) Crie um array de 21 elementos e apresente:
# a. O elemento 3
# b. O último elemento
# c. os elementos no intervalo de 3 ao 9

m = np.arange(21)
print("15) ", m)
print("15)a) ", m[3])
print("15)b) ", m[-1])
print("15)c) ", m[3:10])

# 16) Crie 1 array de 21 elementos usando o comando arange e reshape em uma mesma linha de comando e faça:
# a. Apresente o elemento 2 (linha 2)
# b. Apresente o elemento 3 da linha 2
# c. Apresente as linhas 0 e 1 e seus elementos
# d. Apresente os elementos da coluna 3 de cada linhas do array
# e. Apresente apenas os 3 últimos elementos da 1a e 2a linha do array
# f. Apresente apenas os 5 últimos elementos de cada linha do array

n = np.arange(21).reshape(3, 7)
print("16) ", n)
print("16)a) ", n[1, 1])
print("16)b) ", n[1, 2])
print("16)c) ", n[0], n[1])
print("16)d) ", n[:, 3])
print("16)e) ", n[0, -3:], n[1, -3:])
print("16)f) ", n[:, -5:])