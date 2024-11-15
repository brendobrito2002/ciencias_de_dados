import numpy as np
import matplotlib.pyplot as plt
from skimage import transform
from scipy.datasets import face
from skimage.transform import rescale
from scipy import special, stats
from skimage import data

# 1) Carregue e exiba a imagem “face” em seu formato original.
face = face()
plt.imshow(face)
plt.title("Imagem Original")
plt.show()

# 2) Exiba a imagem anterior em escala cinza
face_gray = np.dot(face[...,:3], [0.2989, 0.5870, 0.1140])
plt.imshow(face_gray, cmap='gray')
plt.title("Imagem em Escala de Cinza")
plt.show()

# 3) Apresente o array NumPy referente à imagem.
print("3) Array da Imagem:\n", face)

# 5) Redimensione a imagem gerada anteriormente para 50% do seu tamanho original
face_resized = rescale(face, 0.5, anti_aliasing=True, channel_axis=-1)
plt.imshow(face_resized)
plt.title("Imagem Redimensionada para 50%")
plt.show()

# 6) Volte a imagem para o tamanho original usando interpolação bilinear
face_original_size = rescale(face_resized, 2, anti_aliasing=True, channel_axis=-1)
plt.imshow(face_original_size)
plt.title("Imagem com Tamanho Original Recuperado (Interpolação Bilinear)")
plt.show()

# 7) Calcule e apresente o fatorial do número 4 como exemplo
resultado = special.factorial(4)
print("7) Fatorial de 4:", resultado)

# 8) Apresente os gráficos das funções de Bessel e da função de erro Gaussiana
x = np.linspace(0, 10, 100)

# Função de Bessel
y_bessel = special.jv(1, x)
plt.plot(x, y_bessel)
plt.title("Função de Bessel")
plt.xlabel("x")
plt.ylabel("Jv(x)")
plt.show()

# Função de erro Gaussiana
y_erf = special.erf(x)
plt.plot(x, y_erf)
plt.title("Função de Erro Gaussiana")
plt.xlabel("x")
plt.ylabel("erf(x)")
plt.show()

# 9) Apresente o gráfico da função Gama
y_gamma = special.gamma(x)
plt.plot(x, y_gamma)
plt.title("Função Gama")
plt.xlabel("x")
plt.ylabel("Gamma(x)")
plt.show()

# 10) Apresente os gráficos dos polinômios de Legendre
x = np.linspace(-1, 1, 100)
for n in range(5):
    y_legendre = special.legendre(n)(x)
    plt.plot(x, y_legendre, label=f'P{n}(x)')
plt.title("Polinômios de Legendre")
plt.xlabel("x")
plt.ylabel("Pn(x)")
plt.legend()
plt.show()

# 11) Apresente os gráficos das funções PDF e CDF
x = np.linspace(-3, 3, 100)
pdf = stats.norm.pdf(x)
cdf = stats.norm.cdf(x)

plt.plot(x, pdf, label="PDF")
plt.plot(x, cdf, label="CDF")
plt.title("PDF e CDF para Distribuição Normal")
plt.legend()
plt.show()

# 12) Apresente o gráfico de probabilidade da função de massa de probabilidade (PMF)
n, p = 10, 0.5
x = np.arange(0, n+1)
pmf = stats.binom.pmf(x, n, p)

plt.bar(x, pmf)
plt.title("PMF da Distribuição Binomial")
plt.xlabel("Número de Sucessos")
plt.ylabel("Probabilidade")
plt.show()

# 13) Gere uma amostra aleatória e apresente a estatística t e o valor p
sample1 = np.random.normal(0, 1, 100)
sample2 = np.random.normal(0, 1, 100)
t_stat, p_value = stats.ttest_ind(sample1, sample2)
print("13) Estatística t:", t_stat)
print("13) Valor p:", p_value)

# 14) Apresente os valores de correlação de Pearson e Spearman e um gráfico com linha de regressão ajustada
x = np.random.rand(50)
y = 2.5 * x + np.random.normal(0, 0.2, 50)

# Correlação de Pearson
pearson_corr, _ = stats.pearsonr(x, y)
spearman_corr, _ = stats.spearmanr(x, y)
print("14)a) Correlação de Pearson:", pearson_corr)
print("14)b) Correlação de Spearman:", spearman_corr)

plt.scatter(x, y, label="Dados")
m, b = np.polyfit(x, y, 1)
plt.plot(x, m * x + b, color="red", label="Linha de Regressão")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Correlação e Regressão Linear")
plt.legend()
plt.show()