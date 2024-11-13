import matplotlib.pyplot as plt
import numpy as np
from scipy import misc

# 1) Carregue e exiba a imagem “face” em seu formato original.
face = misc.face()
plt.imshow(face)
plt.show()

# 2) Exiba a imagem anterior em escala cinza
face_gray = np.dot(face[...,:3], [0.2989, 0.5870, 0.1140])
plt.imshow(face_gray, cmap='gray')
plt.show()

# 3) Apresente o array NumPy referente a imagem.
print("3) ", face)

# 4) Instale o scikit-image no seu ambiente